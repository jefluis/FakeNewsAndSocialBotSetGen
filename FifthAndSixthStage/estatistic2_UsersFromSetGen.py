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
#from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import numpy as np

def calculate_statistics(v, a, d):
    v_serie = np.array(v)
    a_serie = np.array(a)
    d_serie = np.array(d)

    v_media, a_media, d_media = np.mean(v_serie), np.mean(a_serie), np.mean(d_serie)
    v_1quartil, a_1quartil, d_1quartil = np.percentile(v_serie, 25), np.percentile(a_serie, 25), np.percentile(d_serie, 25)
    v_mediana, a_mediana, d_mediana = np.median(v_serie), np.median(a_serie), np.median(d_serie)
    v_3quartil, a_3quartil, d_3quartil = np.percentile(v_serie, 75), np.percentile(a_serie, 75), np.percentile(d_serie, 75)
    v_desviopadrao, a_desviopadrao, d_desviopadrao = np.std(v_serie), np.std(a_serie), np.std(d_serie)
    v_amplitude, a_amplitude, d_amplitude = np.ptp(v_serie), np.ptp(a_serie), np.ptp(d_serie)

    return v_media, a_media, d_media, v_mediana, a_mediana, d_mediana, v_1quartil, a_1quartil, d_1quartil, v_3quartil, a_3quartil, d_3quartil, v_desviopadrao, a_desviopadrao, d_desviopadrao, v_amplitude, a_amplitude, d_amplitude

#Construindo função para receber variáveis e concatená-las com SQL
def queryTweetbyuser (u):   
    return ("SELECT TweetID, Val, Aro, Dom FROM TweetsOfLabeledNews  WHERE UserID = "+ str(u))
#    return ("SELECT TweetID, Val, Aro, Dom FROM TweetsOfLabeledNews  WHERE Val >0 and UserID = "+ str(u))

def buildQuery (user, 
               v_media, a_media, d_media, 
               v_mediana, a_mediana, d_mediana, 
               v_1quartil, a_1quartil, d_1quartil, 
               v_3quartil, a_3quartil, d_3quartil, 
               v_desviopadrao, a_desviopadrao, d_desviopadrao, 
               v_amplitude, a_amplitude, d_amplitude): 
    return ("UPDATE users_from_setgen SET V_media = "+ str(v_media)+", A_media = "+ str(a_media)+", D_media = "+ str(d_media)+
            ", V_mediana = "+ str(v_mediana)+", A_mediana = "+ str(a_mediana)+", D_mediana = "+ str(d_mediana)+
            ", V_1quartil = "+ str(v_1quartil)+", A_1quartil = "+ str(a_1quartil)+", D_1quartil = "+ str(d_1quartil)+
            ", V_3quartil = "+ str(v_3quartil)+", A_3quartil = "+ str(a_3quartil)+", D_3quartil = "+ str(d_3quartil)+
            ", V_desviopadrao = "+ str(v_desviopadrao)+", A_desviopadrao = "+ str(a_desviopadrao)+", D_desviopadrao = "+ str(d_desviopadrao)+            
            ",  V_amplitude = "+ str(v_amplitude)+",  A_amplitude = "+ str(a_amplitude)+",  D_amplitude = "+ str(d_amplitude)+
            ", Update_Control = 1"+" WHERE UserID = "+ str(user))


def process_user(user_id):
    try:
        # Criar uma nova conexão dentro do processo
        db_process = pymysql.connect(host='localhost', user='root', password='jef123*', db='ime', autocommit=True)
        cursor_tweets_fromuser = db_process.cursor()

        # Consulta SQL para obter os dados do usuário
        query = queryTweetbyuser(user_id)       
        cursor_tweets_fromuser.execute(query)    
        tweetList = cursor_tweets_fromuser.fetchall()
        
        #Inicializando as listas de valores dos léxicos dos tweets de cada usuário
        t, v, a, d = [], [], [], []
        
        # Populando a lista de listas com os valores do banco de dados    
        for linha in tweetList:
            t.append(linha[0])
            v.append(linha[1])
            a.append(linha[2])
            d.append(linha[3])                       
                
        # Calculando estatísticas
        v_media, a_media, d_media, v_mediana, a_mediana, d_mediana, v_1quartil, a_1quartil, d_1quartil, v_3quartil, a_3quartil, d_3quartil, v_desviopadrao, a_desviopadrao, d_desviopadrao, v_amplitude, a_amplitude, d_amplitude = calculate_statistics(v, a, d)
         
   
        # Executando a consulta de atualização
        cursor_tweets_fromuser.execute(buildQuery(user_id, v_media, a_media, d_media, v_mediana, a_mediana, d_mediana, v_1quartil, a_1quartil, d_1quartil, v_3quartil, a_3quartil, d_3quartil, v_desviopadrao, a_desviopadrao, d_desviopadrao, v_amplitude, a_amplitude, d_amplitude))

