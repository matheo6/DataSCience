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

H=pd.read_csv('Registros_clim_ticos_del_municipio_de_Durania_a_o_2016.csv')
M=H['Humedad (%)']
L=H['Velocidad del viento(km/h)']
plt.hist(M)
plt.title("Humedad")
plt.show
plt.hist(L)
plt.title("Velocidad del viento")
plt.show

T=L.dropna()
k=M.dropna()
k=k.astype(float)
T=T.astype(float)
k=k.drop([2],axis=0)
##mediana
print(st.mean(k))
print(st.mean(T))
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
print(st.variance(k))
print(st.variance(T))
##Desviacion estandar 
print(np.std(k))
print(np.std(T))
##Covariance
print(np.cov(k,T))
##correlacion
print(np.corrcoef(k,T))



