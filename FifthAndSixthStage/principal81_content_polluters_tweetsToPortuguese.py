# -*- coding: utf-8 -*-
"""
Created on October 18 2023

O objetivo deste script são 3:
a) Para cada Tweet da tabela CONTENT_POLLUTERS_TWEETS, verificar se as palavras contidas nele estão na tabela ESPAÇO EMCOCIONAL 
b) Calcular os valores médios de V-A-D de cada Tweet (usando os valores V-A_D de cada palavra encontrada)   
c) Persistir Valores Médios de V-A-D de cada Tweet na tabela CONTENT_POLLUTERS_TWEETS do banco de dados IME
    
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2024) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire
"""

import pymysql
from tqdm import tqdm

def build_query(valence, arousal, dominance, tweet_id):
    return f"UPDATE content_polluters_tweets_original_pt SET Val = {valence}, Aro = {arousal}, Dom = {dominance}, Control1 = 1 WHERE TweetID = {tweet_id}"

def process_tweets(cursor_vad_columns, vads, tweets):
    n, k = 0, 0
    
    for tweet in tqdm(tweets):
        # Split de cada tweet em palavras
        palavras = tweet['Tweet_Limpo_PT'].split()
        # Calculando frequência de cada palavra na frase(tweet)
        freq = {x: palavras.count(x) for x in set(palavras)}
        p, v, a, d, f = 0, 0, 0, 0, 0
        # Para cada palavra do tweet a lista de vads é percorrida buscando uma palavra igual
        for palavra in palavras:
            palavra_buscada = palavra.lower()
            vad = vads.get(palavra_buscada)
            if vad:
                k += 1
                p += 1
                f += freq[palavra]
                print (palavra,'-->', freq[palavra])
                v += vad['v_mean_sum'] * freq[palavra]
                a += vad['a_mean_sum'] * freq[palavra]
                d += vad['d_mean_sum'] * freq[palavra]
            else:
                n += 1

        print ('TWEET ANALISADO: ',tweet['Tweet_Limpo_PT']) 
        print ('Qtde Palavras de Sentimento no Tweet Analisado = ', p)
        
        tweet_id = tweet['TweetID']
        if f != 0:            
            valence, arousal, dominance = v / f, a / f, d / f
            cursor_vad_columns.execute(build_query(valence, arousal, dominance, tweet_id))
        else:
            cursor_vad_columns.execute(build_query(0, 0, 0, tweet_id))

    return n, k

db = pymysql.connect(host='localhost', user='root', password = 'jef123*', db = 'ime', autocommit=True)

try:
    cursor_espaco_emocional_vad = db.cursor(pymysql.cursors.DictCursor)
    cursor_content_polluters_tweets = db.cursor(pymysql.cursors.DictCursor)
    cursor_vad_columns = db.cursor()

    sql_espaco_emocional = 'SELECT Id_Word, Word_pt, V_Mean_Sum, A_Mean_Sum, D_Mean_Sum FROM espaco_emocional_vad'
    sql_teste_tweets = 'SELECT * FROM content_polluters_tweets_original_pt WHERE Control1=0'

    cursor_espaco_emocional_vad.execute(sql_espaco_emocional)
    vads = {row['Word_pt'].lower(): {'v_mean_sum': row['V_Mean_Sum'], 'a_mean_sum': row['A_Mean_Sum'], 'd_mean_sum': row['D_Mean_Sum']} for row in cursor_espaco_emocional_vad.fetchall()}

    cursor_content_polluters_tweets.execute(sql_teste_tweets)
    tweets = cursor_content_polluters_tweets.fetchall()

    n, k = process_tweets(cursor_vad_columns, vads, tweets)
    
    print(n, k, (k / (n + k)) * 100)

except Exception as e:
    print("Exceção ocorreu: {}".format(e))
    db.rollback()
finally:
    db.close()
    
