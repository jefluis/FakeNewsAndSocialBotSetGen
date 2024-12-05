# -*- coding: utf-8 -*-
"""
Created on August 21 2023

 
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2024) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire

"""
import pymysql
import pandas as pd

def execute_query(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

# Conectar ao banco de dados
db = pymysql.connect(host='localhost', user='root', password='jef123*', db='ime', autocommit=True)


sql_users_from_setGen = '''
    select UserID, 
    prediction_basic_vad_features_LR,
    prediction_basic_vad_features_KNN,
    prediction_basic_vad_features_DT,
    prediction_basic_vad_features_RF,
    prediction_basic_vad_features_Gradient,
    prediction_basic_vad_features_Neural,
    
    prediction_basic_tang_features_LR,
    prediction_basic_tang_features_KNN,
    prediction_basic_tang_features_DT,
    prediction_basic_tang_features_RF,
    prediction_basic_tang_features_Gradient,
    prediction_basic_tang_features_Neural,
    
    prediction_basic_vad_tang_features_LR,
    prediction_basic_vad_tang_features_KNN,
    prediction_basic_vad_tang_features_DT,
    prediction_basic_vad_tang_features_RF,
    prediction_basic_vad_tang_features_Gradient ,
    prediction_basic_vad_tang_features_Neural
    
    from users_from_setgen
    where  prediction_basic_vad_tang_features_LR is not null 
    and TYPE = 'H' '''

# Carregar dados usando consultas SQL
users_from_setGen_data = execute_query(db, sql_users_from_setGen)
 
# Converter os resultados da consulta para um DataFrame do pandas
columns = ['UserID',
    'prediction_basic_vad_features_LR',
    'prediction_basic_vad_features_KNN',
    'prediction_basic_vad_features_DT',
    'prediction_basic_vad_features_RF',
    'prediction_basic_vad_features_Gradient',
    'prediction_basic_vad_features_Neural',
    
    'prediction_basic_tang_features_LR',
    'prediction_basic_tang_features_KNN',
    'prediction_basic_tang_features_DT',
    'prediction_basic_tang_features_RF',
    'prediction_basic_tang_features_Gradient',
    'prediction_basic_tang_features_Neural',
    
    'prediction_basic_vad_tang_features_LR',
    'prediction_basic_vad_tang_features_KNN',
    'prediction_basic_vad_tang_features_DT',
    'prediction_basic_vad_tang_features_RF',
    'prediction_basic_vad_tang_features_Gradient',
    'prediction_basic_vad_tang_features_Neural']

data_df = pd.DataFrame(users_from_setGen_data, columns=columns)

# Função para definirrow['o tipo com base na contagem de 0s e 1s
def definir_tipo(row):
    if (
    row['prediction_basic_vad_features_LR'] +
    row['prediction_basic_vad_features_KNN'] +
    row['prediction_basic_vad_features_DT'] +
    row['prediction_basic_vad_features_RF'] +
    row['prediction_basic_vad_features_Gradient'] +
    row['prediction_basic_vad_features_Neural'] +
    
    row['prediction_basic_tang_features_LR'] +
    row['prediction_basic_tang_features_KNN'] +
    row['prediction_basic_tang_features_DT'] +
    row['prediction_basic_tang_features_RF'] +
    row['prediction_basic_tang_features_Gradient'] +
    row['prediction_basic_tang_features_Neural'] +
    
    row['prediction_basic_vad_tang_features_LR'] +
    row['prediction_basic_vad_tang_features_KNN'] +
    row['prediction_basic_vad_tang_features_DT'] +
    row['prediction_basic_vad_tang_features_RF'] +
    row['prediction_basic_vad_tang_features_Gradient'] +
    row['prediction_basic_vad_tang_features_Neural']
    )  >= 12:
        return 1
    else:
        return 0

# Aplicando a função para definir o tipo em cada linha e criando uma nova coluna com o resultado
data_df['type'] = data_df.apply(definir_tipo, axis=1)

# Atualizando a tabela users_from_setgen com os valores calculados
for index, row in data_df.iterrows():
    user_id = row['UserID']
    user_type = row['type']
    
    update_query = f"UPDATE users_from_setgen SET type = '{user_type}' WHERE UserId = '{user_id}'"
    execute_query(db, update_query)

# Fechar a conexão com o banco de dados
db.close()
 

