# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 01:13:13 2018
Experimento retirado de : https://www.datacamp.com/community/tutorials/random-forests-classifier-python
@author: Samir Ramos
"""

import pymysql

import pandas as pd
import datetime as dt
#from datetime import timezone

# FUNÇÕES

def ConvertDatetimetoTimestamp (date_time):
    timestamp = dt.datetime.timestamp(date_time)
    return (timestamp)


#CARREGANDO O DATASET
# Criando um objeto de conexão com o bd
db = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'ime',  autocommit=True)

# Criando objetos cursor
cursor_randomforest = db.cursor()
cursor2_randomforest = db.cursor()
    
# Montando SQL statements 
sql_accounts = 'SELECT * FROM accounts'
#sql2_accounts = 'SELECT UserID, CreatedAt, CollectedAt, NumberOfFollowings, NumberOfFollowers, NumberOfTweets, LengthOfScreenName, LenDescrInUseProf, Update_Control, Type FROM accounts'
sql2_accounts = 'SELECT UserID, CreatedAt, NumberOfFollowings, NumberOfFollowers, NumberOfTweets, LengthOfScreenName, LenDescrInUseProf, Update_Control, Type FROM accounts'
  
# Interação inicial com o banco de dados 
cursor_randomforest.execute(sql_accounts)
datas = cursor_randomforest.fetchall()  

cursor2_randomforest.execute(sql2_accounts)
datas2 = cursor2_randomforest.fetchall()   

print(datas)
print(datas2)

#Alterando tupla de cada conta (convertendo datetimes em timestamps)
n=0
lista_posix_dates = []
for tupla in datas:
    n = n + 1
    newtupla = tupla
    a1 = ConvertDatetimetoTimestamp(tupla[1])
    a2 = ConvertDatetimetoTimestamp(tupla[2])
    # Como não podemos modificar os elementos de uma tupla, devemos substituí-la por uma tupla diferente
    newtupla = (tupla[0], a1, a2) + tupla[3:]
    lista_posix_dates.append(newtupla)
print(lista_posix_dates)
print('Número de usuários =',n) 

#2 Alterando tupla de cada conta (convertendo datetimes em timestamps)
m=0
lista2_posix_dates = []
for tupla2 in datas2:
    m = m + 1
    newtupla2 = tupla2
    b1 = ConvertDatetimetoTimestamp(tupla2[1])
    #b2 = ConvertDatetimetoTimestamp(tupla2[2])
    # Como não podemos modificar os elementos de uma tupla, devemos substituí-la por uma tupla diferente
    newtupla2 = (tupla2[0], b1) + tupla2[2:]
    lista2_posix_dates.append(newtupla2)
print(lista2_posix_dates)
print('Número de usuários =',m) 



# Importando o módulo numpy
import numpy as np

# Construindo o array "dados"
dados = np.array(lista_posix_dates)
dados2 = np.array(lista2_posix_dates)

# Printando o array "dados"
print(dados)
print(dados2)
# Printando o número de dimensões do array "dados"
print('Número dimensões do array dados =',dados.ndim)
print('Número dimensões do array dados2 =',dados2.ndim)
# Printando o número de elementos do array "dados"
print('Número elementos do array dados =',dados.size)
print('Número elementos do array dados2 =',dados2.size)
# Printando o comprimento do array "dados"
print('comprimento do array "dados" =',len(dados))
print('comprimento do array "dados2" =',len(dados2))


# Criando um DataFrame de um dado dataset (no caso, um numpy array da lista modificada de tuplas)
data=pd.DataFrame({
    'CreatedAt':dados[:,1],
   # 'CollectedAt':dados[:,2],
    'NumberOfFollowings':dados[:,3],
    'NumberOfFollowers':dados[:,4],    
    'NumberOfTweets':dados[:,5],
    'LengthOfScreenName':dados[:,6],
    'LenDescrInUseProf':dados[:,7],    
    'V_media':dados[:,8],
    'A_media':dados[:,9],
    'D_media':dados[:,10],
    'V_1quartil':dados[:,11],
    'A_1quartil':dados[:,12],
    'D_1quartil':dados[:,13],    
    'V_mediana':dados[:,14],
    'A_mediana':dados[:,15],
    'D_mediana':dados[:,16],    
    'V_3quartil':dados[:,17],
    'A_3quartil':dados[:,18],
    'D_3quartil':dados[:,19],    
    'V_desviopadrao':dados[:,20],
    'A_desviopadrao':dados[:,21],
    'D_desviopadrao':dados[:,22],
    'V_amplitude':dados[:,23],
    'A_amplitude':dados[:,24],
    'D_amplitude':dados[:,25],
    'Type':dados[:,27],
})
data.head()

# Criando um DataFrame de um dado dataset (no caso, um numpy array da lista modificada de tuplas)
data2=pd.DataFrame({
    'CreatedAt':dados2[:,1],
   # 'CollectedAt':dados2[:,2],
    'NumberOfFollowings':dados2[:,2],
    'NumberOfFollowers':dados2[:,3],    
    'NumberOfTweets':dados2[:,4],
    'LengthOfScreenName':dados2[:,5],
    'LenDescrInUseProf':dados2[:,6],    
    'Type':dados2[:,8],
})
data2.head()


# Import train_test_split function
from sklearn.model_selection import train_test_split
#'CollectedAt'
X=data[['CreatedAt','NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProf', 'V_media', 'A_media', 'D_media', 'V_1quartil', 'A_1quartil', 'D_1quartil', 'V_mediana', 'A_mediana', 'D_mediana', 'V_3quartil', 'A_3quartil', 'D_3quartil', 'V_desviopadrao', 'A_desviopadrao', 'D_desviopadrao', 'V_amplitude', 'A_amplitude', 'D_amplitude']]  # Features
X2=data2[['CreatedAt','NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProf']]  # Features
y=data['Type']  # Labels
y2=data2['Type']  # Labels

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # 70% training and 30% test
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2) # 70% training and 30% test
#After splitting, you will train the model on the training set and perform predictions on the test set.

#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)
clf2=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)
clf2.fit(X2_train,y2_train)

y_pred=clf.predict(X_test)
y2_pred=clf2.predict(X2_test)

#After training, check the accuracy using actual and predicted values.

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?

print("Accuracy with +18 features =",metrics.accuracy_score(y_test, y_pred))
print("Accuracy without 18 features =:",metrics.accuracy_score(y2_test, y2_pred))


"""
Finding Important Features in Scikit-learn
Here, you are finding important features or selecting features in the IRIS dataset. In scikit-learn, you can perform this task in the following steps:

