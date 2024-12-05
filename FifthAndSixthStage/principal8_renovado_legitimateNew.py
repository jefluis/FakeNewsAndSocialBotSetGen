# -*- coding: utf-8 -*-
"""
Created on October 18 2023

O objetivo deste script são 3:
a) Para cada Tweet da tabela CONTENT_POLLUTERS_TWEETS, verificar se as palavras contidas nele estão na tabela ESPAÇO EMCOCIONAL 
b) Calcular os valores médios de V-A-D de cada Tweet (usando os valores V-A_D de cada palavra encontrada)   
c) Persistir Valores Médios de V-A-D de cada Tweet na tabela CONTENT_POLLUTERS_TWEETS do banco de dados IME
    
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2014) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire
"""


import pymysql
import pandas as pd
from datetime import datetime


# Criando um objeto de conexão com o banco de dados
db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)

try:
    # Criando objetos cursor
    cursor_espaco_emocional = db.cursor()
    cursor_legitimate_users_tweets = db.cursor()
    cursor_vad_columns = db.cursor()
    
    
    # Montando SQL statements 
    sql_espaco_emocional = 'SELECT Id_Word, Word, V_Mean_Sum, A_Mean_Sum, D_Mean_Sum FROM espaco_emocional_vad'
    sql_teste_tweets = 'SELECT * FROM legitimate_users_tweets_original WHERE Control1=0' 
      
    #Construindo função para receber variáveis e concatená-las com SQL
    def buildQuery (w, x, y, z):        
        return ("UPDATE legitimate_users_tweets_original SET Val = "+ str(w)+", Aro = "+ str(x)+", Dom = "+ str(y)+", Control1 = 1"+" WHERE TweetID = "+ str(z))
             
    # Interação inicial com o banco de dados 
    cursor_espaco_emocional.execute(sql_espaco_emocional)
    cursor_legitimate_users_tweets.execute(sql_teste_tweets)
    
    result_vads = cursor_espaco_emocional.fetchall()
    result_tweets = cursor_legitimate_users_tweets.fetchall()
    
    # Consulta do banco e montogem de uma lista (vads) com a palavra e seus valores
    k = 0
    n = 0
    vads = []
    
    print ('INICIO ',datetime.now())
    for row in result_vads:
        vads.append({'palavra': row[1], 'valores': {'v_mean_sum': row[2], 'a_mean_sum': row[3], 'd_mean_sum': row[4]}})
    
    for row in result_tweets:
        # Split de cada tweet em palavras
        user = row[0]
        twid = row[1]
        palavras = row[7].split()
        when = row[3]
        # Calculando frequência de cada palavra na frase(tweet)
        freq = {x:palavras.count(x) for x in set(palavras)} 
        # Inicializando variáveis
        p = 0
        v = 0
        a = 0
        d = 0
        f = 0        
        # Para cada palavra do tweet a lista de vads é percorrida buscando uma palavra igual
        for palavra in palavras:               
            plvr_buscada = palavra.lower()
            for vad in vads:
                # Se a palavra for encontrada, ela é "printada" e seus atributos calculados                                            
                if vad['palavra'] == plvr_buscada :
                    k = k + 1                                        
                    p = p + 1 
                    #print (palavra,'-->', freq[palavra])
                                        
                    f = f + int(freq[palavra])
                    v = v + (vad['valores']['v_mean_sum'])*int(freq[palavra])
                    a = a + (vad['valores']['a_mean_sum'])*int(freq[palavra])
                    d = d + (vad['valores']['d_mean_sum'])*int(freq[palavra])    
                else :                 
                    n = n + 1                
    
        print ('TWEET ANALISADO: ',row[2]) 
        print ('Qtde Palavras de Sentimento no Tweet Analisado = ', p)
        
        if v != 0 :
            #import decimal 
            #decimal.setcontext(decimal.Context(prec=3)) 
            #D = decimal.Decimal 
            #v = D(v)
            #a = D(a)
            #d = D(d)
            #f = D(f)
            twid = row[1]
            val = v/f
            aro = a/f
            dom = d/f
            # Interação com o banco de dados (persistir v-a-d)
            cursor_vad_columns.execute(buildQuery(val, aro, dom, twid)) 
             
        else :           
            twid = row[1]
            cursor_vad_columns.execute(buildQuery(0, 0, 0, twid))            
          
               
    print(n, k, (k/(n+k))*100)
    print ('FIM ',datetime.now())
    
except Exception as e:
    print("Exeception occured:{}".format(e))
    # Rollback in case there is any error
    db.rollback()
finally:   
    db.close()
