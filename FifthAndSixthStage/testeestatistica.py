# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 22:25:42 2018

@author: Samir Ramos
"""

import pymysql
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt



l1 = [4.5725] 
v_serie =  pd.Series(l1)
print('vserie =', v_serie)

def devpadrao(l1) :
    x =  len(l1)
    
    soma = 0
    for valor in l1:
        soma = soma + (valor - v_serie.mean())**2
    v_desviopadrao = math.sqrt(soma/x)
    return (v_desviopadrao)       
       
v_media = v_serie.mean()
v_1quartil = v_serie.quantile(q=0.25)        
v_mediana = v_serie.median()        
v_3quartil = v_serie.quantile(q=0.75)
       
v_desviopadrao = devpadrao(l1)

v_amplitude = (v_serie.max() - v_serie.min())
       
print('Media =',v_media)        
print('Desvio padrao =',v_desviopadrao) 
print('1quartil =',v_1quartil)
print('mediana =',v_mediana)
print('3quartil =',v_3quartil)
print('amplitude =',v_amplitude)






"""
import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

soma = float(a + b + c)
media = float(soma/3)
difquad = (a-media)**2 + (b-media)**2 + (c-media)**2 
desvio = math.sqrt(difquad/3)
print ('Desvio = ', desvio)
print(media)
"""