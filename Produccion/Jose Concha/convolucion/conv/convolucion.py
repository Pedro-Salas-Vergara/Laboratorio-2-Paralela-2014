from numpy.matrixlib.defmatrix import matrix

__author__ = 'jose'
import numpy as np
from PIL import Image
import time
inicio = time.time()
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
def filtroLinealS(arrImg):
    arrAux = arrImg
    nucleo =[[.11,.11,.11],[.11,.11,.11],[.11,.11,.11]]
    for z in range(3):
        for x in range(len(arrAux)):
            for y in range(len(arrAux[0])):
                suma = 0
                for i in range(3):
                    for j in range(3):
                        try:
                            suma += int(arrImg[x-1+i][y-1+j][z]*nucleo[i][j])
                        except IndexError:
                            suma += 0
                arrAux[x][y][z]=suma
    return arrAux
def filtroLinealS2(arrImg):
    arrAux = arrImg
    nucleo =[[.0625,.125,.0625],[.125,.25,.125],[.0625,.125,.0625]]
    for z in range(3):
        for x in range(len(arrAux)):
            for y in range(len(arrAux[0])):
                suma = 0
                for i in range(3):
                    for j in range(3):
                        try:
                            suma += int(arrImg[x-1+i][y-1+j][z]*nucleo[i][j])
                        except IndexError:
                            suma += 0
                arrAux[x][y][z]=suma
    return arrAux
def filtroConvolucion(imagen):
    x,y = imagen.size
    px = imagen.load()
    #MX = [[-1,0,1],[-1,0,1],[-1,0,1]] #mascara lineas horizontales
    MX = [[-1,0,1],[-2,0,2],[-1,0,1]]
    #MY = [[1,1,1],[0,0,0],[-1,-1,-1]] #mascara lineas verticales
    MY = [[1,2,1],[0,0,0],[-1,-2,-1]]

    imagenNuevaX = Image.new('RGB',(x,y))
    imagenNuevaY = Image.new('RGB',(x,y))
    imn = Image.new('RGB',(x,y))
    for j in range(y):
        for i in range(x):
            sumatoria = 0
            sumatoriay = 0
            for mj in range(-1,2):
                for mx in range(-1,2):
                    try:
                        sumatoria += MX[mj+1][mx+1]*px[i+mx,j+mj][1]
                        sumatoriay += MY[mj+1][mx+1]*px[i+mx,j+mj][1]
                    except:
                        sumatoria += 0
                        sumatoriay += 0
            punto1 = sumatoria
            punto2 = sumatoriay
            #Normalizar
            if(punto1 < 0):
                punto1 = 0
            if(punto1 > 255):
                punto1 = 255
            if(punto2 < 0):
                punto2 = 0
            if(punto2 > 255):
                punto2 = 255
            imagenNuevaX.putpixel((i,j),(punto1,punto1,punto1))
            imagenNuevaY.putpixel((i,j),(punto2,punto2,punto2))
    px1 = imagenNuevaX.load()
    px2 = imagenNuevaY.load()
    #Mezclar las mascaras
    for i in range(x):
        for j in range(y):
            p1 = px1[i,j]
            p2 = px2[i,j]
            r = ( p1[0] + p2[0] ) / 2
            g = ( p1[1] + p2[1] ) / 2
            b = ( p1[2] + p2[2] ) / 2
            imn.putpixel((i,j),(r,g,b))
    #imagenNuevaX.show()
    #imagenNuevaY.show()
    return imn #,imagenNuevaX,imagenNuevaY
def convolucionImg(img, caso = 0):
    arrImg = convertirImgMatrixRGB(img)
    if caso ==0:
        arrAux = filtroLinealS(arrImg)
    elif caso == 1:
        arrAux = filtroLinealS2(arrImg)
    elif caso == 2:
        imgAux = filtroConvolucion(img)
        return imgAux
    convImg = Image.fromarray(arrAux)
    return convImg
def main():
    img = Image.open('Lenna.png')
    convImg = convolucionImg(img)
    convImg.save('conv0.png')
    print "Convolution 1 = "+str(time.time()-inicio)
    ini = time.time()
    convImg = convolucionImg(img,1)
    convImg.save('conv1.png')
    print "Convolution 2 = "+str(time.time()-ini)
    ini = time.time()
    convImg= convolucionImg(img,2)
    convImg.save('conv2.png')
    print "Convolution 3 = "+str(time.time()-ini)

main()

final = time.time()-inicio

print "Serial time[seconds] = " + str(final)