# -*- coding: utf-8 -*-
"""
Created on Auguts 19 2024

 
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2024) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire
"""

import pymysql
import pandas as pd
import datetime as dt

import joblib

# Função para converter datetime para timestamp
def convert_datetime_to_timestamp(date_time):
    timestamp = dt.datetime.timestamp(date_time)
    return timestamp

# Conectar ao banco de dados
db = pymysql.connect(host='localhost', user='root', password='jef123*', db='ime', autocommit=True)
cursor = db.cursor()

# Carregar os modelos treinados
#clf_vad_features = joblib.load('modelo_randomforest_original_features.pkl')
#clf_reduced_features = joblib.load('modelo_randomforest_reduced_features.pkl')
#clf_tang_features = joblib.load('modelo_randomforest_expanded_features.pkl')
#clf_vad_tang_features = joblib.load('modelo_randomforest_VAD_Tang_features.pkl')

#Basic Features
clf_basic_features_LR= joblib.load('Logistic Regression_best_model.pkl')
clf_basic_features_KNN= joblib.load('K-Nearest Neighbors_best_model.pkl')
clf_basic_features_DT= joblib.load('Decision Tree_best_model.pkl')
clf_basic_features_RF= joblib.load('Random Forest_best_model.pkl')
clf_basic_features_Gradient= joblib.load('Gradient Boosting_best_model.pkl')
clf_basic_features_Neural= joblib.load('Neural Network_best_model.pkl')

#Basic Features + VAD
clf_basic_vad_features_LR= joblib.load('Logistic Regression_best_model_basic_vad.pkl')
clf_basic_vad_features_KNN= joblib.load('K-Nearest Neighbors_best_model_basic_vad.pkl')
clf_basic_vad_features_DT= joblib.load('Decision Tree_best_model_basic_vad.pkl')
clf_basic_vad_features_RF= joblib.load('Random Forest_best_model_basic_vad.pkl')
clf_basic_vad_features_Gradient= joblib.load('Gradient Boosting_best_model_basic_vad.pkl')
clf_basic_vad_features_Neural= joblib.load('Neural Network_best_model_basic_vad.pkl')

#Basic Features + Tang
clf_basic_tang_features_LR= joblib.load('Logistic Regression_best_model_basic_tang.pkl')
clf_basic_tang_features_KNN= joblib.load('K-Nearest Neighbors_best_model_basic_tang.pkl')
clf_basic_tang_features_DT= joblib.load('Decision Tree_best_model_basic_tang.pkl')
clf_basic_tang_features_RF= joblib.load('Random Forest_best_model_basic_tang.pkl')
clf_basic_tang_features_Gradient= joblib.load('Gradient Boosting_best_model_basic_tang.pkl')
clf_basic_tang_features_Neural= joblib.load('Neural Network_best_model_basic_tang.pkl')

#Basic Features + VAD + Tang
clf_basic_vad_tang_features_LR= joblib.load('Logistic Regression_best_model_basic_vad_tang.pkl')
clf_basic_vad_tang_features_KNN= joblib.load('K-Nearest Neighbors_best_model_basic_vad_tang.pkl')
clf_basic_vad_tang_features_DT= joblib.load('Decision Tree_best_model_basic_vad_tang.pkl')
clf_basic_vad_tang_features_RF= joblib.load('Random Forest_best_model_basic_vad_tang.pkl')
clf_basic_vad_tang_features_Gradient= joblib.load('Gradient Boosting_best_model_basic_vad_tang.pkl')
clf_basic_vad_tang_features_Neural= joblib.load('Neural Network_best_model_basic_vad_tang.pkl')

