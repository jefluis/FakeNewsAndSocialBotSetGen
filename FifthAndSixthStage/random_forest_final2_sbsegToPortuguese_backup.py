# -*- coding: utf-8 -*-
"""
Created on October 31 2023

 
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2024) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire
"""

import pymysql
import pandas as pd
import datetime as dt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
#from IPython import get_ipython

#from datetime import timezone

# FUNÇÕES

def ConvertDatetimetoTimestamp (date_time):
    timestamp = dt.datetime.timestamp(date_time)
    return (timestamp)


#CARREGANDO O DATASET
# Criando um objeto de conexão com o bd

db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)


# Criando objetos cursor
cursor_randomforest = db.cursor()
cursor2_randomforest = db.cursor()
cursor3_randomforest = db.cursor()

cursor_users_from_setGen_randomforest  = db.cursor()

    
# Montando SQL statements 
sql_accounts = 'SELECT * FROM accounts_pt'
#sql2_accounts = 'SELECT UserID, CreatedAt, CollectedAt, NumberOfFollowings, NumberOfFollowers, NumberOfTweets, LengthOfScreenName, LenDescrInUseProfile, Update_Control, Tipo FROM accounts_pt'
sql2_accounts = 'SELECT UserID, CreatedAt, NumberOfFollowings, NumberOfFollowers, NumberOfTweets, LengthOfScreenName, LenDescrInUseProfile, Update_Control, Type FROM accounts_pt'
sql3_accounts = 'SELECT UserID, CreatedAt, NumberOfFollowings, NumberOfFollowers, NumberOfTweets, LengthOfScreenName, LenDescrInUseProfile, Update_Control, type, d1_media, d2_media, d3_media, d4_media, d5_media, d6_media, d7_media, d8_media, d9_media, d10_media, d11_media, d12_media, d13_media, d14_media, d15_media, d16_media, d17_media, d18_media, d19_media, d20_media, d21_media, d22_media, d23_media, d24_media, d25_media, d26_media, d27_media, d28_media, d29_media, d30_media, d31_media, d32_media, d33_media, d34_media, d35_media, d36_media, d37_media, d38_media, d39_media, d40_media, d41_media, d42_media, d43_media, d44_media, d45_media, d46_media, d47_media, d48_media, d49_media, d50_media, d1_1quartil, d2_1quartil, d3_1quartil, d4_1quartil, d5_1quartil, d6_1quartil, d7_1quartil, d8_1quartil, d9_1quartil, d10_1quartil, d11_1quartil, d12_1quartil, d13_1quartil, d14_1quartil, d15_1quartil, d16_1quartil, d17_1quartil, d18_1quartil, d19_1quartil, d20_1quartil, d21_1quartil, d22_1quartil, d23_1quartil, d24_1quartil, d25_1quartil, d26_1quartil, d27_1quartil, d28_1quartil, d29_1quartil, d30_1quartil, d31_1quartil, d32_1quartil, d33_1quartil, d34_1quartil, d35_1quartil, d36_1quartil, d37_1quartil, d38_1quartil, d39_1quartil, d40_1quartil, d41_1quartil, d42_1quartil, d43_1quartil, d44_1quartil, d45_1quartil, d46_1quartil, d47_1quartil, d48_1quartil, d49_1quartil, d50_1quartil, d1_mediana, d2_mediana, d3_mediana, d4_mediana, d5_mediana, d6_mediana, d7_mediana, d8_mediana, d9_mediana, d10_mediana, d11_mediana, d12_mediana, d13_mediana, d14_mediana, d15_mediana, d16_mediana, d17_mediana, d18_mediana, d19_mediana, d20_mediana, d21_mediana, d22_mediana, d23_mediana, d24_mediana, d25_mediana, d26_mediana, d27_mediana, d28_mediana, d29_mediana, d30_mediana, d31_mediana, d32_mediana, d33_mediana, d34_mediana, d35_mediana, d36_mediana, d37_mediana, d38_mediana, d39_mediana, d40_mediana, d41_mediana, d42_mediana, d43_mediana, d44_mediana, d45_mediana, d46_mediana, d47_mediana, d48_mediana, d49_mediana, d50_mediana, d1_3quartil, d2_3quartil, d3_3quartil, d4_3quartil, d5_3quartil, d6_3quartil, d7_3quartil, d8_3quartil, d9_3quartil, d10_3quartil, d11_3quartil, d12_3quartil, d13_3quartil, d14_3quartil, d15_3quartil, d16_3quartil, d17_3quartil, d18_3quartil, d19_3quartil, d20_3quartil, d21_3quartil, d22_3quartil, d23_3quartil, d24_3quartil, d25_3quartil, d26_3quartil, d27_3quartil, d28_3quartil, d29_3quartil, d30_3quartil, d31_3quartil, d32_3quartil, d33_3quartil, d34_3quartil, d35_3quartil, d36_3quartil, d37_3quartil, d38_3quartil, d39_3quartil, d40_3quartil, d41_3quartil, d42_3quartil, d43_3quartil, d44_3quartil, d45_3quartil, d46_3quartil, d47_3quartil, d48_3quartil, d49_3quartil, d50_3quartil, d1_desviopadrao, d2_desviopadrao, d3_desviopadrao, d4_desviopadrao, d5_desviopadrao, d6_desviopadrao, d7_desviopadrao, d8_desviopadrao, d9_desviopadrao, d10_desviopadrao, d11_desviopadrao, d12_desviopadrao, d13_desviopadrao, d14_desviopadrao, d15_desviopadrao, d16_desviopadrao, d17_desviopadrao, d18_desviopadrao, d19_desviopadrao, d20_desviopadrao, d21_desviopadrao, d22_desviopadrao, d23_desviopadrao, d24_desviopadrao, d25_desviopadrao, d26_desviopadrao, d27_desviopadrao, d28_desviopadrao, d29_desviopadrao, d30_desviopadrao, d31_desviopadrao, d32_desviopadrao, d33_desviopadrao, d34_desviopadrao, d35_desviopadrao, d36_desviopadrao, d37_desviopadrao, d38_desviopadrao, d39_desviopadrao, d40_desviopadrao, d41_desviopadrao, d42_desviopadrao, d43_desviopadrao, d44_desviopadrao, d45_desviopadrao, d46_desviopadrao, d47_desviopadrao, d48_desviopadrao, d49_desviopadrao, d50_desviopadrao, d1_amplitude, d2_amplitude, d3_amplitude, d4_amplitude, d5_amplitude, d6_amplitude, d7_amplitude, d8_amplitude, d9_amplitude, d10_amplitude, d11_amplitude, d12_amplitude, d13_amplitude, d14_amplitude, d15_amplitude, d16_amplitude, d17_amplitude, d18_amplitude, d19_amplitude, d20_amplitude, d21_amplitude, d22_amplitude, d23_amplitude, d24_amplitude, d25_amplitude, d26_amplitude, d27_amplitude, d28_amplitude, d29_amplitude, d30_amplitude, d31_amplitude, d32_amplitude, d33_amplitude, d34_amplitude, d35_amplitude, d36_amplitude, d37_amplitude, d38_amplitude, d39_amplitude, d40_amplitude, d41_amplitude, d42_amplitude, d43_amplitude, d44_amplitude, d45_amplitude, d46_amplitude, d47_amplitude, d48_amplitude, d49_amplitude, d50_amplitude FROM accounts_pt'

