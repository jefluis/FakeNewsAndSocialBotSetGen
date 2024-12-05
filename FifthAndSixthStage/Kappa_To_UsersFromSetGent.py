# -*- coding: utf-8 -*-
"""
Created on November 11 2023

 
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2024) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire

Note this is the scoring convention for Fleiss' Kappa

< 0        Poor agreement 
0.01 - 0.20    Slight agreement
0.21 - 0.40    Fair agreement
0.41 - 0.60    Moderate agreement
0.61 - 0.80    Substantial agreement
0.81 - 1.00    Almost perfect agreement

"""
import pymysql
import pandas as pd
from sklearn.metrics import cohen_kappa_score
import numpy as np

def execute_query(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

# Conectar ao banco de dados
db = pymysql.connect(host='localhost', user='root', password='jef123*', db='ime', autocommit=True)

#===============================================================================
# # Query para buscar os dados das contas dos usuários que compartilharam notícias
# # Fake e não Fake e que irei rodar o modelo treinado com VAD e classificar as contas.
# sql_users_from_setGen = '''
#     SELECT prediction_vad, prediction_twitter_features, prediction_tang, prediction_vad_tang
#     FROM users_from_setgen 
#     WHERE prediction_vad is not null'''
#     
# 
# # Carregar dados usando consultas SQL
# users_from_setGen_data = execute_query(db, sql_users_from_setGen)
# 
# # Converter os resultados da consulta para um DataFrame do pandas
# columns = ['prediction_vad', 'prediction_twitter_features', 'prediction_tang', 'prediction_vad_tang']
# data_df = pd.DataFrame(users_from_setGen_data, columns=columns)
# 
# # Converter DataFrame para uma matriz NumPy
# data_array = data_df.to_numpy()
# 
# # Número total de avaliadores (classificadores)
# n = data_array.shape[1]
#   
# # Número total de itens (contas)
# N = data_array.shape[0]
#   
# # Número total de categorias (0 para não bot, 1 para bot)
# k = np.max(data_array) + 1
#   
# # Calcular P0 (proporção de concordância observada)
# P0 = sum(sum((1 if np.any(row == i) else 0) * (sum(1 if data == i else 0 for data in row) - 1) / (n * (n - 1)) for row in data_array) for i in range(k)) / N
#   
# # Calcular Pe (proporção de concordância esperada ao acaso)
# pj = [np.sum(data_array == i) / (N * n) for i in range(k)]
# Pe = np.sum(np.square(pj))
#   
# # Calcular Kappa de Fleiss
# kappa = (P0 - Pe) / (1 - Pe)
#   
# print("Kappa de Fleiss:", kappa)
#===============================================================================



# SEGUNDA FORMA
sql_users_from_setGen = '''
    SELECT UserId, prediction_vad, prediction_twitter_features, prediction_tang, prediction_vad_tang
    FROM users_from_setgen 
    WHERE prediction_vad is not null'''   
 
# Carregar dados usando consultas SQL
users_from_setGen_data = execute_query(db, sql_users_from_setGen)
 
# Criar dicionários para armazenar contagens
count_results_0 = {}
count_results_1 = {}
 
# Iterar sobre os resultados
for row in users_from_setGen_data:
    user_id = row[0]
    predictions = row[1:]
 
    # Inicializar contagem para o usuário se ainda não existir
    if user_id not in count_results_0:
        count_results_0[user_id] = 0
    if user_id not in count_results_1:
        count_results_1[user_id] = 0
 
    # Contar resultados 0 e 1 para cada predição
    count_results_0[user_id] += predictions.count(0)
    count_results_1[user_id] += predictions.count(1)
 
# Fechar a conexão com o banco de dados
db.close()
 
# Exibir os resultados
for user_id in count_results_0:
    print(f"User ID: {user_id}, Count Result 0: {count_results_0[user_id]}, Count Result 1: {count_results_1[user_id]}")

# Criar listas de predições para cada categoria
predictions_0 = [count_results_0.get(user_id, 0) for user_id in count_results_0]
predictions_1 = [count_results_1.get(user_id, 0) for user_id in count_results_1]

# Criar uma matriz de predições
predictions_matrix = np.column_stack((predictions_0, predictions_1))

# Criar rótulos reais e previstos para cada observação
y_true = np.zeros(predictions_matrix.shape[0], dtype=int)  # Cria um array de zeros para os rótulos reais
y_pred = np.argmax(predictions_matrix, axis=1)  # Escolhe o índice da maior predição como rótulo previsto

# Calcular Kappa de Fleiss
kappa_fleiss = cohen_kappa_score(y_true, y_pred, weights='linear')

print(f"Kappa de Fleiss: {kappa_fleiss}")


# Calcular a matriz de confusão
conf_matrix = confusion_matrix(y_true, y_pred)

# Visualizar a matriz de confusão
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['0', '1'], yticklabels=['0', '1'])
plt.xlabel('Rótulos Previstos')
plt.ylabel('Rótulos Reais')
plt.title('Matriz de Confusão')
plt.show()

#===============================================================================
# #Forma do Christian 
# 
# # Número total de avaliadores (classificadores)
# num_cols = data_array.shape[1]
#  
# # Número total de itens (contas)
# num_rows = data_array.shape[0]
#  
# n = 0
# k = num_cols
# C = 0
# N = 0
#  
# for i in range(num_rows):
#     for j in range(num_cols):
#         n += 1
#         N += data_array[i][j]
#         C += data_array[i][j] * (data_array[i][j] - 1)
#  
# mean_n = N / n
# var_n = (C - n * mean_n * (mean_n - 1)) / (n - 1)
#  
# kappa = (mean_n * (k - 1) - var_n) / (mean_n * (k - 1))
#  
# print(f'Fleiss kappa: {kappa:.3f}')
#===============================================================================

# Fechar a conexão com o banco de dados
#db.close()

