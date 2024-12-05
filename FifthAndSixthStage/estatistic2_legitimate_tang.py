# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:42:38 2020

@author: Samir

Updated on December 2022
@author: Jeferson Luis Gonçalves
"""

import math
import pymysql
import pandas as pd
from tqdm import tqdm

# Criando um objeto de conexão com o banco de dados
# Jeferson Begin
#db = pymysql.connect(host = 'localhost', user = 'root', password = 'ime@123', db = 'sbseg',  autocommit=True)
db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)
# Jeferson End

try:
    #Criando função para cálculos estatísticos
    # A função def cria séries no Pandas a partir de listas l1,l2,l3
    # No caso séries de Valência (e outras medidas) de mensagens de cada usuário
    def statistic (l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,l40,l41,l42,l43,l44,l45,l46,l47,l48,l49,l50):   
        d1_serie =  pd.Series(l1)
        d2_serie =  pd.Series(l2)
        d3_serie =  pd.Series(l3)
        d4_serie =  pd.Series(l4)
        d5_serie =  pd.Series(l5)
        d6_serie =  pd.Series(l6)
        d7_serie =  pd.Series(l7)
        d8_serie =  pd.Series(l8)
        d9_serie =  pd.Series(l9)
        d10_serie =  pd.Series(l10)
        d11_serie =  pd.Series(l11)
        d12_serie =  pd.Series(l12)
        d13_serie =  pd.Series(l13)
        d14_serie =  pd.Series(l14)
        d15_serie =  pd.Series(l15)
        d16_serie =  pd.Series(l16)
        d17_serie =  pd.Series(l17)
        d18_serie =  pd.Series(l18)
        d19_serie =  pd.Series(l19)
        d20_serie =  pd.Series(l20)
        d21_serie =  pd.Series(l21)
        d22_serie =  pd.Series(l22)
        d23_serie =  pd.Series(l23)
        d24_serie =  pd.Series(l24)
        d25_serie =  pd.Series(l25)
        d26_serie =  pd.Series(l26)
        d27_serie =  pd.Series(l27)
        d28_serie =  pd.Series(l28)
        d29_serie =  pd.Series(l29)
        d30_serie =  pd.Series(l30)
        d31_serie =  pd.Series(l31)
        d32_serie =  pd.Series(l32)
        d33_serie =  pd.Series(l33)
        d34_serie =  pd.Series(l34)
        d35_serie =  pd.Series(l35)
        d36_serie =  pd.Series(l36)
        d37_serie =  pd.Series(l37)
        d38_serie =  pd.Series(l38)
        d39_serie =  pd.Series(l39)
        d40_serie =  pd.Series(l40)
        d41_serie =  pd.Series(l41)
        d42_serie =  pd.Series(l42)
        d43_serie =  pd.Series(l43)
        d44_serie =  pd.Series(l44)
        d45_serie =  pd.Series(l45)
        d46_serie =  pd.Series(l46)
        d47_serie =  pd.Series(l47)
        d48_serie =  pd.Series(l48)
        d49_serie =  pd.Series(l49)
        d50_serie =  pd.Series(l50)
    
        # MEDIDAS DE TENDÊNCIA CENTRAL
         #Cálculo da Média
        d1_media = d1_serie.mean()
        d2_media = d2_serie.mean()
        d3_media = d3_serie.mean()
        d4_media = d4_serie.mean()
        d5_media = d5_serie.mean()
        d6_media = d6_serie.mean()  
        d7_media = d7_serie.mean()
        d8_media = d8_serie.mean()
        d9_media = d9_serie.mean()  
        d10_media = d10_serie.mean()
        d11_media = d11_serie.mean()
        d12_media = d12_serie.mean()
        d13_media = d13_serie.mean()
        d14_media = d14_serie.mean()
        d15_media = d15_serie.mean()
        d16_media = d16_serie.mean()  
        d17_media = d17_serie.mean()
        d18_media = d18_serie.mean()
        d19_media = d19_serie.mean()  
        d20_media = d20_serie.mean()
        d21_media = d21_serie.mean()
        d22_media = d22_serie.mean()
        d23_media = d23_serie.mean()
        d24_media = d24_serie.mean()
        d25_media = d25_serie.mean()
        d26_media = d26_serie.mean()  
        d27_media = d27_serie.mean()
        d28_media = d28_serie.mean()
        d29_media = d29_serie.mean()  
        d30_media = d30_serie.mean()
        d31_media = d31_serie.mean()
        d32_media = d32_serie.mean()
        d33_media = d33_serie.mean()
        d34_media = d34_serie.mean()
        d35_media = d35_serie.mean()
        d36_media = d36_serie.mean()  
        d37_media = d37_serie.mean()
        d38_media = d38_serie.mean()
        d39_media = d39_serie.mean()  
        d40_media = d40_serie.mean()
        d41_media = d41_serie.mean()
        d42_media = d42_serie.mean()
        d43_media = d43_serie.mean()
        d44_media = d44_serie.mean()
        d45_media = d45_serie.mean()
        d46_media = d46_serie.mean()
        d47_media = d47_serie.mean()
        d48_media = d48_serie.mean()
        d49_media = d49_serie.mean()  
        d50_media = d50_serie.mean()
       
        #Cálculo do 1º Quartil
        d1_1quartil = d1_serie.quantile(q=0.25)
        d2_1quartil = d2_serie.quantile(q=0.25)
        d3_1quartil = d3_serie.quantile(q=0.25)
        d4_1quartil = d4_serie.quantile(q=0.25)
        d5_1quartil = d5_serie.quantile(q=0.25)
        d6_1quartil = d6_serie.quantile(q=0.25)
        d7_1quartil = d7_serie.quantile(q=0.25)
        d8_1quartil = d8_serie.quantile(q=0.25)
        d9_1quartil = d9_serie.quantile(q=0.25)
        d10_1quartil = d10_serie.quantile(q=0.25)
        d11_1quartil = d11_serie.quantile(q=0.25)
        d12_1quartil = d12_serie.quantile(q=0.25)
        d13_1quartil = d13_serie.quantile(q=0.25)
        d14_1quartil = d14_serie.quantile(q=0.25)
        d15_1quartil = d15_serie.quantile(q=0.25)
        d16_1quartil = d16_serie.quantile(q=0.25)
        d17_1quartil = d17_serie.quantile(q=0.25)
        d18_1quartil = d18_serie.quantile(q=0.25)
        d19_1quartil = d19_serie.quantile(q=0.25)
        d20_1quartil = d20_serie.quantile(q=0.25)
        d21_1quartil = d21_serie.quantile(q=0.25)
        d22_1quartil = d22_serie.quantile(q=0.25)
        d23_1quartil = d23_serie.quantile(q=0.25)
        d24_1quartil = d24_serie.quantile(q=0.25)
        d25_1quartil = d25_serie.quantile(q=0.25)
        d26_1quartil = d26_serie.quantile(q=0.25)
        d27_1quartil = d27_serie.quantile(q=0.25)
        d28_1quartil = d28_serie.quantile(q=0.25)
        d29_1quartil = d29_serie.quantile(q=0.25)
        d30_1quartil = d30_serie.quantile(q=0.25)
        d31_1quartil = d31_serie.quantile(q=0.25)
        d32_1quartil = d32_serie.quantile(q=0.25)
        d33_1quartil = d33_serie.quantile(q=0.25)
        d34_1quartil = d34_serie.quantile(q=0.25)
        d35_1quartil = d35_serie.quantile(q=0.25)
        d36_1quartil = d36_serie.quantile(q=0.25)
        d37_1quartil = d37_serie.quantile(q=0.25)
        d38_1quartil = d38_serie.quantile(q=0.25)
        d39_1quartil = d39_serie.quantile(q=0.25)
        d40_1quartil = d40_serie.quantile(q=0.25)
        d41_1quartil = d41_serie.quantile(q=0.25)
        d42_1quartil = d42_serie.quantile(q=0.25)
        d43_1quartil = d43_serie.quantile(q=0.25)
        d44_1quartil = d44_serie.quantile(q=0.25)
        d45_1quartil = d45_serie.quantile(q=0.25)
        d46_1quartil = d46_serie.quantile(q=0.25)
        d47_1quartil = d47_serie.quantile(q=0.25)
        d48_1quartil = d48_serie.quantile(q=0.25)
        d49_1quartil = d49_serie.quantile(q=0.25)
        d50_1quartil = d50_serie.quantile(q=0.25)
        #Cálculo da Mediana
        d1_mediana = d1_serie.median()
        d2_mediana = d2_serie.median()
        d3_mediana = d3_serie.median()
        d4_mediana = d4_serie.median()
        d5_mediana = d5_serie.median()
        d6_mediana = d6_serie.median()
        d7_mediana = d7_serie.median()
        d8_mediana = d8_serie.median()
        d9_mediana = d9_serie.median()
        d10_mediana = d10_serie.median()
        d11_mediana = d11_serie.median()
        d12_mediana = d12_serie.median()
        d13_mediana = d13_serie.median()
        d14_mediana = d14_serie.median()
        d15_mediana = d15_serie.median()
        d16_mediana = d16_serie.median()
        d17_mediana = d17_serie.median()
        d18_mediana = d18_serie.median()
        d19_mediana = d19_serie.median()
        d20_mediana = d20_serie.median()
        d21_mediana = d21_serie.median()
        d22_mediana = d22_serie.median()
        d23_mediana = d23_serie.median()
        d24_mediana = d24_serie.median()
        d25_mediana = d25_serie.median()
        d26_mediana = d26_serie.median()
        d27_mediana = d27_serie.median()
        d28_mediana = d28_serie.median()
        d29_mediana = d29_serie.median()
        d30_mediana = d30_serie.median()
        d31_mediana = d31_serie.median()
        d32_mediana = d32_serie.median()
        d33_mediana = d33_serie.median()
        d34_mediana = d34_serie.median()
        d35_mediana = d35_serie.median()
        d36_mediana = d36_serie.median()
        d37_mediana = d37_serie.median()
        d38_mediana = d38_serie.median()
        d39_mediana = d39_serie.median()
        d40_mediana = d40_serie.median()
        d41_mediana = d41_serie.median()
        d42_mediana = d42_serie.median()
        d43_mediana = d43_serie.median()
        d44_mediana = d44_serie.median()
        d45_mediana = d45_serie.median()
        d46_mediana = d46_serie.median()
        d47_mediana = d47_serie.median()
        d48_mediana = d48_serie.median()
        d49_mediana = d49_serie.median()
        d50_mediana = d50_serie.median()
        
        #Cálculo do 3º Quartil
        d1_3quartil = d1_serie.quantile(q=0.75)
        d2_3quartil = d2_serie.quantile(q=0.75)
        d3_3quartil = d3_serie.quantile(q=0.75)
        d4_3quartil = d4_serie.quantile(q=0.75)
        d5_3quartil = d5_serie.quantile(q=0.75)
        d6_3quartil = d6_serie.quantile(q=0.75)
        d7_3quartil = d7_serie.quantile(q=0.75)
        d8_3quartil = d8_serie.quantile(q=0.75)
        d9_3quartil = d9_serie.quantile(q=0.75)
        d10_3quartil = d10_serie.quantile(q=0.75)
        d11_3quartil = d11_serie.quantile(q=0.75)
        d12_3quartil = d12_serie.quantile(q=0.75)
        d13_3quartil = d13_serie.quantile(q=0.75)
        d14_3quartil = d14_serie.quantile(q=0.75)
        d15_3quartil = d15_serie.quantile(q=0.75)
        d16_3quartil = d16_serie.quantile(q=0.75)
        d17_3quartil = d17_serie.quantile(q=0.75)
        d18_3quartil = d18_serie.quantile(q=0.75)
        d19_3quartil = d19_serie.quantile(q=0.75)
        d20_3quartil = d20_serie.quantile(q=0.75)
        d21_3quartil = d21_serie.quantile(q=0.75)
        d22_3quartil = d22_serie.quantile(q=0.75)
        d23_3quartil = d23_serie.quantile(q=0.75)
        d24_3quartil = d24_serie.quantile(q=0.75)
        d25_3quartil = d25_serie.quantile(q=0.75)
        d26_3quartil = d26_serie.quantile(q=0.75)
        d27_3quartil = d27_serie.quantile(q=0.75)
        d28_3quartil = d28_serie.quantile(q=0.75)
        d29_3quartil = d29_serie.quantile(q=0.75)
        d30_3quartil = d30_serie.quantile(q=0.75)
        d31_3quartil = d31_serie.quantile(q=0.75)
        d32_3quartil = d32_serie.quantile(q=0.75)
        d33_3quartil = d33_serie.quantile(q=0.75)
        d34_3quartil = d34_serie.quantile(q=0.75)
        d35_3quartil = d35_serie.quantile(q=0.75)
        d36_3quartil = d36_serie.quantile(q=0.75)
        d37_3quartil = d37_serie.quantile(q=0.75)
        d38_3quartil = d38_serie.quantile(q=0.75)
        d39_3quartil = d39_serie.quantile(q=0.75)
        d40_3quartil = d40_serie.quantile(q=0.75)
        d41_3quartil = d41_serie.quantile(q=0.75)
        d42_3quartil = d42_serie.quantile(q=0.75)
        d43_3quartil = d43_serie.quantile(q=0.75)
        d44_3quartil = d44_serie.quantile(q=0.75)
        d45_3quartil = d45_serie.quantile(q=0.75)
        d46_3quartil = d46_serie.quantile(q=0.75)
        d47_3quartil = d47_serie.quantile(q=0.75)
        d48_3quartil = d48_serie.quantile(q=0.75)
        d49_3quartil = d49_serie.quantile(q=0.75)
        d50_3quartil = d50_serie.quantile(q=0.75)
                
        # MEDIDAS DE DISPERSÃO
        
        #Cálculo do Desvio Padrão        
        x1 =  len(l1)
        soma1 = 0
        for valor in l1:
            soma1 = soma1 + (valor - d1_serie.mean())**2
        d1_desviopadrao = math.sqrt(soma1/x1)
      
        x2 = len(l2)    
        soma2 = 0
        for valor in l2:
            soma2 = soma2 + (valor - d2_serie.mean())**2
        d2_desviopadrao = math.sqrt(soma2/x2)
                
        x3 = len(l3)  
        soma3 = 0
        for valor in l3:
            soma3 = soma3 + (valor - d3_serie.mean())**2
        d3_desviopadrao = math.sqrt(soma3/x3)
        
        x4 =  len(l4)
        soma4 = 0
        for valor in l4:
            soma4 = soma4 + (valor - d4_serie.mean())**2
        d4_desviopadrao = math.sqrt(soma4/x4)
      
        x5 = len(l5)    
        soma5 = 0
        for valor in l5:
            soma5 = soma5 + (valor - d5_serie.mean())**2
        d5_desviopadrao = math.sqrt(soma5/x5)
                
        x6 = len(l6)  
        soma6 = 0
        for valor in l6:
            soma6 = soma6 + (valor - d6_serie.mean())**2
        d6_desviopadrao = math.sqrt(soma6/x6)
        
        x7 =  len(l7)
        soma7 = 0
        for valor in l7:
            soma7 = soma7 + (valor - d7_serie.mean())**2
        d7_desviopadrao = math.sqrt(soma7/x7)
      
        x8 = len(l8)    
        soma8 = 0
        for valor in l8:
            soma8 = soma8 + (valor - d8_serie.mean())**2
        d8_desviopadrao = math.sqrt(soma8/x8)
                
        x9 = len(l9)  
        soma9 = 0
        for valor in l9:
            soma9 = soma9 + (valor - d9_serie.mean())**2
        d9_desviopadrao = math.sqrt(soma9/x9)
        
        x10 = len(l10)  
        soma10 = 0
        for valor in l10:
            soma10 = soma10 + (valor - d10_serie.mean())**2
        d10_desviopadrao = math.sqrt(soma10/x10)
        
        ####################################################
        x11 =  len(l11)
        soma11 = 0
        for valor in l11:
            soma11 = soma11 + (valor - d11_serie.mean())**2
        d11_desviopadrao = math.sqrt(soma11/x11)
      
        x12 = len(l12)    
        soma12 = 0
        for valor in l12:
            soma12 = soma12 + (valor - d12_serie.mean())**2
        d12_desviopadrao = math.sqrt(soma12/x12)
                
        x13 = len(l13)  
        soma13 = 0
        for valor in l13:
            soma13 = soma13 + (valor - d13_serie.mean())**2
        d13_desviopadrao = math.sqrt(soma13/x13)
        
        x14 =  len(l14)
        soma14 = 0
        for valor in l14:
            soma14 = soma14 + (valor - d14_serie.mean())**2
        d14_desviopadrao = math.sqrt(soma14/x14)
      
        x15 = len(l15)    
        soma15 = 0
        for valor in l15:
            soma15 = soma15 + (valor - d15_serie.mean())**2
        d15_desviopadrao = math.sqrt(soma15/x15)
                
        x16 = len(l16)  
        soma16 = 0
        for valor in l16:
            soma16 = soma16 + (valor - d16_serie.mean())**2
        d16_desviopadrao = math.sqrt(soma16/x16)
        
        x17 =  len(l17)
        soma17 = 0
        for valor in l17:
            soma17 = soma17 + (valor - d17_serie.mean())**2
        d17_desviopadrao = math.sqrt(soma17/x17)
      
        x18 = len(l18)    
        soma18 = 0
        for valor in l18:
            soma18 = soma18 + (valor - d18_serie.mean())**2
        d18_desviopadrao = math.sqrt(soma18/x18)
                
        x19 = len(l19)  
        soma19 = 0
        for valor in l19:
            soma19 = soma19 + (valor - d19_serie.mean())**2
        d19_desviopadrao = math.sqrt(soma19/x19)
        
        x20 = len(l20)  
        soma20 = 0
        for valor in l20:
            soma20 = soma20 + (valor - d20_serie.mean())**2
        d20_desviopadrao = math.sqrt(soma20/x20)
        
        ####################################################
        x21 =  len(l21)
        soma21 = 0
        for valor in l21:
            soma21 = soma21 + (valor - d21_serie.mean())**2
        d21_desviopadrao = math.sqrt(soma21/x21)
      
        x22 = len(l22)    
        soma22 = 0
        for valor in l22:
            soma22 = soma22 + (valor - d22_serie.mean())**2
        d22_desviopadrao = math.sqrt(soma22/x22)
                
        x23 = len(l23)  
        soma23 = 0
        for valor in l23:
            soma23 = soma23 + (valor - d23_serie.mean())**2
        d23_desviopadrao = math.sqrt(soma23/x23)
        
        x24 =  len(l24)
        soma24 = 0
        for valor in l24:
            soma24 = soma24 + (valor - d24_serie.mean())**2
        d24_desviopadrao = math.sqrt(soma24/x24)
      
        x25 = len(l25)    
        soma25 = 0
        for valor in l25:
            soma25 = soma25 + (valor - d25_serie.mean())**2
        d25_desviopadrao = math.sqrt(soma25/x25)
                
        x26 = len(l26)  
        soma26 = 0
        for valor in l26:
            soma26 = soma26 + (valor - d26_serie.mean())**2
        d26_desviopadrao = math.sqrt(soma26/x26)
        
        x27 =  len(l27)
        soma27 = 0
        for valor in l27:
            soma27 = soma27 + (valor - d27_serie.mean())**2
        d27_desviopadrao = math.sqrt(soma27/x27)
      
        x28 = len(l28)    
        soma28 = 0
        for valor in l28:
            soma28 = soma28 + (valor - d28_serie.mean())**2
        d28_desviopadrao = math.sqrt(soma28/x28)
                
        x29 = len(l29)  
        soma29 = 0
        for valor in l29:
            soma29 = soma29 + (valor - d29_serie.mean())**2
        d29_desviopadrao = math.sqrt(soma29/x29)
        
        x30 = len(l30)  
        soma30 = 0
        for valor in l30:
            soma30 = soma30 + (valor - d30_serie.mean())**2
        d30_desviopadrao = math.sqrt(soma30/x30)
        
        ####################################################
        x31 =  len(l31)
        soma31 = 0
        for valor in l31:
            soma31 = soma31 + (valor - d31_serie.mean())**2
        d31_desviopadrao = math.sqrt(soma31/x31)
      
        x32 = len(l32)    
        soma32 = 0
        for valor in l32:
            soma32 = soma32 + (valor - d32_serie.mean())**2
        d32_desviopadrao = math.sqrt(soma32/x32)
                
        x33 = len(l33)  
        soma33 = 0
        for valor in l33:
            soma33 = soma33 + (valor - d33_serie.mean())**2
        d33_desviopadrao = math.sqrt(soma33/x33)
        
        x34 =  len(l34)
        soma34 = 0
        for valor in l34:
            soma34 = soma34 + (valor - d34_serie.mean())**2
        d34_desviopadrao = math.sqrt(soma34/x34)
      
        x35 = len(l35)    
        soma35 = 0
        for valor in l35:
            soma35 = soma35 + (valor - d35_serie.mean())**2
        d35_desviopadrao = math.sqrt(soma35/x35)
                
        x36 = len(l36)  
        soma36 = 0
        for valor in l36:
            soma36 = soma36 + (valor - d36_serie.mean())**2
        d36_desviopadrao = math.sqrt(soma36/x36)
        
        x37 =  len(l37)
        soma37 = 0
        for valor in l37:
            soma37 = soma37 + (valor - d37_serie.mean())**2
        d37_desviopadrao = math.sqrt(soma37/x37)
      
        x38 = len(l38)    
        soma38 = 0
        for valor in l38:
            soma38 = soma38 + (valor - d38_serie.mean())**2
        d38_desviopadrao = math.sqrt(soma38/x38)
                
        x39 = len(l39)  
        soma39 = 0
        for valor in l39:
            soma39 = soma39 + (valor - d39_serie.mean())**2
        d39_desviopadrao = math.sqrt(soma39/x39)
        
        x40 = len(l40)  
        soma40 = 0
        for valor in l40:
            soma40 = soma40 + (valor - d40_serie.mean())**2
        d40_desviopadrao = math.sqrt(soma40/x40)
        
        ####################################################
        x41 =  len(l41)
        soma41 = 0
        for valor in l41:
            soma41 = soma41 + (valor - d41_serie.mean())**2
        d41_desviopadrao = math.sqrt(soma41/x41)
      
        x42 = len(l42)    
        soma42 = 0
        for valor in l42:
            soma42 = soma42 + (valor - d42_serie.mean())**2
        d42_desviopadrao = math.sqrt(soma42/x42)
                
        x43 = len(l43)  
        soma43 = 0
        for valor in l43:
            soma43 = soma43 + (valor - d43_serie.mean())**2
        d43_desviopadrao = math.sqrt(soma43/x43)
        
        x44 =  len(l44)
        soma44 = 0
        for valor in l44:
            soma44 = soma44 + (valor - d44_serie.mean())**2
        d44_desviopadrao = math.sqrt(soma44/x44)
      
        x45 = len(l45)    
        soma45 = 0
        for valor in l45:
            soma45 = soma45 + (valor - d45_serie.mean())**2
        d45_desviopadrao = math.sqrt(soma45/x45)
                
        x46 = len(l46)  
        soma46 = 0
        for valor in l46:
            soma46 = soma46 + (valor - d46_serie.mean())**2
        d46_desviopadrao = math.sqrt(soma46/x46)
        
        x47 =  len(l47)
        soma47 = 0
        for valor in l47:
            soma47 = soma47 + (valor - d47_serie.mean())**2
        d47_desviopadrao = math.sqrt(soma47/x47)
      
        x48 = len(l48)    
        soma48 = 0
        for valor in l48:
            soma48 = soma48 + (valor - d48_serie.mean())**2
        d48_desviopadrao = math.sqrt(soma48/x48)
                
        x49 = len(l49)  
        soma49 = 0
        for valor in l49:
            soma49 = soma49 + (valor - d49_serie.mean())**2
        d49_desviopadrao = math.sqrt(soma49/x49)
        
        x50 = len(l50)  
        soma50 = 0
        for valor in l50:
            soma50 = soma50 + (valor - d50_serie.mean())**2
        d50_desviopadrao = math.sqrt(soma50/x50)
        
        ####################################################
            
        #Cálculo da Amplitude        
        d1_amplitude = (d1_serie.max() - d1_serie.min())
        d2_amplitude = (d2_serie.max() - d2_serie.min())
        d3_amplitude = (d3_serie.max() - d3_serie.min())
        d4_amplitude = (d4_serie.max() - d4_serie.min())
        d5_amplitude = (d5_serie.max() - d5_serie.min())
        d6_amplitude = (d6_serie.max() - d6_serie.min())
        d7_amplitude = (d7_serie.max() - d7_serie.min())
        d8_amplitude = (d8_serie.max() - d8_serie.min())
        d9_amplitude = (d9_serie.max() - d9_serie.min())
        d10_amplitude = (d10_serie.max() - d10_serie.min())
        d11_amplitude = (d11_serie.max() - d11_serie.min())
        d12_amplitude = (d12_serie.max() - d12_serie.min())
        d13_amplitude = (d13_serie.max() - d13_serie.min())
        d14_amplitude = (d14_serie.max() - d14_serie.min())
        d15_amplitude = (d15_serie.max() - d15_serie.min())
        d16_amplitude = (d16_serie.max() - d16_serie.min())
        d17_amplitude = (d17_serie.max() - d17_serie.min())
        d18_amplitude = (d18_serie.max() - d18_serie.min())
        d19_amplitude = (d19_serie.max() - d19_serie.min())
        d20_amplitude = (d20_serie.max() - d20_serie.min())
        d21_amplitude = (d21_serie.max() - d21_serie.min())
        d22_amplitude = (d22_serie.max() - d22_serie.min())
        d23_amplitude = (d23_serie.max() - d23_serie.min())
        d24_amplitude = (d24_serie.max() - d24_serie.min())
        d25_amplitude = (d25_serie.max() - d25_serie.min())
        d26_amplitude = (d26_serie.max() - d26_serie.min())
        d27_amplitude = (d27_serie.max() - d27_serie.min())
        d28_amplitude = (d28_serie.max() - d28_serie.min())
        d29_amplitude = (d29_serie.max() - d29_serie.min())
        d30_amplitude = (d30_serie.max() - d30_serie.min())
        d31_amplitude = (d31_serie.max() - d31_serie.min())
        d32_amplitude = (d32_serie.max() - d32_serie.min())
        d33_amplitude = (d33_serie.max() - d33_serie.min())
        d34_amplitude = (d34_serie.max() - d34_serie.min())
        d35_amplitude = (d35_serie.max() - d35_serie.min())
        d36_amplitude = (d36_serie.max() - d36_serie.min())
        d37_amplitude = (d37_serie.max() - d37_serie.min())
        d38_amplitude = (d38_serie.max() - d38_serie.min())
        d39_amplitude = (d39_serie.max() - d39_serie.min())
        d40_amplitude = (d40_serie.max() - d40_serie.min())
        d41_amplitude = (d41_serie.max() - d41_serie.min())
        d42_amplitude = (d42_serie.max() - d42_serie.min())
        d43_amplitude = (d43_serie.max() - d43_serie.min())
        d44_amplitude = (d44_serie.max() - d44_serie.min())
        d45_amplitude = (d45_serie.max() - d45_serie.min())
        d46_amplitude = (d46_serie.max() - d46_serie.min())
        d47_amplitude = (d47_serie.max() - d47_serie.min())
        d48_amplitude = (d48_serie.max() - d48_serie.min())
        d49_amplitude = (d49_serie.max() - d49_serie.min())
        d50_amplitude = (d50_serie.max() - d50_serie.min())
        
        return (d1_media, d2_media, d3_media, d4_media, d5_media, d6_media, d7_media, d8_media, d9_media, d10_media, d11_media, d12_media, d13_media, d14_media, d15_media, d16_media, d17_media, d18_media, d19_media, d20_media, d21_media, d22_media, d23_media, d24_media, d25_media, d26_media, d27_media, d28_media, d29_media, d30_media, d31_media, d32_media, d33_media, d34_media, d35_media, d36_media, d37_media, d38_media, d39_media, d40_media, d41_media, d42_media, d43_media, d44_media, d45_media, d46_media, d47_media, d48_media, d49_media, d50_media, d1_1quartil, d2_1quartil, d3_1quartil, d4_1quartil, d5_1quartil, d6_1quartil, d7_1quartil, d8_1quartil, d9_1quartil, d10_1quartil, d11_1quartil, d12_1quartil, d13_1quartil, d14_1quartil, d15_1quartil, d16_1quartil, d17_1quartil, d18_1quartil, d19_1quartil, d20_1quartil, d21_1quartil, d22_1quartil, d23_1quartil, d24_1quartil, d25_1quartil, d26_1quartil, d27_1quartil, d28_1quartil, d29_1quartil, d30_1quartil, d31_1quartil, d32_1quartil, d33_1quartil, d34_1quartil, d35_1quartil, d36_1quartil, d37_1quartil, d38_1quartil, d39_1quartil, d40_1quartil, d41_1quartil, d42_1quartil, d43_1quartil, d44_1quartil, d45_1quartil, d46_1quartil, d47_1quartil, d48_1quartil, d49_1quartil, d50_1quartil, d1_mediana, d2_mediana, d3_mediana, d4_mediana, d5_mediana, d6_mediana, d7_mediana, d8_mediana, d9_mediana, d10_mediana, d11_mediana, d12_mediana, d13_mediana, d14_mediana, d15_mediana, d16_mediana, d17_mediana, d18_mediana, d19_mediana, d20_mediana, d21_mediana, d22_mediana, d23_mediana, d24_mediana, d25_mediana, d26_mediana, d27_mediana, d28_mediana, d29_mediana, d30_mediana, d31_mediana, d32_mediana, d33_mediana, d34_mediana, d35_mediana, d36_mediana, d37_mediana, d38_mediana, d39_mediana, d40_mediana, d41_mediana, d42_mediana, d43_mediana, d44_mediana, d45_mediana, d46_mediana, d47_mediana, d48_mediana, d49_mediana, d50_mediana, d1_3quartil, d2_3quartil, d3_3quartil, d4_3quartil, d5_3quartil, d6_3quartil, d7_3quartil, d8_3quartil, d9_3quartil, d10_3quartil, d11_3quartil, d12_3quartil, d13_3quartil, d14_3quartil, d15_3quartil, d16_3quartil, d17_3quartil, d18_3quartil, d19_3quartil, d20_3quartil, d21_3quartil, d22_3quartil, d23_3quartil, d24_3quartil, d25_3quartil, d26_3quartil, d27_3quartil, d28_3quartil, d29_3quartil, d30_3quartil, d31_3quartil, d32_3quartil, d33_3quartil, d34_3quartil, d35_3quartil, d36_3quartil, d37_3quartil, d38_3quartil, d39_3quartil, d40_3quartil, d41_3quartil, d42_3quartil, d43_3quartil, d44_3quartil, d45_3quartil, d46_3quartil, d47_3quartil, d48_3quartil, d49_3quartil, d50_3quartil, d1_desviopadrao, d2_desviopadrao, d3_desviopadrao, d4_desviopadrao, d5_desviopadrao, d6_desviopadrao, d7_desviopadrao, d8_desviopadrao, d9_desviopadrao, d10_desviopadrao, d11_desviopadrao, d12_desviopadrao, d13_desviopadrao, d14_desviopadrao, d15_desviopadrao, d16_desviopadrao, d17_desviopadrao, d18_desviopadrao, d19_desviopadrao, d20_desviopadrao, d21_desviopadrao, d22_desviopadrao, d23_desviopadrao, d24_desviopadrao, d25_desviopadrao, d26_desviopadrao, d27_desviopadrao, d28_desviopadrao, d29_desviopadrao, d30_desviopadrao, d31_desviopadrao, d32_desviopadrao, d33_desviopadrao, d34_desviopadrao, d35_desviopadrao, d36_desviopadrao, d37_desviopadrao, d38_desviopadrao, d39_desviopadrao, d40_desviopadrao, d41_desviopadrao, d42_desviopadrao, d43_desviopadrao, d44_desviopadrao, d45_desviopadrao, d46_desviopadrao, d47_desviopadrao, d48_desviopadrao, d49_desviopadrao, d50_desviopadrao, d1_amplitude, d2_amplitude, d3_amplitude, d4_amplitude, d5_amplitude, d6_amplitude, d7_amplitude, d8_amplitude, d9_amplitude, d10_amplitude, d11_amplitude, d12_amplitude, d13_amplitude, d14_amplitude, d15_amplitude, d16_amplitude, d17_amplitude, d18_amplitude, d19_amplitude, d20_amplitude, d21_amplitude, d22_amplitude, d23_amplitude, d24_amplitude, d25_amplitude, d26_amplitude, d27_amplitude, d28_amplitude, d29_amplitude, d30_amplitude, d31_amplitude, d32_amplitude, d33_amplitude, d34_amplitude, d35_amplitude, d36_amplitude, d37_amplitude, d38_amplitude, d39_amplitude, d40_amplitude, d41_amplitude, d42_amplitude, d43_amplitude, d44_amplitude, d45_amplitude, d46_amplitude, d47_amplitude, d48_amplitude, d49_amplitude, d50_amplitude)
        
    #Construindo função para receber variáveis e concatená-las com SQL
    def queryTweetbyuser (u):        
        return ("SELECT TweetID,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20,D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,D32,D33,D34,D35,D36,D37,D38,D39,D40,D41,D42,D43,D44,D45,D46,D47,D48,D49,D50 FROM legitimate_users_tweets_original WHERE UserID = "+ str(u))
    
    def buildQuery (u,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,c39,c40,c41,c42,c43,c44,c45,c46,c47,c48,c49,c50,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,i41,i42,i43,i44,i45,i46,i47,i48,i49,i50,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16,o17,o18,o19,o20,o21,o22,o23,o24,o25,o26,o27,o28,o29,o30,o31,o32,o33,o34,o35,o36,o37,o38,o39,o40,o41,o42,o43,o44,o45,o46,o47,o48,o49,o50):        
        #Jeferson Begin
        #return ("UPDATE legitimate_users_sbseg SET D1_media = "+ str(a1)+", D2_media = "+ str(a2)+", D3_media = "+ str(a3)+", D4_media = "+ str(a4)+", D5_media = "+ str(a5)+", D6_media = "+ str(a6)+", D7_media = "+ str(a7)+", D8_media = "+ str(a8)+", D9_media = "+ str(a9)+", D10_media = "+ str(10)+", D11_media = "+ str(a11)+", D12_media = "+ str(a12)+", D13_media = "+ str(a13)+", D14_media = "+ str(a14)+", D15_media = "+ str(a15)+", D16_media = "+ str(a16)+", D17_media = "+ str(a17)+", D18_media = "+ str(a18)+", D19_media = "+ str(a19)+", D20_media = "+ str(a20)+", D21_media = "+ str(a21)+", D22_media = "+ str(a22)+", D23_media = "+ str(a23)+", D24_media = "+ str(a24)+", D25_media = "+ str(a25)+", D26_media = "+ str(a26)+", D27_media = "+ str(a27)+", D28_media = "+ str(a28)+", D29_media = "+ str(a29)+", D30_media = "+ str(a30)+", D31_media = "+ str(a31)+", D32_media = "+ str(a32)+", D33_media = "+ str(a33)+", D34_media = "+ str(a34)+", D35_media = "+ str(a35)+", D36_media = "+ str(a36)+", D37_media = "+ str(a37)+", D38_media = "+ str(a38)+", D39_media = "+ str(a39)+", D40_media = "+ str(a40)+", D41_media = "+ str(a41)+", D42_media = "+ str(a42)+", D43_media = "+ str(a43)+", D44_media = "+ str(a44)+", D45_media = "+ str(a45)+", D46_media = "+ str(a46)+", D47_media = "+ str(a47)+", D48_media = "+ str(a48)+", D49_media = "+ str(a49)+", D50_media = "+ str(a50)+", D1_1quartil = "+ str(b1)+", D2_1quartil = "+ str(b2)+", D3_1quartil = "+ str(b3)+", D4_1quartil = "+ str(b4)+", D5_1quartil = "+ str(b5)+", D6_1quartil = "+ str(b6)+", D7_1quartil = "+ str(b7)+", D8_1quartil = "+ str(b8)+", D9_1quartil = "+ str(b9)+", D10_1quartil = "+ str(10)+", D11_1quartil = "+ str(b11)+", D12_1quartil = "+ str(b12)+", D13_1quartil = "+ str(b13)+", D14_1quartil = "+ str(b14)+", D15_1quartil = "+ str(b15)+", D16_1quartil = "+ str(b16)+", D17_1quartil = "+ str(b17)+", D18_1quartil = "+ str(b18)+", D19_1quartil = "+ str(b19)+", D20_1quartil = "+ str(b20)+", D21_1quartil = "+ str(b21)+", D22_1quartil = "+ str(b22)+", D23_1quartil = "+ str(b23)+", D24_1quartil = "+ str(b24)+", D25_1quartil = "+ str(b25)+", D26_1quartil = "+ str(b26)+", D27_1quartil = "+ str(b27)+", D28_1quartil = "+ str(b28)+", D29_1quartil = "+ str(b29)+", D30_1quartil = "+ str(b30)+", D31_1quartil = "+ str(b31)+", D32_1quartil = "+ str(b32)+", D33_1quartil = "+ str(b33)+", D34_1quartil = "+ str(b34)+", D35_1quartil = "+ str(b35)+", D36_1quartil = "+ str(b36)+", D37_1quartil = "+ str(b37)+", D38_1quartil = "+ str(b38)+", D39_1quartil = "+ str(b39)+", D40_1quartil = "+ str(b40)+", D41_1quartil = "+ str(b41)+", D42_1quartil = "+ str(b42)+", D43_1quartil = "+ str(b43)+", D44_1quartil = "+ str(b44)+", D45_1quartil = "+ str(b45)+", D46_1quartil = "+ str(b46)+", D47_1quartil = "+ str(b47)+", D48_1quartil = "+ str(b48)+", D49_1quartil = "+ str(b49)+", D50_1quartil = "+ str(b50)+", D1_mediana = "+ str(c1)+", D2_mediana = "+ str(c2)+", D3_mediana = "+ str(c3)+", D4_mediana = "+ str(c4)+", D5_mediana = "+ str(c5)+", D6_mediana = "+ str(c6)+", D7_mediana = "+ str(c7)+", D8_mediana = "+ str(c8)+", D9_mediana = "+ str(c9)+", D10_mediana = "+ str(10)+", D11_mediana = "+ str(c11)+", D12_mediana = "+ str(c12)+", D13_mediana = "+ str(c13)+", D14_mediana = "+ str(c14)+", D15_mediana = "+ str(c15)+", D16_mediana = "+ str(c16)+", D17_mediana = "+ str(c17)+", D18_mediana = "+ str(c18)+", D19_mediana = "+ str(c19)+", D20_mediana = "+ str(c20)+", D21_mediana = "+ str(c21)+", D22_mediana = "+ str(c22)+", D23_mediana = "+ str(c23)+", D24_mediana = "+ str(c24)+", D25_mediana = "+ str(c25)+", D26_mediana = "+ str(c26)+", D27_mediana = "+ str(c27)+", D28_mediana = "+ str(c28)+", D29_mediana = "+ str(c29)+", D30_mediana = "+ str(c30)+", D31_mediana = "+ str(c31)+", D32_mediana = "+ str(c32)+", D33_mediana = "+ str(c33)+", D34_mediana = "+ str(c34)+", D35_mediana = "+ str(c35)+", D36_mediana = "+ str(c36)+", D37_mediana = "+ str(c37)+", D38_mediana = "+ str(c38)+", D39_mediana = "+ str(c39)+", D40_mediana = "+ str(c40)+", D41_mediana = "+ str(c41)+", D42_mediana = "+ str(c42)+", D43_mediana = "+ str(c43)+", D44_mediana = "+ str(c44)+", D45_mediana = "+ str(c45)+", D46_mediana = "+ str(c46)+", D47_mediana = "+ str(c47)+", D48_mediana = "+ str(c48)+", D49_mediana = "+ str(c49)+", D50_mediana = "+ str(c50)+", D1_3quartil = "+ str(e1)+", D2_3quartil = "+ str(e2)+", D3_3quartil = "+ str(e3)+", D4_3quartil = "+ str(e4)+", D5_3quartil = "+ str(e5)+", D6_3quartil = "+ str(e6)+", D7_3quartil = "+ str(e7)+", D8_3quartil = "+ str(e8)+", D9_3quartil = "+ str(e9)+", D10_3quartil = "+ str(10)+", D11_3quartil = "+ str(e11)+", D12_3quartil = "+ str(e12)+", D13_3quartil = "+ str(e13)+", D14_3quartil = "+ str(e14)+", D15_3quartil = "+ str(e15)+", D16_3quartil = "+ str(e16)+", D17_3quartil = "+ str(e17)+", D18_3quartil = "+ str(e18)+", D19_3quartil = "+ str(e19)+", D20_3quartil = "+ str(e20)+", D21_3quartil = "+ str(e21)+", D22_3quartil = "+ str(e22)+", D23_3quartil = "+ str(e23)+", D24_3quartil = "+ str(e24)+", D25_3quartil = "+ str(e25)+", D26_3quartil = "+ str(e26)+", D27_3quartil = "+ str(e27)+", D28_3quartil = "+ str(e28)+", D29_3quartil = "+ str(e29)+", D30_3quartil = "+ str(e30)+", D31_3quartil = "+ str(e31)+", D32_3quartil = "+ str(e32)+", D33_3quartil = "+ str(e33)+", D34_3quartil = "+ str(e34)+", D35_3quartil = "+ str(e35)+", D36_3quartil = "+ str(e36)+", D37_3quartil = "+ str(e37)+", D38_3quartil = "+ str(e38)+", D39_3quartil = "+ str(e39)+", D40_3quartil = "+ str(e40)+", D41_3quartil = "+ str(e41)+", D42_3quartil = "+ str(e42)+", D43_3quartil = "+ str(e43)+", D44_3quartil = "+ str(e44)+", D45_3quartil = "+ str(e45)+", D46_3quartil = "+ str(e46)+", D47_3quartil = "+ str(e47)+", D48_3quartil = "+ str(e48)+", D49_3quartil = "+ str(e49)+", D50_3quartil = "+ str(e50)+", D1_desviopadrao = "+ str(i1)+", D2_desviopadrao = "+ str(i2)+", D3_desviopadrao = "+ str(i3)+", D4_desviopadrao = "+ str(i4)+", D5_desviopadrao = "+ str(i5)+", D6_desviopadrao = "+ str(i6)+", D7_desviopadrao = "+ str(i7)+", D8_desviopadrao = "+ str(i8)+", D9_desviopadrao = "+ str(i9)+", D10_desviopadrao = "+ str(10)+", D11_desviopadrao = "+ str(i11)+", D12_desviopadrao = "+ str(i12)+", D13_desviopadrao = "+ str(i13)+", D14_desviopadrao = "+ str(i14)+", D15_desviopadrao = "+ str(i15)+", D16_desviopadrao = "+ str(i16)+", D17_desviopadrao = "+ str(i17)+", D18_desviopadrao = "+ str(i18)+", D19_desviopadrao = "+ str(i19)+", D20_desviopadrao = "+ str(i20)+", D21_desviopadrao = "+ str(i21)+", D22_desviopadrao = "+ str(i22)+", D23_desviopadrao = "+ str(i23)+", D24_desviopadrao = "+ str(i24)+", D25_desviopadrao = "+ str(i25)+", D26_desviopadrao = "+ str(i26)+", D27_desviopadrao = "+ str(i27)+", D28_desviopadrao = "+ str(i28)+", D29_desviopadrao = "+ str(i29)+", D30_desviopadrao = "+ str(i30)+", D31_desviopadrao = "+ str(i31)+", D32_desviopadrao = "+ str(i32)+", D33_desviopadrao = "+ str(i33)+", D34_desviopadrao = "+ str(i34)+", D35_desviopadrao = "+ str(i35)+", D36_desviopadrao = "+ str(i36)+", D37_desviopadrao = "+ str(i37)+", D38_desviopadrao = "+ str(i38)+", D39_desviopadrao = "+ str(i39)+", D40_desviopadrao = "+ str(i40)+", D41_desviopadrao = "+ str(i41)+", D42_desviopadrao = "+ str(i42)+", D43_desviopadrao = "+ str(i43)+", D44_desviopadrao = "+ str(i44)+", D45_desviopadrao = "+ str(i45)+", D46_desviopadrao = "+ str(i46)+", D47_desviopadrao = "+ str(i47)+", D48_desviopadrao = "+ str(i48)+", D49_desviopadrao = "+ str(i49)+", D50_desviopadrao = "+ str(i50)+", D1_amplitude = "+ str(o1)+", D2_amplitude = "+ str(o2)+", D3_amplitude = "+ str(o3)+", D4_amplitude = "+ str(o4)+", D5_amplitude = "+ str(o5)+", D6_amplitude = "+ str(o6)+", D7_amplitude = "+ str(o7)+", D8_amplitude = "+ str(o8)+", D9_amplitude = "+ str(o9)+", D10_amplitude = "+ str(10)+", D11_amplitude = "+ str(o11)+", D12_amplitude = "+ str(o12)+", D13_amplitude = "+ str(o13)+", D14_amplitude = "+ str(o14)+", D15_amplitude = "+ str(o15)+", D16_amplitude = "+ str(o16)+", D17_amplitude = "+ str(o17)+", D18_amplitude = "+ str(o18)+", D19_amplitude = "+ str(o19)+", D20_amplitude = "+ str(o20)+", D21_amplitude = "+ str(o21)+", D22_amplitude = "+ str(o22)+", D23_amplitude = "+ str(o23)+", D24_amplitude = "+ str(o24)+", D25_amplitude = "+ str(o25)+", D26_amplitude = "+ str(o26)+", D27_amplitude = "+ str(o27)+", D28_amplitude = "+ str(o28)+", D29_amplitude = "+ str(o29)+", D30_amplitude = "+ str(o30)+", D31_amplitude = "+ str(o31)+", D32_amplitude = "+ str(o32)+", D33_amplitude = "+ str(o33)+", D34_amplitude = "+ str(o34)+", D35_amplitude = "+ str(o35)+", D36_amplitude = "+ str(o36)+", D37_amplitude = "+ str(o37)+", D38_amplitude = "+ str(o38)+", D39_amplitude = "+ str(o39)+", D40_amplitude = "+ str(o40)+", D41_amplitude = "+ str(o41)+", D42_amplitude = "+ str(o42)+", D43_amplitude = "+ str(o43)+", D44_amplitude = "+ str(o44)+", D45_amplitude = "+ str(o45)+", D46_amplitude = "+ str(o46)+", D47_amplitude = "+ str(o47)+", D48_amplitude = "+ str(o48)+", D49_amplitude = "+ str(o49)+", D50_amplitude = "+ str(o50)+", Update_Control3 = 1"+" WHERE UserID = "+ str(u))
        return ("UPDATE legitimate_users SET D1_media = "+ str(a1)+", D2_media = "+ str(a2)+", D3_media = "+ str(a3)+", D4_media = "+ str(a4)+", D5_media = "+ str(a5)+", D6_media = "+ str(a6)+", D7_media = "+ str(a7)+", D8_media = "+ str(a8)+", D9_media = "+ str(a9)+", D10_media = "+ str(10)+", D11_media = "+ str(a11)+", D12_media = "+ str(a12)+", D13_media = "+ str(a13)+", D14_media = "+ str(a14)+", D15_media = "+ str(a15)+", D16_media = "+ str(a16)+", D17_media = "+ str(a17)+", D18_media = "+ str(a18)+", D19_media = "+ str(a19)+", D20_media = "+ str(a20)+", D21_media = "+ str(a21)+", D22_media = "+ str(a22)+", D23_media = "+ str(a23)+", D24_media = "+ str(a24)+", D25_media = "+ str(a25)+", D26_media = "+ str(a26)+", D27_media = "+ str(a27)+", D28_media = "+ str(a28)+", D29_media = "+ str(a29)+", D30_media = "+ str(a30)+", D31_media = "+ str(a31)+", D32_media = "+ str(a32)+", D33_media = "+ str(a33)+", D34_media = "+ str(a34)+", D35_media = "+ str(a35)+", D36_media = "+ str(a36)+", D37_media = "+ str(a37)+", D38_media = "+ str(a38)+", D39_media = "+ str(a39)+", D40_media = "+ str(a40)+", D41_media = "+ str(a41)+", D42_media = "+ str(a42)+", D43_media = "+ str(a43)+", D44_media = "+ str(a44)+", D45_media = "+ str(a45)+", D46_media = "+ str(a46)+", D47_media = "+ str(a47)+", D48_media = "+ str(a48)+", D49_media = "+ str(a49)+", D50_media = "+ str(a50)+", D1_1quartil = "+ str(b1)+", D2_1quartil = "+ str(b2)+", D3_1quartil = "+ str(b3)+", D4_1quartil = "+ str(b4)+", D5_1quartil = "+ str(b5)+", D6_1quartil = "+ str(b6)+", D7_1quartil = "+ str(b7)+", D8_1quartil = "+ str(b8)+", D9_1quartil = "+ str(b9)+", D10_1quartil = "+ str(10)+", D11_1quartil = "+ str(b11)+", D12_1quartil = "+ str(b12)+", D13_1quartil = "+ str(b13)+", D14_1quartil = "+ str(b14)+", D15_1quartil = "+ str(b15)+", D16_1quartil = "+ str(b16)+", D17_1quartil = "+ str(b17)+", D18_1quartil = "+ str(b18)+", D19_1quartil = "+ str(b19)+", D20_1quartil = "+ str(b20)+", D21_1quartil = "+ str(b21)+", D22_1quartil = "+ str(b22)+", D23_1quartil = "+ str(b23)+", D24_1quartil = "+ str(b24)+", D25_1quartil = "+ str(b25)+", D26_1quartil = "+ str(b26)+", D27_1quartil = "+ str(b27)+", D28_1quartil = "+ str(b28)+", D29_1quartil = "+ str(b29)+", D30_1quartil = "+ str(b30)+", D31_1quartil = "+ str(b31)+", D32_1quartil = "+ str(b32)+", D33_1quartil = "+ str(b33)+", D34_1quartil = "+ str(b34)+", D35_1quartil = "+ str(b35)+", D36_1quartil = "+ str(b36)+", D37_1quartil = "+ str(b37)+", D38_1quartil = "+ str(b38)+", D39_1quartil = "+ str(b39)+", D40_1quartil = "+ str(b40)+", D41_1quartil = "+ str(b41)+", D42_1quartil = "+ str(b42)+", D43_1quartil = "+ str(b43)+", D44_1quartil = "+ str(b44)+", D45_1quartil = "+ str(b45)+", D46_1quartil = "+ str(b46)+", D47_1quartil = "+ str(b47)+", D48_1quartil = "+ str(b48)+", D49_1quartil = "+ str(b49)+", D50_1quartil = "+ str(b50)+", D1_mediana = "+ str(c1)+", D2_mediana = "+ str(c2)+", D3_mediana = "+ str(c3)+", D4_mediana = "+ str(c4)+", D5_mediana = "+ str(c5)+", D6_mediana = "+ str(c6)+", D7_mediana = "+ str(c7)+", D8_mediana = "+ str(c8)+", D9_mediana = "+ str(c9)+", D10_mediana = "+ str(10)+", D11_mediana = "+ str(c11)+", D12_mediana = "+ str(c12)+", D13_mediana = "+ str(c13)+", D14_mediana = "+ str(c14)+", D15_mediana = "+ str(c15)+", D16_mediana = "+ str(c16)+", D17_mediana = "+ str(c17)+", D18_mediana = "+ str(c18)+", D19_mediana = "+ str(c19)+", D20_mediana = "+ str(c20)+", D21_mediana = "+ str(c21)+", D22_mediana = "+ str(c22)+", D23_mediana = "+ str(c23)+", D24_mediana = "+ str(c24)+", D25_mediana = "+ str(c25)+", D26_mediana = "+ str(c26)+", D27_mediana = "+ str(c27)+", D28_mediana = "+ str(c28)+", D29_mediana = "+ str(c29)+", D30_mediana = "+ str(c30)+", D31_mediana = "+ str(c31)+", D32_mediana = "+ str(c32)+", D33_mediana = "+ str(c33)+", D34_mediana = "+ str(c34)+", D35_mediana = "+ str(c35)+", D36_mediana = "+ str(c36)+", D37_mediana = "+ str(c37)+", D38_mediana = "+ str(c38)+", D39_mediana = "+ str(c39)+", D40_mediana = "+ str(c40)+", D41_mediana = "+ str(c41)+", D42_mediana = "+ str(c42)+", D43_mediana = "+ str(c43)+", D44_mediana = "+ str(c44)+", D45_mediana = "+ str(c45)+", D46_mediana = "+ str(c46)+", D47_mediana = "+ str(c47)+", D48_mediana = "+ str(c48)+", D49_mediana = "+ str(c49)+", D50_mediana = "+ str(c50)+", D1_3quartil = "+ str(e1)+", D2_3quartil = "+ str(e2)+", D3_3quartil = "+ str(e3)+", D4_3quartil = "+ str(e4)+", D5_3quartil = "+ str(e5)+", D6_3quartil = "+ str(e6)+", D7_3quartil = "+ str(e7)+", D8_3quartil = "+ str(e8)+", D9_3quartil = "+ str(e9)+", D10_3quartil = "+ str(10)+", D11_3quartil = "+ str(e11)+", D12_3quartil = "+ str(e12)+", D13_3quartil = "+ str(e13)+", D14_3quartil = "+ str(e14)+", D15_3quartil = "+ str(e15)+", D16_3quartil = "+ str(e16)+", D17_3quartil = "+ str(e17)+", D18_3quartil = "+ str(e18)+", D19_3quartil = "+ str(e19)+", D20_3quartil = "+ str(e20)+", D21_3quartil = "+ str(e21)+", D22_3quartil = "+ str(e22)+", D23_3quartil = "+ str(e23)+", D24_3quartil = "+ str(e24)+", D25_3quartil = "+ str(e25)+", D26_3quartil = "+ str(e26)+", D27_3quartil = "+ str(e27)+", D28_3quartil = "+ str(e28)+", D29_3quartil = "+ str(e29)+", D30_3quartil = "+ str(e30)+", D31_3quartil = "+ str(e31)+", D32_3quartil = "+ str(e32)+", D33_3quartil = "+ str(e33)+", D34_3quartil = "+ str(e34)+", D35_3quartil = "+ str(e35)+", D36_3quartil = "+ str(e36)+", D37_3quartil = "+ str(e37)+", D38_3quartil = "+ str(e38)+", D39_3quartil = "+ str(e39)+", D40_3quartil = "+ str(e40)+", D41_3quartil = "+ str(e41)+", D42_3quartil = "+ str(e42)+", D43_3quartil = "+ str(e43)+", D44_3quartil = "+ str(e44)+", D45_3quartil = "+ str(e45)+", D46_3quartil = "+ str(e46)+", D47_3quartil = "+ str(e47)+", D48_3quartil = "+ str(e48)+", D49_3quartil = "+ str(e49)+", D50_3quartil = "+ str(e50)+", D1_desviopadrao = "+ str(i1)+", D2_desviopadrao = "+ str(i2)+", D3_desviopadrao = "+ str(i3)+", D4_desviopadrao = "+ str(i4)+", D5_desviopadrao = "+ str(i5)+", D6_desviopadrao = "+ str(i6)+", D7_desviopadrao = "+ str(i7)+", D8_desviopadrao = "+ str(i8)+", D9_desviopadrao = "+ str(i9)+", D10_desviopadrao = "+ str(10)+", D11_desviopadrao = "+ str(i11)+", D12_desviopadrao = "+ str(i12)+", D13_desviopadrao = "+ str(i13)+", D14_desviopadrao = "+ str(i14)+", D15_desviopadrao = "+ str(i15)+", D16_desviopadrao = "+ str(i16)+", D17_desviopadrao = "+ str(i17)+", D18_desviopadrao = "+ str(i18)+", D19_desviopadrao = "+ str(i19)+", D20_desviopadrao = "+ str(i20)+", D21_desviopadrao = "+ str(i21)+", D22_desviopadrao = "+ str(i22)+", D23_desviopadrao = "+ str(i23)+", D24_desviopadrao = "+ str(i24)+", D25_desviopadrao = "+ str(i25)+", D26_desviopadrao = "+ str(i26)+", D27_desviopadrao = "+ str(i27)+", D28_desviopadrao = "+ str(i28)+", D29_desviopadrao = "+ str(i29)+", D30_desviopadrao = "+ str(i30)+", D31_desviopadrao = "+ str(i31)+", D32_desviopadrao = "+ str(i32)+", D33_desviopadrao = "+ str(i33)+", D34_desviopadrao = "+ str(i34)+", D35_desviopadrao = "+ str(i35)+", D36_desviopadrao = "+ str(i36)+", D37_desviopadrao = "+ str(i37)+", D38_desviopadrao = "+ str(i38)+", D39_desviopadrao = "+ str(i39)+", D40_desviopadrao = "+ str(i40)+", D41_desviopadrao = "+ str(i41)+", D42_desviopadrao = "+ str(i42)+", D43_desviopadrao = "+ str(i43)+", D44_desviopadrao = "+ str(i44)+", D45_desviopadrao = "+ str(i45)+", D46_desviopadrao = "+ str(i46)+", D47_desviopadrao = "+ str(i47)+", D48_desviopadrao = "+ str(i48)+", D49_desviopadrao = "+ str(i49)+", D50_desviopadrao = "+ str(i50)+", D1_amplitude = "+ str(o1)+", D2_amplitude = "+ str(o2)+", D3_amplitude = "+ str(o3)+", D4_amplitude = "+ str(o4)+", D5_amplitude = "+ str(o5)+", D6_amplitude = "+ str(o6)+", D7_amplitude = "+ str(o7)+", D8_amplitude = "+ str(o8)+", D9_amplitude = "+ str(o9)+", D10_amplitude = "+ str(10)+", D11_amplitude = "+ str(o11)+", D12_amplitude = "+ str(o12)+", D13_amplitude = "+ str(o13)+", D14_amplitude = "+ str(o14)+", D15_amplitude = "+ str(o15)+", D16_amplitude = "+ str(o16)+", D17_amplitude = "+ str(o17)+", D18_amplitude = "+ str(o18)+", D19_amplitude = "+ str(o19)+", D20_amplitude = "+ str(o20)+", D21_amplitude = "+ str(o21)+", D22_amplitude = "+ str(o22)+", D23_amplitude = "+ str(o23)+", D24_amplitude = "+ str(o24)+", D25_amplitude = "+ str(o25)+", D26_amplitude = "+ str(o26)+", D27_amplitude = "+ str(o27)+", D28_amplitude = "+ str(o28)+", D29_amplitude = "+ str(o29)+", D30_amplitude = "+ str(o30)+", D31_amplitude = "+ str(o31)+", D32_amplitude = "+ str(o32)+", D33_amplitude = "+ str(o33)+", D34_amplitude = "+ str(o34)+", D35_amplitude = "+ str(o35)+", D36_amplitude = "+ str(o36)+", D37_amplitude = "+ str(o37)+", D38_amplitude = "+ str(o38)+", D39_amplitude = "+ str(o39)+", D40_amplitude = "+ str(o40)+", D41_amplitude = "+ str(o41)+", D42_amplitude = "+ str(o42)+", D43_amplitude = "+ str(o43)+", D44_amplitude = "+ str(o44)+", D45_amplitude = "+ str(o45)+", D46_amplitude = "+ str(o46)+", D47_amplitude = "+ str(o47)+", D48_amplitude = "+ str(o48)+", D49_amplitude = "+ str(o49)+", D50_amplitude = "+ str(o50)+", Update_Control3 = 1"+" WHERE UserID = "+ str(u))
        #Jeferson End
        
    # Criando objetos cursor    
    cursor_content_polluters_tweets = db.cursor()
    cursor_tweets_fromuser = db.cursor()
    cursor_polluters = db.cursor()
    
    # Montando SQL statements 
    sql_content_polluters_tweets = 'SELECT UserID FROM legitimate_users_tweets_original'
    #Jeferson Begin
    #sql_content_polluters = 'SELECT UserID FROM legitimate_users_sbseg'    
    sql_content_polluters = 'SELECT UserID FROM legitimate_users'
    #Jeferson Begin
    
    #WHERE Update_Control is NULL
      
    # Interação inicial com o banco de dados     
    cursor_content_polluters_tweets.execute(sql_content_polluters_tweets)    
    result_users = cursor_content_polluters_tweets.fetchall()
    
    #Inicializando lista de usuários
    users = []
    n = 0
    #Persistindo lista de usuários
    for row in set(result_users):
        n = n + 1
        users.append(row[0])
    #print(users)
    #print('Número total de usuários em legitimate users =',n)
        
    for user in tqdm(users):
        # Buscar na tabela content_polluters_tweets  todos os tweets gerados por cada usuário 
        cursor_tweets_fromuser.execute(queryTweetbyuser(user))
        #print(user)            
        # Buscar as linhas referentes ao usuário
        tweetList = cursor_tweets_fromuser.fetchall()
        #Inicializando as listas de v-a-d dos tweets de cada usuário
        t = []        
        D1 = []
        D2 = []
        D3 = []
        D4 = []
        D5 = []
        D6 = []
        D7 = []
        D8 = []
        D9 = []
        D10 = []
        D11 = []
        D12 = []
        D13 = []
        D14 = []
        D15 = []
        D16 = []
        D17 = []
        D18 = []
        D19 = []
        D20 = []
        D21 = []
        D22 = []
        D23 = []
        D24 = []
        D25 = []
        D26 = []
        D27 = []
        D28 = []
        D29 = []
        D30 = []
        D31 = []
        D32 = []
        D33 = []
        D34 = []
        D35 = []
        D36 = []
        D37 = []
        D38 = []
        D39 = []
        D40 = []
        D41 = []
        D42 = []
        D43 = []
        D44 = []
        D45 = []
        D46 = []
        D47 = []
        D48 = []
        D49 = []
        D50 = []          
        # Printando cada lista
        for linha in tweetList:                
            # Guardar os valores em cada lista
            #print(linha)
            t.append(linha[0])            
            D1.append(linha[1])
            D2.append(linha[2])
            D3.append(linha[3])
            D4.append(linha[4])
            D5.append(linha[5])
            D6.append(linha[6])
            D7.append(linha[7])
            D8.append(linha[8])
            D9.append(linha[9])
            D10.append(linha[10])
            D11.append(linha[11])
            D12.append(linha[12])
            D13.append(linha[13])
            D14.append(linha[14])
            D15.append(linha[15])
            D16.append(linha[16])
            D17.append(linha[17])
            D18.append(linha[18])
            D19.append(linha[19])
            D20.append(linha[20])
            D21.append(linha[21])
            D22.append(linha[22])
            D23.append(linha[23])
            D24.append(linha[24])
            D25.append(linha[25])
            D26.append(linha[26])
            D27.append(linha[27])
            D28.append(linha[28])
            D29.append(linha[29])
            D30.append(linha[30])
            D31.append(linha[31])
            D32.append(linha[32])
            D33.append(linha[33])
            D34.append(linha[34])
            D35.append(linha[35])
            D36.append(linha[36])
            D37.append(linha[37])
            D38.append(linha[38])
            D39.append(linha[39])
            D40.append(linha[40])
            D41.append(linha[41])
            D42.append(linha[42])
            D43.append(linha[43])
            D44.append(linha[44])
            D45.append(linha[45])
            D46.append(linha[46])
            D47.append(linha[47])
            D48.append(linha[48])
            D49.append(linha[49])
            D50.append(linha[50])
           
       #Print das listas de v, de a, e de d, dos tweets de cada usuário(conta)
        #print ('======')
        #print ('lista de D1 dos  tweets do usuário', user,' =',D1)
        #print ('======')
        #print ('lista de D25 dos tweets do usuário', user,' =',D25)
        #print ('======')
        #print ('lista de D50 de tweets do usuário', user,' =',D50)
        
        
        #Calculando Estatísticas da Conta em relação a V-A-D
        #v_media, a_media, d_media, v_1quartil, a_1quartil, d_1quartil, v_mediana, a_mediana, d_mediana, v_3quartil, a_3quartil, d_3quartil, v_desviopadrao, a_desviopadrao, d_desviopadrao, v_amplitude, a_amplitude, d_amplitude = statistic (v, a, d)
        
        d1_media, d2_media, d3_media, d4_media, d5_media, d6_media, d7_media, d8_media, d9_media, d10_media, d11_media, d12_media, d13_media, d14_media, d15_media, d16_media, d17_media, d18_media, d19_media, d20_media, d21_media, d22_media, d23_media, d24_media, d25_media, d26_media, d27_media, d28_media, d29_media, d30_media, d31_media, d32_media, d33_media, d34_media, d35_media, d36_media, d37_media, d38_media, d39_media, d40_media, d41_media, d42_media, d43_media, d44_media, d45_media, d46_media, d47_media, d48_media, d49_media, d50_media, d1_1quartil, d2_1quartil, d3_1quartil, d4_1quartil, d5_1quartil, d6_1quartil, d7_1quartil, d8_1quartil, d9_1quartil, d10_1quartil, d11_1quartil, d12_1quartil, d13_1quartil, d14_1quartil, d15_1quartil, d16_1quartil, d17_1quartil, d18_1quartil, d19_1quartil, d20_1quartil, d21_1quartil, d22_1quartil, d23_1quartil, d24_1quartil, d25_1quartil, d26_1quartil, d27_1quartil, d28_1quartil, d29_1quartil, d30_1quartil, d31_1quartil, d32_1quartil, d33_1quartil, d34_1quartil, d35_1quartil, d36_1quartil, d37_1quartil, d38_1quartil, d39_1quartil, d40_1quartil, d41_1quartil, d42_1quartil, d43_1quartil, d44_1quartil, d45_1quartil, d46_1quartil, d47_1quartil, d48_1quartil, d49_1quartil, d50_1quartil, d1_mediana, d2_mediana, d3_mediana, d4_mediana, d5_mediana, d6_mediana, d7_mediana, d8_mediana, d9_mediana, d10_mediana, d11_mediana, d12_mediana, d13_mediana, d14_mediana, d15_mediana, d16_mediana, d17_mediana, d18_mediana, d19_mediana, d20_mediana, d21_mediana, d22_mediana, d23_mediana, d24_mediana, d25_mediana, d26_mediana, d27_mediana, d28_mediana, d29_mediana, d30_mediana, d31_mediana, d32_mediana, d33_mediana, d34_mediana, d35_mediana, d36_mediana, d37_mediana, d38_mediana, d39_mediana, d40_mediana, d41_mediana, d42_mediana, d43_mediana, d44_mediana, d45_mediana, d46_mediana, d47_mediana, d48_mediana, d49_mediana, d50_mediana, d1_3quartil, d2_3quartil, d3_3quartil, d4_3quartil, d5_3quartil, d6_3quartil, d7_3quartil, d8_3quartil, d9_3quartil, d10_3quartil, d11_3quartil, d12_3quartil, d13_3quartil, d14_3quartil, d15_3quartil, d16_3quartil, d17_3quartil, d18_3quartil, d19_3quartil, d20_3quartil, d21_3quartil, d22_3quartil, d23_3quartil, d24_3quartil, d25_3quartil, d26_3quartil, d27_3quartil, d28_3quartil, d29_3quartil, d30_3quartil, d31_3quartil, d32_3quartil, d33_3quartil, d34_3quartil, d35_3quartil, d36_3quartil, d37_3quartil, d38_3quartil, d39_3quartil, d40_3quartil, d41_3quartil, d42_3quartil, d43_3quartil, d44_3quartil, d45_3quartil, d46_3quartil, d47_3quartil, d48_3quartil, d49_3quartil, d50_3quartil, d1_desviopadrao, d2_desviopadrao, d3_desviopadrao, d4_desviopadrao, d5_desviopadrao, d6_desviopadrao, d7_desviopadrao, d8_desviopadrao, d9_desviopadrao, d10_desviopadrao, d11_desviopadrao, d12_desviopadrao, d13_desviopadrao, d14_desviopadrao, d15_desviopadrao, d16_desviopadrao, d17_desviopadrao, d18_desviopadrao, d19_desviopadrao, d20_desviopadrao, d21_desviopadrao, d22_desviopadrao, d23_desviopadrao, d24_desviopadrao, d25_desviopadrao, d26_desviopadrao, d27_desviopadrao, d28_desviopadrao, d29_desviopadrao, d30_desviopadrao, d31_desviopadrao, d32_desviopadrao, d33_desviopadrao, d34_desviopadrao, d35_desviopadrao, d36_desviopadrao, d37_desviopadrao, d38_desviopadrao, d39_desviopadrao, d40_desviopadrao, d41_desviopadrao, d42_desviopadrao, d43_desviopadrao, d44_desviopadrao, d45_desviopadrao, d46_desviopadrao, d47_desviopadrao, d48_desviopadrao, d49_desviopadrao, d50_desviopadrao, d1_amplitude, d2_amplitude, d3_amplitude, d4_amplitude, d5_amplitude, d6_amplitude, d7_amplitude, d8_amplitude, d9_amplitude, d10_amplitude, d11_amplitude, d12_amplitude, d13_amplitude, d14_amplitude, d15_amplitude, d16_amplitude, d17_amplitude, d18_amplitude, d19_amplitude, d20_amplitude, d21_amplitude, d22_amplitude, d23_amplitude, d24_amplitude, d25_amplitude, d26_amplitude, d27_amplitude, d28_amplitude, d29_amplitude, d30_amplitude, d31_amplitude, d32_amplitude, d33_amplitude, d34_amplitude, d35_amplitude, d36_amplitude, d37_amplitude, d38_amplitude, d39_amplitude, d40_amplitude, d41_amplitude, d42_amplitude, d43_amplitude, d44_amplitude, d45_amplitude, d46_amplitude, d47_amplitude, d48_amplitude, d49_amplitude, d50_amplitude = statistic(D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20,D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,D32,D33,D34,D35,D36,D37,D38,D39,D40,D41,D42,D43,D44,D45,D46,D47,D48,D49,D50)        
        
        # Interação com o banco de dados (persistir v-a-d)
        #cursor_polluters.execute(buildQuery(user, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34, D35, D36, D37, D38, D39, D40, D41, D42, D43, D44, D45, D46, D47, D48, D49, D50)) 
        #print('+++++++++++++++')
        #print('Médias(d1,d25,d50):',d1_media, d25_media, d50_media, '1Quartis(d1,d25,d50):', d1_1quartil, d25_1quartil, d50_1quartil, 'Medianas(d1,d25,d50):', d1_mediana, d25_mediana, d50_mediana, '3Quartis(d1,d25,d50):', d1_3quartil, d25_3quartil, d50_3quartil, 'DesvPadrao(d1,d25,d50):',  d1_desviopadrao, d25_desviopadrao, d50_desviopadrao, 'Amplitude(d1,d25,d50):', d1_amplitude, d25_amplitude, d50_amplitude) 
        #print('+++++++++++++++')
        
        # Interação com o banco de dados (persistir estatistica)
        cursor_polluters.execute(buildQuery(user, d1_media, d2_media, d3_media, d4_media, d5_media, d6_media, d7_media, d8_media, d9_media, d10_media, d11_media, d12_media, d13_media, d14_media, d15_media, d16_media, d17_media, d18_media, d19_media, d20_media, d21_media, d22_media, d23_media, d24_media, d25_media, d26_media, d27_media, d28_media, d29_media, d30_media, d31_media, d32_media, d33_media, d34_media, d35_media, d36_media, d37_media, d38_media, d39_media, d40_media, d41_media, d42_media, d43_media, d44_media, d45_media, d46_media, d47_media, d48_media, d49_media, d50_media, d1_1quartil, d2_1quartil, d3_1quartil, d4_1quartil, d5_1quartil, d6_1quartil, d7_1quartil, d8_1quartil, d9_1quartil, d10_1quartil, d11_1quartil, d12_1quartil, d13_1quartil, d14_1quartil, d15_1quartil, d16_1quartil, d17_1quartil, d18_1quartil, d19_1quartil, d20_1quartil, d21_1quartil, d22_1quartil, d23_1quartil, d24_1quartil, d25_1quartil, d26_1quartil, d27_1quartil, d28_1quartil, d29_1quartil, d30_1quartil, d31_1quartil, d32_1quartil, d33_1quartil, d34_1quartil, d35_1quartil, d36_1quartil, d37_1quartil, d38_1quartil, d39_1quartil, d40_1quartil, d41_1quartil, d42_1quartil, d43_1quartil, d44_1quartil, d45_1quartil, d46_1quartil, d47_1quartil, d48_1quartil, d49_1quartil, d50_1quartil, d1_mediana, d2_mediana, d3_mediana, d4_mediana, d5_mediana, d6_mediana, d7_mediana, d8_mediana, d9_mediana, d10_mediana, d11_mediana, d12_mediana, d13_mediana, d14_mediana, d15_mediana, d16_mediana, d17_mediana, d18_mediana, d19_mediana, d20_mediana, d21_mediana, d22_mediana, d23_mediana, d24_mediana, d25_mediana, d26_mediana, d27_mediana, d28_mediana, d29_mediana, d30_mediana, d31_mediana, d32_mediana, d33_mediana, d34_mediana, d35_mediana, d36_mediana, d37_mediana, d38_mediana, d39_mediana, d40_mediana, d41_mediana, d42_mediana, d43_mediana, d44_mediana, d45_mediana, d46_mediana, d47_mediana, d48_mediana, d49_mediana, d50_mediana, d1_3quartil, d2_3quartil, d3_3quartil, d4_3quartil, d5_3quartil, d6_3quartil, d7_3quartil, d8_3quartil, d9_3quartil, d10_3quartil, d11_3quartil, d12_3quartil, d13_3quartil, d14_3quartil, d15_3quartil, d16_3quartil, d17_3quartil, d18_3quartil, d19_3quartil, d20_3quartil, d21_3quartil, d22_3quartil, d23_3quartil, d24_3quartil, d25_3quartil, d26_3quartil, d27_3quartil, d28_3quartil, d29_3quartil, d30_3quartil, d31_3quartil, d32_3quartil, d33_3quartil, d34_3quartil, d35_3quartil, d36_3quartil, d37_3quartil, d38_3quartil, d39_3quartil, d40_3quartil, d41_3quartil, d42_3quartil, d43_3quartil, d44_3quartil, d45_3quartil, d46_3quartil, d47_3quartil, d48_3quartil, d49_3quartil, d50_3quartil, d1_desviopadrao, d2_desviopadrao, d3_desviopadrao, d4_desviopadrao, d5_desviopadrao, d6_desviopadrao, d7_desviopadrao, d8_desviopadrao, d9_desviopadrao, d10_desviopadrao, d11_desviopadrao, d12_desviopadrao, d13_desviopadrao, d14_desviopadrao, d15_desviopadrao, d16_desviopadrao, d17_desviopadrao, d18_desviopadrao, d19_desviopadrao, d20_desviopadrao, d21_desviopadrao, d22_desviopadrao, d23_desviopadrao, d24_desviopadrao, d25_desviopadrao, d26_desviopadrao, d27_desviopadrao, d28_desviopadrao, d29_desviopadrao, d30_desviopadrao, d31_desviopadrao, d32_desviopadrao, d33_desviopadrao, d34_desviopadrao, d35_desviopadrao, d36_desviopadrao, d37_desviopadrao, d38_desviopadrao, d39_desviopadrao, d40_desviopadrao, d41_desviopadrao, d42_desviopadrao, d43_desviopadrao, d44_desviopadrao, d45_desviopadrao, d46_desviopadrao, d47_desviopadrao, d48_desviopadrao, d49_desviopadrao, d50_desviopadrao, d1_amplitude, d2_amplitude, d3_amplitude, d4_amplitude, d5_amplitude, d6_amplitude, d7_amplitude, d8_amplitude, d9_amplitude, d10_amplitude, d11_amplitude, d12_amplitude, d13_amplitude, d14_amplitude, d15_amplitude, d16_amplitude, d17_amplitude, d18_amplitude, d19_amplitude, d20_amplitude, d21_amplitude, d22_amplitude, d23_amplitude, d24_amplitude, d25_amplitude, d26_amplitude, d27_amplitude, d28_amplitude, d29_amplitude, d30_amplitude, d31_amplitude, d32_amplitude, d33_amplitude, d34_amplitude, d35_amplitude, d36_amplitude, d37_amplitude, d38_amplitude, d39_amplitude, d40_amplitude, d41_amplitude, d42_amplitude, d43_amplitude, d44_amplitude, d45_amplitude, d46_amplitude, d47_amplitude, d48_amplitude, d49_amplitude, d50_amplitude))


except Exception as e:
    print("Exception occurred:{}".format(e))
    # Rollback caso haja algum erro
    db.rollback()
finally:   
    db.close()
