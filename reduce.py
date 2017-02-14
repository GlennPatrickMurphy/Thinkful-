# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:41:28 2017

@author: GlennMurphy
"""

import numpy as np 
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt


Iris=datasets.load_iris()

plt.scatter(Iris.data[:,1],Iris.data[:,2],c=Iris.target)
plt.title('Iris Data' )
plt.show()

#PCA
PCA_Iris=pd.DataFrame(Iris.data, columns=Iris.feature_names)

sklearn_pca=sklearnPCA(n_components=2)
Y_sklearn=sklearn_pca.fit_transform(PCA_Iris)

for x in range(0,150):
    plt.scatter(Y_sklearn[x,0],Y_sklearn[x,1],c=['blue' if Iris.target[x]==0 else 'red' if Iris.target[x]==1 else 'green'] )
plt.title('PCA')
plt.show()

#LDA

LDA_Iris=PCA_Iris
LDA_Target=pd.DataFrame(Iris.target)

sklearn_lda=LDA(n_components=2)
X_sklearn=sklearn_lda.fit_transform(LDA_Iris,LDA_Target)

for x in range(0,150):
    plt.scatter(X_sklearn[x,0],X_sklearn[x,1],c=['blue' if Iris.target[x]==0 else 'red' if Iris.target[x]==1 else 'green'] )
plt.title('LDA')
plt.show()

