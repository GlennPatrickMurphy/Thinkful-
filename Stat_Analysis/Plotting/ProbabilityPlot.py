# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 23:05:21 2016

@author: GlennMurphy
"""

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.mlab as mlab 

mean = 0 
variance =1 
sigma = np.sqrt(variance)

x= np.linspace(-3,3,100)

plt.plot(x,mlab.normpdf(x,mean,sigma))
plt.show()
