# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:53:38 2017

@author: GlennMurphy
"""

from sklearn import datasets
from sklearn import svm
from sklearn.cross_validation import KFold
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()

X=iris.data
target=iris.target


svc = svm.SVC(kernel='linear',C=1)

skf= KFold(len(X),n_folds=5)

#Kfolds

for train_index, test_index in skf:
    model = svc.fit(X[train_index], target[train_index])
    
val=cross_val_score(model,X,target,cv=skf,n_jobs=1)
print val 

print val.mean()
print val.std()

