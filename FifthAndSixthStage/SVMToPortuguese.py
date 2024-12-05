# -*- coding: utf-8 -*-
"""
Created on October 31 2023

 
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2024) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire
"""

import pymysql
import pandas as pd
import datetime as dt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.svm import SVC
from sklearn.utils import class_weight


# FUNÇÕES
def convert_datetime_to_timestamp(date_time):
    timestamp = dt.datetime.timestamp(date_time)
    return timestamp

def execute_query(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

### Inicializo as listas de features que serão utilizadas para treinamento dos modelos e irão facilitar o reuso
# Será usado para treinamento do modelo que irá usar somente dados do twitter
basic_features_twitter =  ['CreatedAt', 'NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 
                     'LengthOfScreenName', 'LenDescrInUseProfile'] 

vad_features = ['V_media', 'A_media', 'D_media', 
               'V_1quartil', 'A_1quartil', 'D_1quartil', 
               'V_mediana', 'A_mediana', 'D_mediana', 
               'V_3quartil', 'A_3quartil', 'D_3quartil', 
               'V_desviopadrao', 'A_desviopadrao', 'D_desviopadrao', 
               'V_amplitude', 'A_amplitude', 'D_amplitude']

Tang_Features = ['d1_media', 'd2_media', 'd3_media', 'd4_media', 'd5_media', 'd6_media', 'd7_media', 'd8_media', 'd9_media','d10_media', 'd11_media', 'd12_media', 'd13_media', 'd14_media', 'd15_media', 'd16_media', 'd17_media', 'd18_media', 'd19_media', 'd20_media', 'd21_media', 'd22_media', 'd23_media', 'd24_media', 'd25_media', 'd26_media', 'd27_media', 'd28_media', 'd29_media', 'd30_media', 'd31_media', 'd32_media', 'd33_media', 'd34_media', 'd35_media', 'd36_media', 'd37_media', 'd38_media', 'd39_media', 'd40_media', 'd41_media', 'd42_media', 'd43_media', 'd44_media', 'd45_media', 'd46_media', 'd47_media', 'd48_media', 'd49_media', 'd50_media', 
                 'd1_1quartil', 'd2_1quartil', 'd3_1quartil', 'd4_1quartil', 'd5_1quartil', 'd6_1quartil', 'd7_1quartil', 'd8_1quartil', 'd9_1quartil', 'd10_1quartil', 'd11_1quartil', 'd12_1quartil', 'd13_1quartil', 'd14_1quartil', 'd15_1quartil', 'd16_1quartil', 'd17_1quartil', 'd18_1quartil', 'd19_1quartil', 'd20_1quartil', 'd21_1quartil', 'd22_1quartil', 'd23_1quartil', 'd24_1quartil', 'd25_1quartil', 'd26_1quartil', 'd27_1quartil', 'd28_1quartil', 'd29_1quartil', 'd30_1quartil', 'd31_1quartil', 'd32_1quartil', 'd33_1quartil', 'd34_1quartil', 'd35_1quartil', 'd36_1quartil', 'd37_1quartil', 'd38_1quartil', 'd39_1quartil', 'd40_1quartil', 'd41_1quartil', 'd42_1quartil', 'd43_1quartil', 'd44_1quartil', 'd45_1quartil', 'd46_1quartil', 'd47_1quartil', 'd48_1quartil', 'd49_1quartil', 'd50_1quartil', 
                 'd1_mediana', 'd2_mediana', 'd3_mediana', 'd4_mediana', 'd5_mediana', 'd6_mediana', 'd7_mediana', 'd8_mediana', 'd9_mediana', 'd10_mediana', 'd11_mediana', 'd12_mediana', 'd13_mediana', 'd14_mediana', 'd15_mediana', 'd16_mediana', 'd17_mediana', 'd18_mediana', 'd19_mediana', 'd20_mediana', 'd21_mediana', 'd22_mediana', 'd23_mediana', 'd24_mediana', 'd25_mediana', 'd26_mediana', 'd27_mediana', 'd28_mediana', 'd29_mediana', 'd30_mediana', 'd31_mediana', 'd32_mediana', 'd33_mediana', 'd34_mediana', 'd35_mediana', 'd36_mediana', 'd37_mediana', 'd38_mediana', 'd39_mediana', 'd40_mediana', 'd41_mediana', 'd42_mediana', 'd43_mediana', 'd44_mediana', 'd45_mediana', 'd46_mediana', 'd47_mediana', 'd48_mediana', 'd49_mediana', 'd50_mediana', 
                 'd1_3quartil', 'd2_3quartil', 'd3_3quartil', 'd4_3quartil', 'd5_3quartil', 'd6_3quartil', 'd7_3quartil', 'd8_3quartil', 'd9_3quartil', 'd10_3quartil', 'd11_3quartil', 'd12_3quartil', 'd13_3quartil', 'd14_3quartil', 'd15_3quartil', 'd16_3quartil', 'd17_3quartil', 'd18_3quartil', 'd19_3quartil', 'd20_3quartil', 'd21_3quartil', 'd22_3quartil', 'd23_3quartil', 'd24_3quartil', 'd25_3quartil', 'd26_3quartil', 'd27_3quartil', 'd28_3quartil', 'd29_3quartil', 'd30_3quartil', 'd31_3quartil', 'd32_3quartil', 'd33_3quartil', 'd34_3quartil', 'd35_3quartil', 'd36_3quartil', 'd37_3quartil', 'd38_3quartil', 'd39_3quartil', 'd40_3quartil', 'd41_3quartil', 'd42_3quartil', 'd43_3quartil', 'd44_3quartil', 'd45_3quartil', 'd46_3quartil', 'd47_3quartil', 'd48_3quartil', 'd49_3quartil', 'd50_3quartil', 
                 'd1_desviopadrao', 'd2_desviopadrao', 'd3_desviopadrao', 'd4_desviopadrao', 'd5_desviopadrao', 'd6_desviopadrao', 'd7_desviopadrao', 'd8_desviopadrao', 'd9_desviopadrao', 'd10_desviopadrao', 'd11_desviopadrao', 'd12_desviopadrao', 'd13_desviopadrao', 'd14_desviopadrao', 'd15_desviopadrao', 'd16_desviopadrao', 'd17_desviopadrao', 'd18_desviopadrao', 'd19_desviopadrao', 'd20_desviopadrao', 'd21_desviopadrao', 'd22_desviopadrao', 'd23_desviopadrao', 'd24_desviopadrao', 'd25_desviopadrao', 'd26_desviopadrao', 'd27_desviopadrao', 'd28_desviopadrao', 'd29_desviopadrao', 'd30_desviopadrao', 'd31_desviopadrao', 'd32_desviopadrao', 'd33_desviopadrao', 'd34_desviopadrao', 'd35_desviopadrao', 'd36_desviopadrao', 'd37_desviopadrao', 'd38_desviopadrao', 'd39_desviopadrao', 'd40_desviopadrao', 'd41_desviopadrao', 'd42_desviopadrao', 'd43_desviopadrao', 'd44_desviopadrao', 'd45_desviopadrao', 'd46_desviopadrao', 'd47_desviopadrao', 'd48_desviopadrao', 'd49_desviopadrao', 'd50_desviopadrao', 
                 'd1_amplitude', 'd2_amplitude', 'd3_amplitude', 'd4_amplitude', 'd5_amplitude', 'd6_amplitude', 'd7_amplitude', 'd8_amplitude', 'd9_amplitude', 'd10_amplitude', 'd11_amplitude', 'd12_amplitude', 'd13_amplitude', 'd14_amplitude', 'd15_amplitude', 'd16_amplitude', 'd17_amplitude', 'd18_amplitude', 'd19_amplitude', 'd20_amplitude', 'd21_amplitude', 'd22_amplitude', 'd23_amplitude', 'd24_amplitude', 'd25_amplitude', 'd26_amplitude', 'd27_amplitude', 'd28_amplitude', 'd29_amplitude', 'd30_amplitude', 'd31_amplitude', 'd32_amplitude', 'd33_amplitude', 'd34_amplitude', 'd35_amplitude', 'd36_amplitude', 'd37_amplitude', 'd38_amplitude', 'd39_amplitude', 'd40_amplitude', 'd41_amplitude', 'd42_amplitude', 'd43_amplitude', 'd44_amplitude', 'd45_amplitude', 'd46_amplitude', 'd47_amplitude', 'd48_amplitude', 'd49_amplitude', 'd50_amplitude']  # Features

full_feature_names = ['UserID'] + basic_features_twitter + ['Type'] + vad_features + Tang_Features 
 
# Converter a lista em uma string usando o método join()
feature_names_string = ', '.join(full_feature_names) 

# Conectar ao banco de dados
db = pymysql.connect(host='localhost', user='root', password='jef123*', db='ime', autocommit=True)

# Consulta SQL para selecionar os dados
sql_accounts = '''SELECT ''' + feature_names_string + ''' FROM accounts_pt '''

# Carregar dados usando consultas SQL
datas = execute_query(db, sql_accounts)

# Criar listas para armazenar os dados processados das contas que tem o label para treinamento dos modelos
data_list = []
for tupla in datas:
    posix_dates = (tupla[0], convert_datetime_to_timestamp(tupla[1])) + tupla[2:]
    data_list.append(posix_dates)
        
data_df = pd.DataFrame(data_list, columns= full_feature_names)

#variável target para todos os modelos
y = data_df['Type']


# Modelo SVM
#_____________________________________________________________________________________
#_____________________________________________________________________________________

#### Treinamento com features básicas de dados da conta do Twitter ####
# Dividir o conjunto de dados em features e rótulos
X_reduced = data_df[basic_features_twitter]
# Dividir o conjunto de dados em treino e teste
X_train_reduced, X_test_reduced, y_train_reduced, y_test_reduced = train_test_split(X_reduced, y, test_size=0.2, random_state=42)

# Inicializar o modelo SVM
svm_model = SVC(kernel='linear', C=1.0, random_state=42, class_weight='balanced')

# Treinar o modelo
svm_model.fit(X_train_reduced, y_train_reduced)

# Fazer previsões no conjunto de teste
y_pred_reduced = svm_model.predict(X_test_reduced)

# Calcular as métricas do modelo no conjunto de teste
accuracy = accuracy_score(y_test_reduced, y_pred_reduced)
roc_auc = roc_auc_score(y_test_reduced, y_pred_reduced)
#Para chat
precision = precision_score(y_test_reduced, y_pred_reduced, pos_label='1')
recall = recall_score(y_test_reduced, y_pred_reduced, pos_label='1')
f1 = f1_score(y_test_reduced, y_pred_reduced, pos_label='1')
#Para Humano
precision_h = precision_score(y_test_reduced, y_pred_reduced, pos_label='0')
recall_h = recall_score(y_test_reduced, y_pred_reduced, pos_label='0')
f1_h = f1_score(y_test_reduced, y_pred_reduced, pos_label='0')


print("*** Trained with Basic Twitter Features ***")
print("Accuracy:", accuracy)
print("ROC AUC Score:", roc_auc)

print('--> Chat:')
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

print('--> Para Humano:')
print("Precision:", precision_h)
print("Recall:", recall_h)
print("F1-score:", f1_h)

# Salvar o modelo treinado com features reduzidas
joblib.dump(clf_reduced, 'svm_model_reduced_features.pkl')

# Plotar a matriz de confusão
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test_reduced, y_pred_reduced), annot=True, fmt='g', cmap='Blues', 
            xticklabels=['Human', 'Bot'], yticklabels=['Human', 'Bot'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

'''
Finding Important Features in Scikit-learn
'''
feature_imp_basic = pd.Series(svm_model.feature_importances_,index=basic_features_twitter).sort_values(ascending=False)
print('Principais features - Modelo com dados básicos do Twitter')
print(feature_imp_basic)
print('+++++++++++++++++++++++++++++++')

# Creating a bar plot
sns.barplot(x=feature_imp_basic, y=feature_imp_basic.index)
# Add labels to your graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features Modelo com dados básicos do Twitter")
plt.legend()
plt.show()
print('+++++++++++++++++++++++++++++++')


#### Treinamento com features VAD e suas estatísticas ####
# Dividir o conjunto de dados em features e rótulos
features = basic_features_twitter + vad_features
X = data_df[features]

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar o modelo SVM
svm_model = SVC(kernel='linear', C=1.0, random_state=42, class_weight='balanced')

# Treinar o modelo
svm_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = svm_model.predict(X_test)

# Calcular as métricas do modelo no conjunto de teste
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)
#Para chat
precision = precision_score(y_test, y_pred, pos_label='1')
recall = recall_score(y_test, y_pred, pos_label='1')
f1 = f1_score(y_test, y_pred, pos_label='1')
#Para humano
precision_h = precision_score(y_test, y_pred, pos_label='0')
recall_h = recall_score(y_test, y_pred, pos_label='0')
f1_h = f1_score(y_test, y_pred, pos_label='0')

