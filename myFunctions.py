# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 23:46:13 2017

@author: Maria Camila Gomez
"""
import cv2
import glob
import numpy as np;
 
def componentes(imagen):
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2LAB);
    imagen2 = imagen[:,:,1];
    return imagen2;

def fill(th, im_th):
    # Copy the thresholded image.
    im_floodfill = im_th.copy() 
    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8) 
    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0,0), 255);
    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill);
    # Combine the two images to get the foreground.
    im_out = im_th | im_floodfill_inv
    return im_out;

def reconocedor(img):
    fil, col = img.shape[:2]
    #cv2.imshow('Origin', img)
    contador = 0
    respuesta = 0
    for filename in glob.glob('seniales/*.jpg'):
        im= cv2.imread(filename)
        im = cv2.resize(im, (col,fil))
        res = cv2.matchTemplate(img,im,cv2.TM_CCORR)
        threshold = 0.9
        while ((res[0])[0] > 10): 
            (res[0])[0] = (res[0])[0] / 10;
        loc = (res[0])[0]/10 >= threshold
        contador = contador +1
        if(loc):
            respuesta = contador
        #cv2.imshow(filename, im)
    #cv2.waitKey() # Permanece la imagen en pantalla hasta presionar una tecla
    #cv2.destroyAllWindows() # Cierra todas las ventanas abiertas
    return respuesta;
    