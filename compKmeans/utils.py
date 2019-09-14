import matplotlib.pyplot as plt

def getXY( xylist ):
    x = []
    y = []
    for tmp in xylist:
        x.append(tmp[0])
        y.append(tmp[1])
    return x, y

def showCluster(points, label_pred, centers_pred, k):
    plt.title("K-means")
    data = {}
    for i in range(k):
        data.update({i:[]})

    for (label, _XY) in zip(label_pred, points):
        data[label].append(_XY)

    for cent, c, marker in zip( range(k), ['r', 'g', 'b', 'y'], ['^', 'o', '*', 's'] ): #画出数据点散点图
        X, Y = getXY(data[cent])
        plt.scatter(X, Y, c=c, marker=marker, label='label{0}'.format('%d'%cent))
 
    centroidsX, centroidsY = getXY(centers_pred)
    plt.scatter(centroidsX, centroidsY, s=100, c='black', marker='+', alpha=1)  # 画出质心点
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    plt.legend(loc=2)
    plt.show()



# 数据可视化
# def showCluster(points, label_pred, centers_pred, k):
#     plt.title("K-means")
#     fig = plt.figure()    
#     data = {}
#     for i in range(k):
#         data.update({i:[]})

#     for (label, _XY) in zip(label_pred, points):
#         data[label].append(_XY)
#     ax = fig.add_subplot(111)

#     for cent, c, marker in zip( range(3), ['r', 'g', 'b', 'y'], ['^', 'o', '*', 's'] ): #画出数据点散点图
#         X, Y = getXY(data[cent])
#         ax.scatter(X, Y, s=80, c=c, marker=marker)
 
#     # centroidsX, centroidsY = getXY(centers_pred)
#     # ax.scatter(centroidsX, centroidsY, s=1000, c='black', marker='+', alpha=1)  # 画出质心点
#     # ax.set_xlabel('X Label')
#     # ax.set_ylabel('Y Label')
#     # ax.legend(loc=2)
#     plt.show()