# Query para buscar os dados das contas dos usuários que compartilharam notícias
# Fake e não Fake e que irei rodar o modelo treinado com V A e classificar as contas.
#sql_users_from_setGen = 'select * from users_from_setgen where v_media > 0 limit 500'
sql_users_from_setGen = 'select u.* from users_from_setgen as u inner join ( select  userid, count(tweetid) as Mensagens from TweetsOfLabeledNews group by UserId having Mensagens > 10) as T2 where T2.userid = u.userid and u.v_media > 0'

# Interação inicial com o banco de dados 
cursor_randomforest.execute(sql_accounts)
datas = cursor_randomforest.fetchall()  

cursor2_randomforest.execute(sql2_accounts)
datas2 = cursor2_randomforest.fetchall()

cursor3_randomforest.execute(sql3_accounts)
datas3 = cursor3_randomforest.fetchall()   
  
# Jeferson begin
cursor_users_from_setGen_randomforest.execute(sql_users_from_setGen)
datas_users_from_setGen = cursor_users_from_setGen_randomforest.fetchall() 

# Jeferson End 

#########################################
print('Query com VAD')
print(datas)

#Jeferson Begin
print('***********************************************')
print('Query users_from_setGen')
print(datas_users_from_setGen)
#Jeferso End

print('***********************************************')
print('Query com somente dados de perfil do twitter')
print(datas2)

print('***********************************************')
print('Query com 50 dimensões do Tang')
print(datas3)

#Alterando tupla de cada conta (convertendo datetimes em timestamps)
n=0
lista_posix_dates = []
for tupla in datas:
    n = n + 1
    newtupla = tupla
    n1 = ConvertDatetimetoTimestamp(tupla[1])
    n2 = ConvertDatetimetoTimestamp(tupla[2])
    # Como não podemos modificar os elementos de uma tupla, devemos substituí-la por uma tupla diferente
    newtupla = (tupla[0], n1, n2) + tupla[3:]
    lista_posix_dates.append(newtupla)
    
print('***********************************************')  
print('Lista com VAD')  
print(lista_posix_dates)
print('Número de usuários =',n) 

# Jeferson begin
#Alterando tupla de cada conta (convertendo datetimes em timestamps)
users_from_setGen=0
lista_users_from_setGen_posix_dates = []
for tupla_users_from_setGen in datas_users_from_setGen:
    users_from_setGen = users_from_setGen + 1
    newtupla_users_from_setGen = tupla_users_from_setGen
    users_from_setGen1 = ConvertDatetimetoTimestamp(tupla_users_from_setGen[1])
    users_from_setGen2 = ConvertDatetimetoTimestamp(tupla_users_from_setGen[2])
    # Como não podemos modificar os elementos de uma tupla, devemos substituí-la por uma tupla diferente
    newtupla_users_from_setGen = (tupla_users_from_setGen[0], users_from_setGen1, users_from_setGen2) + tupla_users_from_setGen[3:]
    lista_users_from_setGen_posix_dates.append(newtupla_users_from_setGen)
print('***********************************************')  
print('Lista users_from_setGen')  
print(lista_users_from_setGen_posix_dates)
print('Número de usuários =',users_from_setGen) 

# Jeferson End

#2 Alterando tupla de cada conta (convertendo datetimes em timestamps)
m=0
lista2_posix_dates = []
for tupla2 in datas2:
    m = m + 1
    newtupla2 = tupla2
    m1 = ConvertDatetimetoTimestamp(tupla2[1])    
    # Como não podemos modificar os elementos de uma tupla, devemos substituí-la por uma tupla diferente
    newtupla2 = (tupla2[0], m1) + tupla2[2:]
    lista2_posix_dates.append(newtupla2)
print('***********************************************')  
print('Lista somente perfil do twitter')  
print(lista2_posix_dates)
print('Número de usuários =',m)

p=0
lista3_posix_dates = []
for tupla3 in datas3:
    p = p + 1
    newtupla3 = tupla3
    p1 = ConvertDatetimetoTimestamp(tupla3[1])   
    # Como não podemos modificar os elementos de uma tupla, devemos substituí-la por uma tupla diferente
    # Jeferson Begin
    #newtupla3 = (tupla3[0], b1) + tupla3[2:]
    newtupla3 = (tupla3[0], p1) + tupla3[2:]
    # Jeferson End
    lista3_posix_dates.append(newtupla3)
print('***********************************************')  
print('Lista com 50 dimensões do Tang')  
print(lista3_posix_dates)
print('Número de usuários =',p)  
#################################################


# Importando o módulo numpy ########
# Construindo o array "dados"
dados = np.array(lista_posix_dates)
dados2 = np.array(lista2_posix_dates)
dados3 = np.array(lista3_posix_dates)

#Jeferson begin
dados_users_from_setGen = np.array(lista_users_from_setGen_posix_dates)
#Jeferson end

####################################
# Printando o array "dados"
print('***********************************************')  
print('Lista com VAD') 
print(dados)

print('***********************************************')  
print('Lista com Users_from_setGen') 
print(dados_users_from_setGen)

print('***********************************************')  
print('Lista somente perfil Twitter') 
print(dados2)

print('***********************************************')  
print('Lista com 50 dimensões do Tang') 
print(dados3)


# Printando o número de dimensões do array "dados"
print('Número dimensões do array dados =',dados.ndim)
print('Número dimensões do array dados2 =',dados2.ndim)
print('Número dimensões do array dados3 =',dados3.ndim)

print('Número dimensões do array dados_users_from_setGen =',dados_users_from_setGen.ndim)


# Printando o número de elementos do array "dados"
print('Número elementos do array dados =',dados.size)
print('Número elementos do array dados2 =',dados2.size)
print('Número elementos do array dados3 =',dados3.size)

print('Número elementos do array dados_users_from_setGen =',dados_users_from_setGen.size)

