# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np
m= np.arange(729).reshape(9,9,9)
print(m)
print('')
def change(l,m,s):
    k= np.array(l[(int(m/9)*3):(int(m/9)*3)+3,(int((m%9)/3))*3:(int((m%9)/3))*3+3,(int(m%3)*3):(int(m%3)*3)+3])
    l[(int(m/9)*3):(int(m/9)*3)+3,(int((m%9)/3))*3:(int((m%9)/3))*3+3,(int(m%3)*3):(int(m%3)*3)+3]=l[(int(s/9)*3):(int(s/9)*3)+3,(int((s%9)/3))*3:(int((s%9)/3))*3+3,(int(s%3)*3):(int(s%3)*3)+3]
    l[(int(s/9)*3):(int(s/9)*3)+3,(int((s%9)/3))*3:(int((s%9)/3))*3+3,(int(s%3)*3):(int(s%3)*3)+3]=k
    return l 
print(change(m,13,0))