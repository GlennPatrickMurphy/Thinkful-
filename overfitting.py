# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 21:16:05 2017

@author: GlennMurphy
"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error
from math import sqrt


# Set seed for reproducible results
np.random.seed(414)

# Gen toy data
X = np.linspace(0, 15, 1000)
y = 3 * np.sin(X) + np.random.normal(1 + X, .2, 1000)

train_X, train_y = X[:700], y[:700]
test_X, test_y = X[700:], y[700:]

train_df = pd.DataFrame({'X': train_X, 'y': train_y})
test_df = pd.DataFrame({'X': test_X, 'y': test_y})

# Linear Fit
poly_1 = smf.ols(formula='y ~ 1 + X', data=train_df).fit()

# Quadratic Fit
poly_2 = smf.ols(formula='y ~ 1 + X + I(X**2)', data=train_df).fit()

def Poly1(x):
    return poly_1.params['Intercept']+poly_1.params['X']*x
    
    
test_df['Linear']=map(Poly1,test_df['X'])


def Poly2(x):
    return poly_2.params['Intercept']+(poly_2.params['X']*x)+((poly_2.params['I(X ** 2)'])*(x**2))
    
test_df['Quad']=map(Poly2,test_df['X'])

rms_Linear = sqrt(mean_squared_error(test_df['y'],test_df['Linear']))

print rms_Linear

rms_Quad = sqrt(mean_squared_error(test_df['y'],test_df['Quad']))

print rms_Quad



plt.plot(test_df['X'],test_df['y'],'r',test_df['X'],test_df['Linear'],'b',test_df['X'],test_df['Quad'],'g')

