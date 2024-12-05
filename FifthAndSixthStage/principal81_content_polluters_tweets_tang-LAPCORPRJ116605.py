# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 23:02:31 2020

@author: Samir

O objetivo deste script são 3:
a) Para cada Tweet da tabela CONTENT_POLLUTERS_TWEETS, verificar se as palavras contidas nele estão na tabela ESPAÇO EMCOCIONAL_EMDEDDING 
b) Calcular os valores médios de embedding de cada Tweet (usando os valores D1 a D50 de cada palavra encontrada)   
c) Persistir Valores Médios de embedding de cada Tweet na tabela CONTENT_POLLUTERS_TWEETS do banco de dados IME
    
@author: Samir de Oliveira Ramos - samir.ramos@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-8 2018/2019) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Alex Garcia
"""


import pymysql
from tqdm import tqdm
#import pandas as pd
#import matplotlib.pyplot as plt
#import decimal 


# Criando um objeto de conexão com o banco de dados
#Jeferson Inicio
#db = pymysql.connect(host = 'localhost', user = 'root', password = 'ime@123', db = 'sbseg',  autocommit=True)
db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)
#Jeferson Fim

try:
    # Criando objetos cursor
    cursor_espaco_emocional_tang = db.cursor()
    cursor_content_polluters_tweets = db.cursor()
    cursor_tang_columns = db.cursor()
    
    
    # Montando SQL statements 
    sql_espaco_emocional_tang = 'SELECT * FROM espaco_emocional_tang'
    sql_teste_tweets = 'SELECT * FROM content_polluters_tweets_original WHERE Control2=0'     
    #este WHERE torna o script incremental
     
    #Construindo função para receber variáveis e concatená-las com SQL
    def buildQuery (i, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32, d33, d34, d35, d36, d37, d38, d39, d40, d41, d42, d43, d44, d45, d46, d47, d48, d49, d50):        
        return ("UPDATE content_polluters_tweets_original SET D1 = "+ str(d1)+", D2 = "+ str(d2)+", D3 = "+ str(d3)+", D4 = "+ str(d4)+", D5 = "+ str(d5)+", D6 = "+ str(d6)+", D7 = "+ str(d7)+", D8 = "+ str(d8)+", D9 = "+ str(d9)+", D10 = "+ str(d10)+", D11 = "+ str(d11)+", D12 = "+ str(d12)+", D13 = "+ str(d13)+", D14 = "+ str(d14)+", D15 = "+ str(d15)+", D16 = "+ str(d16)+", D17 = "+ str(d17)+", D18 = "+ str(d18)+", D19 = "+ str(d19)+", D20 = "+ str(d20)+", D21 = "+ str(d21)+", D22 = "+ str(d22)+", D23 = "+ str(d23)+", D24 = "+ str(d24)+", D25 = "+ str(d25)+", D26 = "+ str(d26)+", D27 = "+ str(d27)+", D28 = "+ str(d28)+", D29 = "+ str(d29)+", D30 = "+ str(d30)+", D31 = "+ str(d31)+", D32 = "+ str(d32)+", D33 = "+ str(d33)+", D34 = "+ str(d34)+", D35 = "+ str(d35)+", D36 = "+ str(d36)+", D37 = "+ str(d37)+", D38 = "+ str(d38)+", D39 = "+ str(d39)+", D40 = "+ str(d40)+", D41 = "+ str(d41)+", D42 = "+ str(d42)+", D43 = "+ str(d43)+", D44 = "+ str(d44)+", D45 = "+ str(d45)+", D46 = "+ str(d46)+", D47 = "+ str(d47)+", D48 = "+ str(d48)+", D49 = "+ str(d49)+", D50 = "+ str(d50)+", Control2 = 1"+" WHERE TweetID = "+ str(i))
        
    # Interação inicial com o banco de dados 
    cursor_espaco_emocional_tang.execute(sql_espaco_emocional_tang)
    cursor_content_polluters_tweets.execute(sql_teste_tweets)
    
    result_tang = cursor_espaco_emocional_tang.fetchall()
    result_tweets = cursor_content_polluters_tweets.fetchall()
    
    # Consulta do banco e montogem de uma lista (embeddings) com a palavra e seus valores
    k = 0
    n = 0
    tang = []
    
    for lin in result_tang:
        tang.append({'palavra': lin[1], 'valores': {'D1': lin[2], 'D2': lin[3], 'D3': lin[4], 'D4': lin[5], 'D5': lin[6], 'D6': lin[7], 'D7': lin[8], 'D8': lin[9], 'D9': lin[10], 'D10': lin[11], 'D11': lin[12], 'D12': lin[13], 'D13': lin[14], 'D14': lin[15], 'D15': lin[16], 'D16': lin[17], 'D17': lin[18], 'D18': lin[19], 'D19': lin[20], 'D20': lin[21], 'D21': lin[22], 'D22': lin[23], 'D23': lin[24], 'D24': lin[25], 'D25': lin[26], 'D26': lin[27], 'D27': lin[28], 'D28': lin[29], 'D29': lin[30], 'D30': lin[31], 'D31': lin[32], 'D32': lin[33], 'D33': lin[34], 'D34': lin[35], 'D35': lin[36], 'D36': lin[37], 'D37': lin[38], 'D38': lin[39], 'D39': lin[40], 'D40': lin[41], 'D41': lin[42], 'D42': lin[43], 'D43': lin[44], 'D44': lin[45], 'D45': lin[46], 'D46': lin[47], 'D47': lin[48], 'D48': lin[49], 'D49': lin[50], 'D50': lin[51]}})
        #print(tang[0])
    for row in tqdm(result_tweets):
        # Split de cada tweet em palavras
        user = row[0]
        twid = row[1]
        when = row[3]
        palavras = row[7].split()
        #print(palavras)
        
        # Calculando frequência de cada palavra na frase(tweet)
        freq = {x:palavras.count(x) for x in set(palavras)} 
        # Inicializando variáveis
        p = 0
        d1 = 0
        d2 = 0
        d3 = 0
        d4 = 0
        d5 = 0
        d6 = 0
        d7 = 0
        d8 = 0
        d9 = 0
        d10 = 0
        d11 = 0
        d12 = 0
        d13 = 0
        d14 = 0
        d15 = 0
        d16 = 0
        d17 = 0
        d18 = 0
        d19 = 0
        d20 = 0
        d21 = 0
        d22 = 0
        d23 = 0
        d24 = 0
        d25 = 0
        d26 = 0
        d27 = 0
        d28 = 0
        d29 = 0
        d30 = 0
        d31 = 0
        d32 = 0
        d33 = 0
        d34 = 0
        d35 = 0
        d36 = 0
        d37 = 0
        d38 = 0
        d39 = 0
        d40 = 0
        d41 = 0
        d42 = 0
        d43 = 0
        d44 = 0
        d45 = 0
        d46 = 0
        d47 = 0
        d48 = 0
        d49 = 0
        d50 = 0
        f = 0        
        # Para cada palavra do tweet a lista de vads é percorrida buscando uma palavra igual
        for palavra in palavras:               
            plvr_buscada = palavra.lower()
            for val in tang:
                # Se a palavra for encontrada, ela é "printada" e seus atributos calculados                                            
                if val['palavra'] == plvr_buscada :
                    k = k + 1                                        
                    p = p + 1 
                    #print (palavra,'-->', freq[palavra])
                                        
                    f = f + int(freq[palavra])
                    d1 = d1 + (val['valores']['D1'])*int(freq[palavra])
                    d2 = d2 + (val['valores']['D2'])*int(freq[palavra])
                    d3 = d3 + (val['valores']['D3'])*int(freq[palavra]) 
                    d4 = d4 + (val['valores']['D4'])*int(freq[palavra])
                    d5 = d5 + (val['valores']['D5'])*int(freq[palavra]) 
                    d6 = d6 + (val['valores']['D6'])*int(freq[palavra])
                    d7 = d7 + (val['valores']['D7'])*int(freq[palavra]) 
                    d8 = d8 + (val['valores']['D8'])*int(freq[palavra]) 
                    d9 = d9 + (val['valores']['D9'])*int(freq[palavra]) 
                    d10 = d10 + (val['valores']['D10'])*int(freq[palavra])
                    d11 = d11 + (val['valores']['D11'])*int(freq[palavra])
                    d12 = d12 + (val['valores']['D12'])*int(freq[palavra])
                    d13 = d13 + (val['valores']['D13'])*int(freq[palavra]) 
                    d14 = d14 + (val['valores']['D14'])*int(freq[palavra])
                    d15 = d15 + (val['valores']['D15'])*int(freq[palavra]) 
                    d16 = d16 + (val['valores']['D16'])*int(freq[palavra])
                    d17 = d17 + (val['valores']['D17'])*int(freq[palavra]) 
                    d18 = d18 + (val['valores']['D18'])*int(freq[palavra]) 
                    d19 = d19 + (val['valores']['D19'])*int(freq[palavra]) 
                    d20 = d20 + (val['valores']['D20'])*int(freq[palavra]) 
                    d21 = d21 + (val['valores']['D21'])*int(freq[palavra])
                    d22 = d22 + (val['valores']['D22'])*int(freq[palavra])
                    d23 = d23 + (val['valores']['D23'])*int(freq[palavra]) 
                    d24 = d24 + (val['valores']['D24'])*int(freq[palavra])
                    d25 = d25 + (val['valores']['D25'])*int(freq[palavra]) 
                    d26 = d26 + (val['valores']['D26'])*int(freq[palavra])
                    d27 = d27 + (val['valores']['D27'])*int(freq[palavra]) 
                    d28 = d28 + (val['valores']['D28'])*int(freq[palavra]) 
                    d29 = d29 + (val['valores']['D29'])*int(freq[palavra]) 
                    d30 = d30 + (val['valores']['D30'])*int(freq[palavra]) 
                    d31 = d31 + (val['valores']['D31'])*int(freq[palavra])
                    d32 = d32 + (val['valores']['D32'])*int(freq[palavra])
                    d33 = d33 + (val['valores']['D33'])*int(freq[palavra]) 
                    d34 = d34 + (val['valores']['D34'])*int(freq[palavra])
                    d35 = d35 + (val['valores']['D35'])*int(freq[palavra]) 
                    d36 = d36 + (val['valores']['D36'])*int(freq[palavra])
                    d37 = d37 + (val['valores']['D37'])*int(freq[palavra]) 
                    d38 = d38 + (val['valores']['D38'])*int(freq[palavra]) 
                    d39 = d39 + (val['valores']['D39'])*int(freq[palavra]) 
                    d40 = d40 + (val['valores']['D40'])*int(freq[palavra])
                    d41 = d41 + (val['valores']['D41'])*int(freq[palavra])
                    d42 = d42 + (val['valores']['D42'])*int(freq[palavra])
                    d43 = d43 + (val['valores']['D43'])*int(freq[palavra]) 
                    d44 = d44 + (val['valores']['D44'])*int(freq[palavra])
                    d45 = d45 + (val['valores']['D45'])*int(freq[palavra]) 
                    d46 = d46 + (val['valores']['D46'])*int(freq[palavra])
                    d47 = d47 + (val['valores']['D47'])*int(freq[palavra]) 
                    d48 = d48 + (val['valores']['D48'])*int(freq[palavra]) 
                    d49 = d49 + (val['valores']['D49'])*int(freq[palavra]) 
                    d50 = d50 + (val['valores']['D50'])*int(freq[palavra]) 
                else :                 
                    n = n + 1                
    
        #print ('TWEET ANALISADO: ',row[7]) 
        #print ('Qtde Palavras de vocab Tang no Tweet Analisado = ', p)
        
        if d1 != 0 :
            
            #decimal.setcontext(decimal.Context(prec=3)) 
            #D = decimal.Decimal 
            #v = D(v)
            #a = D(a)
            #d = D(d)
            #f = D(f)
            twid = row[1]
            D1 = d1/f
            D2 = d2/f
            D3 = d3/f
            D4 = d4/f
            D5 = d5/f
            D6 = d6/f
            D7 = d7/f
            D8 = d8/f
            D9 = d9/f
            D10 = d10/f
            D11 = d11/f
            D12 = d12/f
            D13 = d13/f
            D14 = d14/f
            D15 = d15/f
            D16 = d16/f
            D17 = d17/f
            D18 = d18/f
            D19 = d19/f
            D20 = d20/f
            D21 = d21/f
            D22 = d22/f
            D23 = d23/f
            D24 = d24/f
            D25 = d25/f
            D26 = d26/f
            D27 = d27/f
            D28 = d28/f
            D29 = d29/f
            D30 = d30/f
            D31 = d31/f
            D32 = d32/f
            D33 = d33/f
            D34 = d34/f
            D35 = d35/f
            D36 = d36/f
            D37 = d37/f
            D38 = d38/f
            D39 = d39/f
            D40 = d40/f
            D41 = d41/f
            D42 = d42/f
            D43 = d43/f
            D44 = d44/f
            D45 = d45/f
            D46 = d46/f
            D47 = d47/f
            D48 = d48/f
            D49 = d49/f
            D50 = d50/f
            # Interação com o banco de dados (persistir v-a-d)
            cursor_tang_columns.execute(buildQuery(twid, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34, D35, D36, D37, D38, D39, D40, D41, D42, D43, D44, D45, D46, D47, D48, D49, D50)) 
            
            # Select the updated row and print the updated column value through a function
            def sqlUpdatedQuery (k):        
                return ("SELECT * FROM content_polluters_tweets_original WHERE TweetID = "+ str(k))                        
            # Execute the SQL SELECT query
            cursor_tang_columns.execute(sqlUpdatedQuery(twid))            
            # Fetch the updated row
            updatedRow = cursor_tang_columns.fetchall()
            # Print the updated row...
            #for column in updatedRow:
                #print(column)    
            #print ('************************************************') 
            
        else :           
            twid = row[1]
            cursor_tang_columns.execute(buildQuery(twid, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))            
            # Select the updated row and print the updated column value through a function
            def sqlUpdateQuery (z):        
                return ("SELECT * FROM content_polluters_tweets_original WHERE TweetID = "+ str(z))                        
            # Execute the SQL SELECT query
            cursor_tang_columns.execute(sqlUpdateQuery(twid))            
            # Fetch the updated row
            updatedRow = cursor_tang_columns.fetchall()
            # Print the updated row...
            #for column in updatedRow:
                 #print(column)    
            #print ('************************************************')              
               
    #print(n, k, (k/(n+k))*100)
    
except Exception as e:
    print("Exception occurred:{}".format(e))
    # Rollback in case there is any error
    db.rollback()
finally:   
    db.close()
