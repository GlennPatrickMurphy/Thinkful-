# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 14:39:22 2016

@author: GlennMurphy
"""

import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.show()
plt.savefig("BoxPlot.png")
plt.hist(x,histtype='bar')
plt.show()