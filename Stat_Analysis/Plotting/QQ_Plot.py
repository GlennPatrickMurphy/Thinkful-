# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:07:10 2016

@author: GlennMurphy
"""

#QQ PLots
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure()
test_data=np.random.normal(size=1000)
graph1 = stats.probplot(test_data,dist="norm",plot=plt)
plt.show()
plt.figure()
test_data2 =np.random.uniform(size=1000)
graph2=stats.probplot(test_data2,dist="norm",plot=plt)
plt.show()

