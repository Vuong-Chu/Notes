# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:13:51 2021

@author: minhv
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

data = pd.read_csv("C:\\Users\\minhv\\Practice\\b5.csv")

X = data.values
scaled_X = scale(X)

pca = PCA()
pca.fit(X)
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))

pca5 = PCA(n_components=5)
pca5.fit(X)
Percentage_of_variance = pca5.explained_variance_ratio_
Factor_score_coefficient = pca5.components_

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

states = pd.read_csv("C:\\Users\\minhv\\Practice\\ClusterData.csv")
z = linkage(states.iloc[:,2:],"ward")
index = states.iloc[:,1]

plt.figure(figsize = (25,10))
plt.title('Cluster with All Searches and Personality')
plt.ylabel('distance')
dendrogram(
    z,
    labels=index,
    leaf_rotation=0.,
    leaf_font_size=18.
    )
plt.show()