# Printando o comprimento do array "dados"
print('comprimento do array "dados" =',len(dados))
print('comprimento do array "dados2" =',len(dados2))
print('comprimento do array "dados3" =',len(dados3))

print('comprimento do array "dados_users_from_setGen" =',len(dados_users_from_setGen))

##################################################

# Criando um DataFrame de um dado dataset (no caso, um numpy array da lista modificada de tuplas)
data=pd.DataFrame({
    'CreatedAt':dados[:,1],
   # 'CollectedAt':dados[:,2],
    'NumberOfFollowings':dados[:,3],
    'NumberOfFollowers':dados[:,4],    
    'NumberOfTweets':dados[:,5],
    'LengthOfScreenName':dados[:,6],
    'LenDescrInUseProfile':dados[:,7],    
    'V_media':dados[:,8],
    'A_media':dados[:,9],
    'D_media':dados[:,10],
    'V_1quartil':dados[:,11],
    'A_1quartil':dados[:,12],
    'D_1quartil':dados[:,13],    
    'V_mediana':dados[:,14],
    'A_mediana':dados[:,15],
    'D_mediana':dados[:,16],    
    'V_3quartil':dados[:,17],
    'A_3quartil':dados[:,18],
    'D_3quartil':dados[:,19],    
    'V_desviopadrao':dados[:,20],
    'A_desviopadrao':dados[:,21],
    'D_desviopadrao':dados[:,22],
    'V_amplitude':dados[:,23],
    'A_amplitude':dados[:,24],
    'D_amplitude':dados[:,25],
    'type':dados[:,27],
})
data.head()

#Jeferson begin

# Criando um DataFrame de um dado dataset (no caso, um numpy array da lista modificada de tuplas)
data_users_from_setGen=pd.DataFrame({
    'CreatedAt':dados_users_from_setGen[:,1],
   # 'CollectedAt':dados_users_from_setGen[:,2],
    'NumberOfFollowings':dados_users_from_setGen[:,3],
    'NumberOfFollowers':dados_users_from_setGen[:,4],    
    'NumberOfTweets':dados_users_from_setGen[:,5],
    'LengthOfScreenName':dados_users_from_setGen[:,6],
    'LenDescrInUseProfile':dados_users_from_setGen[:,7],    
    'V_media':dados_users_from_setGen[:,8],
    'A_media':dados_users_from_setGen[:,9],
    'D_media':dados_users_from_setGen[:,10],
    'V_1quartil':dados_users_from_setGen[:,11],
    'A_1quartil':dados_users_from_setGen[:,12],
    'D_1quartil':dados_users_from_setGen[:,13],    
    'V_mediana':dados_users_from_setGen[:,14],
    'A_mediana':dados_users_from_setGen[:,15],
    'D_mediana':dados_users_from_setGen[:,16],    
    'V_3quartil':dados_users_from_setGen[:,17],
    'A_3quartil':dados_users_from_setGen[:,18],
    'D_3quartil':dados_users_from_setGen[:,19],    
    'V_desviopadrao':dados_users_from_setGen[:,20],
    'A_desviopadrao':dados_users_from_setGen[:,21],
    'D_desviopadrao':dados_users_from_setGen[:,22],
    'V_amplitude':dados_users_from_setGen[:,23],
    'A_amplitude':dados_users_from_setGen[:,24],
    'D_amplitude':dados_users_from_setGen[:,25],
    'type':dados_users_from_setGen[:,27],
})
data_users_from_setGen.head()

#################################################################################################
# Criando um DataFrame de um dado dataset (no caso, um numpy array da lista modificada de tuplas)
data2=pd.DataFrame({
    'CreatedAt':dados2[:,1],
   # 'CollectedAt':dados2[:,2],
    'NumberOfFollowings':dados2[:,2],
    'NumberOfFollowers':dados2[:,3],    
    'NumberOfTweets':dados2[:,4],
    'LengthOfScreenName':dados2[:,5],
    'LenDescrInUseProfile':dados2[:,6],    
    'type':dados2[:,8],
})
data2.head()

