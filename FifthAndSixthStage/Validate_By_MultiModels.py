# -*- coding: utf-8 -*-
"""
Created on August 22 2024

 
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2024) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire
"""
import time
import pymysql
import pandas as pd
import datetime as dt
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold , cross_val_score
#from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold, cross_validate

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

from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from scipy.stats import randint
from imblearn.over_sampling import SMOTE  # Imbalanced-learn library

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
# Consulta SQL para selecionar os dados
full_feature_names = ['labelnews', 'TweetCount', 'ReTweetCount', 
    'favorite_count', 'alternativeName', 'total_users',
    'total_users_type_1','total_users_type_0', 'bot']

features_for_train_semConta = ['TweetCount', 'ReTweetCount', 
    'favorite_count']

features_for_train_comConta = ['TweetCount', 'ReTweetCount', 
    'favorite_count', 'bot']
    
sql_accounts = '''SELECT 
    t.labelednewsId as labelnews, 
    COUNT(t.TweetID) AS TweetCount, 
    SUM(t.retweet_count) AS ReTweetCount, 
    SUM(t.favorite_count) AS favorite_count, 
    l.alternativeName as alternativeName,
    COUNT(u.type) AS total_users,    
    SUM(CASE WHEN u.type = 1 THEN 1 ELSE 0 END) AS total_users_type_1,
    SUM(CASE WHEN u.type = 0 THEN 1 ELSE 0 END) AS total_users_type_0,
    CASE WHEN SUM(CASE WHEN u.type = 1 THEN 1 ELSE 0 END) > 
              SUM(CASE WHEN u.type = 0 THEN 1 ELSE 0 END) THEN 1 ELSE 0 END AS bot
FROM  
    tweetsoflabelednews AS t 
JOIN 
    users_from_setgen AS u ON u.userid = t.userid
JOIN
    labelednews AS l ON t.labelednewsId = l.id
JOIN 
    noticias_balanceadas as N on T.LabeledNewsId = N.LabeledNewsId     
WHERE 
   u.type <> 'H'
GROUP BY 
    t.labelednewsId,  l.alternativeName ''' 

# Conectar ao banco de dados
db = pymysql.connect(host='localhost', user='root', password='jef123*', db='ime', autocommit=True)

# Carregar dados usando consultas SQL
datas = execute_query(db, sql_accounts)

# Criar listas para armazenar os dados processados das contas que tem o label para treinamento dos modelos
data_list = []
for tupla in datas:
    posix_dates =  tupla[0:]
    data_list.append(posix_dates)
 
        
data_df = pd.DataFrame(data_list, columns= full_feature_names)
# Converter as colunas 'ReTweetCount' e 'favorite_count' para números inteiros
data_df['ReTweetCount'] = data_df['ReTweetCount'].astype(int)
data_df['favorite_count'] = data_df['favorite_count'].astype(int)
data_df['TweetCount'] = data_df['TweetCount'].astype(int)

# Verificar dados faltantes
print("Verificando dados faltantes:")
print(data_df.isnull().sum())

data_df_com_Conta = pd.DataFrame(data_list, columns= full_feature_names)
# Converter as colunas 'ReTweetCount' e 'favorite_count' para números inteiros
data_df_com_Conta['ReTweetCount'] = data_df_com_Conta['ReTweetCount'].astype(int)
data_df_com_Conta['favorite_count'] = data_df_com_Conta['favorite_count'].astype(int)
data_df_com_Conta['TweetCount'] = data_df_com_Conta['TweetCount'].astype(int)

#variável target para todos os modelos
#y = data_df['alternativeName']
#y = np.where(data_df['alternativeName'] == 'VERDADEIRO\r', 0, 1) 
y = np.where(data_df['alternativeName'].str.strip() == 'VERDADEIRO', 0, 1)
#y = y.astype(int)

