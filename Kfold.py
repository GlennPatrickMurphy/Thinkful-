# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:11:09 2016

@author: GlennMurphy
"""
import numpy as np
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_value
from math import sqrt
from sklearn.model_selection import KFold

 
loansData= pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData=loansData.reset_index(drop=True)
loansData['Interest_Rate']=map(lambda x:float(x[0:len(x)-1]),loansData['Interest.Rate'])

loansData['Loan_Length']=map(lambda x:float(x[0:len(x)-7]),loansData['Loan.Length'])

loansData['FICO.Score']=map(lambda x:float(str(x).split("-")[0]),loansData['FICO.Range'])

house_ownership = loansData['Home.Ownership']
house_ownership = [4 if x == 'OWN' else 3 if x == 'MORTGAGE' else 2 if x == 'RENT' else 1 if x == 'OTHER' else 0 for x in house_ownership]


X,Y,Z=loansData['Loan_Length'],loansData['FICO.Score'],loansData['Interest_Rate']

#Kfolds

kf=KFold(n_splits=10)


for k,(train,test) in enumerate(kf.split(X,Y,Z)):
    #dependent
    
    y=np.matrix(Z[train]).transpose()
    x1=np.matrix(X[train]).transpose()
    x2=np.matrix(Y[train]).transpose()
    x=np.column_stack([x1,x2])
    t=sm.add_constant(x)
    model=sm.OLS(y,t)
    f=model.fit()
    print f.params
    r1=np.matrix(X[test]).transpose()
    r2=np.matrix(Y[test]).transpose()
    r3=np.column_stack([r1,r2])
    r4=sm.add_constant(r3)
    predict = f.predict(r4)
    print mean_squared_error(Z[test],predict)
   
    