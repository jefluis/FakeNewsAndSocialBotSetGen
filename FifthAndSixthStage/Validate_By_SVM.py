# -*- coding: utf-8 -*-
"""
Created on may 07 2024

 
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2024) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire
"""
import pymysql
import pandas as pd
import datetime as dt
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_validate, StratifiedKFold
#from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.utils import class_weight
from scipy.stats import uniform, loguniform

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

features_for_train = ['TweetCount', 'ReTweetCount', 
#    'favorite_count']
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

#variável target para todos os modelos
#y = data_df['alternativeName']
#y = np.where(data_df['alternativeName'] == 'VERDADEIRO\r', 0, 1) 
y = np.where(data_df['alternativeName'].str.strip() == 'VERDADEIRO', 0, 1)
#y = y.astype(int)

# Modelo SVM

# Dividir o conjunto de dados em features e rótulos
X_reduced = data_df[features_for_train]
# Dividir o conjunto de dados em treino e teste
X_train_reduced, X_test_reduced, y_train_reduced, y_test_reduced = train_test_split(X_reduced, y, test_size=0.2, random_state=42)

 # Definir a grade de parâmetros para o GridSearchCV
param_dist = {
 #    'C': [0.1, 1, 10, 100],
     'C': loguniform(0.1, 10),   
     #'kernel': ['linear', 'rbf', 'poly'],
     'kernel': ['linear', 'rbf'],
     'gamma': ['scale', 'auto']       
}
 
# Inicializar o modelo SVM
svm_model = SVC(class_weight='balanced', random_state=42)

# Inicializar o RandomizedSearchCV com validação cruzada de 10 folds e 30 iterações
#random_search = RandomizedSearchCV(estimator=svm_model, param_distributions=param_dist, n_iter=30, scoring='accuracy', cv=10, n_jobs=-1, verbose=2, random_state=42)
random_search = RandomizedSearchCV(estimator=svm_model, param_distributions=param_dist, n_iter=30, scoring='accuracy', cv=StratifiedKFold(10), n_jobs=-1, verbose=2, random_state=42)

# Treinar o RandomizedSearchCV
random_search.fit(X_train_reduced, y_train_reduced)

# Obter os melhores parâmetros encontrados pelo RandomizedSearchCV
best_params = random_search.best_params_

# Treinar o modelo com os melhores parâmetros
best_svm_model = random_search.best_estimator_

# Avaliar o modelo usando validação cruzada e calcular as métricas
scoring = ['accuracy', 'precision', 'recall', 'f1']
cv_results = cross_validate(best_svm_model, X_train_reduced, y_train_reduced, cv=StratifiedKFold(10), scoring=scoring)

# Calcular as médias e desvios padrão das métricas
accuracy_mean = np.mean(cv_results['test_accuracy'])
accuracy_std = np.std(cv_results['test_accuracy'])
precision_mean = np.mean(cv_results['test_precision'])
precision_std = np.std(cv_results['test_precision'])
recall_mean = np.mean(cv_results['test_recall'])
recall_std = np.std(cv_results['test_recall'])
f1_mean = np.mean(cv_results['test_f1'])
f1_std = np.std(cv_results['test_f1'])

print("*** Results ***")
print("Best Parameters:", best_params)
print("Accuracy: {:.4f} ± {:.4f}".format(accuracy_mean, accuracy_std))
print("Precision: {:.4f} ± {:.4f}".format(precision_mean, precision_std))
print("Recall: {:.4f} ± {:.4f}".format(recall_mean, recall_std))
print("F1-score: {:.4f} ± {:.4f}".format(f1_mean, f1_std))

# Fazer previsões no conjunto de teste para outras métricas que não são médias de k-fold
y_pred_reduced = best_svm_model.predict(X_test_reduced)
roc_auc = roc_auc_score(y_test_reduced, y_pred_reduced)
print("ROC AUC Score:", roc_auc)

# Calcular as métricas do modelo no conjunto de teste
accuracy = accuracy_score(y_test_reduced, y_pred_reduced)
precision = precision_score(y_test_reduced, y_pred_reduced, pos_label=1)
recall = recall_score(y_test_reduced, y_pred_reduced, pos_label=1)
f1 = f1_score(y_test_reduced, y_pred_reduced, pos_label=1)
precision_h = precision_score(y_test_reduced, y_pred_reduced, pos_label=0)
recall_h = recall_score(y_test_reduced, y_pred_reduced, pos_label=0)
f1_h = f1_score(y_test_reduced, y_pred_reduced, pos_label=0)

print("Accuracy (Test Set):", accuracy)
print("Precision (Test Set):", precision)
print("Recall (Test Set):", recall)
print("F1-score (Test Set):", f1)
print("Precision Não Fake (Test Set):", precision_h)
print("Recall Não Fake (Test Set):", recall_h)
print("F1-score Não Fake (Test Set):", f1_h)

# Salvar o modelo treinado com features reduzidas
joblib.dump(best_svm_model, 'svm_model_reduced_features_paulo.pkl')

'''
Finding Important Features in Scikit-learn
'''
# Obtendo os coeficientes das features do modelo SVM linear
if best_params['kernel'] == 'linear':
    coeficients = best_svm_model.coef_[0]

    # Criando uma série pandas para melhor visualização
    feature_importance_linear_svm = pd.Series(coeficients, index=features_for_train).sort_values(ascending=False)

    # Imprimindo as features mais importantes
    print("Principais features - Modelo SVM com kernel linear:")
    print(feature_importance_linear_svm)

    # Plotando as features mais importantes
    sns.barplot(x=feature_importance_linear_svm, y=feature_importance_linear_svm.index)
    plt.xlabel('Importância da Feature')
    plt.ylabel('Features')
    plt.title("Visualizando as Features Mais Importantes - Modelo SVM com kernel linear")
    plt.show()

# Fechar a conexão com o banco de dados
db.close()

#===============================================================================
# Para GridSearchCV
# # Inicializar o GridSearchCV
# grid_search = GridSearchCV(estimator=svm_model, param_grid=param_grid, scoring='accuracy', cv=3, n_jobs=-1, verbose=2)
# 
# # Treinar o GridSearchCV
# grid_search.fit(X_train_reduced, y_train_reduced)
# 
# # Obter os melhores parâmetros encontrados pelo GridSearchCV
# best_params = grid_search.best_params_
# 
# # Treinar o modelo com os melhores parâmetros
# best_svm_model = grid_search.best_estimator_

# Fazer previsões no conjunto de teste
#y_pred_reduced = best_svm_model.predict(X_test_reduced)


#===============================================================================



#Marcando o formato antigo
# Inicializar o modelo SVM
#svm_model = SVC(kernel='linear', C=1.0, random_state=42, class_weight='balanced')

# Treinar o modelo
#svm_model.fit(X_train_reduced, y_train_reduced)

# Fazer previsões no conjunto de teste
#y_pred_reduced = svm_model.predict(X_test_reduced)


#===============================================================================
# # Antes de calcular usando a média e desvio padrão kfold = 10
# # Calcular as métricas do modelo no conjunto de teste
# accuracy = accuracy_score(y_test_reduced, y_pred_reduced)
# roc_auc = roc_auc_score(y_test_reduced, y_pred_reduced)
# # Para Fake
# precision = precision_score(y_test_reduced, y_pred_reduced, pos_label=1)
# recall = recall_score(y_test_reduced, y_pred_reduced, pos_label=1)
# f1 = f1_score(y_test_reduced, y_pred_reduced, pos_label=1)
# # Para Não Fake
# precision_h = precision_score(y_test_reduced, y_pred_reduced, pos_label=0)
# recall_h = recall_score(y_test_reduced, y_pred_reduced, pos_label=0)
# f1_h = f1_score(y_test_reduced, y_pred_reduced, pos_label=0)
# 
# print("Best Parameters:", best_params)
# print("Accuracy:", accuracy)
# print("ROC AUC Score:", roc_auc)
# 
# print('--> Fake:')
# print("Precision:", precision)
# print("Recall:", recall)
# print("F1-score:", f1)
# 
# print('--> Não Fake:')
# print("Precision:", precision_h)
# print("Recall:", recall_h)
# print("F1-score:", f1_h)
# 
# # Salvar o modelo treinado com features reduzidas
# joblib.dump(best_svm_model, 'svm_model_reduced_features_paulo.pkl')
# 
# 
# '''
# Finding Important Features in Scikit-learn
# '''
# # Obtendo os coeficientes das features do modelo SVM linear
# if best_params['kernel'] == 'linear':
#     coeficients = best_svm_model.coef_[0]
# 
#     # Criando uma série pandas para melhor visualização
#     feature_importance_linear_svm = pd.Series(coeficients, index=features_for_train).sort_values(ascending=False)
# 
#     # Imprimindo as features mais importantes
#     print("Principais features - Modelo SVM com kernel linear:")
#     print(feature_importance_linear_svm)
# 
#     # Plotando as features mais importantes
#     sns.barplot(x=feature_importance_linear_svm, y=feature_importance_linear_svm.index)
#     plt.xlabel('Importância da Feature')
#     plt.ylabel('Features')
#     plt.title("Visualizando as Features Mais Importantes - Modelo SVM com kernel linear")
#     plt.show()
#===============================================================================

