# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:12:53 2017

@author: GlennMurphy
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import sklearn.cross_validation as cv

Column_Headers=pd.read_csv('UCI HAR Dataset/UCI HAR Dataset/features.txt',sep='\s+', engine='python',names=list('ab'))

#Fixing Column Headers

Data=pd.read_csv('UCI HAR Dataset/UCI HAR Dataset/train/X_train.txt',sep='\s+',names=Column_Headers['b'])
Subject_Data=pd.read_csv('UCI HAR Dataset/UCI HAR Dataset/train/subject_train.txt')
Activity=pd.read_csv('UCI HAR Dataset/UCI HAR Dataset/train/Y_train.txt', names=['activity'])

Data['Subject']=Subject_Data
Activity['Subject']=Subject_Data

TrainData=Data[Data['Subject']>= 27]
Activity=Activity[Activity['Subject']>=27]



X_test=pd.read_csv('UCI HAR Dataset/UCI HAR Dataset/test/X_test.txt',sep='\s+',names=Column_Headers['b'])
Subject_test=pd.read_csv('UCI HAR Dataset/UCI HAR Dataset/test/subject_test.txt')
Activity_test=pd.read_csv('UCI HAR Dataset/UCI HAR Dataset/test/Y_test.txt', names=['activity'])

X_test['Subject']=Subject_test
Activity_test['Subject']=Subject_test

Val_Data=X_test[(X_test['Subject']>=21)&(X_test['Subject']<=27)]
ValActivity_test=Activity_test[(Activity_test['Subject']>=21)&(Activity_test['Subject']<=27)]

TestData=X_test[X_test['Subject']<= 6]
Activity_test=Activity_test[Activity_test['Subject']<=6]
#random forest 

clf=RandomForestClassifier(n_estimators=500)
clf.fit(TrainData,Activity['activity'])

preds=clf.predict(TestData)

# determining the importance of the feature
feature_table={'Column Names': Column_Headers['b'],'Feature Importance':clf.feature_importances_[:561]}
features=pd.DataFrame(feature_table,columns=['Column Names','Feature Importance'])
print features.sort_values(by='Feature Importance',ascending=False)[0:10]



print clf.score(TestData,Activity_test['activity'])
print cv.cross_val_score(clf, Val_Data, ValActivity_test['activity'], scoring='accuracy', cv=10)
print pd.crosstab(Activity_test['activity'],preds,rownames=['Actual'],colnames=['preds'])

