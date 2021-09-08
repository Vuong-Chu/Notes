# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:13:51 2021

@author: minhv
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

data = pd.read_csv("C:\\Users\\b5.csv")

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

states = pd.read_csv("C:\\Users\\ClusterData.csv")
states.index = states.iloc[:,1]
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

import pylab as pl
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("C:\\Users\\ccdefault.csv")
ccd = data.iloc[:,1:]
np.random.seed(123456)
test_index = np.random.uniform(0,1,len(ccd)) >= 0.333
train = ccd[test_index == True]
test = ccd[test_index == False]

features = list(train.columns.values)

n = 5
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(train[features],train["DEFAULT"])
predict = clf.predict(test[features])
accurate = np.where(predict == test["DEFAULT"],1,0).sum()/float(len(test))*100
print("Neighbors: {0:d}, Accuracy: {1:2.2f}".format(n,accurate))


from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope

data = pd.read_csv("C:\\AnomalyData.csv")
state_code = data["state_code"]
data = data.loc[:,"data science":"Openness"]

param = "modern dance"
qv1 = data[param].quantile(0.25)
qv3 = data[param].quantile(0.75)
iqv = 1.5*(qv3 - qv1)
outlier_mask = state_code[(data[param]>qv3+iqv) | (data[param]<qv1-iqv)]
outlier_data = data[param][(data[param]>qv3+iqv) | (data[param]<qv1-iqv)]

fig = pl.figure(figsize=(4,6))
ax = fig.add_subplot(1,1,1)
for name, y in zip(outlier_mask, outlier_data):
    ax.text(1,y,name)
ax.boxplot(data[param])
ax.set_ylabel(param)

import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv("C:\\Users\\winequality-red.csv")

x = data.loc[:,:"alcohol"]
y = data["quality"]

scaler = StandardScaler()
x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.333, random_state=1)

lasso = Lasso(alpha=0.001)
lasso.fit(x_train, y_train)

svr = SVR(C=8, epsilon=0.2, gamma=0.5)
svr.fit(x_train, y_train)

#To limit value in a range
y_pred_lasso = np.round(np.clip(lasso.predict(x_test),1,10)).astype(int)
MAE_lasso = np.round(1 - mean_absolute_error(y_test, y_pred_lasso)/y_test.std(),2)

y_pred_svr = np.round(np.clip(svr.predict(x_test),1,10)).astype(int)
MAE_svr = np.round(1 - mean_absolute_error(y_test, y_pred_svr)/y_test.std(),2)