#################################################################################################
# Criando um DataFrame de um dado dataset (no caso, um numpy array da lista modificada de tuplas)
data3=pd.DataFrame({
    'CreatedAt':dados3[:,1],
   # 'CollectedAt':dados3[:,2],
    'NumberOfFollowings':dados3[:,2],
    'NumberOfFollowers':dados3[:,3],    
    'NumberOfTweets':dados3[:,4],
    'LengthOfScreenName':dados3[:,5],
    'LenDescrInUseProfile':dados3[:,6], 
    'Update_Control':dados3[:,7],
    'type':dados3[:,8],    
    'd1_media':dados3[:,9],
    'd2_media':dados3[:,10],
    'd3_media':dados3[:,11],
    'd4_media':dados3[:,12],
    'd5_media':dados3[:,13],
    'd6_media':dados3[:,14],
    'd7_media':dados3[:,15],
    'd8_media':dados3[:,16],
    'd9_media':dados3[:,17],
    'd10_media':dados3[:,18],
    'd11_media':dados3[:,19],
    'd12_media':dados3[:,20],
    'd13_media':dados3[:,21],
    'd14_media':dados3[:,22],
    'd15_media':dados3[:,23],
    'd16_media':dados3[:,24],
    'd17_media':dados3[:,25],
    'd18_media':dados3[:,26],
    'd19_media':dados3[:,27],
    'd20_media':dados3[:,28],
    'd21_media':dados3[:,29],
    'd22_media':dados3[:,30],
    'd23_media':dados3[:,31],
    'd24_media':dados3[:,32],
    'd25_media':dados3[:,33],
    'd26_media':dados3[:,34],
    'd27_media':dados3[:,35],
    'd28_media':dados3[:,36],
    'd29_media':dados3[:,37],
    'd30_media':dados3[:,38],
    'd31_media':dados3[:,39],
    'd32_media':dados3[:,40],
    'd33_media':dados3[:,41],
    'd34_media':dados3[:,42],
    'd35_media':dados3[:,43],
    'd36_media':dados3[:,44],
    'd37_media':dados3[:,45],
    'd38_media':dados3[:,46],
    'd39_media':dados3[:,47],
    'd40_media':dados3[:,48],
    'd41_media':dados3[:,49],
    'd42_media':dados3[:,50],
    'd43_media':dados3[:,51],
    'd44_media':dados3[:,52],
    'd45_media':dados3[:,53],
    'd46_media':dados3[:,54],
    'd47_media':dados3[:,55],
    'd48_media':dados3[:,56],
    'd49_media':dados3[:,57],
    'd50_media':dados3[:,58],
    'd1_1quartil':dados3[:,59],
    'd2_1quartil':dados3[:,60],
    'd3_1quartil':dados3[:,61],
    'd4_1quartil':dados3[:,62],
    'd5_1quartil':dados3[:,63],
    'd6_1quartil':dados3[:,64],
    'd7_1quartil':dados3[:,65],
    'd8_1quartil':dados3[:,66],
    'd9_1quartil':dados3[:,67],
    'd10_1quartil':dados3[:,68],
    'd11_1quartil':dados3[:,69],
    'd12_1quartil':dados3[:,70],
    'd13_1quartil':dados3[:,71],
    'd14_1quartil':dados3[:,72],
    'd15_1quartil':dados3[:,73],
    'd16_1quartil':dados3[:,74],
    'd17_1quartil':dados3[:,75],
    'd18_1quartil':dados3[:,76],
    'd19_1quartil':dados3[:,77],
    'd20_1quartil':dados3[:,78],
    'd21_1quartil':dados3[:,79],
    'd22_1quartil':dados3[:,80],
    'd23_1quartil':dados3[:,81],
    'd24_1quartil':dados3[:,82],
    'd25_1quartil':dados3[:,83],
    'd26_1quartil':dados3[:,84],
    'd27_1quartil':dados3[:,85],
    'd28_1quartil':dados3[:,86],
    'd29_1quartil':dados3[:,87],
    'd30_1quartil':dados3[:,88],
    'd31_1quartil':dados3[:,89],
    'd32_1quartil':dados3[:,90],
    'd33_1quartil':dados3[:,91],
    'd34_1quartil':dados3[:,92],
    'd35_1quartil':dados3[:,93],
    'd36_1quartil':dados3[:,94],
    'd37_1quartil':dados3[:,95],
    'd38_1quartil':dados3[:,96],
    'd39_1quartil':dados3[:,97],
    'd40_1quartil':dados3[:,98],
    'd41_1quartil':dados3[:,99],
    'd42_1quartil':dados3[:,100],
    'd43_1quartil':dados3[:,101],
    'd44_1quartil':dados3[:,102],
    'd45_1quartil':dados3[:,103],
    'd46_1quartil':dados3[:,104],
    'd47_1quartil':dados3[:,105],
    'd48_1quartil':dados3[:,106],
    'd49_1quartil':dados3[:,107],
    'd50_1quartil':dados3[:,108],    
    'd1_mediana':dados3[:,109],
    'd2_mediana':dados3[:,110],
    'd3_mediana':dados3[:,111],
    'd4_mediana':dados3[:,112],
    'd5_mediana':dados3[:,113],
    'd6_mediana':dados3[:,114],
    'd7_mediana':dados3[:,115],
    'd8_mediana':dados3[:,116],
    'd9_mediana':dados3[:,117],
    'd10_mediana':dados3[:,118],
    'd11_mediana':dados3[:,119],
    'd12_mediana':dados3[:,120],
    'd13_mediana':dados3[:,121],
    'd14_mediana':dados3[:,122],
    'd15_mediana':dados3[:,123],
    'd16_mediana':dados3[:,124],
    'd17_mediana':dados3[:,125],
    'd18_mediana':dados3[:,126],
    'd19_mediana':dados3[:,127],
    'd20_mediana':dados3[:,128],
    'd21_mediana':dados3[:,129],
    'd22_mediana':dados3[:,130],
    'd23_mediana':dados3[:,131],
    'd24_mediana':dados3[:,132],
    'd25_mediana':dados3[:,133],
    'd26_mediana':dados3[:,134],
    'd27_mediana':dados3[:,135],
    'd28_mediana':dados3[:,136],
    'd29_mediana':dados3[:,137],
    'd30_mediana':dados3[:,138],
    'd31_mediana':dados3[:,139],
    'd32_mediana':dados3[:,140],
    'd33_mediana':dados3[:,141],
    'd34_mediana':dados3[:,142],
    'd35_mediana':dados3[:,143],
    'd36_mediana':dados3[:,144],
    'd37_mediana':dados3[:,145],
    'd38_mediana':dados3[:,146],
    'd39_mediana':dados3[:,147],
    'd40_mediana':dados3[:,148],
    'd41_mediana':dados3[:,149],
    'd42_mediana':dados3[:,150],
    'd43_mediana':dados3[:,151],
    'd44_mediana':dados3[:,152],
    'd45_mediana':dados3[:,153],
    'd46_mediana':dados3[:,154],
    'd47_mediana':dados3[:,155],
    'd48_mediana':dados3[:,156],
    'd49_mediana':dados3[:,157],
    'd50_mediana':dados3[:,158],
    'd1_3quartil':dados3[:,159],
    'd2_3quartil':dados3[:,160],
    'd3_3quartil':dados3[:,161],
    'd4_3quartil':dados3[:,162],
    'd5_3quartil':dados3[:,163],
    'd6_3quartil':dados3[:,164],
    'd7_3quartil':dados3[:,165],
    'd8_3quartil':dados3[:,166],
    'd9_3quartil':dados3[:,167],
    'd10_3quartil':dados3[:,168],
    'd11_3quartil':dados3[:,169],
    'd12_3quartil':dados3[:,170],
    'd13_3quartil':dados3[:,171],
    'd14_3quartil':dados3[:,172],
    'd15_3quartil':dados3[:,173],
    'd16_3quartil':dados3[:,174],
    'd17_3quartil':dados3[:,175],
    'd18_3quartil':dados3[:,176],
    'd19_3quartil':dados3[:,177],
    'd20_3quartil':dados3[:,178],
    'd21_3quartil':dados3[:,179],
    'd22_3quartil':dados3[:,180],
    'd23_3quartil':dados3[:,181],
    'd24_3quartil':dados3[:,182],
    'd25_3quartil':dados3[:,183],
    'd26_3quartil':dados3[:,184],
    'd27_3quartil':dados3[:,185],
    'd28_3quartil':dados3[:,186],
    'd29_3quartil':dados3[:,187],
    'd30_3quartil':dados3[:,188],
    'd31_3quartil':dados3[:,189],
    'd32_3quartil':dados3[:,190],
    'd33_3quartil':dados3[:,191],
    'd34_3quartil':dados3[:,192],
    'd35_3quartil':dados3[:,193],
    'd36_3quartil':dados3[:,194],
    'd37_3quartil':dados3[:,195],
    'd38_3quartil':dados3[:,196],
    'd39_3quartil':dados3[:,197],
    'd40_3quartil':dados3[:,198],
    'd41_3quartil':dados3[:,199],
    'd42_3quartil':dados3[:,200],
    'd43_3quartil':dados3[:,201],
    'd44_3quartil':dados3[:,202],
    'd45_3quartil':dados3[:,203],
    'd46_3quartil':dados3[:,204],
    'd47_3quartil':dados3[:,205],
    'd48_3quartil':dados3[:,206],
    'd49_3quartil':dados3[:,207],
    'd50_3quartil':dados3[:,208],
    'd1_desviopadrao':dados3[:,209],
    'd2_desviopadrao':dados3[:,210],
    'd3_desviopadrao':dados3[:,211],
    'd4_desviopadrao':dados3[:,212],
    'd5_desviopadrao':dados3[:,213],
    'd6_desviopadrao':dados3[:,214],
    'd7_desviopadrao':dados3[:,215],
    'd8_desviopadrao':dados3[:,216],
    'd9_desviopadrao':dados3[:,217],
    'd10_desviopadrao':dados3[:,218],
    'd11_desviopadrao':dados3[:,219],
    'd12_desviopadrao':dados3[:,220],
    'd13_desviopadrao':dados3[:,221],
    'd14_desviopadrao':dados3[:,222],
    'd15_desviopadrao':dados3[:,223],
    'd16_desviopadrao':dados3[:,224],
    'd17_desviopadrao':dados3[:,225],
    'd18_desviopadrao':dados3[:,226],
    'd19_desviopadrao':dados3[:,227],
    'd20_desviopadrao':dados3[:,228],
    'd21_desviopadrao':dados3[:,229],
    'd22_desviopadrao':dados3[:,230],
    'd23_desviopadrao':dados3[:,231],
    'd24_desviopadrao':dados3[:,232],
    'd25_desviopadrao':dados3[:,233],
    'd26_desviopadrao':dados3[:,234],
    'd27_desviopadrao':dados3[:,235],
    'd28_desviopadrao':dados3[:,236],
    'd29_desviopadrao':dados3[:,237],
    'd30_desviopadrao':dados3[:,238],
    'd31_desviopadrao':dados3[:,239],
    'd32_desviopadrao':dados3[:,240],
    'd33_desviopadrao':dados3[:,241],
    'd34_desviopadrao':dados3[:,242],
    'd35_desviopadrao':dados3[:,243],
    'd36_desviopadrao':dados3[:,244],
    'd37_desviopadrao':dados3[:,245],
    'd38_desviopadrao':dados3[:,246],
    'd39_desviopadrao':dados3[:,247],
    'd40_desviopadrao':dados3[:,248],
    'd41_desviopadrao':dados3[:,249],
    'd42_desviopadrao':dados3[:,250],
    'd43_desviopadrao':dados3[:,251],
    'd44_desviopadrao':dados3[:,252],
    'd45_desviopadrao':dados3[:,253],
    'd46_desviopadrao':dados3[:,254],
    'd47_desviopadrao':dados3[:,255],
    'd48_desviopadrao':dados3[:,256],
    'd49_desviopadrao':dados3[:,257],
    'd50_desviopadrao':dados3[:,258],
    'd1_amplitude':dados3[:,259],
    'd2_amplitude':dados3[:,260],
    'd3_amplitude':dados3[:,261],
    'd4_amplitude':dados3[:,262],
    'd5_amplitude':dados3[:,263],
    'd6_amplitude':dados3[:,264],
    'd7_amplitude':dados3[:,265],
    'd8_amplitude':dados3[:,266],
    'd9_amplitude':dados3[:,267],
    'd10_amplitude':dados3[:,268],
    'd11_amplitude':dados3[:,269],
    'd12_amplitude':dados3[:,270],
    'd13_amplitude':dados3[:,271],
    'd14_amplitude':dados3[:,272],
    'd15_amplitude':dados3[:,273],
    'd16_amplitude':dados3[:,274],
    'd17_amplitude':dados3[:,275],
    'd18_amplitude':dados3[:,276],
    'd19_amplitude':dados3[:,277],
    'd20_amplitude':dados3[:,278],
    'd21_amplitude':dados3[:,279],
    'd22_amplitude':dados3[:,280],
    'd23_amplitude':dados3[:,281],
    'd24_amplitude':dados3[:,282],
    'd25_amplitude':dados3[:,283],
    'd26_amplitude':dados3[:,284],
    'd27_amplitude':dados3[:,285],
    'd28_amplitude':dados3[:,286],
    'd29_amplitude':dados3[:,287],
    'd30_amplitude':dados3[:,288],
    'd31_amplitude':dados3[:,289],
    'd32_amplitude':dados3[:,290],
    'd33_amplitude':dados3[:,291],
    'd34_amplitude':dados3[:,292],
    'd35_amplitude':dados3[:,293],
    'd36_amplitude':dados3[:,294],
    'd37_amplitude':dados3[:,295],
    'd38_amplitude':dados3[:,296],
    'd39_amplitude':dados3[:,297],
    'd40_amplitude':dados3[:,298],
    'd41_amplitude':dados3[:,299],
    'd42_amplitude':dados3[:,300],
    'd43_amplitude':dados3[:,301],
    'd44_amplitude':dados3[:,302],
    'd45_amplitude':dados3[:,303],
    'd46_amplitude':dados3[:,304],
    'd47_amplitude':dados3[:,305],
    'd48_amplitude':dados3[:,306],
    'd49_amplitude':dados3[:,307],
    'd50_amplitude':dados3[:,308],    
})
data3.head()
################################################################################################