# *** PASSAR A BASE DO USERS_FROM_SETGEN NOS MODELOS TREINADOS ***
# Query para buscar os dados das contas dos usuários que compartilharam notícias
# Fake e não Fake e que irei rodar o modelo treinado com VAD, Tang e somente dados básicos do twitter
# e classificar as contas.
sql_users_from_setGen = '''
    SELECT u.UserID, CreatedAt, NumberOfFollowings, NumberOfFollowers, NumberOfTweets, 
            LengthOfScreenName, LenDescrInUseProf as LenDescrInUseProfile, type, 
            V_media, A_media, D_media, 
            V_1quartil ,  A_1quartil ,  D_1quartil , 
            V_mediana ,  A_mediana ,  D_mediana , 
            V_3quartil ,  A_3quartil ,  D_3quartil , 
            V_desviopadrao ,  A_desviopadrao ,  D_desviopadrao , 
            V_amplitude ,  A_amplitude ,  D_amplitude,
            d1_media, d2_media, d3_media, d4_media, d5_media, d6_media, d7_media, d8_media, d9_media, d10_media, d11_media, d12_media, d13_media, d14_media, d15_media, d16_media, d17_media, d18_media, d19_media, d20_media, d21_media, d22_media, d23_media, d24_media, d25_media, d26_media, d27_media, d28_media, d29_media, d30_media, d31_media, d32_media, d33_media, d34_media, d35_media, d36_media, d37_media, d38_media, d39_media, d40_media, d41_media, d42_media, d43_media, d44_media, d45_media, d46_media, d47_media, d48_media, d49_media, d50_media, 
            d1_1quartil, d2_1quartil, d3_1quartil, d4_1quartil, d5_1quartil, d6_1quartil, d7_1quartil, d8_1quartil, d9_1quartil, d10_1quartil, d11_1quartil, d12_1quartil, d13_1quartil, d14_1quartil, d15_1quartil, d16_1quartil, d17_1quartil, d18_1quartil, d19_1quartil, d20_1quartil, d21_1quartil, d22_1quartil, d23_1quartil, d24_1quartil, d25_1quartil, d26_1quartil, d27_1quartil, d28_1quartil, d29_1quartil, d30_1quartil, d31_1quartil, d32_1quartil, d33_1quartil, d34_1quartil, d35_1quartil, d36_1quartil, d37_1quartil, d38_1quartil, d39_1quartil, d40_1quartil, d41_1quartil, d42_1quartil, d43_1quartil, d44_1quartil, d45_1quartil, d46_1quartil, d47_1quartil, d48_1quartil, d49_1quartil, d50_1quartil, 
            d1_mediana, d2_mediana, d3_mediana, d4_mediana, d5_mediana, d6_mediana, d7_mediana, d8_mediana, d9_mediana, d10_mediana, d11_mediana, d12_mediana, d13_mediana, d14_mediana, d15_mediana, d16_mediana, d17_mediana, d18_mediana, d19_mediana, d20_mediana, d21_mediana, d22_mediana, d23_mediana, d24_mediana, d25_mediana, d26_mediana, d27_mediana, d28_mediana, d29_mediana, d30_mediana, d31_mediana, d32_mediana, d33_mediana, d34_mediana, d35_mediana, d36_mediana, d37_mediana, d38_mediana, d39_mediana, d40_mediana, d41_mediana, d42_mediana, d43_mediana, d44_mediana, d45_mediana, d46_mediana, d47_mediana, d48_mediana, d49_mediana, d50_mediana, 
            d1_3quartil, d2_3quartil, d3_3quartil, d4_3quartil, d5_3quartil, d6_3quartil, d7_3quartil, d8_3quartil, d9_3quartil, d10_3quartil, d11_3quartil, d12_3quartil, d13_3quartil, d14_3quartil, d15_3quartil, d16_3quartil, d17_3quartil, d18_3quartil, d19_3quartil, d20_3quartil, d21_3quartil, d22_3quartil, d23_3quartil, d24_3quartil, d25_3quartil, d26_3quartil, d27_3quartil, d28_3quartil, d29_3quartil, d30_3quartil, d31_3quartil, d32_3quartil, d33_3quartil, d34_3quartil, d35_3quartil, d36_3quartil, d37_3quartil, d38_3quartil, d39_3quartil, d40_3quartil, d41_3quartil, d42_3quartil, d43_3quartil, d44_3quartil, d45_3quartil, d46_3quartil, d47_3quartil, d48_3quartil, d49_3quartil, d50_3quartil, 
            d1_desviopadrao, d2_desviopadrao, d3_desviopadrao, d4_desviopadrao, d5_desviopadrao, d6_desviopadrao, d7_desviopadrao, d8_desviopadrao, d9_desviopadrao, d10_desviopadrao, d11_desviopadrao, d12_desviopadrao, d13_desviopadrao, d14_desviopadrao, d15_desviopadrao, d16_desviopadrao, d17_desviopadrao, d18_desviopadrao, d19_desviopadrao, d20_desviopadrao, d21_desviopadrao, d22_desviopadrao, d23_desviopadrao, d24_desviopadrao, d25_desviopadrao, d26_desviopadrao, d27_desviopadrao, d28_desviopadrao, d29_desviopadrao, d30_desviopadrao, d31_desviopadrao, d32_desviopadrao, d33_desviopadrao, d34_desviopadrao, d35_desviopadrao, d36_desviopadrao, d37_desviopadrao, d38_desviopadrao, d39_desviopadrao, d40_desviopadrao, d41_desviopadrao, d42_desviopadrao, d43_desviopadrao, d44_desviopadrao, d45_desviopadrao, d46_desviopadrao, d47_desviopadrao, d48_desviopadrao, d49_desviopadrao, d50_desviopadrao, 
            d1_amplitude, d2_amplitude, d3_amplitude, d4_amplitude, d5_amplitude, d6_amplitude, d7_amplitude, d8_amplitude, d9_amplitude, d10_amplitude, d11_amplitude, d12_amplitude, d13_amplitude, d14_amplitude, d15_amplitude, d16_amplitude, d17_amplitude, d18_amplitude, d19_amplitude, d20_amplitude, d21_amplitude, d22_amplitude, d23_amplitude, d24_amplitude, d25_amplitude, d26_amplitude, d27_amplitude, d28_amplitude, d29_amplitude, d30_amplitude, d31_amplitude, d32_amplitude, d33_amplitude, d34_amplitude, d35_amplitude, d36_amplitude, d37_amplitude, d38_amplitude, d39_amplitude, d40_amplitude, d41_amplitude, d42_amplitude, d43_amplitude, d44_amplitude, d45_amplitude, d46_amplitude, d47_amplitude, d48_amplitude, d49_amplitude, d50_amplitude 
    FROM users_from_setgen AS u
    INNER JOIN (
        SELECT userid, COUNT(tweetid) AS Mensagens
        FROM TweetsOfLabeledNews
        GROUP BY UserId
        HAVING Mensagens > 5
    ) AS T2
    WHERE T2.userid = u.userid AND u.v_media > 0 AND TYPE = 'H' '''

# Carregar dados usando consultas SQL
cursor.execute(sql_users_from_setGen)
users_from_setGen_data = cursor.fetchall()

# Criar listas para armazenar os dados dos usuários a serem classificados    
users_from_setGen_list = []
# Iterar sobre os dados e fazer as predições
for tupla in users_from_setGen_data:
    posix_dates_users = (tupla[0], convert_datetime_to_timestamp(tupla[1])) + tupla[2:]
    users_from_setGen_list.append(posix_dates_users)
  
 
