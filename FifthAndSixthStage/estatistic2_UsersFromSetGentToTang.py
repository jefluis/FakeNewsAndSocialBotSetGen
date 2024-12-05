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
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import numpy as np

#Criando função para cálculos estatísticos
def calculate_statistics(*args):
    dataframes = [pd.Series(data) for data in args]
    means = [serie.mean() for serie in dataframes]
    quartiles_1st = [serie.quantile(0.25) for serie in dataframes]
    medians = [serie.median() for serie in dataframes]
    quartiles_3rd = [serie.quantile(0.75) for serie in dataframes]
    std_devs = [np.std(serie) for serie in dataframes]
    amplitudes = [(serie.max() - serie.min()) for serie in dataframes]
    
    statistics = {
        f'd{i+1}': {
            'mean': mean,
            '1st quartile': q1,
            'median': median,
            '3rd quartile': q3,
            'standard deviation': std_dev,
            'amplitude': amplitude
        }
        for i, (mean, q1, median, q3, std_dev, amplitude) in enumerate(zip(means, quartiles_1st, medians, quartiles_3rd, std_devs, amplitudes))
    }
    return statistics


# Função para processar um usuário
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
        t = []        
        # Inicializando uma lista de listas para armazenar D1 a D50
        lexicon_values = [[] for _ in range(50)]
        
        # Populando a lista de listas com os valores do banco de dados        
        for linha in tweetList:                
            t.append(linha[0])
            for i in range(50):
                lexicon_values[i].append(linha[i+1]) 
                
        # Calculando estatísticas
        result = calculate_statistics(*lexicon_values)
    
        # Construindo e executando a consulta SQL de atualização
        update_query = "UPDATE users_from_setgen SET "
        update_values = []
        for i in range(50):
            field_name = f'd{i + 1}'
            update_query += f"{field_name}_media = %s, "
            update_query += f"{field_name}_1quartil = %s, "
            update_query += f"{field_name}_mediana = %s, "
            update_query += f"{field_name}_3quartil = %s, "
            update_query += f"{field_name}_desviopadrao = %s, "
            update_query += f"{field_name}_amplitude = %s"
            
            update_values.extend([
                result[field_name]['mean'],
                result[field_name]['1st quartile'],
                result[field_name]['median'],
                result[field_name]['3rd quartile'],
                result[field_name]['standard deviation'],
                result[field_name]['amplitude']
            ])
            
            if i < 49:
                update_query += ", "
        
        update_query += ", Update_Control3 = 1 WHERE userid = %s;"
        update_values.append(user_id)
    
        # Executando a consulta de atualização
        cursor_tweets_fromuser.execute(update_query, update_values)
        
#        print(f"Usuário {user_id} processado com sucesso.")     

    except Exception as e:
        print(f"Erro ao processar usuário {user_id}: {e}")
        # Rollback caso haja algum erro
        db_process.rollback()
    finally:
        # Não feche a conexão aqui para reutilizá-la posteriormente
        cursor_tweets_fromuser.close()
        db_process.close()  # Fechar a conexão após o uso
 
# Função para obter os tweets do usuário a partir do banco de dados
def queryTweetbyuser(user_id):
    return f"SELECT TweetID,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20,D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,D32,D33,D34,D35,D36,D37,D38,D39,D40,D41,D42,D43,D44,D45,D46,D47,D48,D49,D50 FROM TweetsOfLabeledNews WHERE UserID = {user_id}"


# Função principal
def main():

    # Criando um objeto de conexão com o banco de dados
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)
    
    try:
        # Criando objetos cursor    
        cursor_UsersWithTweet = db.cursor()
    
#        sql_Users_tweets = 'SELECT distinct UserID FROM TweetsOfLabeledNews'
        sql_Users_tweets = 'SELECT UserID FROM users_from_setgen where Update_Control3 = 0'
        
        cursor_UsersWithTweet.execute(sql_Users_tweets)   
        result_users = cursor_UsersWithTweet.fetchall()
        
        # Lista de IDs de usuários para os quais você deseja calcular as estatísticas
        user_ids = [row[0] for row in result_users]    
        
        max_processes = 4  # Ajuste este valor conforme necessário
        # Usando ProcessPoolExecutor para processar os usuários em paralelo
        with ProcessPoolExecutor(max_workers=max_processes) as executor:         
            # Iterar sobre os IDs dos usuários e processá-los em paralelo
            results = list(tqdm(executor.map(process_user, user_ids), total=len(user_ids)))
    
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
    

if __name__ == "__main__":
    main()
    
 