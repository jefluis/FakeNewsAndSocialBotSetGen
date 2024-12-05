# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 01:42:00 2018

@author: Samir Ramos
"""
"""
RandomForest
A subset of observations and a subset of variables are randomly picked to build multiple
independent tree-based models. The trees are more un-correlated as only a subset of
variables are used during the split of the tree, rather than greedily choosing the best split
point in the construction of the tree. See Listing 4-11.
"""

from sklearn.ensemble import RandomForestClassifier
num_trees = 100
clf_RF = RandomForestClassifier(n_estimators=num_trees).fit(X_train, y_train)
results = cross_validation.cross_val_score(clf_RF, X_train, y_train, cv=kfold)
print "\nRandom Forest (Bagging) - Train : ", results.mean()
print "Random Forest (Bagging) - Test : ", metrics.accuracy_score(clf_
RF.predict(X_test), y_test)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

X, y = digit.data, digit.target
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
crossvalidation = KFold(n=X.shape[0], n_folds=3,
shuffle=True, random_state=1)
RF_cls = RandomForestClassifier(n_estimators=300)
score = np.mean(cross_val_score(RF_cls, X, y,
scoring='accuracy', cv=crossvalidation, n_jobs=1))
print 'Accuracy: %.3f' % score
Accuracy: 0.977


"""
Just setting the number of estimators is sufficient for most problems you
encounter, and setting it correctly is a matter of using the highest number
possible given the time and resource constraints of the host computer. You
can demonstrate this by calculating and drawing a validation curve for the
algorithm.
"""


from sklearn.learning_curve import validation_curve
train_scores, test_scores = validation_curve(RF_cls, X, y,
'n_estimators', param_range=[
10,50,100,200,300,500,800,1000,1500],
cv=crossvalidation, scoring='accuracy', n_jobs=1)
print 'mean cv accuracy %s' % np.mean(train_scores,axis=1)
mean cv accuracy [ 0.93600445 0.9738453 0.9771842
0.97607123 0.9738453 0.97774068
0.97885364 0.97774068 0.97885364]