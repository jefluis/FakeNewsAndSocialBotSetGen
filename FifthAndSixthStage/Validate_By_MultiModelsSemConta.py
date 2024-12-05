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
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE, ADASYN
import pickle
import warnings
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score, roc_auc_score
from collections import Counter

# Suprimir avisos de futuras mudanças
warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn")

# FUNÇÕES
def execute_query(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

# Inicializo as listas de features
full_feature_names = ['labelnews', 'TweetCount', 'ReTweetCount', 
    'favorite_count', 'alternativeName', 'total_users',
    'total_users_type_1','total_users_type_0']

features_for_train_semConta = ['TweetCount', 'ReTweetCount', 
    'favorite_count']
    
sql_accounts = '''SELECT 
    t.labelednewsId as labelnews, 
    COUNT(t.TweetID) AS TweetCount, 
    SUM(t.retweet_count) AS ReTweetCount, 
    SUM(t.favorite_count) AS favorite_count, 
    l.alternativeName as alternativeName,
    COUNT(u.type) AS total_users,    
    SUM(CASE WHEN u.type = 1 THEN 1 ELSE 0 END) AS total_users_type_1,
    SUM(CASE WHEN u.type = 0 THEN 1 ELSE 0 END) AS total_users_type_0
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

# Criar DataFrame com os dados
data_df = pd.DataFrame(datas, columns=full_feature_names)
data_df[['ReTweetCount', 'favorite_count', 'TweetCount']] = data_df[['ReTweetCount', 'favorite_count', 'TweetCount']].astype(int)

# Variável target
y = np.where(data_df['alternativeName'].str.strip() == 'VERDADEIRO', 0, 1)

# Dividir os dados em treino e teste
X_SemConta = data_df[features_for_train_semConta]
X_train, X_test, y_train, y_test = train_test_split(X_SemConta, y, test_size=0.2, random_state=42)

# Verificar a distribuição das classes
print("Distribuição original das classes em y_train:")
print(pd.Series(y_train).value_counts())

# SMOTE
smote = SMOTE(
    sampling_strategy='minority',  # Ajusta para o número de amostras da classe majoritária
    k_neighbors=5,
    n_jobs=-1,
    random_state=42
)
#X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Verifique o novo balanceamento
print("Distribuição das classes após SMOTE:")
print(Counter(y_train_resampled))

# Tentar ADASYN para balanceamento de classes
# Aplicar ADASYN
#adasyn = ADASYN(sampling_strategy='auto', random_state=42)
#print("Tentando ajustar ADASYN...")
#X_train_resampled, y_train_resampled = adasyn.fit_resample(X_train, y_train)

print("Distribuição das classes após resampling:")
print(pd.Series(y_train_resampled).value_counts())



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
            max_iter=500,
            learning_rate_init=0.01,
            early_stopping=True,
            validation_fraction=0.1,
            n_iter_no_change=10
        ),
        'params': {'model__hidden_layer_sizes': [(50,), (100,), (50, 50)], 'model__activation': ['tanh', 'relu']}
    }
}

print("SEM CONTA")
# Treinar e avaliar modelos com validação cruzada e Grid Search
results = []
for model_name, mp in models_params.items():
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', mp['model'])
    ])
    
    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    grid_search = GridSearchCV(pipeline, mp['params'], cv=cv, scoring='accuracy')

    # Registrar o tempo de início
    start_time = time.time()
    print(f"Modelo: {model_name}")
    print(f"Start Time (seconds): {start_time:.2f}")
    
    # Treinar o modelo
    grid_search.fit(X_train_resampled, y_train_resampled)
    
    # Registrar o tempo de término
    end_time = time.time()
    print(f"End Time (seconds): {end_time:.2f}")
    
    # Calcular o tempo de treinamento
    training_time = end_time - start_time
    print(f"Training Time (seconds): {training_time:.2f}")
    
    # Melhor modelo e suas previsões
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    
    # Avaliar modelo
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)

    print("Distribuição de classes no conjunto de teste:")
    print(pd.Series(y_test).value_counts())
    print("\nDistribuição de classes nas previsões:")
    print(pd.Series(y_pred).value_counts())

    num_Fake = np.count_nonzero(y_train_resampled == 1)
    num_NaoFake = np.count_nonzero(y_train_resampled == 0)
    positive_class_weight = num_NaoFake / max(num_Fake, 1)
    
    print("Number of positive samples:", num_Fake)
    print("Number of negative samples:", num_NaoFake)
    print("Positive class weight:", positive_class_weight)
    
    # Display feature importances if applicable
    if hasattr(best_model.named_steps['model'], 'feature_importances_'):
        importances = best_model.named_steps['model'].feature_importances_
        feature_importances = pd.DataFrame(importances, index=X_train_resampled.columns, columns=['Importance']).sort_values(by='Importance', ascending=False)
        print("Feature Importances:")
        print(feature_importances)

    # Realizar validação cruzada para métricas com desvio padrão
    cv_accuracy = cross_val_score(best_model, X_train_resampled, y_train_resampled, cv=cv, scoring='accuracy')
    cv_precision = cross_val_score(best_model, X_train_resampled, y_train_resampled, cv=cv, scoring='precision_macro')
    cv_recall = cross_val_score(best_model, X_train_resampled, y_train_resampled, cv=cv, scoring='recall_macro')
    cv_f1 = cross_val_score(best_model, X_train_resampled, y_train_resampled, cv=cv, scoring='f1_macro')
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
        'Training Time (seconds)': training_time
    })
    
    # Salvar o melhor modelo em um arquivo pickle
    with open(f'{model_name}_best_model_without_bot.pkl', 'wb') as f:
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
        
    print("-" * 80)
# Fechar a conexão com o banco de dados
db.close()



