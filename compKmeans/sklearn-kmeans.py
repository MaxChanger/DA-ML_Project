#############K-means-鸢尾花聚类############
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
#from sklearn import datasets
from sklearn.datasets import load_iris
from utils import *

iris = load_iris()
X = iris.data[:] 

estimator = KMeans(n_clusters=3,max_iter=1000,tol=1e-10)    #构造聚类器
estimator.fit(X)    #聚类
label_pred = estimator.labels_  #获取聚类标签
centers_pred = estimator.cluster_centers_   # 聚类中心

#绘制k-means结果
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]

plt.scatter(x0[:, 0], x0[:, 1], c = "red", marker='^', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c = "green", marker='o', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c = "blue", marker='*', label='label2')

centroidsX, centroidsY = getXY(centers_pred)

plt.scatter(centroidsX, centroidsY, s=100, c='black', marker='+', alpha=1)  # 画出质心点
plt.title("sklearn.cluster K-means")
plt.xlabel('X Label')
plt.ylabel('y Label')
plt.legend(loc=2)
plt.show()