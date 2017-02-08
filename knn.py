# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:02:57 2017

@author: GlennMurphy
"""
import numpy as np
import math 
import pandas as pd 
import matplotlib.pyplot as plt

def KNN(K):
    df['distance']=map(lambda a,b:math.sqrt((a-X)**2+(b-Y)**2),df['Sepal_Length'],df['Sepal_Width'])
    N=df['distance'].sort_values()[0:K].index
    Classes=df.loc[N,'Class'].value_counts()
    return Classes


df=pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/iris/iris.data.csv',names=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class'])
df['Class']=map(lambda x:x[5:len(x)],df['Class'])
plt.scatter(df['Sepal_Length'],df['Sepal_Width'],c=[1,0,0,1])

X=np.random.randint(4,7)+np.random.random([1])
Y=np.random.randint(2,4)+np.random.random([1])
K=10
Val=KNN(K).sort_values(ascending=False)
Class=Val.index.values[1]
print "\n The majority class with K={0} is {1}".format(K,Class)



plt.scatter(X,Y,c=[0 , 0 , 1, 1])