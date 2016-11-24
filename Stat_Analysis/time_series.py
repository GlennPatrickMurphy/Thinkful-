# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:38:52 2016

@author: GlennMurphy
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt



df = pd.read_csv('LoanStats3b.csv',header=1,low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']
lcs_log= np.log(loan_count_summary)
#Fixing Axis 
fig,(ax1,ax2)=plt.subplots(1,2,sharey=True)

#plotting rolling mean and variance 

rolmean=pd.rolling_mean(loan_count_summary,1)
rolstd=pd.rolling_std(loan_count_summary,2)

ax1.bar(loan_count_summary.index,loan_count_summary)
#mean=plt.plot(rolmean, color='red')
#std=plt.plot(rolstd, color='black')

ax2.bar(loan_count_summary.index,loan_count_summary)
mean=plt.plot(rolmean, color='red')
std=plt.plot(rolstd, color='black')

ax1.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.yaxis.tick_right()
ax2.tick_params(labelleft='off')
ax1.set_xlim(201201, 201212)
ax2.set_xlim(201301, 201312)



#ACF
sm.graphics.tsa.plot_acf(loan_count_summary)

#PACF
sm.graphics.tsa.plot_pacf(loan_count_summary)
