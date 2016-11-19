# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 13:52:42 2016

@author: GlennMurphy
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm 
import matplotlib.pyplot as scatter

#pulling in the data
loansData= pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

#making interest rate into a float 

def AddOne(x):
    
    return 1
    
def funownership(x):
    if x == 'MORTGAGE':      
        return 2
    if x=='RENT':
        return 3
    if x=='OWN':
        return 4
    if x=='OTHER':
        return 1
    return 1 
    

#creating a y intercept

loansData['Intercept']=map(AddOne,loansData['Interest.Rate'])
loansData['Ownership_Col']=map(funownership,loansData['Home.Ownership'])
#creating a row for annual income base off monthly 
loansData['annual_inc']=map(lambda x: float(x*12), loansData['Monthly.Income'])
#making a datafram 
loansData['Interest_Rate']=map(lambda x:float(x[0:len(x)-1]),loansData['Interest.Rate'])
df=pd.DataFrame(loansData)

 #interest rate = annual income * coefficient + house ownership * coefficient + intercept

InterestRate=loansData['Interest_Rate']
AnnualInc=loansData['annual_inc']
AnnualInc[np.isnan(AnnualInc)] = 0
Ownership=loansData['Ownership_Col']


#Dependant Variable
y=np.matrix(InterestRate).transpose()

#Independent variables 
x1=np.matrix(AnnualInc).transpose()
x2=np.matrix(Ownership).transpose()
#x3=np.matrix(AnnualInc*Ownership).transpose()

#put the columns together
x=np.column_stack([x1,x2])

#creating model
X=sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

f.summary()


scatter
#scatter(df['Ownership'],df['Interest_Rate'])

#xlabel('Home Ownership')
#ylabel('interest rate')
#title('Ownership vs annual income')
#show()