full_feature_names = ['CreatedAt', 'NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 
                 'LengthOfScreenName', 'LenDescrInUseProfile', 'Type',
                 'V_media', 'A_media', 'D_media', 
                 'V_1quartil', 'A_1quartil', 'D_1quartil', 
                 'V_mediana', 'A_mediana', 'D_mediana', 
                 'V_3quartil', 'A_3quartil', 'D_3quartil', 
                 'V_desviopadrao', 'A_desviopadrao', 'D_desviopadrao', 
                 'V_amplitude', 'A_amplitude', 'D_amplitude',
                 'd1_media', 'd2_media', 'd3_media', 'd4_media', 'd5_media', 'd6_media', 'd7_media', 'd8_media', 'd9_media','d10_media', 'd11_media', 'd12_media', 'd13_media', 'd14_media', 'd15_media', 'd16_media', 'd17_media', 'd18_media', 'd19_media', 'd20_media', 'd21_media', 'd22_media', 'd23_media', 'd24_media', 'd25_media', 'd26_media', 'd27_media', 'd28_media', 'd29_media', 'd30_media', 'd31_media', 'd32_media', 'd33_media', 'd34_media', 'd35_media', 'd36_media', 'd37_media', 'd38_media', 'd39_media', 'd40_media', 'd41_media', 'd42_media', 'd43_media', 'd44_media', 'd45_media', 'd46_media', 'd47_media', 'd48_media', 'd49_media', 'd50_media', 
                 'd1_1quartil', 'd2_1quartil', 'd3_1quartil', 'd4_1quartil', 'd5_1quartil', 'd6_1quartil', 'd7_1quartil', 'd8_1quartil', 'd9_1quartil', 'd10_1quartil', 'd11_1quartil', 'd12_1quartil', 'd13_1quartil', 'd14_1quartil', 'd15_1quartil', 'd16_1quartil', 'd17_1quartil', 'd18_1quartil', 'd19_1quartil', 'd20_1quartil', 'd21_1quartil', 'd22_1quartil', 'd23_1quartil', 'd24_1quartil', 'd25_1quartil', 'd26_1quartil', 'd27_1quartil', 'd28_1quartil', 'd29_1quartil', 'd30_1quartil', 'd31_1quartil', 'd32_1quartil', 'd33_1quartil', 'd34_1quartil', 'd35_1quartil', 'd36_1quartil', 'd37_1quartil', 'd38_1quartil', 'd39_1quartil', 'd40_1quartil', 'd41_1quartil', 'd42_1quartil', 'd43_1quartil', 'd44_1quartil', 'd45_1quartil', 'd46_1quartil', 'd47_1quartil', 'd48_1quartil', 'd49_1quartil', 'd50_1quartil', 
                 'd1_mediana', 'd2_mediana', 'd3_mediana', 'd4_mediana', 'd5_mediana', 'd6_mediana', 'd7_mediana', 'd8_mediana', 'd9_mediana', 'd10_mediana', 'd11_mediana', 'd12_mediana', 'd13_mediana', 'd14_mediana', 'd15_mediana', 'd16_mediana', 'd17_mediana', 'd18_mediana', 'd19_mediana', 'd20_mediana', 'd21_mediana', 'd22_mediana', 'd23_mediana', 'd24_mediana', 'd25_mediana', 'd26_mediana', 'd27_mediana', 'd28_mediana', 'd29_mediana', 'd30_mediana', 'd31_mediana', 'd32_mediana', 'd33_mediana', 'd34_mediana', 'd35_mediana', 'd36_mediana', 'd37_mediana', 'd38_mediana', 'd39_mediana', 'd40_mediana', 'd41_mediana', 'd42_mediana', 'd43_mediana', 'd44_mediana', 'd45_mediana', 'd46_mediana', 'd47_mediana', 'd48_mediana', 'd49_mediana', 'd50_mediana', 
                 'd1_3quartil', 'd2_3quartil', 'd3_3quartil', 'd4_3quartil', 'd5_3quartil', 'd6_3quartil', 'd7_3quartil', 'd8_3quartil', 'd9_3quartil', 'd10_3quartil', 'd11_3quartil', 'd12_3quartil', 'd13_3quartil', 'd14_3quartil', 'd15_3quartil', 'd16_3quartil', 'd17_3quartil', 'd18_3quartil', 'd19_3quartil', 'd20_3quartil', 'd21_3quartil', 'd22_3quartil', 'd23_3quartil', 'd24_3quartil', 'd25_3quartil', 'd26_3quartil', 'd27_3quartil', 'd28_3quartil', 'd29_3quartil', 'd30_3quartil', 'd31_3quartil', 'd32_3quartil', 'd33_3quartil', 'd34_3quartil', 'd35_3quartil', 'd36_3quartil', 'd37_3quartil', 'd38_3quartil', 'd39_3quartil', 'd40_3quartil', 'd41_3quartil', 'd42_3quartil', 'd43_3quartil', 'd44_3quartil', 'd45_3quartil', 'd46_3quartil', 'd47_3quartil', 'd48_3quartil', 'd49_3quartil', 'd50_3quartil', 
                 'd1_desviopadrao', 'd2_desviopadrao', 'd3_desviopadrao', 'd4_desviopadrao', 'd5_desviopadrao', 'd6_desviopadrao', 'd7_desviopadrao', 'd8_desviopadrao', 'd9_desviopadrao', 'd10_desviopadrao', 'd11_desviopadrao', 'd12_desviopadrao', 'd13_desviopadrao', 'd14_desviopadrao', 'd15_desviopadrao', 'd16_desviopadrao', 'd17_desviopadrao', 'd18_desviopadrao', 'd19_desviopadrao', 'd20_desviopadrao', 'd21_desviopadrao', 'd22_desviopadrao', 'd23_desviopadrao', 'd24_desviopadrao', 'd25_desviopadrao', 'd26_desviopadrao', 'd27_desviopadrao', 'd28_desviopadrao', 'd29_desviopadrao', 'd30_desviopadrao', 'd31_desviopadrao', 'd32_desviopadrao', 'd33_desviopadrao', 'd34_desviopadrao', 'd35_desviopadrao', 'd36_desviopadrao', 'd37_desviopadrao', 'd38_desviopadrao', 'd39_desviopadrao', 'd40_desviopadrao', 'd41_desviopadrao', 'd42_desviopadrao', 'd43_desviopadrao', 'd44_desviopadrao', 'd45_desviopadrao', 'd46_desviopadrao', 'd47_desviopadrao', 'd48_desviopadrao', 'd49_desviopadrao', 'd50_desviopadrao', 
                 'd1_amplitude', 'd2_amplitude', 'd3_amplitude', 'd4_amplitude', 'd5_amplitude', 'd6_amplitude', 'd7_amplitude', 'd8_amplitude', 'd9_amplitude', 'd10_amplitude', 'd11_amplitude', 'd12_amplitude', 'd13_amplitude', 'd14_amplitude', 'd15_amplitude', 'd16_amplitude', 'd17_amplitude', 'd18_amplitude', 'd19_amplitude', 'd20_amplitude', 'd21_amplitude', 'd22_amplitude', 'd23_amplitude', 'd24_amplitude', 'd25_amplitude', 'd26_amplitude', 'd27_amplitude', 'd28_amplitude', 'd29_amplitude', 'd30_amplitude', 'd31_amplitude', 'd32_amplitude', 'd33_amplitude', 'd34_amplitude', 'd35_amplitude', 'd36_amplitude', 'd37_amplitude', 'd38_amplitude', 'd39_amplitude', 'd40_amplitude', 'd41_amplitude', 'd42_amplitude', 'd43_amplitude', 'd44_amplitude', 'd45_amplitude', 'd46_amplitude', 'd47_amplitude', 'd48_amplitude', 'd49_amplitude', 'd50_amplitude' 
                 ]

 
