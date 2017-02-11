# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:11:08 2017

@author: GlennMurphy
"""
import numpy as np 
from operator import itemgetter
import math
import scipy.cluster.vq as sc
import pandas as pd 
import matplotlib.pyplot as plt


def dist(array,X,Y):
    distance=[math.sqrt((array[a][0]-X)**2+(array[a][1]-Y)**2) for a in range(0,len(array))]  
    return min(enumerate(distance), key=itemgetter(1))[0] 

  
df=pd.read_csv('http://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/un/un.csv')
for x in ['GDPperCapita','lifeMale','lifeFemale','infantMortality']:
    df=df[np.isfinite(df[x])]
    if x=='GDPperCapita':
        continue
    array=sc.kmeans(df[['GDPperCapita',x]],3)
    Data=df[['GDPperCapita',x]]
    string=x+'group'
    df[string]=[dist(array[0],Data.loc[t,'GDPperCapita'],Data.loc[t,x]) for t in Data.index]

plt.scatter(df['GDPperCapita'],df['lifeMale'],color=['b' if x==0 else 'g' if x==1 else 'm' for x in df['lifeMalegroup']])
plt.xlabel('GDPperCapita')
plt.ylabel('Life Male')
plt.figure()
plt.scatter(df['GDPperCapita'],df['lifeFemale'],color=['b' if x==0 else 'g' if x==1 else 'm' for x in df['lifeFemalegroup']])
plt.xlabel('GDPperCapita')
plt.ylabel('lifeFemale')
plt.figure()
plt.scatter(df['GDPperCapita'],df['infantMortality'],color=['b' if x==0 else 'g' if x==1 else 'm' for x in df['infantMortalitygroup']])
plt.xlabel('GDPperCapita')
plt.ylabel('infantMortality')
plt.figure()
