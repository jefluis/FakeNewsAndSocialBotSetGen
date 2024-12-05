# -*- coding: utf-8 -*-
"""
Created on may 05 2024

 
@author: Jeferson - jefluis@yahoo.com.br Aluno SRXXXXXXX
Mestrado em Sistemas e Computação (SE-9 2021/2024) no Instituto Militar de Engenharia (IME)
Dissertação: 
Orientadores: Ronaldo Goldschmidt / Paulo Freire
"""
import pymysql
import pandas as pd
import datetime as dt
import numpy as np
#from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold, cross_val_score, cross_val_predict, cross_validate
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, make_scorer
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from scipy.stats import randint
from imblearn.over_sampling import SMOTE  # Imbalanced-learn library

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

#variável target para todos os modelos
#y = data_df['alternativeName']
#y = np.where(data_df['alternativeName'] == 'VERDADEIRO\r', 0, 1) 
y = np.where(data_df['alternativeName'].str.strip() == 'VERDADEIRO', 0, 1)
#y = y.astype(int)

#===============================================================================
# # Dividir o conjunto de dados em features e rótulos
# X_reduced = data_df[features_for_train]
# # Dividir o conjunto de dados em treino e teste
# X_train_reduced, X_test_reduced, y_train_reduced, y_test_reduced = train_test_split(X_reduced, y, test_size=0.2, random_state=42)
#  
# num_Fake = np.count_nonzero(y_train_reduced == 1)
# num_NaoFake = np.count_nonzero(y_train_reduced == 0)
# # Calcular o peso de classe positivo para lidar com desequilíbrio de classe
# positive_class_weight = num_NaoFake / max(num_Fake, 1)
# 
# print("Number of positive samples:", num_Fake)
# print("Number of negative samples:", num_NaoFake)
# print("Positive class weight:", positive_class_weight)
#===============================================================================

#Novo trecho
#===============================================================================
# # Definir a grade de parâmetros para o GridSearchCV
# param_grid = {
#     'n_estimators': [100, 300, 500],
#     'learning_rate': [0.01, 0.1, 0.3],
#     'max_depth': [3, 6, 9],
#     'min_child_weight': [1, 5, 10],
#     'subsample': [0.8, 1.0],
#     'colsample_bytree': [0.8, 1.0],
#     'gamma': [0, 0.1, 0.3]
# }
# 
# grid_search = GridSearchCV(estimator=XGBClassifier(objective='binary:logistic', random_state=42, scale_pos_weight=positive_class_weight),
#                            param_grid=param_grid,
#                            scoring='accuracy',
#                            cv=10,
#                            n_jobs=-1,
#                            verbose=2)
#===============================================================================
#===============================================================================
# 
# # Treinar o GridSearchCV
# grid_search.fit(X_train_reduced, y_train_reduced)
# 
# # Obter os melhores parâmetros encontrados pelo GridSearchCV
# best_params = grid_search.best_params_
# 
# # Treinar o modelo com os melhores parâmetros
# best_xgb_model = grid_search.best_estimator_
# 
# # Fazer previsões no conjunto de teste
# y_pred_reduced = best_xgb_model.predict(X_test_reduced)
#===============================================================================

#===============================================================================
# #Parte antiga, estou deixando marcada
# 
# # Treinar o modelo XGBoost
# # Inicializar o modelo XGBoost
# #clf_reduced = XGBClassifier(objective='binary:logistic', random_state=42)
# 
# clf_reduced = XGBClassifier(objective='binary:logistic', random_state=42, scale_pos_weight=positive_class_weight)
# clf_reduced.fit(X_train_reduced, y_train_reduced)
# 
# # Avaliar a precisão do modelo no conjunto de teste com features reduzidas
# y_pred_reduced = clf_reduced.predict(X_test_reduced)
#===============================================================================
 

#########################################################
#Trecho com randomizeCV e SMOTE
# Dividir o conjunto de dados em features e rótulos
X_reduced = data_df[features_for_train]
# Dividir o conjunto de dados em treino e teste
X_train_reduced, X_test_reduced, y_train_reduced, y_test_reduced = train_test_split(X_reduced, y, test_size=0.2, random_state=42, stratify=y)
# Aplicar SMOTE para balancear as classes no conjunto de treino
smote = SMOTE(random_state=42)
X_train_reduced, y_train_reduced = smote.fit_resample(X_train_reduced, y_train_reduced)

num_Fake = np.count_nonzero(y_train_reduced == 1)
num_NaoFake = np.count_nonzero(y_train_reduced == 0)
# Calcular o peso de classe positivo para lidar com desequilíbrio de classe
positive_class_weight = num_NaoFake / max(num_Fake, 1)
 
print("Number of positive samples:", num_Fake)
print("Number of negative samples:", num_NaoFake)
print("Positive class weight:", positive_class_weight)
# Definir a grade de parâmetros para o RandomizedSearchCV
param_dist = {
    'n_estimators': randint(100, 1000),
    'learning_rate': [0.01, 0.1, 0.3],
    'max_depth': randint(3, 10),
    'min_child_weight': randint(1, 10),
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0],
    'gamma': [0, 0.1, 0.3],
    'scale_pos_weight': [1, positive_class_weight]
}

# Inicializar o modelo XGBoost
clf_reduced = XGBClassifier(objective='binary:logistic', random_state=42)