# Converter a lista de dados para um DataFrame do pandas
data_users_from_setGen_df = pd.DataFrame(users_from_setGen_list, columns=['UserID'] + full_feature_names)
    

#### RODAR MODELO com features básicas de dados da conta do Twitter ####
selected_features = ['CreatedAt', 'NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 
                     'LengthOfScreenName', 'LenDescrInUseProfile']
  
#### RODAR MODELO com features VAD e suas estatísticas ####
feature_names_vad = ['CreatedAt', 'NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 
                 'LengthOfScreenName', 'LenDescrInUseProfile', 
                 'V_media', 'A_media', 'D_media', 
                 'V_1quartil', 'A_1quartil', 'D_1quartil', 
                 'V_mediana', 'A_mediana', 'D_mediana', 
                 'V_3quartil', 'A_3quartil', 'D_3quartil', 
                 'V_desviopadrao', 'A_desviopadrao', 'D_desviopadrao', 
                 'V_amplitude', 'A_amplitude', 'D_amplitude']


#### RODAR MODELO com features do Tang e suas estatísticas ####
Tang_Features = ['CreatedAt', 'NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 
                     'LengthOfScreenName', 'LenDescrInUseProfile', 
                     'd1_media', 'd2_media', 'd3_media', 'd4_media', 'd5_media', 'd6_media', 'd7_media', 'd8_media', 'd9_media','d10_media', 'd11_media', 'd12_media', 'd13_media', 'd14_media', 'd15_media', 'd16_media', 'd17_media', 'd18_media', 'd19_media', 'd20_media', 'd21_media', 'd22_media', 'd23_media', 'd24_media', 'd25_media', 'd26_media', 'd27_media', 'd28_media', 'd29_media', 'd30_media', 'd31_media', 'd32_media', 'd33_media', 'd34_media', 'd35_media', 'd36_media', 'd37_media', 'd38_media', 'd39_media', 'd40_media', 'd41_media', 'd42_media', 'd43_media', 'd44_media', 'd45_media', 'd46_media', 'd47_media', 'd48_media', 'd49_media', 'd50_media', 
                     'd1_1quartil', 'd2_1quartil', 'd3_1quartil', 'd4_1quartil', 'd5_1quartil', 'd6_1quartil', 'd7_1quartil', 'd8_1quartil', 'd9_1quartil', 'd10_1quartil', 'd11_1quartil', 'd12_1quartil', 'd13_1quartil', 'd14_1quartil', 'd15_1quartil', 'd16_1quartil', 'd17_1quartil', 'd18_1quartil', 'd19_1quartil', 'd20_1quartil', 'd21_1quartil', 'd22_1quartil', 'd23_1quartil', 'd24_1quartil', 'd25_1quartil', 'd26_1quartil', 'd27_1quartil', 'd28_1quartil', 'd29_1quartil', 'd30_1quartil', 'd31_1quartil', 'd32_1quartil', 'd33_1quartil', 'd34_1quartil', 'd35_1quartil', 'd36_1quartil', 'd37_1quartil', 'd38_1quartil', 'd39_1quartil', 'd40_1quartil', 'd41_1quartil', 'd42_1quartil', 'd43_1quartil', 'd44_1quartil', 'd45_1quartil', 'd46_1quartil', 'd47_1quartil', 'd48_1quartil', 'd49_1quartil', 'd50_1quartil', 
                     'd1_mediana', 'd2_mediana', 'd3_mediana', 'd4_mediana', 'd5_mediana', 'd6_mediana', 'd7_mediana', 'd8_mediana', 'd9_mediana', 'd10_mediana', 'd11_mediana', 'd12_mediana', 'd13_mediana', 'd14_mediana', 'd15_mediana', 'd16_mediana', 'd17_mediana', 'd18_mediana', 'd19_mediana', 'd20_mediana', 'd21_mediana', 'd22_mediana', 'd23_mediana', 'd24_mediana', 'd25_mediana', 'd26_mediana', 'd27_mediana', 'd28_mediana', 'd29_mediana', 'd30_mediana', 'd31_mediana', 'd32_mediana', 'd33_mediana', 'd34_mediana', 'd35_mediana', 'd36_mediana', 'd37_mediana', 'd38_mediana', 'd39_mediana', 'd40_mediana', 'd41_mediana', 'd42_mediana', 'd43_mediana', 'd44_mediana', 'd45_mediana', 'd46_mediana', 'd47_mediana', 'd48_mediana', 'd49_mediana', 'd50_mediana', 
                     'd1_3quartil', 'd2_3quartil', 'd3_3quartil', 'd4_3quartil', 'd5_3quartil', 'd6_3quartil', 'd7_3quartil', 'd8_3quartil', 'd9_3quartil', 'd10_3quartil', 'd11_3quartil', 'd12_3quartil', 'd13_3quartil', 'd14_3quartil', 'd15_3quartil', 'd16_3quartil', 'd17_3quartil', 'd18_3quartil', 'd19_3quartil', 'd20_3quartil', 'd21_3quartil', 'd22_3quartil', 'd23_3quartil', 'd24_3quartil', 'd25_3quartil', 'd26_3quartil', 'd27_3quartil', 'd28_3quartil', 'd29_3quartil', 'd30_3quartil', 'd31_3quartil', 'd32_3quartil', 'd33_3quartil', 'd34_3quartil', 'd35_3quartil', 'd36_3quartil', 'd37_3quartil', 'd38_3quartil', 'd39_3quartil', 'd40_3quartil', 'd41_3quartil', 'd42_3quartil', 'd43_3quartil', 'd44_3quartil', 'd45_3quartil', 'd46_3quartil', 'd47_3quartil', 'd48_3quartil', 'd49_3quartil', 'd50_3quartil', 
                     'd1_desviopadrao', 'd2_desviopadrao', 'd3_desviopadrao', 'd4_desviopadrao', 'd5_desviopadrao', 'd6_desviopadrao', 'd7_desviopadrao', 'd8_desviopadrao', 'd9_desviopadrao', 'd10_desviopadrao', 'd11_desviopadrao', 'd12_desviopadrao', 'd13_desviopadrao', 'd14_desviopadrao', 'd15_desviopadrao', 'd16_desviopadrao', 'd17_desviopadrao', 'd18_desviopadrao', 'd19_desviopadrao', 'd20_desviopadrao', 'd21_desviopadrao', 'd22_desviopadrao', 'd23_desviopadrao', 'd24_desviopadrao', 'd25_desviopadrao', 'd26_desviopadrao', 'd27_desviopadrao', 'd28_desviopadrao', 'd29_desviopadrao', 'd30_desviopadrao', 'd31_desviopadrao', 'd32_desviopadrao', 'd33_desviopadrao', 'd34_desviopadrao', 'd35_desviopadrao', 'd36_desviopadrao', 'd37_desviopadrao', 'd38_desviopadrao', 'd39_desviopadrao', 'd40_desviopadrao', 'd41_desviopadrao', 'd42_desviopadrao', 'd43_desviopadrao', 'd44_desviopadrao', 'd45_desviopadrao', 'd46_desviopadrao', 'd47_desviopadrao', 'd48_desviopadrao', 'd49_desviopadrao', 'd50_desviopadrao', 
                     'd1_amplitude', 'd2_amplitude', 'd3_amplitude', 'd4_amplitude', 'd5_amplitude', 'd6_amplitude', 'd7_amplitude', 'd8_amplitude', 'd9_amplitude', 'd10_amplitude', 'd11_amplitude', 'd12_amplitude', 'd13_amplitude', 'd14_amplitude', 'd15_amplitude', 'd16_amplitude', 'd17_amplitude', 'd18_amplitude', 'd19_amplitude', 'd20_amplitude', 'd21_amplitude', 'd22_amplitude', 'd23_amplitude', 'd24_amplitude', 'd25_amplitude', 'd26_amplitude', 'd27_amplitude', 'd28_amplitude', 'd29_amplitude', 'd30_amplitude', 'd31_amplitude', 'd32_amplitude', 'd33_amplitude', 'd34_amplitude', 'd35_amplitude', 'd36_amplitude', 'd37_amplitude', 'd38_amplitude', 'd39_amplitude', 'd40_amplitude', 'd41_amplitude', 'd42_amplitude', 'd43_amplitude', 'd44_amplitude', 'd45_amplitude', 'd46_amplitude', 'd47_amplitude', 'd48_amplitude', 'd49_amplitude', 'd50_amplitude']  # Features