# Import train_test_split function
#'CollectedAt'
X=data[['CreatedAt','NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProfile', 'V_media', 'A_media', 'D_media', 'V_1quartil', 'A_1quartil', 'D_1quartil', 'V_mediana', 'A_mediana', 'D_mediana', 'V_3quartil', 'A_3quartil', 'D_3quartil', 'V_desviopadrao', 'A_desviopadrao', 'D_desviopadrao', 'V_amplitude', 'A_amplitude', 'D_amplitude']]  # Features
X2=data2[['CreatedAt','NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProfile']]  # Features
#####
# avaliar se deve retirar no x3 o update control e o type
X3=data3[['CreatedAt', 'NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProfile', 'd1_media', 'd2_media', 'd3_media', 'd4_media', 'd5_media', 'd6_media', 'd7_media', 'd8_media', 'd9_media','d10_media', 'd11_media', 'd12_media', 'd13_media', 'd14_media', 'd15_media', 'd16_media', 'd17_media', 'd18_media', 'd19_media', 'd20_media', 'd21_media', 'd22_media', 'd23_media', 'd24_media', 'd25_media', 'd26_media', 'd27_media', 'd28_media', 'd29_media', 'd30_media', 'd31_media', 'd32_media', 'd33_media', 'd34_media', 'd35_media', 'd36_media', 'd37_media', 'd38_media', 'd39_media', 'd40_media', 'd41_media', 'd42_media', 'd43_media', 'd44_media', 'd45_media', 'd46_media', 'd47_media', 'd48_media', 'd49_media', 'd50_media', 'd1_1quartil', 'd2_1quartil', 'd3_1quartil', 'd4_1quartil', 'd5_1quartil', 'd6_1quartil', 'd7_1quartil', 'd8_1quartil', 'd9_1quartil', 'd10_1quartil', 'd11_1quartil', 'd12_1quartil', 'd13_1quartil', 'd14_1quartil', 'd15_1quartil', 'd16_1quartil', 'd17_1quartil', 'd18_1quartil', 'd19_1quartil', 'd20_1quartil', 'd21_1quartil', 'd22_1quartil', 'd23_1quartil', 'd24_1quartil', 'd25_1quartil', 'd26_1quartil', 'd27_1quartil', 'd28_1quartil', 'd29_1quartil', 'd30_1quartil', 'd31_1quartil', 'd32_1quartil', 'd33_1quartil', 'd34_1quartil', 'd35_1quartil', 'd36_1quartil', 'd37_1quartil', 'd38_1quartil', 'd39_1quartil', 'd40_1quartil', 'd41_1quartil', 'd42_1quartil', 'd43_1quartil', 'd44_1quartil', 'd45_1quartil', 'd46_1quartil', 'd47_1quartil', 'd48_1quartil', 'd49_1quartil', 'd50_1quartil', 'd1_mediana', 'd2_mediana', 'd3_mediana', 'd4_mediana', 'd5_mediana', 'd6_mediana', 'd7_mediana', 'd8_mediana', 'd9_mediana', 'd10_mediana', 'd11_mediana', 'd12_mediana', 'd13_mediana', 'd14_mediana', 'd15_mediana', 'd16_mediana', 'd17_mediana', 'd18_mediana', 'd19_mediana', 'd20_mediana', 'd21_mediana', 'd22_mediana', 'd23_mediana', 'd24_mediana', 'd25_mediana', 'd26_mediana', 'd27_mediana', 'd28_mediana', 'd29_mediana', 'd30_mediana', 'd31_mediana', 'd32_mediana', 'd33_mediana', 'd34_mediana', 'd35_mediana', 'd36_mediana', 'd37_mediana', 'd38_mediana', 'd39_mediana', 'd40_mediana', 'd41_mediana', 'd42_mediana', 'd43_mediana', 'd44_mediana', 'd45_mediana', 'd46_mediana', 'd47_mediana', 'd48_mediana', 'd49_mediana', 'd50_mediana', 'd1_3quartil', 'd2_3quartil', 'd3_3quartil', 'd4_3quartil', 'd5_3quartil', 'd6_3quartil', 'd7_3quartil', 'd8_3quartil', 'd9_3quartil', 'd10_3quartil', 'd11_3quartil', 'd12_3quartil', 'd13_3quartil', 'd14_3quartil', 'd15_3quartil', 'd16_3quartil', 'd17_3quartil', 'd18_3quartil', 'd19_3quartil', 'd20_3quartil', 'd21_3quartil', 'd22_3quartil', 'd23_3quartil', 'd24_3quartil', 'd25_3quartil', 'd26_3quartil', 'd27_3quartil', 'd28_3quartil', 'd29_3quartil', 'd30_3quartil', 'd31_3quartil', 'd32_3quartil', 'd33_3quartil', 'd34_3quartil', 'd35_3quartil', 'd36_3quartil', 'd37_3quartil', 'd38_3quartil', 'd39_3quartil', 'd40_3quartil', 'd41_3quartil', 'd42_3quartil', 'd43_3quartil', 'd44_3quartil', 'd45_3quartil', 'd46_3quartil', 'd47_3quartil', 'd48_3quartil', 'd49_3quartil', 'd50_3quartil', 'd1_desviopadrao', 'd2_desviopadrao', 'd3_desviopadrao', 'd4_desviopadrao', 'd5_desviopadrao', 'd6_desviopadrao', 'd7_desviopadrao', 'd8_desviopadrao', 'd9_desviopadrao', 'd10_desviopadrao', 'd11_desviopadrao', 'd12_desviopadrao', 'd13_desviopadrao', 'd14_desviopadrao', 'd15_desviopadrao', 'd16_desviopadrao', 'd17_desviopadrao', 'd18_desviopadrao', 'd19_desviopadrao', 'd20_desviopadrao', 'd21_desviopadrao', 'd22_desviopadrao', 'd23_desviopadrao', 'd24_desviopadrao', 'd25_desviopadrao', 'd26_desviopadrao', 'd27_desviopadrao', 'd28_desviopadrao', 'd29_desviopadrao', 'd30_desviopadrao', 'd31_desviopadrao', 'd32_desviopadrao', 'd33_desviopadrao', 'd34_desviopadrao', 'd35_desviopadrao', 'd36_desviopadrao', 'd37_desviopadrao', 'd38_desviopadrao', 'd39_desviopadrao', 'd40_desviopadrao', 'd41_desviopadrao', 'd42_desviopadrao', 'd43_desviopadrao', 'd44_desviopadrao', 'd45_desviopadrao', 'd46_desviopadrao', 'd47_desviopadrao', 'd48_desviopadrao', 'd49_desviopadrao', 'd50_desviopadrao', 'd1_amplitude', 'd2_amplitude', 'd3_amplitude', 'd4_amplitude', 'd5_amplitude', 'd6_amplitude', 'd7_amplitude', 'd8_amplitude', 'd9_amplitude', 'd10_amplitude', 'd11_amplitude', 'd12_amplitude', 'd13_amplitude', 'd14_amplitude', 'd15_amplitude', 'd16_amplitude', 'd17_amplitude', 'd18_amplitude', 'd19_amplitude', 'd20_amplitude', 'd21_amplitude', 'd22_amplitude', 'd23_amplitude', 'd24_amplitude', 'd25_amplitude', 'd26_amplitude', 'd27_amplitude', 'd28_amplitude', 'd29_amplitude', 'd30_amplitude', 'd31_amplitude', 'd32_amplitude', 'd33_amplitude', 'd34_amplitude', 'd35_amplitude', 'd36_amplitude', 'd37_amplitude', 'd38_amplitude', 'd39_amplitude', 'd40_amplitude', 'd41_amplitude', 'd42_amplitude', 'd43_amplitude', 'd44_amplitude', 'd45_amplitude', 'd46_amplitude', 'd47_amplitude', 'd48_amplitude', 'd49_amplitude', 'd50_amplitude']]  # Features