#        print(f"Usuário {user_id} processado com sucesso.")     

    except Exception as e:
        print(f"Erro ao processar usuário {user_id}: {e}")
        # Rollback caso haja algum erro
        db_process.rollback()
    finally:
        # Não feche a conexão aqui para reutilizá-la posteriormente
        cursor_tweets_fromuser.close()
        db_process.close()  # Fechar a conexão após o uso

# Função principal
def main():
    
    # Criando um objeto de conexão com o banco de dados
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)
    
    try:
        # Criando objetos cursor    
        cursor_UsersWithTweet = db.cursor()
    
        sql_Users_tweets = 'SELECT UserID FROM users_from_setgen where Update_Control IS NULL'
        cursor_UsersWithTweet.execute(sql_Users_tweets)   
        result_users = cursor_UsersWithTweet.fetchall()

        # Lista de IDs de usuários para os quais você deseja calcular as estatísticas    
        users = [row[0] for row in result_users]

        max_processes = 4  # Ajuste este valor conforme necessário
        # Usando ProcessPoolExecutor para processar os usuários em paralelo
        with ProcessPoolExecutor(max_workers=max_processes) as executor:         
            # Iterar sobre os IDs dos usuários e processá-los em paralelo
            results = list(tqdm(executor.map(process_user, users), total=len(users)))
    
        # Os resultados agora contêm o resultado das consultas SQL de atualização para cada usuário processado
        # Você pode querer imprimir ou manipular esses resultados conforme necessário
        #===========================================================================
        # print("Resultados das consultas de atualização:")
        # for result in results:
        #     print(result)
        #===========================================================================
    
    except Exception as e:
        print("Exception occurred:{}".format(e))
        # Rollback caso haja algum erro
        db.rollback()
    finally:   
        db.close()        

#===============================================================================
# # Função principal
# def main():
#     
#     # Criando um objeto de conexão com o banco de dados
#     db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)
#     
#     try:
#         # Criando objetos cursor    
#         cursor_UsersWithTweet = db.cursor()
#         cursor_SetEstatisticInUser = db.cursor()
#     
#         sql_Users_tweets = 'SELECT UserID FROM users_from_setgen'
#         cursor_UsersWithTweet.execute(sql_Users_tweets)   
#         result_users = cursor_UsersWithTweet.fetchall()
#     
#         users = [row[0] for row in result_users]
#      
#         #Vou criar uma varíavel para armazenar as query´s de update até 100 e depois rodar"
#         vCountQuery = 0 
#            
#         with ThreadPoolExecutor() as executor:
#     #        dbMulti = pymysql.connect(host='localhost', user='root', password='jef123*', db='ime', autocommit=True)
#     #        cursor_tweets_fromuser = dbMulti.cursor()
#             for user in tqdm(users):    
#                 cursor_tweets_fromuser = db.cursor()        
#                 cursor_tweets_fromuser.execute(queryTweetbyuser(user))
#                 tweetList = cursor_tweets_fromuser.fetchall()
#                 t, v, a, d = [], [], [], []
#     
#                 for linha in tweetList:
#                     t.append(linha[0])
#                     v.append(linha[1])
#                     a.append(linha[2])
#                     d.append(linha[3])
#     
#                 #===================================================================
#                 # if len(tweetList) == 0 :
#                 #     continue;
#                 #===================================================================
#             
#                 v_media, a_media, d_media, v_mediana, a_mediana, d_mediana, v_1quartil, a_1quartil, d_1quartil, v_3quartil, a_3quartil, d_3quartil, v_desviopadrao, a_desviopadrao, d_desviopadrao, v_amplitude, a_amplitude, d_amplitude = calculate_statistics(v, a, d)
#     
#                 cursor_SetEstatisticInUser.execute(buildQuery(user, v_media, a_media, d_media, v_mediana, a_mediana, d_mediana, v_1quartil, a_1quartil, d_1quartil, v_3quartil, a_3quartil, d_3quartil, v_desviopadrao, a_desviopadrao, d_desviopadrao, v_amplitude, a_amplitude, d_amplitude))
#            
#             db.commit()  # Faça o commit das transações após o loop
#     except Exception as e:
#         print(f"Exceção ocorreu: {e}")
#         db.rollback()
#     finally:
#         db.close()
#===============================================================================


if __name__ == "__main__":
    main()
    