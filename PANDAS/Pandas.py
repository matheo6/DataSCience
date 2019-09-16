# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:14:43 2019

@author: Estudiantes
"""

import numpy as np
import pandas as pd
l= np.random.randint(low=0,high=10,size=(5,5))
df1=pd.DataFrame(data=l)
df2=pd.DataFrame(data=l,columns=['punt1','punt2','punt3','punt4','punt5'])
df3=pd.DataFrame(data=l,columns=['punt1','punt2','punt3','punt4','punt5'],index=['est1','est2','est3','est4','est5'])
df1.rename(index={0:"a",1:"b",2:"c",3:"d",4:"e"})
df1.rename(index={"a":"a",1:"b",2:"c",3:"d",4:"e"})
df1
docentes=pd.read_csv('Docentes_De_Planta.csv')
docentes.head()
docentes.tail()
docentes.columns
docentes.index
docentes.describe()
docentes.dtypes
docentes=pd.read_csv('Docentes_De_Planta.csv',index_col='Facultad')