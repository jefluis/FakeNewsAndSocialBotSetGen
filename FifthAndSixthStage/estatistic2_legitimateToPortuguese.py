# -*- coding: utf-8 -*-
"""
Created on October 18 2023
   
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2014) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire
"""

import pymysql
import pandas as pd
import math
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

#Criando função para cálculos estatísticos
def statistic (l1,l2,l3):   
    v_serie =  pd.Series(l1)
    a_serie =  pd.Series(l2)
    d_serie =  pd.Series(l3)
    
    # MEDIDAS DE TENDÊNCIA CENTRAL
    #Cálculo da Média
    v_media = v_serie.mean()
    a_media = a_serie.mean()
    d_media = d_serie.mean()       
    #Cálculo do 1º Quartil
    v_1quartil = v_serie.quantile(q=0.25)
    a_1quartil = a_serie.quantile(q=0.25)
    d_1quartil = d_serie.quantile(q=0.25)
    #Cálculo da Mediana
    v_mediana = v_serie.median()
    a_mediana = a_serie.median()
    d_mediana = d_serie.median()
    #Cálculo do 3º Quartil
    v_3quartil = v_serie.quantile(q=0.75)
    a_3quartil = a_serie.quantile(q=0.75)
    d_3quartil = d_serie.quantile(q=0.75)
            
    # MEDIDAS DE DISPERSÃO
    
    #Cálculo do Desvio Padrão           
    x1 =  len(l1)
    soma1 = 0
    for valor in l1:
        soma1 = soma1 + (valor - v_serie.mean())**2
    v_desviopadrao = math.sqrt(soma1/x1)
    
    x2 = len(l2)    
    soma2 = 0
    for valor in l2:
        soma2 = soma2 + (valor - a_serie.mean())**2
    a_desviopadrao = math.sqrt(soma2/x2)
            
    x3 = len(l3)  
    soma3 = 0
    for valor in l3:
        soma3 = soma3 + (valor - d_serie.mean())**2
    d_desviopadrao = math.sqrt(soma3/x3)
    
    #Cálculo da Amplitude
    v_amplitude = (v_serie.max() - v_serie.min())
    a_amplitude = (a_serie.max() - a_serie.min())
    d_amplitude = (d_serie.max() - d_serie.min())
    
    return (v_media,a_media,d_media,v_mediana,a_mediana,d_mediana,v_1quartil,a_1quartil,d_1quartil,v_3quartil,a_3quartil,d_3quartil,v_desviopadrao,a_desviopadrao,d_desviopadrao,v_amplitude,a_amplitude,d_amplitude)

# retorna todos os tweets de um usuário
def queryTweetbyuser (u):        
    return ("SELECT TweetID, Val, Aro, Dom FROM legitimate_users_tweets_original_pt WHERE UserID = "+ str(u))

def buildQuery (user, 
               v_media, a_media, d_media, 
               v_mediana, a_mediana, d_mediana, 
               v_1quartil, a_1quartil, d_1quartil, 
               v_3quartil, a_3quartil, d_3quartil, 
               v_desviopadrao, a_desviopadrao, d_desviopadrao, 
               v_amplitude, a_amplitude, d_amplitude): 
    return ("UPDATE legitimate_usersToPortuguese SET V_media = "+ str(v_media)+", A_media = "+ str(a_media)+", D_media = "+ str(d_media)+
            ", V_mediana = "+ str(v_mediana)+", A_mediana = "+ str(a_mediana)+", D_mediana = "+ str(d_mediana)+
            ", V_1quartil = "+ str(v_1quartil)+", A_1quartil = "+ str(a_1quartil)+", D_1quartil = "+ str(d_1quartil)+
            ", V_3quartil = "+ str(v_3quartil)+", A_3quartil = "+ str(a_3quartil)+", D_3quartil = "+ str(d_3quartil)+
            ", V_desviopadrao = "+ str(v_desviopadrao)+", A_desviopadrao = "+ str(a_desviopadrao)+", D_desviopadrao = "+ str(d_desviopadrao)+            
            ",  V_amplitude = "+ str(v_amplitude)+",  A_amplitude = "+ str(a_amplitude)+",  D_amplitude = "+ str(d_amplitude)+
            ", Update_Control = 1"+" WHERE UserID = "+ str(user))

