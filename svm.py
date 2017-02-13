# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:53:38 2017

@author: GlennMurphy
"""

from sklearn import datasets
from sklearn import svm
from matplotlib.colors import ListedColormap
import numpy as np 

iris = datasets.load_iris()

import matplotlib.pyplot as plt
plt.scatter(iris.data[:, 1], iris.data[:, 2], c=iris.target)
plt.xlabel(iris.feature_names[1])
plt.ylabel(iris.feature_names[2])

#The first 100 observations correspond to setosa and versicolor
plt.scatter(iris.data[0:150, 1], iris.data[0:150, 2], c=iris.target[0:150])
plt.xlabel(iris.feature_names[1])
plt.ylabel(iris.feature_names[2])



svc = svm.SVC(kernel='linear',C=1)

X = iris.data[0:150, 1:3]
y = iris.target[0:150]
svc.fit(X, y)

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

def plot_estimator(estimator, X, y):
    estimator.fit(X, y)
    x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = estimator.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.axis('tight')
    plt.axis('off')
    plt.tight_layout()

plot_estimator(svc, X, y)