#### Treinamento sem atributo conta ####
# Dividir o conjunto de dados em features e rótulos
X = data_df[features_for_train_semConta]
# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

 #Modelo com parametros SMOTE e com testes de parâmetros para buscar o melhor resultado
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# Aplicar SMOTE para balancear as classes no conjunto de treino
#smote = SMOTE(random_state=42)
#X_train, y_train = smote.fit_resample(X_train, y_train)

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
print("SEM CONTA")
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
    #print(y_test.value_counts())
    print(pd.Series(y_test).value_counts())
    print("\nDistribuição de classes nas previsões:")
    print(pd.Series(y_pred).value_counts())

    num_Fake = np.count_nonzero(y_train == 1)
    num_NaoFake = np.count_nonzero(y_train == 0)
    positive_class_weight = num_NaoFake / max(num_Fake, 1)
    
    print("Number of positive samples:", num_Fake)
    print("Number of negative samples:", num_NaoFake)
    print("Positive class weight:", positive_class_weight)


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
    with open(f'{model_name}_best_model_basic_vad.pkl', 'wb') as f:
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

print("COM CONTA")
#######################################################################################
#### Treinamento sem atributo conta ####
# Dividir o conjunto de dados em features e rótulos
X_ComConta = data_df[features_for_train_comConta]
# Dividir o conjunto de dados em treino e teste
X_ComContatrain, X_ComContatest, y_ComContatrain, y_ComContatest = train_test_split(X_ComConta, y, test_size=0.2, random_state=42)

 #Modelo com parametros SMOTE e com testes de parâmetros para buscar o melhor resultado
#X_ComContatrain, X_ComContatest, y_ComContatrain, y_ComContatest = train_test_split(X_ComConta, y, test_size=0.3, random_state=42, stratify=y)
# Aplicar SMOTE para balancear as classes no conjunto de treino
#smote = SMOTE(random_state=42)
#X_ComContatrain, y_ComContatrain = smote.fit_resample(X_ComContatrain, y_ComContatrain)

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
    grid_search.fit(X_ComContatrain, y_ComContatrain)
    
    # Registrar o tempo de término
    end_time = time.time()
    print(f"end Time (seconds): {end_time:.2f}")
    
    # Calcular o tempo de treinamento
    training_time = end_time - start_time
    print(f"tempo de treinamento (seconds): {training_time:.2f}")
    
    # Melhor modelo e suas previsões
    best_model = grid_search.best_estimator_
    y_ComContapred = best_model.predict(X_ComContatest)
    
    # Avaliar modelo
    accuracy = accuracy_score(y_ComContatest, y_ComContapred)
    #report = classification_report(y_test, y_pred, output_dict=True)
    report = classification_report(y_ComContatest, y_ComContapred, output_dict=True, zero_division=0)

    print("Distribuição de classes no conjunto de teste:")
    #print(y_ComContatest.value_counts())
    print(pd.Series(y_ComContatest).value_counts())
    print("\nDistribuição de classes nas previsões:")
    print(pd.Series(y_ComContapred).value_counts())

    num_Fake = np.count_nonzero(y_ComContatrain == 1)
    num_NaoFake = np.count_nonzero(y_ComContatrain == 0)
    positive_class_weight = num_NaoFake / max(num_Fake, 1)
    
    print("Number of positive samples:", num_Fake)
    print("Number of negative samples:", num_NaoFake)
    print("Positive class weight:", positive_class_weight)


    # Realizar validação cruzada para métricas com desvio padrão
    cv_accuracy = cross_val_score(best_model, X_ComContatrain, y_ComContatrain, cv=cv, scoring='accuracy')
    cv_precision = cross_val_score(best_model, X_ComContatrain, y_ComContatrain, cv=cv, scoring='precision_macro')
    cv_recall = cross_val_score(best_model, X_ComContatrain, y_ComContatrain, cv=cv, scoring='recall_macro')
    cv_f1 = cross_val_score(best_model, X_ComContatrain, y_ComContatrain, cv=cv, scoring='f1_macro')
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
    with open(f'{model_name}_best_model_basic_vad.pkl', 'wb') as f:
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


