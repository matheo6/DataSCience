# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import matplotlib.pyplot as plt
import skimage
import os
import numpy as np

def desorder(m):
    for x in range(m.size):
        aux=np.random.randint(16)
        aux1= m[aux]
        m[aux]=m[x]
        m[x]=aux1
    return m

def reorderPicture(order,l):
    lx,ly=l.shape
    k=np.zeros((lx,ly))
    for x in range(order.size):
        k[((int(x/4))*(int(lx/4))):(((int(x/4))*(int(lx/4)))+(int(lx/4))),(int(x%4)*(int(ly/4))):((int(x%4)*(int(ly/4)))+(int(ly/4)))]=l[((int((order[x])/4))*(int(lx/4))):(((int((order[x])/4))*(int(lx/4)))+(int(lx/4))),(int((order[x])%4)*(int(ly/4))):((int((order[x])%4)*(int(ly/4)))+(int(ly/4)))]
    return k
    
    
    
order =np.arange(16)
oreder=desorder(order)

filename=os.path.join('D:\DataSCience-master\ProccesingL','lina3.jpg')#crea la ruta para cargar la imagen
l=io.imread(filename)#carga la imagen a color
m=((l.mean(axis=2))/255)#hace el promedio para convertirla a escala de grises
plt.imshow(m,cmap=plt.cm.gray)
plt.imshow(reorderPicture(order,m),cmap=plt.cm.gray)