#### RODAR MODELO com features do Vad_Tang e suas estatísticas ####
VAD_Tang_Features = ['CreatedAt', 'NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 
                     'LengthOfScreenName', 'LenDescrInUseProfile', 
                     'V_media', 'A_media', 'D_media', 
                     'V_1quartil', 'A_1quartil', 'D_1quartil', 
                     'V_mediana', 'A_mediana', 'D_mediana', 
                     'V_3quartil', 'A_3quartil', 'D_3quartil', 
                     'V_desviopadrao', 'A_desviopadrao', 'D_desviopadrao', 
                     'V_amplitude', 'A_amplitude', 'D_amplitude',                     
                     'd1_media', 'd2_media', 'd3_media', 'd4_media', 'd5_media', 'd6_media', 'd7_media', 'd8_media', 'd9_media','d10_media', 'd11_media', 'd12_media', 'd13_media', 'd14_media', 'd15_media', 'd16_media', 'd17_media', 'd18_media', 'd19_media', 'd20_media', 'd21_media', 'd22_media', 'd23_media', 'd24_media', 'd25_media', 'd26_media', 'd27_media', 'd28_media', 'd29_media', 'd30_media', 'd31_media', 'd32_media', 'd33_media', 'd34_media', 'd35_media', 'd36_media', 'd37_media', 'd38_media', 'd39_media', 'd40_media', 'd41_media', 'd42_media', 'd43_media', 'd44_media', 'd45_media', 'd46_media', 'd47_media', 'd48_media', 'd49_media', 'd50_media', 
                     'd1_1quartil', 'd2_1quartil', 'd3_1quartil', 'd4_1quartil', 'd5_1quartil', 'd6_1quartil', 'd7_1quartil', 'd8_1quartil', 'd9_1quartil', 'd10_1quartil', 'd11_1quartil', 'd12_1quartil', 'd13_1quartil', 'd14_1quartil', 'd15_1quartil', 'd16_1quartil', 'd17_1quartil', 'd18_1quartil', 'd19_1quartil', 'd20_1quartil', 'd21_1quartil', 'd22_1quartil', 'd23_1quartil', 'd24_1quartil', 'd25_1quartil', 'd26_1quartil', 'd27_1quartil', 'd28_1quartil', 'd29_1quartil', 'd30_1quartil', 'd31_1quartil', 'd32_1quartil', 'd33_1quartil', 'd34_1quartil', 'd35_1quartil', 'd36_1quartil', 'd37_1quartil', 'd38_1quartil', 'd39_1quartil', 'd40_1quartil', 'd41_1quartil', 'd42_1quartil', 'd43_1quartil', 'd44_1quartil', 'd45_1quartil', 'd46_1quartil', 'd47_1quartil', 'd48_1quartil', 'd49_1quartil', 'd50_1quartil', 
                     'd1_mediana', 'd2_mediana', 'd3_mediana', 'd4_mediana', 'd5_mediana', 'd6_mediana', 'd7_mediana', 'd8_mediana', 'd9_mediana', 'd10_mediana', 'd11_mediana', 'd12_mediana', 'd13_mediana', 'd14_mediana', 'd15_mediana', 'd16_mediana', 'd17_mediana', 'd18_mediana', 'd19_mediana', 'd20_mediana', 'd21_mediana', 'd22_mediana', 'd23_mediana', 'd24_mediana', 'd25_mediana', 'd26_mediana', 'd27_mediana', 'd28_mediana', 'd29_mediana', 'd30_mediana', 'd31_mediana', 'd32_mediana', 'd33_mediana', 'd34_mediana', 'd35_mediana', 'd36_mediana', 'd37_mediana', 'd38_mediana', 'd39_mediana', 'd40_mediana', 'd41_mediana', 'd42_mediana', 'd43_mediana', 'd44_mediana', 'd45_mediana', 'd46_mediana', 'd47_mediana', 'd48_mediana', 'd49_mediana', 'd50_mediana', 
                     'd1_3quartil', 'd2_3quartil', 'd3_3quartil', 'd4_3quartil', 'd5_3quartil', 'd6_3quartil', 'd7_3quartil', 'd8_3quartil', 'd9_3quartil', 'd10_3quartil', 'd11_3quartil', 'd12_3quartil', 'd13_3quartil', 'd14_3quartil', 'd15_3quartil', 'd16_3quartil', 'd17_3quartil', 'd18_3quartil', 'd19_3quartil', 'd20_3quartil', 'd21_3quartil', 'd22_3quartil', 'd23_3quartil', 'd24_3quartil', 'd25_3quartil', 'd26_3quartil', 'd27_3quartil', 'd28_3quartil', 'd29_3quartil', 'd30_3quartil', 'd31_3quartil', 'd32_3quartil', 'd33_3quartil', 'd34_3quartil', 'd35_3quartil', 'd36_3quartil', 'd37_3quartil', 'd38_3quartil', 'd39_3quartil', 'd40_3quartil', 'd41_3quartil', 'd42_3quartil', 'd43_3quartil', 'd44_3quartil', 'd45_3quartil', 'd46_3quartil', 'd47_3quartil', 'd48_3quartil', 'd49_3quartil', 'd50_3quartil', 
                     'd1_desviopadrao', 'd2_desviopadrao', 'd3_desviopadrao', 'd4_desviopadrao', 'd5_desviopadrao', 'd6_desviopadrao', 'd7_desviopadrao', 'd8_desviopadrao', 'd9_desviopadrao', 'd10_desviopadrao', 'd11_desviopadrao', 'd12_desviopadrao', 'd13_desviopadrao', 'd14_desviopadrao', 'd15_desviopadrao', 'd16_desviopadrao', 'd17_desviopadrao', 'd18_desviopadrao', 'd19_desviopadrao', 'd20_desviopadrao', 'd21_desviopadrao', 'd22_desviopadrao', 'd23_desviopadrao', 'd24_desviopadrao', 'd25_desviopadrao', 'd26_desviopadrao', 'd27_desviopadrao', 'd28_desviopadrao', 'd29_desviopadrao', 'd30_desviopadrao', 'd31_desviopadrao', 'd32_desviopadrao', 'd33_desviopadrao', 'd34_desviopadrao', 'd35_desviopadrao', 'd36_desviopadrao', 'd37_desviopadrao', 'd38_desviopadrao', 'd39_desviopadrao', 'd40_desviopadrao', 'd41_desviopadrao', 'd42_desviopadrao', 'd43_desviopadrao', 'd44_desviopadrao', 'd45_desviopadrao', 'd46_desviopadrao', 'd47_desviopadrao', 'd48_desviopadrao', 'd49_desviopadrao', 'd50_desviopadrao', 
                     'd1_amplitude', 'd2_amplitude', 'd3_amplitude', 'd4_amplitude', 'd5_amplitude', 'd6_amplitude', 'd7_amplitude', 'd8_amplitude', 'd9_amplitude', 'd10_amplitude', 'd11_amplitude', 'd12_amplitude', 'd13_amplitude', 'd14_amplitude', 'd15_amplitude', 'd16_amplitude', 'd17_amplitude', 'd18_amplitude', 'd19_amplitude', 'd20_amplitude', 'd21_amplitude', 'd22_amplitude', 'd23_amplitude', 'd24_amplitude', 'd25_amplitude', 'd26_amplitude', 'd27_amplitude', 'd28_amplitude', 'd29_amplitude', 'd30_amplitude', 'd31_amplitude', 'd32_amplitude', 'd33_amplitude', 'd34_amplitude', 'd35_amplitude', 'd36_amplitude', 'd37_amplitude', 'd38_amplitude', 'd39_amplitude', 'd40_amplitude', 'd41_amplitude', 'd42_amplitude', 'd43_amplitude', 'd44_amplitude', 'd45_amplitude', 'd46_amplitude', 'd47_amplitude', 'd48_amplitude', 'd49_amplitude', 'd50_amplitude']  # Features

