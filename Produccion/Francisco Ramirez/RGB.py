__author__ = 'francisco'

import numpy as np
from PIL import Image


# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))


# procedimiento : Suma los componentes R, G, B del pixel de la imagen con el color que se quiere
# y cada suma se divide en dos, obteniendo un promedio
def mezclarRGB(img,r,g,b):
    arrImg=convertirImgMatrixRGB(img)
    #print arrImg
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            #print str(i),",",str(j)
            #print arrImg[i][j]
            arrImg[i][j][0] = (arrImg[i][j][0]+r)/2
            arrImg[i][j][1] = (arrImg[i][j][1]+g)/2
            arrImg[i][j][2] = (arrImg[i][j][2]+b)/2
            #print arrImg[i][j]
    imgNegativa=Image.fromarray(arrImg)
    return imgNegativa



def main():
    img=Image.open("ViendoFacebook.png")
    r=0
    g=0
    b=0
    imgNegativa=mezclarRGB(img,r,g,b)
    imgNegativa.save("output3.png")    #guarda la imagen negativo

main()