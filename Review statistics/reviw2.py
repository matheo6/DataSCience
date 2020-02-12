# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:09:11 2020
@author: Administrador
"""
from matplotlib import pyplot as plt
from scipy.stats.stats import pearsonr as scipy
import pandas as pd
import statistics as st
import numpy as np
##histograma
H=pd.read_csv('Registros_clim_ticos_del_municipio_de_Durania_a_o_2016.csv')
M=H['Humedad (%)']
L=H['Velocidad del viento(km/h)']
plt.hist(M)
plt.title("Humedad/Velocidad del viento")
plt.hist(L)
plt.show

T=L.dropna()
k=M.dropna()
k=k.astype(float)
T=T.astype(float)
k=k.drop([2],axis=0)

##frecuencias
plt.psd(T)
plt.psd(k)
plt.show()
##scatter
fig,ax=plt.subplots()
ax.scatter(k,T,s=30,c='r',alpha=0.3,label='distribucion',edgecolors='none')
ax.set_xlabel('velocidad', fontsize=15)
ax.set_ylabel('humedad', fontsize=15)
ax.grid(True)
fig.tight_layout()

plt.show
##mediana barra
print(st.mean(k))
print(st.mean(T))

fig,ax=plt.subplots()
ax.bar(st.mean(k),st.mean(k))
ax.bar(st.mean(T),st.mean(T))
ax.set_xlabel('velocidad/humedad', fontsize=15)
ax.grid(True)
fig.tight_layout()
plt.show
##moda
print(st.mode(k))
print(st.mode(T))
##mediana
print(st.median(k))
print(st.median(T))
##mediana agrupada
print(st.median_grouped(k))
print(st.median_grouped(T))
##Rango
def data_range(x):
    return max(x)-min(x)
print(data_range(k))
print(data_range(T))
##varianza poblacional
print(st.pvariance(k))
print(st.pvariance(T))
##varianza 
print("varianza humedad"+st.variance(k))
print("varianza velocidad"+st.variance(T))
##Desviacion estandar 
print("desviacion estandar humedad"+np.std(k))
print("desviacion estandar velocidad"+np.std(T))

##Covariance
print("covarianza"+np.cov(k,T))


##correlacion
print("correlacion"+np.corrcoef(k,T))

