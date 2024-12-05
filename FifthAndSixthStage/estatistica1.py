# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 01:10:50 2018

@author: Samir Ramos
"""

import pandas as pd
import matplotlib.pyplot as plt


 # Select the updated row and print the updated column value through a function
def sqlUpdateQuery (z):        
                
    return ("SELECT * FROM teste_tweets WHERE Tweet_ID = "+ str(z))         

#A DataFrame is a two-dimensional labeled data structure
#with columns of potentially different types. You can think of it like 
#a spreadsheet or SQL table. DataFrames are the most commonly used pandas
#objects.
    
data = pd.DataFrame({
'
})
    
    
t = (0,10,0.1)
x = (t)
y = (t)
df = pd.DataFrame({'Time':t, 'x':x, 'y':y})  
    
    
    
    
    
"""
data = pd.DataFrame({
'Gender': ['f', 'f', 'm', 'f', 'm',
'm', 'f', 'm', 'f', 'm', 'm'],
'TV': [3.4, 3.5, 2.6, 4.7, 4.1, 4.1,
5.1, 3.9, 3.7, 2.1, 4.3]
})
"""

  
    # Group the data
grouped = data.groupby('Gender')
# Do some overview statistics
print(grouped.describe())
# Plot the data:
grouped.boxplot()
plt.show()
#--------------------------------------------
# Get the groups as DataFrames
df_female = grouped.get_group('f')
# Get the corresponding numpy-array
values_female = grouped.get_group('f').values