# -*- coding: utf-8 -*-
"""
%--------------------------------------------------------------------------
%------- CÓDIGO -----------------------------------------------------------
%------- Proyecto 1 -------------------------------------------------------
%------- Por: Maria Camila Gomez maria.gomez26@udea.edu.co ----------------
%-------      CC 1152454724 -----------------------------------------------
%------- Por: Santiago Romero santiago.romero@udea.edu.co -----------------
%-------      CC 1026154938 -----------------------------------------------
%------- Por: Milena Cardenas milena.cardenas@udea.edu.co -----------------
%-------      CC 1036934864 -----------------------------------------------
%------- Curso Básico de Procesamiento de Imágenes y Visión Artificial-----
%------- Marzo de 2017-----------------------------------------------------
%--------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------
#--1. Inicializo el sistema -----------------------------------------------
#--------------------------------------------------------------------------
import cv2
import numpy as np
import myFunctions as ff
    
print("Reconocedor de señales")

imagen = cv2.imread('imagen_2.jpg')
fil, col = imagen.shape[:2]
componente = ff.componentes(imagen)

min1 = componente;

min2=np.array(min1);
min3=(min2>170).choose(min2,255)                    #Umbraliza imagen segun un ...umbral
min3=(min2<170).choose(min2,0) 
min3 = cv2.resize(min3,(col,fil));
#copiaImagen = imagen;
#copiaImagen[min3==0]=0;


th,copiaImagen = cv2.threshold(min3,150,255,cv2.THRESH_BINARY)

copiaImagen = ff.fill(th, copiaImagen);

th,copiaImagen = cv2.threshold(copiaImagen,150,255,cv2.THRESH_BINARY)

kernel = np.ones((5,5),np.uint8)
copiaImagen = cv2.morphologyEx(copiaImagen, cv2.MORPH_CLOSE, kernel)

im, l, n = cv2.findContours(copiaImagen,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(copiaImagen, l, 0, (0,255,0), 3)

imagenDos=copiaImagen;
copiaImagen=imagen;
copiaImagen[imagenDos==0]=0;


for h,cnt in enumerate(l):
    mask = np.zeros(copiaImagen.shape,np.uint8)
    cv2.drawContours(mask,[cnt],0,255,-1)
    area = cv2.contourArea(cnt)
    if area > 80000 :
        if area < 90000:
            # cv2.imshow('segmento', mask)
            x,y,w,h = cv2.boundingRect(cnt)
            box=copiaImagen[y:y+h,x:x+w]
            senal = ff.reconocedor(box);
            if(senal == 1):
                print "Pare"
            elif(senal == 2):
                print "Derecha"
            elif(senal == 3):
                print "Izquierda"
            else:
                print "No hay señal"



#cv2.imshow('Imagen Grises', copiaImagen) # Se muestra la imagen
#cv2.waitKey() # Permanece la imagen en pantalla hasta presionar una tecla
#cv2.destroyAllWindows() # Cierra todas las ventanas abiertas
