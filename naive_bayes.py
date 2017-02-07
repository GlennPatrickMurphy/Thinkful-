# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:37:29 2017

@author: GlennMurphy
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

df= pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/ideal-weight/ideal_weight.csv',header=0,names=['id','sex','actual','ideal','diff'])

df['sex']=map(lambda x:x[1:len(x)-1],df['sex'])
df['sex']=[1 if x=='Male' else 0 for x in df['sex']]

plt.title('Weight vs Ideal')
plt.xlabel('Weight')
plt.ylabel('People')
plt.hist(df['actual'],fc=(0,0,1,0.5),label=['Actual'])
plt.hist(df['ideal'],fc=(1,0,0,0.5),label=['Ideal'])
plt.legend()
plt.figure()

plt.title('Difference in Actual vs Ideal Weight')
plt.xlabel('Weight')
plt.ylabel('People')
plt.hist(df['diff'])

X_Train=df[['ideal','actual','diff']]
Y_Train=df['sex']
gnb=GaussianNB()
ypred=gnb.fit(X_Train,Y_Train).predict(X_Train)
print("Number of mislabeled points out of a total %d points : %d" % (X_Train.shape[0],(Y_Train != ypred).sum()))
Case1=gnb.predict(pd.DataFrame([[130,160,-20]],columns=['actual','ideal','diff'])).tolist()
Case2=gnb.predict(pd.DataFrame([[160,145,15]],columns=['actual','ideal','diff'])).tolist()
print Case1,Case2