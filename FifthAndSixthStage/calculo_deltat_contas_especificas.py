# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 07:18:44 2018

@author: Samir Ramos

Updated on December 2022
@author: Jeferson Luis Gonçalves
"""


import pymysql
import pandas as pd
import math
#import numpy as np
#import matplotlib.pyplot as plt
import sys
import datetime as dt

# Criando um objeto de conexão com o banco de dados
# Jeferson Begin
#db = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'ime',  autocommit=True)
db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)
# Jeferson End

try:
    # Criando função para transformar datetime em timestamp
    def ConvertDatetimetoTimestamp (date_time):
        timestamp = dt.datetime.timestamp(date_time)
        return (timestamp)
    
    #Criando função para cálculos estatísticos
    def statistic (l):   
        dt_serie =  pd.Series(l)
        
       
        # MEDIDAS DE TENDÊNCIA CENTRAL
         #Cálculo da Média
        dt_media = dt_serie.mean()
            
        #Cálculo do 1º Quartil
        dt_1quartil = dt_serie.quantile(q=0.25)
        
        #Cálculo da Mediana
        dt_mediana = dt_serie.median()
       
        #Cálculo do 3º Quartil
        dt_3quartil = dt_serie.quantile(q=0.75)
       
                
        # MEDIDAS DE DISPERSÃO
        
        #Cálculo do Desvio Padrão           
        x1 =  len(l)
        soma1 = 0
        for valor in l:
            soma1 = soma1 + (valor - dt_serie.mean())**2
        dt_desviopadrao = math.sqrt(soma1/x1)
      
       
        
        #Cálculo da Amplitude
        dt_amplitude = (dt_serie.max() - dt_serie.min())
        
            
        return (dt_media,dt_mediana,dt_1quartil,dt_3quartil,dt_desviopadrao,dt_amplitude)
        
    #Construindo função para receber variáveis e concatená-las com SQL
    def queryTweetbyuser0 (u):        
        return ("SELECT TweetID, CreatedAt FROM legitimate_users_tweets WHERE UserID = "+ str(u))
    
    def queryTweetbyuser1 (u):        
        return ("SELECT TweetID, CreatedAt FROM content_polluters_tweets WHERE UserID = "+ str(u))
    
    def buildQuery (u,f,i,l,p,s,x): 
        return ("UPDATE accounts SET Dt_media = "+ str(f)+", Dt_1quartil = "+ str(i)+", Dt_mediana = "+ str(l)+", Dt_3quartil = "+ str(p)+", Dt_desviopadrao = "+ str(s)+", Dt_amplitude = "+ str(x)+" WHERE UserID = "+ str(u))
    # Criando objetos cursor  
    cursor_accounts = db.cursor()
    cursor_content_polluters_tweets = db.cursor()
    cursor_legitimate_users_tweets = db.cursor()
    cursor_tweets_fromuser = db.cursor()
   
    
    # Montando SQL statements 
    sql_users0_accounts = 'SELECT UserID FROM accounts WHERE Type = 0'
    sql_content_polluters_tweets = 'SELECT UserID, CreatedAt FROM content_polluters_tweets'
    sql_legitimate_users_tweets = 'SELECT UserID, CreatedAt FROM legitimate_users_tweets'
    #sql_content_polluters = 'SELECT UserID FROM legitimate_users'
          
    # Interação inicial com o banco de dados  
    cursor_accounts.execute(sql_users0_accounts)
    result_users0 = cursor_accounts.fetchall()
    
    #cursor_content_polluters_tweets.execute(sql_content_polluters_tweets)    
    #result_users = cursor_content_polluters_tweets.fetchall()
    
    #Inicializando lista de usuários
    users0 = []
    n = 0
    #Guardar (em tempo de execução) lista de usuários
    for row in set(result_users0):
        n = n + 1
        users0.append(row[0])
    print(users0)
    print('Número total de usuários de Accounts =',n)
    ttotal0 = []    
    for user in users0:
        print('Vamos trabalhar dados do usuário', user)
        # Buscar na tabela legitimate_users_tweets todos os tweets gerados por cada usuário 
        cursor_tweets_fromuser.execute(queryTweetbyuser0(user))            
        # Buscar as linhas referentes ao usuário
        tweetList0 = cursor_tweets_fromuser.fetchall()
        #Inicializando as listas de timestamps dos tweets de cada usuário
        t = []
        m=0  
        lista_posix_dates0 = []
        # Printando cada lista
        for linha in tweetList0:  
            m = m + 1
            # Transformar os valores de datetime para timestamp                        
            t0 = ConvertDatetimetoTimestamp(linha[1])
            # Como não podemos modificar os elementos de uma tupla, devemos substituí-la por uma tupla diferente
            newtupla = (linha[0], t0)
            lista_posix_dates0.append(newtupla)
            #print(lista_posix_dates0)                   
            # Guardar os valores de timestamp t0 em uma lista t
            t.append(t0)
            
        #Print das listas de timestamp dos tweets de cada usuário(conta)
        print ('======')
        print ('lista de Timestamp dos  tweets do usuário tipo 0 ', user,' =',t)
        print ('======')
        #Ordenando t
        t.sort()        
        #Cálculo dos delta t's na lista t        
        j = len(t)        
        if j<2: continue
        newt = []
        while j>1:
            delta = t[j-1] - t[j-2]
            newt.append(delta)
            j = j-1
        
            
       
        #Calculando Estatísticas da Conta em relação a V-A-D
        dt_media, dt_1quartil, dt_mediana, dt_3quartil, dt_desviopadrao, dt_amplitude = statistic (newt)
        print('+++++++++++++++')
        print (dt_media, dt_1quartil, dt_mediana, dt_3quartil, dt_desviopadrao, dt_amplitude)       
        print('+++++++++++++++')
      
       
        
        # Interação com o banco de dados (persistir estatistica)
        cursor_accounts.execute(buildQuery(user, dt_media, dt_1quartil, dt_mediana, dt_3quartil, dt_desviopadrao, dt_amplitude))
        # Seleciona a linha atualizada e printa o valor da coluna atualizada através de uma função
        def sqlUpdatedQuery (z):        
             return ("SELECT * FROM accounts WHERE UserID = "+ str(z))                        
        # Execute the SQL UPDATE query para cada usuário com estatística já inserida
        cursor_accounts.execute(sqlUpdatedQuery(user))            
        # Busca (Fetch) da linha atualizada
        updatedRow =  cursor_accounts.fetchall()
        # Mostrar a linha atualizada
        for column in updatedRow:
            print(column)   
                           
        print ('************************************************') 
        
       
       

except Exception as e:
    print(sys.exc_info())
    #print("Exeception occured:{}".format(e))
    # Rollback caso haja algum erro
    db.rollback()
finally:   
    db.close()
