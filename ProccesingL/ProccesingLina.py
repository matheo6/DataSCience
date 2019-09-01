# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:51:11 2019

@author: Administrador
"""
import matplotlib.pyplot as plt
import skimage
import os
import numpy as np

from skimage import io
def matrizExtended(m):#funcion para complementar y ampliar la matriz original con los pixeles inversos de las esquinas
    lx,ly=m.shape # lx=numero de filas de m, ly numero de columnas de m
    k=np.zeros((lx+2,ly+2))
    k[1:lx+1,1:ly+1]=m
    k[lx+1,1:(ly+1)]=m[0,:]
    k[0,1:(ly+1)]=m[lx-1,:]
    k[:,0]=k[:,ly]
    k[:,ly+1]=k[:,1]
    return k

#funncion convolucion para multiplicar la mascara y sacar el promedio en la matris resultante
def comvolution(m,mask): #m= matriz aumentada con las filas y columnas de las esquinas invertidas, mask= mascara 
    lx,ly=m.shape # lx=numero de filas de m, ly numero de columnas de m
    c=np.zeros((lx-2,ly-2))#nueva matriz donde se almacenara los resultados de los promedios de las multiplicaciones entre la mascaray las subregiones de 3x3
    for x in range(lx-2):#for para las filas
        for y in range(ly-2):#for para las columnas
            c[x,y]=np.mean(np.array((m[x:x+3,y:y+3]))*mask)#operacion entre matrices de 3x3 que avanzan de a una en la matriz amentada desde 0 a 
    return c #devuelve la matriz

filename=os.path.join('D:\matriz3D','lina3.jpg')#crea la ruta para cargar la imagen
l=io.imread(filename)#carga la imagen a color
m=((l.mean(axis=2))/255)#hace el promedio para convertirla a escala de grises
h=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
lina=comvolution(matrizExtended(m),h)
plt.imshow(lina,cmap=plt.cm.gray)