y=data['type']  # Labels
y2=data2['type']  # Labels
y3=data3['type']  # Labels

X_users_from_setGen=data_users_from_setGen[['CreatedAt','NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProfile', 'V_media', 'A_media', 'D_media', 'V_1quartil', 'A_1quartil', 'D_1quartil', 'V_mediana', 'A_mediana', 'D_mediana', 'V_3quartil', 'A_3quartil', 'D_3quartil', 'V_desviopadrao', 'A_desviopadrao', 'D_desviopadrao', 'V_amplitude', 'A_amplitude', 'D_amplitude']]  # Features


###############################################################################################
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # 70% training and 30% test
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2) # 70% training and 30% test
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2) # 70% training and 30% test


#After splitting, you will train the model on the training set and perform predictions on the test set.

#Import Random Forest Model
#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)
clf2=RandomForestClassifier(n_estimators=100)
clf3=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)
clf2.fit(X2_train,y2_train)
clf3.fit(X3_train,y3_train)

y_pred=clf.predict(X_test)
y2_pred=clf2.predict(X2_test)
y3_pred=clf3.predict(X3_test)

#After training, check the accuracy using actual and predicted values.

#Import scikit-learn metrics module for accuracy calculation
# Model Accuracy, how often is the classifier correct?
print("Accuracy with +18 features =",metrics.accuracy_score(y_test, y_pred))
print("Accuracy without 18 features =:",metrics.accuracy_score(y2_test, y2_pred))
print("Accuracy with +300 features =:",metrics.accuracy_score(y3_test, y3_pred))