# Serve para processar os tweets de cada usuário
#===============================================================================
# def process_user(user):
#     try:
#         # Criar uma nova conexão para cada thread
#         db = pymysql.connect(host='localhost', user='root', password='jef123*', db='ime', autocommit=True)
# 
#         cursor_tweets_fromuser = db.cursor()
#         cursor_SetEstatisticInUser = db.cursor()
# 
#         cursor_tweets_fromuser.execute(queryTweetbyuser(user))
#         tweetList = cursor_tweets_fromuser.fetchall()
#         t, v, a, d = [], [], [], []
# 
#         for linha in tweetList:
#             t.append(linha[0])
#             v.append(linha[1])
#             a.append(linha[2])
#             d.append(linha[3])
# 
#         v_media,a_media,d_media,v_mediana,a_mediana,d_mediana,v_1quartil,a_1quartil,d_1quartil,v_3quartil,a_3quartil,d_3quartil,v_desviopadrao,a_desviopadrao,d_desviopadrao,v_amplitude,a_amplitude,d_amplitude = statistic(v, a, d)
# 
#         cursor_SetEstatisticInUser.execute(buildQuery(user, v_media, a_media, d_media, v_mediana, a_mediana, d_mediana, v_1quartil, a_1quartil, d_1quartil, v_3quartil, a_3quartil, d_3quartil, v_desviopadrao, a_desviopadrao, d_desviopadrao, v_amplitude, a_amplitude, d_amplitude))
# 
#         print(f"Usuário {user} processado.")
#     except Exception as e:
#         print(f"Erro ao processar usuário {user}: {e}")
#===============================================================================


# Criando um objeto de conexão com o banco de dados
db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)

try:
    cursor_UsersWithTweet = db.cursor()
    cursor_SetEstatisticInUser = db.cursor()

    sql_Users_tweets = 'SELECT distinct UserID FROM legitimate_users_tweets_original_pt'
    cursor_UsersWithTweet.execute(sql_Users_tweets)   
    result_users = cursor_UsersWithTweet.fetchall()

    users = [row[0] for row in result_users]

    #Vou criar uma varíavel para armazenar as query´s de update até 100 e depois rodar"
    vCountQuery = 0 
    
    with ThreadPoolExecutor() as executor:
        for user in tqdm(users):
            cursor_tweets_fromuser = db.cursor()
            cursor_tweets_fromuser.execute(queryTweetbyuser(user))
            tweetList = cursor_tweets_fromuser.fetchall()
            t, v, a, d = [], [], [], []

            for linha in tweetList:
                t.append(linha[0])
                v.append(linha[1])
                a.append(linha[2])
                d.append(linha[3])

            v_media, a_media, d_media, v_mediana, a_mediana, d_mediana, v_1quartil, a_1quartil, d_1quartil, v_3quartil, a_3quartil, d_3quartil, v_desviopadrao, a_desviopadrao, d_desviopadrao, v_amplitude, a_amplitude, d_amplitude = statistic(v, a, d)

            cursor_SetEstatisticInUser.execute(buildQuery(user, v_media, a_media, d_media, v_mediana, a_mediana, d_mediana, v_1quartil, a_1quartil, d_1quartil, v_3quartil, a_3quartil, d_3quartil, v_desviopadrao, a_desviopadrao, d_desviopadrao, v_amplitude, a_amplitude, d_amplitude))
    #===========================================================================
    #         vCountQuery += 1
    #         if vCountQuery == 100:                    
    #             db.commit()
    #             agora = datetime.datetime.now()
    #             print(f"Transação bem-sucedida para os últimos {vCountQuery} registros! - {agora}")
    #             vCountQuery = 0
    #   
    # # Finalizar a transação, se houver atualizações pendentes
    # if vCountQuery > 0:
    #     db.commit()  
    #===========================================================================
        
        db.commit()  # Faça o commit das transações após o loop
except Exception as e:
    print(f"Exceção ocorreu: {e}")
    db.rollback()
finally:
    db.close()