First, you need to create a random forests model.
Second, use the feature importance variable to see feature importance scores.
Third, visualize these scores using the seaborn library.
"""
from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)
clf2=RandomForestClassifier(n_estimators=100)
#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)


##A random forest classifier.
#Fonte: http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
#A random forest is a meta estimator that fits a number of decision tree classifiers 
#on various sub-samples of the dataset and use averaging to improve the predictive accuracy 
#and control over-fitting. The sub-sample size is always the same as the original input sample size
#but the samples are drawn with replacement if bootstrap=True (default).

#2Train the model using the training sets y_pred=clf.predict(X_test)
clf2.fit(X2_train,y2_train)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)


import pandas as pd
#'CollectedAt',
feature_names = ['CreatedAt','NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProf', 'V_media', 'A_media', 'D_media', 'V_1quartil', 'A_1quartil', 'D_1quartil', 'V_mediana', 'A_mediana', 'D_mediana', 'V_3quartil', 'A_3quartil', 'D_3quartil', 'V_desviopadrao', 'A_desviopadrao', 'D_desviopadrao', 'V_amplitude', 'A_amplitude', 'D_amplitude']
feature2_names = ['CreatedAt','NumberOfFollowings', 'NumberOfFollowers', 'NumberOfTweets', 'LengthOfScreenName', 'LenDescrInUseProf']

feature_imp = pd.Series(clf.feature_importances_,index=feature_names).sort_values(ascending=False)
feature2_imp = pd.Series(clf2.feature_importances_,index=feature2_names).sort_values(ascending=False)
print(feature_imp)
print('+++++++++++++++++++++++++++++++')
print(feature2_imp)


#You can also visualize the feature importance. Visualizations are easy to understand and interpretable.

#For visualization, you can use a combination of matplotlib and seaborn. Because seaborn is built on top of matplotlib, it offers a number of customized themes and provides additional plot types. Matplotlib is a superset of seaborn and both are equally important for good visualizations.

import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
get_ipython().magic('matplotlib inline')
# Creating a bar plot
sns.barplot(x=feature_imp, y=feature_imp.index)
# Add labels to your graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.legend()
plt.show()
print('+++++++++++++++++++++++++++++++')
# Creating a bar plot
sns.barplot(x=feature2_imp, y=feature2_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.legend()
plt.show()


"""
Generating the Model on Selected Features
Here, you can remove the "sepal width" feature because it has very low importance, and select the 3 remaining features.

# Import train_test_split function
from sklearn.cross_validation import train_test_split
# Split dataset into features and labels
X=data[['petal length', 'petal width','sepal length']]  # Removed feature "sepal length"
y=data['species']                                       
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.70, random_state=5) # 70% training and 30% test
#After spliting, you will generate a model on the selected training set features, perform predictions on the selected test set features, and compare actual and predicted values.

from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

# prediction on test set
y_pred=clf.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

('Accuracy:', 0.95238095238095233)

You can see that after removing the least important features (sepal length), the accuracy increased. 
This is because you removed misleading data and noise, resulting in an increased accuracy. 
A lesser amount of features also reduces the training time.

Conclusion
Congratulations, you have made it to the end of this tutorial!

In this tutorial, you have learned what random forests is, how it works, finding important features, 
the comparison between random forests and decision trees, advantages and disadvantages. 
You have also learned model building, evaluation and finding important features in scikit-learn. B

If you would like to learn more about machine learning, I recommend you take a look at our 
Supervised Learning in R: Classification course.
"""