"""
Finding Important Features in Scikit-learn
Here, you are finding important features or selecting features in the dataset. In scikit-learn, you can perform this task in the following steps:

First, you need to create a random forests model.
Second, use the feature importance variable to see feature importance scores.
Third, visualize these scores using the seaborn library.
"""

#Importa Pandas
#'CollectedAt'foi retirado
feature_names = ['CreatedAt','NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProfile', 'V_media', 'A_media', 'D_media', 'V_1quartil', 'A_1quartil', 'D_1quartil', 'V_mediana', 'A_mediana', 'D_mediana', 'V_3quartil', 'A_3quartil', 'D_3quartil', 'V_desviopadrao', 'A_desviopadrao', 'D_desviopadrao', 'V_amplitude', 'A_amplitude', 'D_amplitude']
feature2_names = ['CreatedAt','NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProfile']
feature3_names = ['CreatedAt', 'NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProfile', 'd1_media', 'd2_media', 'd3_media', 'd4_media', 'd5_media', 'd6_media', 'd7_media', 'd8_media', 'd9_media','d10_media', 'd11_media', 'd12_media', 'd13_media', 'd14_media', 'd15_media', 'd16_media', 'd17_media', 'd18_media', 'd19_media', 'd20_media', 'd21_media', 'd22_media', 'd23_media', 'd24_media', 'd25_media', 'd26_media', 'd27_media', 'd28_media', 'd29_media', 'd30_media', 'd31_media', 'd32_media', 'd33_media', 'd34_media', 'd35_media', 'd36_media', 'd37_media', 'd38_media', 'd39_media', 'd40_media', 'd41_media', 'd42_media', 'd43_media', 'd44_media', 'd45_media', 'd46_media', 'd47_media', 'd48_media', 'd49_media', 'd50_media', 'd1_1quartil', 'd2_1quartil', 'd3_1quartil', 'd4_1quartil', 'd5_1quartil', 'd6_1quartil', 'd7_1quartil', 'd8_1quartil', 'd9_1quartil', 'd10_1quartil', 'd11_1quartil', 'd12_1quartil', 'd13_1quartil', 'd14_1quartil', 'd15_1quartil', 'd16_1quartil', 'd17_1quartil', 'd18_1quartil', 'd19_1quartil', 'd20_1quartil', 'd21_1quartil', 'd22_1quartil', 'd23_1quartil', 'd24_1quartil', 'd25_1quartil', 'd26_1quartil', 'd27_1quartil', 'd28_1quartil', 'd29_1quartil', 'd30_1quartil', 'd31_1quartil', 'd32_1quartil', 'd33_1quartil', 'd34_1quartil', 'd35_1quartil', 'd36_1quartil', 'd37_1quartil', 'd38_1quartil', 'd39_1quartil', 'd40_1quartil', 'd41_1quartil', 'd42_1quartil', 'd43_1quartil', 'd44_1quartil', 'd45_1quartil', 'd46_1quartil', 'd47_1quartil', 'd48_1quartil', 'd49_1quartil', 'd50_1quartil', 'd1_mediana', 'd2_mediana', 'd3_mediana', 'd4_mediana', 'd5_mediana', 'd6_mediana', 'd7_mediana', 'd8_mediana', 'd9_mediana', 'd10_mediana', 'd11_mediana', 'd12_mediana', 'd13_mediana', 'd14_mediana', 'd15_mediana', 'd16_mediana', 'd17_mediana', 'd18_mediana', 'd19_mediana', 'd20_mediana', 'd21_mediana', 'd22_mediana', 'd23_mediana', 'd24_mediana', 'd25_mediana', 'd26_mediana', 'd27_mediana', 'd28_mediana', 'd29_mediana', 'd30_mediana', 'd31_mediana', 'd32_mediana', 'd33_mediana', 'd34_mediana', 'd35_mediana', 'd36_mediana', 'd37_mediana', 'd38_mediana', 'd39_mediana', 'd40_mediana', 'd41_mediana', 'd42_mediana', 'd43_mediana', 'd44_mediana', 'd45_mediana', 'd46_mediana', 'd47_mediana', 'd48_mediana', 'd49_mediana', 'd50_mediana', 'd1_3quartil', 'd2_3quartil', 'd3_3quartil', 'd4_3quartil', 'd5_3quartil', 'd6_3quartil', 'd7_3quartil', 'd8_3quartil', 'd9_3quartil', 'd10_3quartil', 'd11_3quartil', 'd12_3quartil', 'd13_3quartil', 'd14_3quartil', 'd15_3quartil', 'd16_3quartil', 'd17_3quartil', 'd18_3quartil', 'd19_3quartil', 'd20_3quartil', 'd21_3quartil', 'd22_3quartil', 'd23_3quartil', 'd24_3quartil', 'd25_3quartil', 'd26_3quartil', 'd27_3quartil', 'd28_3quartil', 'd29_3quartil', 'd30_3quartil', 'd31_3quartil', 'd32_3quartil', 'd33_3quartil', 'd34_3quartil', 'd35_3quartil', 'd36_3quartil', 'd37_3quartil', 'd38_3quartil', 'd39_3quartil', 'd40_3quartil', 'd41_3quartil', 'd42_3quartil', 'd43_3quartil', 'd44_3quartil', 'd45_3quartil', 'd46_3quartil', 'd47_3quartil', 'd48_3quartil', 'd49_3quartil', 'd50_3quartil', 'd1_desviopadrao', 'd2_desviopadrao', 'd3_desviopadrao', 'd4_desviopadrao', 'd5_desviopadrao', 'd6_desviopadrao', 'd7_desviopadrao', 'd8_desviopadrao', 'd9_desviopadrao', 'd10_desviopadrao', 'd11_desviopadrao', 'd12_desviopadrao', 'd13_desviopadrao', 'd14_desviopadrao', 'd15_desviopadrao', 'd16_desviopadrao', 'd17_desviopadrao', 'd18_desviopadrao', 'd19_desviopadrao', 'd20_desviopadrao', 'd21_desviopadrao', 'd22_desviopadrao', 'd23_desviopadrao', 'd24_desviopadrao', 'd25_desviopadrao', 'd26_desviopadrao', 'd27_desviopadrao', 'd28_desviopadrao', 'd29_desviopadrao', 'd30_desviopadrao', 'd31_desviopadrao', 'd32_desviopadrao', 'd33_desviopadrao', 'd34_desviopadrao', 'd35_desviopadrao', 'd36_desviopadrao', 'd37_desviopadrao', 'd38_desviopadrao', 'd39_desviopadrao', 'd40_desviopadrao', 'd41_desviopadrao', 'd42_desviopadrao', 'd43_desviopadrao', 'd44_desviopadrao', 'd45_desviopadrao', 'd46_desviopadrao', 'd47_desviopadrao', 'd48_desviopadrao', 'd49_desviopadrao', 'd50_desviopadrao', 'd1_amplitude', 'd2_amplitude', 'd3_amplitude', 'd4_amplitude', 'd5_amplitude', 'd6_amplitude', 'd7_amplitude', 'd8_amplitude', 'd9_amplitude', 'd10_amplitude', 'd11_amplitude', 'd12_amplitude', 'd13_amplitude', 'd14_amplitude', 'd15_amplitude', 'd16_amplitude', 'd17_amplitude', 'd18_amplitude', 'd19_amplitude', 'd20_amplitude', 'd21_amplitude', 'd22_amplitude', 'd23_amplitude', 'd24_amplitude', 'd25_amplitude', 'd26_amplitude', 'd27_amplitude', 'd28_amplitude', 'd29_amplitude', 'd30_amplitude', 'd31_amplitude', 'd32_amplitude', 'd33_amplitude', 'd34_amplitude', 'd35_amplitude', 'd36_amplitude', 'd37_amplitude', 'd38_amplitude', 'd39_amplitude', 'd40_amplitude', 'd41_amplitude', 'd42_amplitude', 'd43_amplitude', 'd44_amplitude', 'd45_amplitude', 'd46_amplitude', 'd47_amplitude', 'd48_amplitude', 'd49_amplitude', 'd50_amplitude']