# Fazer as predições com os modelos para todos os exemplos de entrada
#prediction_reduced_features = clf_reduced_features.predict(data_users_from_setGen_df[selected_features])
#prediction_original_features = clf_vad_features.predict(data_users_from_setGen_df[feature_names_vad])
#prediction_expanded_features = clf_tang_features.predict(data_users_from_setGen_df[Tang_Features])
#prediction_vad_tang_features = clf_vad_tang_features.predict(data_users_from_setGen_df[VAD_Tang_Features])

#Fazer as predições com os modelos para todos os exemplos de entrada - (Basic Features)
prediction_basic_features_LR = clf_basic_features_LR.predict(data_users_from_setGen_df[selected_features])
prediction_basic_features_KNN =clf_basic_features_KNN.predict(data_users_from_setGen_df[selected_features])
prediction_basic_features_DT = clf_basic_features_DT.predict(data_users_from_setGen_df[selected_features])
prediction_basic_features_RF = clf_basic_features_RF.predict(data_users_from_setGen_df[selected_features])
prediction_basic_features_Gradient =clf_basic_features_Gradient.predict(data_users_from_setGen_df[selected_features])
prediction_basic_features_Neural =clf_basic_features_Neural.predict(data_users_from_setGen_df[selected_features])

#Fazer as predições com os modelos para todos os exemplos de entrada - (Basic Features + VAD)
prediction_basic_vad_features_LR = clf_basic_vad_features_LR.predict(data_users_from_setGen_df[feature_names_vad])
prediction_basic_vad_features_KNN = clf_basic_vad_features_KNN.predict(data_users_from_setGen_df[feature_names_vad])
prediction_basic_vad_features_DT = clf_basic_vad_features_DT.predict(data_users_from_setGen_df[feature_names_vad])
prediction_basic_vad_features_RF = clf_basic_vad_features_RF.predict(data_users_from_setGen_df[feature_names_vad])
prediction_basic_vad_features_Gradient = clf_basic_vad_features_Gradient.predict(data_users_from_setGen_df[feature_names_vad])
prediction_basic_vad_features_Neural = clf_basic_vad_features_Neural.predict(data_users_from_setGen_df[feature_names_vad])

