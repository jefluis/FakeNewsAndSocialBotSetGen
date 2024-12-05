# -*- coding: utf-8 -*-
"""
Created on August 17 2024

 
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2024) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire
"""

#import matplotlib.pyplot as plt
#import seaborn as sns
#import joblib
#from sklearn.utils import class_weight

import time
import pymysql
import datetime as dt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
import pickle
import warnings
from sklearn.preprocessing import StandardScaler

# Suprimir avisos de futuras mudanças
warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn")

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

# Verificar dados faltantes
print("Verificando dados faltantes:")
print(data_df.isnull().sum())

#variável target para todos os modelos
y = data_df['Type']

#### Treinamento com features do VAD + Tang e suas estatísticas ####
# Treinar o modelo Random Forest com um conjunto expandido de features
features = basic_features_twitter + vad_features + Tang_Features 
X = data_df[features]
# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir modelos e seus parâmetros para Grid Search
models_params = {
    'Logistic Regression': {
        'model': LogisticRegression(max_iter=200, class_weight='balanced'),
        'params': {'model__C': [0.1, 1, 10], 'model__solver': ['lbfgs', 'liblinear']}
    },
    'K-Nearest Neighbors': {
        'model': KNeighborsClassifier(),
        'params': {'model__n_neighbors': [3, 5, 7], 'model__weights': ['uniform', 'distance']}
    },
#    'Support Vector Machine': {
#        'model': SVC(class_weight='balanced'),
#        'params': {'model__C': [0.1, 1, 10], 'model__kernel': ['linear', 'rbf']}
#    },
    'Decision Tree': {
        'model': DecisionTreeClassifier(class_weight='balanced'),
        'params': {'model__max_depth': [3, 5, 7], 'model__criterion': ['gini', 'entropy']}
    },
    'Random Forest': {
        'model': RandomForestClassifier(class_weight='balanced'),
        'params': {'model__n_estimators': [50, 100, 150], 'model__max_features': ['sqrt', 'log2', None, 0.5]}
    },
    'Gradient Boosting': {
        'model': GradientBoostingClassifier(),
        'params': {'model__n_estimators': [50, 100, 150], 'model__learning_rate': [0.01, 0.1, 0.2]}
    },
    'Neural Network': {        
        'model': MLPClassifier(
            #hidden_layer_sizes=(100, 50),  # Ajuste do tamanho das camadas ocultas
            max_iter=500,                  # Aumentar o número de iterações
            learning_rate_init=0.01,       # Ajuste da taxa de aprendizado
            early_stopping=True,           # Habilitar early stopping
            validation_fraction=0.1,       # Fração dos dados para validação
            n_iter_no_change=10),          # Número de iterações sem mudança antes de parar        
        'params': {'model__hidden_layer_sizes': [(50,), (100,), (50, 50)], 'model__activation': ['tanh', 'relu']}
    }
}
# Treinar e avaliar modelos com validação cruzada e Grid Search
results = []
for model_name, mp in models_params.items():
    pipeline = Pipeline([
        ('scaler', StandardScaler()),  # Adicionando o escalonador
        ('model', mp['model'])
    ])
    
    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    grid_search = GridSearchCV(pipeline, mp['params'], cv=cv, scoring='accuracy')

    # Registrar o tempo de início
    start_time = time.time()
    print(f"Modelo: {model_name}")
    print(f"start Time (seconds): {start_time:.2f}")
    
    # Treinar o modelo
    grid_search.fit(X_train, y_train)
    
    # Registrar o tempo de término
    end_time = time.time()
    print(f"end Time (seconds): {end_time:.2f}")
    
    # Calcular o tempo de treinamento
    training_time = end_time - start_time
    print(f"tempo de treinamento (seconds): {training_time:.2f}")
    
    # Melhor modelo e suas previsões
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    
    # Avaliar modelo
    accuracy = accuracy_score(y_test, y_pred)
    #report = classification_report(y_test, y_pred, output_dict=True)
    report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)

    print("Distribuição de classes no conjunto de teste:")
    print(y_test.value_counts())
    print("\nDistribuição de classes nas previsões:")
    print(pd.Series(y_pred).value_counts())
    
    # Realizar validação cruzada para métricas com desvio padrão
    cv_accuracy = cross_val_score(best_model, X_train, y_train, cv=cv, scoring='accuracy')
    cv_precision = cross_val_score(best_model, X_train, y_train, cv=cv, scoring='precision_macro')
    cv_recall = cross_val_score(best_model, X_train, y_train, cv=cv, scoring='recall_macro')
    cv_f1 = cross_val_score(best_model, X_train, y_train, cv=cv, scoring='f1_macro')
    results.append({
        'Model': model_name,
        'Best Parameters': grid_search.best_params_,
        'Accuracy': accuracy,
        'Classification Report': report,
        'Cross-Validation Scores': {
            'Accuracy': (np.mean(cv_accuracy), np.std(cv_accuracy)),
            'Precision': (np.mean(cv_precision), np.std(cv_precision)),
            'Recall': (np.mean(cv_recall), np.std(cv_recall)),
            'F1 Score': (np.mean(cv_f1), np.std(cv_f1))
        },
        'Training Time (seconds)': training_time  # Adicionando o tempo de treinamento aos resultados
    })
    
    # Salvar o melhor modelo em um arquivo pickle
    with open(f'{model_name}_best_model_basic_vad_tang.pkl', 'wb') as f:
        pickle.dump(best_model, f)

# Mostrar resultados
for result in results:
    print(f"Model: {result['Model']}")
    print(f"Best Parameters: {result['Best Parameters']}")
    print(f"Accuracy: {result['Accuracy']}")
    print("Classification Report:")
    print(pd.DataFrame(result['Classification Report']).transpose())
    print("Cross-Validation Scores:")
    for metric, (mean, std) in result['Cross-Validation Scores'].items():
        print(f"{metric}: {mean:.3f} ± {std:.3f}")
    print(f"Training Time (seconds): {result['Training Time (seconds)']:.2f}")        
    print("\n")

# Fechar a conexão com o banco de dados
db.close()