feature_imp = pd.Series(clf.feature_importances_,index=feature_names).sort_values(ascending=False)
feature2_imp = pd.Series(clf2.feature_importances_,index=feature2_names).sort_values(ascending=False)
feature3_imp = pd.Series(clf3.feature_importances_,index=feature3_names).sort_values(ascending=False)

print('Principais features - Modelo com VAD')
print(feature_imp)
print('+++++++++++++++++++++++++++++++')

print('Principais features - Modelo com dados básicos do Twitter')
print(feature2_imp)
print('+++++++++++++++++++++++++++++++')

print('Principais features - Modelo com 50 dimensões Tang')
print(feature3_imp)
print('++++++++++++FIM++++++++++++++++')


#You can also visualize the feature importance. Visualizations are easy to understand and interpretable.

#For visualization, you can use a combination of matplotlib and seaborn. Because seaborn is built on top of matplotlib, it offers a number of customized themes and provides additional plot Tipos. Matplotlib is a superset of seaborn and both are equally important for good visualizations.


#%matplotlib inline
#get_ipython().magic('matplotlib inline')
# Creating a bar plot
sns.barplot(x=feature_imp, y=feature_imp.index)
# Add labels to your graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features VAD")
plt.legend()
plt.show()
print('+++++++++++++++++++++++++++++++')

# Creating a bar plot
sns.barplot(x=feature2_imp, y=feature2_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features com perfil Twitter")
plt.legend()
plt.show()

print('+++++++++++++++++++++++++++++++')
sns.barplot(x=feature3_imp, y=feature3_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features + 50 dimensões tang")
plt.legend()
plt.show()
print('+++++++++++++++++++++++++++++++')


"""
Generating the Model on Selected Features
Here, you can remove the "sepal width" feature because it has very low importance, and select the 3 remaining features.

# Import train_test_split function
from sklearn.cross_validation import train_test_split
# Split dataset into features and labels
X=data[['petal length', 'petal width','sepal length']]  # Removed feature "sepal length"
y=data['species']                                       
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.70, random_state=5) # 70% training and 30% test
#After spliting, you will generate a model on the selected training set features, perform predictions on the selected test set features, and compare actual and predicted values.

from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

# prediction on test set
y_pred=clf.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

('Accuracy:', 0.95238095238095233)

You can see that after removing the least important features (sepal length), the accuracy increased. 
This is because you removed misleading data and noise, resulting in an increased accuracy. 
A lesser amount of features also reduces the training time.

Conclusion
Congratulations, you have made it to the end of this tutorial!

In this tutorial, you have learned what random forests is, how it works, finding important features, 
the comparison between random forests and decision trees, advantages and disadvantages. 
You have also learned model building, evaluation and finding important features in scikit-learn. B

If you would like to learn more about machine learning, I recommend you take a look at our 
Supervised Learning in R: Classification course.
"""


#https://www.geeksforgeeks.org/saving-a-machine-learning-model/amp/
#import joblib

# Salvar o modelo treinado usando joblib
joblib.dump(clf, 'modelo_randomforest_vad.pkl')

# Carregar o modelo usando joblib
modelo_carregado = joblib.load('modelo_randomforest_vad.pkl')

# Fazer previsões na base de dados de usuários set gen
previsao_usuarios = modelo_carregado.predict(X_users_from_setGen)

print('***********************************************')  
print('Classificaçaõ usuários') 
print(previsao_usuarios)


