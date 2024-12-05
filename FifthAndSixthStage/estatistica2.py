# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 00:09:37 2018
Este módulo realiza o cálculo estatístico relativo a V-A-D 
@author: Samir Ramos
"""

import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando um objeto de conexão com o banco de dados
db = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'ime',  autocommit=True)

try:
    #Criando função para cálculos estatísticos
    def statistic (l1,l2,l3):   
        v_serie =  pd.Series(l1)
        a_serie =  pd.Series(l2)
        d_serie =  pd.Series(l3)
        
        # MEDIDAS DE TENDÊNCIA CENTRAL
         #Cálculo da Média
        v_media = '{:.2f}'.format(v_serie.mean())
        a_media = '{:.2f}'.format(a_serie.mean())
        d_media = '{:.2f}'.format(d_serie.mean())       
        #Cálculo do 1º Quartil
        v_1quartil = '{:.2f}'.format(v_serie.quantile(q=0.25))
        a_1quartil = '{:.2f}'.format(a_serie.quantile(q=0.25))
        d_1quartil = '{:.2f}'.format(d_serie.quantile(q=0.25))
        #Cálculo da Mediana
        v_mediana = '{:.2f}'.format(v_serie.median())
        a_mediana = '{:.2f}'.format(a_serie.median())
        d_mediana = '{:.2f}'.format(d_serie.median())
        #Cálculo do 3º Quartil
        v_3quartil = '{:.2f}'.format(v_serie.quantile(q=0.75))
        a_3quartil = '{:.2f}'.format(a_serie.quantile(q=0.75))
        d_3quartil = '{:.2f}'.format(d_serie.quantile(q=0.75))
                
        # MEDIDAS DE DISPERSÃO
        
        #Cálculo do Desvio Padrão
        v_desviopadrao = '{:.2f}'.format(v_serie.std())
        a_desviopadrao = '{:.2f}'.format(a_serie.std())
        d_desviopadrao = '{:.2f}'.format(d_serie.std())
        #Cálculo da Amplitude
        v_amplitude = '{:.2f}'.format(v_serie.max() - v_serie.min())
        a_amplitude = '{:.2f}'.format(a_serie.max() - a_serie.min())
        d_amplitude = '{:.2f}'.format(d_serie.max() - d_serie.min())
            
        return (v_media,a_media,d_media,v_mediana,a_mediana,d_mediana,v_1quartil,a_1quartil,d_1quartil,v_3quartil,a_3quartil,d_3quartil,v_desviopadrao,a_desviopadrao,d_desviopadrao,v_amplitude,a_amplitude,d_amplitude)
        
    #Construindo função para receber variáveis e concatená-las com SQL
    def queryTweetbyuser (u):        
        return ("SELECT Tweet_ID, Valence, Arousal, Dominance FROM teste_tweets WHERE User_ID = "+ str(u))
    
    def buildQuery (u,f,g,h,i,j,k,l,m,o,p,q,r,s,v,w,x,y,z):        
        return ("UPDATE content_polluters SET V_media = "+ str(f)+", A_media = "+ str(g)+", D_media = "+ str(h)+", V_1quartil = "+ str(i)+", A_1quartil = "+ str(j)+", D_1quartil = "+ str(k)+", V_mediana = "+ str(l)+", A_mediana = "+ str(m)+", D_mediana = "+ str(o)+", V_3quartil = "+ str(p)+", A_3quartil = "+ str(q)+", D_3quartil = "+ str(r)+", V_desviopadrao = "+ str(s)+", A_desviopadrao = "+ str(v)+", D_desviopadrao = "+ str(w)+",  V_amplitude = "+ str(x)+",  A_amplitude = "+ str(y)+",  D_amplitude = "+ str(z)+" WHERE UserID = "+ str(u))
    
    # Criando objetos cursor    
    cursor_teste_tweets = db.cursor()
    cursor_tweets_fromuser = db.cursor()
    cursor_polluters = db.cursor()
    
    # Montando SQL statements 
    sql_teste_tweets = 'SELECT User_ID FROM teste_tweets'
    sql_content_polluters = 'SELECT UserID FROM content_polluters'
          
    # Interação inicial com o banco de dados     
    cursor_teste_tweets.execute(sql_teste_tweets)    
    result_users = cursor_teste_tweets.fetchall()
    
    #Inicializando lista de usuários
    users = []
    n = 0
    #Persistindo lista de usuários
    for row in set(result_users):
        n = n + 1
        users.append(row[0])
    print(users)
    print('Número de usuários =',n)
    
    
    for user in users:
        # Buscar na tabela teste_tweets  todos os tweets gerados por cada usuário 
        cursor_tweets_fromuser.execute(queryTweetbyuser(user))            
        # Buscar as linhas referentes ao usuário
        tweetList = cursor_tweets_fromuser.fetchall()
        #Inicializando as listas de v-a-d dos tweets de cada usuário
        t = []
        v = []
        a = [] 
        d = []           
        # Printando cada lista
        for linha in tweetList:                
            # Guardar os valores em cada lista
            t.append(linha[0])
            v.append(linha[1])
            a.append(linha[2])
            d.append(linha[3])
        #Print das listas de v, de a, e de d, dos tweets de cada usuário(conta)
        print ('======')
        print ('lista de Valência dos  tweets do usuário', user,' =', v)
        print ('======')
        print ('lista de Excitação dos tweets do usuário', user,' =', a)
        print ('======')
        print ('lista de Dominância de tweets do usuário', user,' =', d)
        
        
        #Calculando Estatísticas da Conta em relação a V-A-D
        v_media, a_media, d_media, v_1quartil, a_1quartil, d_1quartil, v_mediana, a_mediana, d_mediana, v_3quartil, a_3quartil, d_3quartil, v_desviopadrao, a_desviopadrao, d_desviopadrao, v_amplitude, a_amplitude, d_amplitude = statistic (v,a,d)
        print('+++++++++++++++')
        print (v_media,a_media,d_media,v_1quartil,a_1quartil,d_1quartil,v_mediana,a_mediana,d_mediana,v_3quartil,a_3quartil,d_3quartil,v_desviopadrao,a_desviopadrao,d_desviopadrao,v_amplitude,a_amplitude,d_amplitude)       
        print('+++++++++++++++')
        # Interação com o banco de dados (persistir estatistica)
        cursor_polluters.execute(buildQuery(user,v_media,a_media,d_media,v_mediana,a_mediana,d_mediana,v_1quartil,a_1quartil,d_1quartil,v_3quartil,a_3quartil,d_3quartil,v_desviopadrao,a_desviopadrao,d_desviopadrao,v_amplitude,a_amplitude,d_amplitude))
        # Seleciona a linha atualizada e printa o valor da coluna atualizada através de uma função
        def sqlUpdatedQuery (z):        
             return ("SELECT * FROM content_polluters WHERE UserID = "+ str(z))                        
        # Execute the SQL UPDATE query para cada usuário com estatística já inserida
        cursor_polluters.execute(sqlUpdatedQuery(user))            
        # Busca (Fetch) da linha atualizada
        updatedRow = cursor_polluters.fetchall()
        # Mostrar a linha atualizada
        for column in updatedRow:
            print(column)   
                           
        print ('************************************************') 

except Exception as e:
    print("Exeception occured:{}".format(e))
    # Rollback caso haja algum erro
    db.rollback()
finally:   
    db.close()