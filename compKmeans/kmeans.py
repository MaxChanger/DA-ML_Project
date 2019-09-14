#########################################
# 2019-08-31 Jiadai Sun
# sunjiadai@foxmail.com
# 
# python .\kmeans.py --n_iteration 100 --n_clusters 4
# 
#########################################
from collections import defaultdict
from random import uniform
from math import sqrt
import matplotlib.pyplot as plt  
from sklearn.datasets import load_iris
from utils import *
import argparse

def point_avg(points):
    """ 求点集的平均坐标点 """

    dimensions = len(points[0])
    new_center = []

    for dimension in range(dimensions):
        dim_sum = 0  # dimension sum
        for p in points:
            dim_sum += p[dimension]     # 欧式距离
        new_center.append(dim_sum / float(len(points))) # 第一个维度的均值, 第二个维度的均值 average of each dimension
    # print(new_center)
    return new_center


def update_centers(data_set, label_preds):
    ''' 更新中心点的坐标 '''
    new_means = defaultdict(list)   # 构建一个默认value为list的字典 key为label value为一个Point List
    centers = []
    for label_pred, point in zip(label_preds, data_set):
        new_means[label_pred].append(point)

    for _, points in new_means.items():
        centers.append(point_avg(points))

    return centers

def distance(a, b):
    ''' 求两个点之间的距离 '''
    dimensions = len(a) # 二维的就是 x y    
    _sum = 0
    for dimension in range(dimensions):
        _df = (a[dimension] - b[dimension]) ** 2
        _sum += _df
    return sqrt(_sum)

def assign_points(data_points, centers):
    ''' 为所有点设置label '''
    label_pred = []
    for point in data_points:    # 遍历所有的点
        shortest = float("inf")  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):   # 找到距离最近的的中心点
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        label_pred.append(shortest_index)   # 为每一个点指定中心点的label
    return label_pred


def generate_k(data_set, n_clusters):
    """ 计算每个维度的min和max 然后生成其中间的随机数    """
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)

    for point in data_set:
        for i in range(dimensions):
            val = point[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for _k in range(n_clusters):
        rand_point = []
        for i in range(dimensions):
            min_val = min_max['min_%d' % i]
            max_val = min_max['max_%d' % i]
            
            rand_point.append(uniform(min_val, max_val))

        centers.append(rand_point)

    return centers



def k_means(dataset, n_clusters, n_iteration):
    k_points = generate_k(dataset, n_clusters)   # 随机生成中心

    label_preds = assign_points(dataset, k_points)
    
    old_labels = None
    # while label_preds != old_labels:
    #     new_centers = update_centers(dataset, label_preds)
    #     old_labels = label_preds
    #     label_preds = assign_points(dataset, new_centers)
    
    for i in range(n_iteration):
        if label_preds == old_labels:
            print('stop at {0}th_iteration'.format('%d'%i))
            break
        new_centers = update_centers(dataset, label_preds)
        old_labels = label_preds
        label_preds = assign_points(dataset, new_centers)

    return label_preds, new_centers


if __name__ == '__main__':
    # points = [
    #     [1, 2],
    #     [2, 1],
    #     [3, 1],
    #     [5, 4],
    #     [5, 5],
    #     [6, 5],
    #     [10, 8],
    #     [7, 9],
    #     [11, 5],
    #     [14, 9],
    #     [14, 14],
    #     ]
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_iteration",   help="n_iteration", type=int, default=1)
    parser.add_argument("--n_clusters",   help="n_clusters", type=int, default=3)

    args = parser.parse_args()
    print(args)
    
    iris = load_iris()
    X = iris.data[:] # 取data
    
    points = []
    for item in X:
        points.append([item[0],item[1]])

    label_pred, centers_pred = k_means(points, args.n_clusters, args.n_iteration)
    showCluster(points, label_pred, centers_pred, args.n_clusters)
   