# Inicializar o RandomizedSearchCV com validação cruzada estratificada de 10 folds e 100 iterações
random_search = RandomizedSearchCV(estimator=clf_reduced, param_distributions=param_dist, n_iter=100, scoring='accuracy', cv=StratifiedKFold(10), n_jobs=-1, verbose=2, random_state=42)

# Treinar o RandomizedSearchCV
random_search.fit(X_train_reduced, y_train_reduced)

# Obter os melhores parâmetros encontrados pelo RandomizedSearchCV
best_params = random_search.best_params_

# Treinar o modelo com os melhores parâmetros
best_xgb_model = random_search.best_estimator_

# Fazer previsões no conjunto de teste
y_pred_reduced = best_xgb_model.predict(X_test_reduced)  
######################################################### 

# Validação cruzada para métricas com desvio padrão
#===============================================================================
# scoring = {
#     'accuracy': 'accuracy',
#     'precision': make_scorer(precision_score, pos_label=1),
#     'recall': make_scorer(recall_score, pos_label=1),
#     'f1': make_scorer(f1_score, pos_label=1)
# }
#===============================================================================
scoring = ['accuracy', 'precision', 'recall', 'f1']
#cv_results = cross_validate(best_xgb_model, X_train_reduced, y_train_reduced, cv=StratifiedKFold(10), scoring=scoring, return_train_score=False)
cv_results = cross_validate(best_xgb_model, X_train_reduced, y_train_reduced, cv=StratifiedKFold(10), scoring=scoring)


accuracy_scores = cv_results['test_accuracy']
precision_scores = cv_results['test_precision']
recall_scores = cv_results['test_recall']
f1_scores = cv_results['test_f1']

print("Accuracy: Mean = {:.3f}, Std Dev = {:.3f}".format(accuracy_scores.mean(), accuracy_scores.std()))
print("Precision: Mean = {:.3f}, Std Dev = {:.3f}".format(precision_scores.mean(), precision_scores.std()))
print("Recall: Mean = {:.3f}, Std Dev = {:.3f}".format(recall_scores.mean(), recall_scores.std()))
print("F1-score: Mean = {:.3f}, Std Dev = {:.3f}".format(f1_scores.mean(), f1_scores.std()))

# Calcular as métricas do modelo no conjunto de teste
accuracy = accuracy_score(y_test_reduced, y_pred_reduced)
roc_auc = roc_auc_score(y_test_reduced, y_pred_reduced)
# Para Fake
precision = precision_score(y_test_reduced, y_pred_reduced, pos_label=1)
recall = recall_score(y_test_reduced, y_pred_reduced, pos_label=1)
f1 = f1_score(y_test_reduced, y_pred_reduced, pos_label=1)
# Para Não Fake
precision_h = precision_score(y_test_reduced, y_pred_reduced, pos_label=0)
recall_h = recall_score(y_test_reduced, y_pred_reduced, pos_label=0)
f1_h = f1_score(y_test_reduced, y_pred_reduced, pos_label=0)

print("Best Parameters:", best_params)
print("Accuracy:", accuracy)
print("ROC AUC Score:", roc_auc)

print('--> Fake:')
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

print('--> Para Não Fake:')
print("Precision:", precision_h)
print("Recall:", recall_h)
print("F1-score:", f1_h)
 
# Salvar o modelo treinado com features reduzidas
joblib.dump(best_xgb_model, 'modelo_xgboost_reduced_features_paulo.pkl')
 
# Encontrar as principais features
feature_imp_basic = pd.Series(best_xgb_model.feature_importances_, index=features_for_train).sort_values(ascending=False)
print('Principais features - Modelo com dados básicos do Twitter')
print(feature_imp_basic)
print('+++++++++++++++++++++++++++++++')

# Criar um gráfico de barras
sns.barplot(x=feature_imp_basic, y=feature_imp_basic.index)
# Adicionar rótulos ao gráfico
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features (XGBoost)Modelo com dados básicos do Twitter")
plt.legend()
plt.show()
print('+++++++++++++++++++++++++++++++')
 
# Fechar a conexão com o banco de dados
db.close()

#===============================================================================
# # antes de usar a média do kfold = 10 e desvio padrão
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
# print('--> Para Não Fake:')
# print("Precision:", precision_h)
# print("Recall:", recall_h)
# print("F1-score:", f1_h)
#  
# # Salvar o modelo treinado com features reduzidas
# 
# #joblib.dump(clf_reduced, 'modelo_xgboost_reduced_features_paulo.pkl')
# joblib.dump(best_xgb_model, 'modelo_xgboost_reduced_features_paulo.pkl')
#  
# '''
# Finding Important Features in XGBoost
# '''
# #feature_imp_basic = pd.Series(clf_reduced.feature_importances_,index=features_for_train).sort_values(ascending=False)
# feature_imp_basic = pd.Series(best_xgb_model.feature_importances_, index=features_for_train).sort_values(ascending=False)
# print('Principais features - Modelo com dados básicos do Twitter')
# print(feature_imp_basic)
# print('+++++++++++++++++++++++++++++++')
# 
# 
# # Creating a bar plot
# sns.barplot(x=feature_imp_basic, y=feature_imp_basic.index)
# # Add labels to your graph
# plt.xlabel('Feature Importance Score')
# plt.ylabel('Features')
# plt.title("Visualizing Important Features (XGBoost)Modelo com dados básicos do Twitter")
# plt.legend()
# plt.show()
# print('+++++++++++++++++++++++++++++++')
#  
#  
# # Fechar a conexão com o banco de dados
# db.close()
#===============================================================================