#Fazer as predições com os modelos para todos os exemplos de entrada (Basic Features + Tang)
prediction_basic_tang_features_LR = clf_basic_tang_features_LR.predict(data_users_from_setGen_df[Tang_Features])
prediction_basic_tang_features_KNN = clf_basic_tang_features_KNN.predict(data_users_from_setGen_df[Tang_Features])
prediction_basic_tang_features_DT = clf_basic_tang_features_DT.predict(data_users_from_setGen_df[Tang_Features])
prediction_basic_tang_features_RF = clf_basic_tang_features_RF.predict(data_users_from_setGen_df[Tang_Features])
prediction_basic_tang_features_Gradient = clf_basic_tang_features_Gradient.predict(data_users_from_setGen_df[Tang_Features])
prediction_basic_tang_features_Neural = clf_basic_tang_features_Neural.predict(data_users_from_setGen_df[Tang_Features])


#Fazer as predições com os modelos para todos os exemplos de entrada - (Basic Features + VAD + Tang)
prediction_basic_vad_tang_features_LR = clf_basic_vad_tang_features_LR.predict(data_users_from_setGen_df[VAD_Tang_Features])
prediction_basic_vad_tang_features_KNN = clf_basic_vad_tang_features_KNN.predict(data_users_from_setGen_df[VAD_Tang_Features])
prediction_basic_vad_tang_features_DT = clf_basic_vad_tang_features_DT.predict(data_users_from_setGen_df[VAD_Tang_Features])
prediction_basic_vad_tang_features_RF = clf_basic_vad_tang_features_RF.predict(data_users_from_setGen_df[VAD_Tang_Features])
prediction_basic_vad_tang_features_Gradient = clf_basic_vad_tang_features_Gradient.predict(data_users_from_setGen_df[VAD_Tang_Features])
prediction_basic_vad_tang_features_Neural = clf_basic_vad_tang_features_Neural.predict(data_users_from_setGen_df[VAD_Tang_Features])


# Adicionar as previsões ao DataFrame
#data_users_from_setGen_df['prediction_twitter_features'] = prediction_reduced_features
#data_users_from_setGen_df['prediction_vad'] = prediction_original_features
#data_users_from_setGen_df['prediction_Tang'] = prediction_expanded_features
#data_users_from_setGen_df['prediction_vad_Tang'] = prediction_vad_tang_features

# Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features)
data_users_from_setGen_df['prediction_basic_features_LR'] = prediction_basic_features_LR
data_users_from_setGen_df['prediction_basic_features_KNN'] = prediction_basic_features_KNN
data_users_from_setGen_df['prediction_basic_features_DT'] = prediction_basic_features_DT
data_users_from_setGen_df['prediction_basic_features_RF'] = prediction_basic_features_RF
data_users_from_setGen_df['prediction_basic_features_Gradient'] = prediction_basic_features_Gradient
data_users_from_setGen_df['prediction_basic_features_Neural'] = prediction_basic_features_Neural

# Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features + VAD)
data_users_from_setGen_df['prediction_basic_vad_features_LR'] = prediction_basic_vad_features_LR
data_users_from_setGen_df['prediction_basic_vad_features_KNN'] = prediction_basic_vad_features_KNN
data_users_from_setGen_df['prediction_basic_vad_features_DT'] = prediction_basic_vad_features_DT
data_users_from_setGen_df['prediction_basic_vad_features_RF'] = prediction_basic_vad_features_RF
data_users_from_setGen_df['prediction_basic_vad_features_Gradient'] = prediction_basic_vad_features_Gradient
data_users_from_setGen_df['prediction_basic_vad_features_Neural'] = prediction_basic_vad_features_Neural

# Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features + Tang)
data_users_from_setGen_df['prediction_basic_tang_features_LR'] = prediction_basic_tang_features_LR
data_users_from_setGen_df['prediction_basic_tang_features_KNN'] = prediction_basic_tang_features_KNN
data_users_from_setGen_df['prediction_basic_tang_features_DT'] = prediction_basic_tang_features_DT
data_users_from_setGen_df['prediction_basic_tang_features_RF'] = prediction_basic_tang_features_RF
data_users_from_setGen_df['prediction_basic_tang_features_Gradient'] = prediction_basic_tang_features_Gradient
data_users_from_setGen_df['prediction_basic_tang_features_Neural'] = prediction_basic_tang_features_Neural

# Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features + VAD + Tang)
data_users_from_setGen_df['prediction_basic_vad_tang_features_LR'] = prediction_basic_vad_tang_features_LR
data_users_from_setGen_df['prediction_basic_vad_tang_features_KNN'] = prediction_basic_vad_tang_features_KNN
data_users_from_setGen_df['prediction_basic_vad_tang_features_DT'] = prediction_basic_vad_tang_features_DT
data_users_from_setGen_df['prediction_basic_vad_tang_features_RF'] = prediction_basic_vad_tang_features_RF
data_users_from_setGen_df['prediction_basic_vad_tang_features_Gradient'] = prediction_basic_vad_tang_features_Gradient
data_users_from_setGen_df['prediction_basic_vad_tang_features_Neural'] = prediction_basic_vad_tang_features_Neural

# Atualizar os resultados na tabela users_from_setgen
for index, row in data_users_from_setGen_df.iterrows():
    user_id = row['UserID']
#    prediction_original_features = row['prediction_vad']
#    prediction_reduced_features = row['prediction_twitter_features']
#    prediction_expanded_features = row['prediction_Tang']
#    prediction_vad_tang_features = row['prediction_vad_Tang']

    # Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features)
    prediction_basic_features_LR= row['prediction_basic_features_LR']
    prediction_basic_features_KNN = row['prediction_basic_features_KNN'] 
    prediction_basic_features_DT = row['prediction_basic_features_DT'] 
    prediction_basic_features_RF = row['prediction_basic_features_RF']
    prediction_basic_features_Gradient = row['prediction_basic_features_Gradient']
    prediction_basic_features_Neural = row['prediction_basic_features_Neural']  
    
    # Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features + VAD)
    prediction_basic_vad_features_LR = row['prediction_basic_vad_features_LR'] 
    prediction_basic_vad_features_KNN = row['prediction_basic_vad_features_KNN'] 
    prediction_basic_vad_features_DT = row['prediction_basic_vad_features_DT'] 
    prediction_basic_vad_features_RF = row['prediction_basic_vad_features_RF'] 
    prediction_basic_vad_features_Gradient = row['prediction_basic_vad_features_Gradient']
    prediction_basic_vad_features_Neural = row['prediction_basic_vad_features_Neural'] 
    
    # Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features + Tang)
    prediction_basic_tang_features_LR = row['prediction_basic_tang_features_LR']
    prediction_basic_tang_features_KNN = row['prediction_basic_tang_features_KNN'] 
    prediction_basic_tang_features_DT = row['prediction_basic_tang_features_DT']
    prediction_basic_tang_features_RF = row['prediction_basic_tang_features_RF']
    prediction_basic_tang_features_Gradient = row['prediction_basic_tang_features_Gradient']
    prediction_basic_tang_features_Neural = row['prediction_basic_tang_features_Neural']
    
    # Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features + VAD + Tang)
    prediction_basic_vad_tang_features_LR = row['prediction_basic_vad_tang_features_LR']
    prediction_basic_vad_tang_features_KNN = row['prediction_basic_vad_tang_features_KNN']
    prediction_basic_vad_tang_features_DT = row['prediction_basic_vad_tang_features_DT']
    prediction_basic_vad_tang_features_RF = row['prediction_basic_vad_tang_features_RF'] 
    prediction_basic_vad_tang_features_Gradient = row['prediction_basic_vad_tang_features_Gradient']
    prediction_basic_vad_tang_features_Neural= row['prediction_basic_vad_tang_features_Neural']

#    prediction_vad={prediction_original_features},  
#    prediction_twitter_features={prediction_reduced_features},   
#    prediction_Tang={prediction_expanded_features}, 
#    prediction_vad_Tang={prediction_vad_tang_features}, 
        
    update_query = f'''UPDATE users_from_setgen SET
    
    # Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features)
    prediction_basic_features_LR={prediction_basic_features_LR},
    prediction_basic_features_KNN ={prediction_basic_features_KNN}, 
    prediction_basic_features_DT ={prediction_basic_features_DT}, 
    prediction_basic_features_RF ={prediction_basic_features_RF},
    prediction_basic_features_Gradient ={prediction_basic_features_Gradient},
    prediction_basic_features_Neural ={prediction_basic_features_Neural},  
    
    # Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features + VAD)
    prediction_basic_vad_features_LR ={prediction_basic_vad_features_LR}, 
    prediction_basic_vad_features_KNN ={prediction_basic_vad_features_KNN}, 
    prediction_basic_vad_features_DT ={prediction_basic_vad_features_DT}, 
    prediction_basic_vad_features_RF ={prediction_basic_vad_features_RF}, 
    prediction_basic_vad_features_Gradient ={prediction_basic_vad_features_Gradient},
    prediction_basic_vad_features_Neural ={prediction_basic_vad_features_Neural}, 
    
    # Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features + Tang)
    prediction_basic_tang_features_LR ={prediction_basic_tang_features_LR},
    prediction_basic_tang_features_KNN ={prediction_basic_tang_features_KNN}, 
    prediction_basic_tang_features_DT ={prediction_basic_tang_features_DT},
    prediction_basic_tang_features_RF ={prediction_basic_tang_features_RF},
    prediction_basic_tang_features_Gradient ={prediction_basic_tang_features_Gradient},
    prediction_basic_tang_features_Neural ={prediction_basic_tang_features_Neural},
    
    # Adicionar as novas previsões vindo do MultiMoldels ao DataFrame - (Basic Features + VAD + Tang)
    prediction_basic_vad_tang_features_LR ={prediction_basic_vad_tang_features_LR},
    prediction_basic_vad_tang_features_KNN ={prediction_basic_vad_tang_features_KNN},
    prediction_basic_vad_tang_features_DT ={prediction_basic_vad_tang_features_DT},
    prediction_basic_vad_tang_features_RF ={prediction_basic_vad_tang_features_RF}, 
    prediction_basic_vad_tang_features_Gradient ={prediction_basic_vad_tang_features_Gradient},
    prediction_basic_vad_tang_features_Neural ={prediction_basic_vad_tang_features_Neural}  
     
    WHERE UserID={user_id} '''
    
    cursor.execute(update_query)

# Fechar a conexão com o banco de dados
db.close()