print("*** Trained with VAD + Twitter Features ***")
print("Accuracy:", accuracy)
print("ROC AUC Score:", roc_auc)

print('--> Chat:')
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

print('--> Para Humano:')
print("Precision:", precision_h)
print("Recall:", recall_h)
print("F1-score:", f1_h)

#https://www.geeksforgeeks.org/saving-a-machine-learning-model/amp/
# Salvar o modelo treinado
joblib.dump(clf, 'svm_model_original_features.pkl')

# Plotar a matriz de confusão
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='g', cmap='Blues', 
            xticklabels=['Human', 'Bot'], yticklabels=['Human', 'Bot'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

'''
Finding Important Features in Scikit-learn
Here, you are finding important features or selecting features in the dataset. 
In scikit-learn, you can perform this task in the following steps:

First, you need to create a random forests model.
Second, use the feature importance variable to see feature importance scores.
Third, visualize these scores using the seaborn library.
'''

feature_imp = pd.Series(svm_model.feature_importances_,index=features).sort_values(ascending=False)
print('Principais features - Modelo com VAD + Twitter')
print(feature_imp)
print('+++++++++++++++++++++++++++++++')

'''You can also visualize the feature importance. Visualizations are easy to understand and interpretable.
For visualization, you can use a combination of matplotlib and seaborn. 
Because seaborn is built on top of matplotlib, it offers a number of customized themes and provides additional plot Tipos.
Matplotlib is a superset of seaborn and both are equally important for good visualizations.'''

# Creating a bar plot
sns.barplot(x=feature_imp, y=feature_imp.index)
# Add labels to your graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features VAD")
plt.legend()
plt.show()
print('+++++++++++++++++++++++++++++++')

#### Treinamento com features do Tang e suas estatísticas ####
# Treinar o modelo Random Forest com um conjunto expandido de features
features = basic_features_twitter + Tang_Features 
X_expanded = data_df[features]
X_train_expanded, X_test_expanded, y_train_expanded, y_test_expanded = train_test_split(X_expanded, y, test_size=0.2, random_state=42)

# Inicializar o modelo SVM
svm_model = SVC(kernel='linear', C=1.0, random_state=42, class_weight='balanced')

# Treinar o modelo
svm_model.fit(X_train_expanded, y_train_expanded)

# Fazer previsões no conjunto de teste
y_pred_expanded = svm_model.predict(X_test_expanded)

accuracy = accuracy_score(y_test_expanded, y_pred_expanded)
roc_auc = roc_auc_score(y_test_expanded, y_pred_expanded)
#para bot
precision = precision_score(y_test_expanded, y_pred_expanded, pos_label='1')
recall = recall_score(y_test_expanded, y_pred_expanded, pos_label='1')
f1 = f1_score(y_test_expanded, y_pred_expanded, pos_label='1')
#para humano
precision_h = precision_score(y_test_expanded, y_pred_expanded, pos_label='0')
recall_h = recall_score(y_test_expanded, y_pred_expanded, pos_label='0')
f1_h = f1_score(y_test_expanded, y_pred_expanded, pos_label='0')

print("*** Trained with Tang Features + Twitter ***")
print("Accuracy:", accuracy)
print("ROC AUC Score:", roc_auc)

print('--> Chat:')
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

print('--> Para Humano:')
print("Precision:", precision_h)
print("Recall:", recall_h)
print("F1-score:", f1_h)

# Salvar o modelo treinado com features expandidas
joblib.dump(clf_expanded, 'svm_model_expanded_features.pkl')

# Plotar a matriz de confusão
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test_expanded, y_pred_expanded), annot=True, fmt='g', cmap='Blues', 
            xticklabels=['Human', 'Bot'], yticklabels=['Human', 'Bot'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

'''
Finding Important Features in Scikit-learn
'''

feature_imp_tang = pd.Series(svm_model.feature_importances_,index=features).sort_values(ascending=False)
print('Principais features - Modelo com Tang e estatísticas')
print(feature_imp_tang)
print('+++++++++++++++++++++++++++++++')

# Creating a bar plot
sns.barplot(x=feature_imp_tang, y=feature_imp_tang.index)
# Add labels to your graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features Modelo com Tang e estatísticas")
plt.legend()
plt.show()
print('+++++++++++++++++++++++++++++++')


#### Treinamento com features do VAD + Tang e suas estatísticas ####
# Treinar o modelo Random Forest com um conjunto expandido de features
features = basic_features_twitter + vad_features + Tang_Features 
X_VAD_Tang = data_df[features]
X_train_VAD_Tang, X_test_VAD_Tang, y_train_VAD_Tang, y_test_VAD_Tang = train_test_split(X_VAD_Tang, y, test_size=0.2, random_state=42)

# Inicializar o modelo SVM
svm_model = SVC(kernel='linear', C=1.0, random_state=42, class_weight='balanced')

# Treinar o modelo
svm_model.fit(X_train_VAD_Tang, y_train_VAD_Tang)

# Fazer previsões no conjunto de teste
y_pred_VAD_Tang = svm_model.predict(X_test_VAD_Tang)

accuracy = accuracy_score(y_test_VAD_Tang, y_pred_VAD_Tang)
roc_auc = roc_auc_score(y_test_VAD_Tang, y_pred_VAD_Tang)
#para bot
precision = precision_score(y_test_VAD_Tang, y_pred_VAD_Tang, pos_label='1')
recall = recall_score(y_test_VAD_Tang, y_pred_VAD_Tang, pos_label='1')
f1 = f1_score(y_test_VAD_Tang, y_pred_VAD_Tang, pos_label='1')
#para humano
precision_h = precision_score(y_test_VAD_Tang, y_pred_VAD_Tang, pos_label='0')
recall_h = recall_score(y_test_VAD_Tang, y_pred_VAD_Tang, pos_label='0')
f1_h = f1_score(y_test_VAD_Tang, y_pred_VAD_Tang, pos_label='0')

print("*** Trained with VAD_Tang Features + Twitter ***")
print("Accuracy:", accuracy)
print("ROC AUC Score:", roc_auc)

print('--> Chat:')
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

print('--> Para Humano:')
print("Precision:", precision_h)
print("Recall:", recall_h)
print("F1-score:", f1_h)


# Salvar o modelo treinado com features expandidas
joblib.dump(clf_VAD_Tang, 'svm_model_VAD_Tang_features.pkl')


# Plotar a matriz de confusão
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test_VAD_Tang, y_pred_VAD_Tang), annot=True, fmt='g', cmap='Blues', 
            xticklabels=['Human', 'Bot'], yticklabels=['Human', 'Bot'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
'''
Finding Important Features in Scikit-learn
'''

feature_imp_VAD_Tang = pd.Series(svm_model.feature_importances_,index=features).sort_values(ascending=False)
print('Principais features - Modelo com VAD_Tang e estatísticas')
print(feature_imp_VAD_Tang)
print('+++++++++++++++++++++++++++++++')

# Creating a bar plot
sns.barplot(x=feature_imp_VAD_Tang, y=feature_imp_VAD_Tang.index)
# Add labels to your graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features Modelo com VAD_Tang e estatísticas")
plt.legend()
plt.show()
print('+++++++++++++++++++++++++++++++')



# Fechar a conexão com o banco de dados
db.close()
