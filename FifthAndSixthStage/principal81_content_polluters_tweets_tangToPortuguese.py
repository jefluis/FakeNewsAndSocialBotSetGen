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
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import datetime

def buildQuery(i, d_values):
    update_query = "UPDATE content_polluters_tweets_original_PT SET "
    for idx, d_value in enumerate(d_values, start=1):
        update_query += f"D{idx} = {d_value}, "
    update_query += f"Control2 = 1 WHERE TweetID = {i}"
    return update_query

def process_tweet_wrapper(args):
    row, tang = args
    return process_tweet(row, tang)

def process_tweet(row, tang): 
    twid = row['TweetID']        
    palavras = row['Tweet_Limpo_PT'].split()
    
    freq = {x: palavras.count(x) for x in set(palavras)} 
    p = 0
    f = 0
    d_values = [0] * 50 

    for palavra in palavras:
#    for palavra in tqdm(palavras, desc='Processing words', leave=False):   
        plvr_buscada = palavra.lower()
        
        if plvr_buscada and plvr_buscada in tang:
            val = tang[plvr_buscada]
            p += 1
            f += int(freq[palavra])
            for i in range(50):
                d_values[i] += val['D' + str(i + 1)] * int(freq[palavra])
        else:
            # lógica para lidar com palavras não encontradas em 'tang'
            pass

    for i in range(50):
        if d_values[i] != 0:
            d_values[i] /= f

    return twid, d_values 


db = pymysql.connect(host='localhost', user='root', password='jef123*', db='ime', autocommit=True)

try:
    cursor_espaco_emocional_tang = db.cursor(pymysql.cursors.DictCursor)
    cursor_content_polluters_tweets = db.cursor(pymysql.cursors.DictCursor)
    cursor_tang_columns = db.cursor()

    # Montando SQL statements     
    sql_espaco_emocional_tang = 'SELECT * FROM espaco_emocional_tang'
    sql_teste_tweets = 'SELECT * FROM content_polluters_tweets_original_PT WHERE Control2=0'
    
    cursor_espaco_emocional_tang.execute(sql_espaco_emocional_tang)
    tang = {row['Word_PT'].lower(): 
            {
'D1': row['D1'],   'D2': row['D2'],   'D3': row['D3'],   'D4': row['D4'],   'D5': row['D5'],   'D6': row['D6'],   'D7': row['D7'],   'D8': row['D8'],   'D9': row['D9'],  'D10': row['D10'],
'D11': row['D11'], 'D12': row['D12'], 'D13': row['D13'], 'D14': row['D14'], 'D15': row['D15'], 'D16': row['D16'], 'D17': row['D17'], 'D18': row['D18'], 'D19': row['D19'], 'D20': row['D20'], 
'D21': row['D21'], 'D22': row['D22'], 'D23': row['D23'], 'D24': row['D24'], 'D25': row['D25'], 'D26': row['D26'], 'D27': row['D27'], 'D28': row['D28'], 'D29': row['D29'], 'D30': row['D30'], 
'D31': row['D31'], 'D32': row['D32'], 'D33': row['D33'], 'D34': row['D34'], 'D35': row['D35'], 'D36': row['D36'], 'D37': row['D37'], 'D38': row['D38'], 'D39': row['D39'], 'D40': row['D34'], 
'D41': row['D41'], 'D42': row['D42'], 'D43': row['D43'], 'D44': row['D44'], 'D45': row['D45'], 'D46': row['D46'], 'D47': row['D47'], 'D48': row['D48'], 'D49': row['D49'], 'D50': row['D50']
            
             } 
            for row in cursor_espaco_emocional_tang.fetchall()}
    
    cursor_content_polluters_tweets.execute(sql_teste_tweets)
    result_tweets = cursor_content_polluters_tweets.fetchall()
    
    #Vou criar uma varíavel para armazenar as query´s de update até 100 e depois rodar"
    vCountQuery = 0 

    with ThreadPoolExecutor() as executor:
        # Crie uma lista de tuplas contendo o row e o dicionário tang
        args_list = [(row, tang) for row in result_tweets]
        for vtwid, vd_values in tqdm(executor.map(process_tweet_wrapper, args_list), total=len(result_tweets)):
     

 #       for vtwid, vd_values in tqdm(executor.map(process_tweet, result_tweets, tang), total=len(result_tweets)):
            cursor_tang_columns.execute(buildQuery(vtwid, vd_values))
            vCountQuery += 1
            if vCountQuery == 1000:                    
                db.commit()
                agora = datetime.datetime.now()
                print(f"Transação bem-sucedida para os últimos {vCountQuery} registros! - {agora}")
                vCountQuery = 0
     
    # Finalizar a transação, se houver atualizações pendentes
    if vCountQuery > 0:
        db.commit()     
        
    print("****** fim ****** ")

except Exception as e:
    print("Exception occurred: {}".format(e))
    db.rollback()
finally:
    db.close()
