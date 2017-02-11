# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:11:08 2017

@author: GlennMurphy
"""
import numpy as np 

import math
import scipy.cluster.vq as sc
import pandas as pd 
import matplotlib.pyplot as plt


def dist(array,X,Y):
    if len(array)==1:
        return math.sqrt((array[0][0]-X)**2+(array[0][1]-Y)**2)
    distance=[math.sqrt((array[a][0]-X)**2+(array[a][1]-Y)**2) for a in range(0,len(array)-1)]
    return min(distance)

  
df=pd.read_csv('http://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/un/un.csv')
df['distance']=0
Average=[0,0,0,0,0,0,0,0,0,0]
for x in ['GDPperCapita','lifeMale','lifeFemale','infantMortality']:
    df=df[np.isfinite(df[x])]
    if x=='GDPperCapita':
        continue
    for k in range(1,11):
        array=sc.kmeans(df[['GDPperCapita',x]],k)
        Data=df[['GDPperCapita',x]]
        df['distance']=[dist(array[0],Data.loc[t,'GDPperCapita'],Data.loc[t,x]) for t in Data.index]
        Average[k-1]=df['distance'].mean()
        
k=[1,2,3,4,5,6,7,8,9,10]        
plt.scatter(k,Average)
plt.xlabel('Number of Centrodes')
plt.ylabel('Mean Distance')
