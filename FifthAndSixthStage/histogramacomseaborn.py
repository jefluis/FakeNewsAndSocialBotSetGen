# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 23:01:00 2018

@author: Samir Ramos
"""

#obtendo os dados
import pandas as pd
df_swing = pd.read_csv('nome do arquivo csv')
# se quiser ver como ficou
df_swing[['coluna A', 'coluna B', 'coluna X']]

# Para fazer um histograma de dados do dataset, usamos a seguinte biblioteca como funcao 
import matplotlib.ppyplot as plt
# agora passamos a coluna dem_share do Dataframe. 
# A variável 'underscore' é muito usada em Python como variável dummie.
_ = plt.hist(df_swing['dem_share'])
#uma laternativa é usar um Numpy array com os mesmos dados
# _ = plt.xlabel ('percent of vote for Obama')
# _ = plt.ylabel ('number of counties')
# sempre ponha nome em seus eixos
#mostrando o resultado
plt.show()
#note que o plt.hist retorna arrays que não estamos interessados. O foco é o plot.

#Podemos progarmar as caixas (bins) dos eixos do histograma
bin_edges = [0,10,20,30,40,50,60,70,80,90,100]
_ = plt.hist(df_swing['dem_share'], bin = bin_edges)
#ou o usar o bins default do plt.hist 
plt.show()
#Usando a palavra chave bins podemos especificar o número de bins que queremos
#  e o Matplotlib irá gerar o numerode bins espaçados que pedimos
_ = plt.hist(df_swing['dem_share'], bin = 20)
plt.show()
# Melhor é usar os default settings do Seaborn, 
# um excelente pacote de visualozaçãp de dados estat´siticos 
# MatPlotlib=based, criado por Michael Waskom
import seaborn as sns
sns.set()
_ = plt.hist(df_swing['dem_share'])
_ = plt.xlabel ('percent of vote for Obama')
_ = plt.ylabel ('number of counties')
plt.show()
# para usar bee swarm plot
_ = sns.swarmplot(x='state', y='dem_share', data=df_swing)
_ = plt.xlabel('state')
_ = plt.ylabel('percent of vote for Obama')
plt.show()



