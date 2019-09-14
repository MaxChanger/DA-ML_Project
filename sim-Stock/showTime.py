#########################################
# 2019-09-07 Jiadai Sun
# sunjiadai@foxmail.com
# 
# python .\showTime.py --update 0.1 --xmax 100 --fixed
# 
#########################################
import matplotlib.pyplot as plt
import numpy as np
import argparse

def getColor( x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    if k > 0:
        return 'r'
    if k <= 0:
        return 'g'

def creatDate(args):
    x, y = [], []
    for i in range(args.xmax):
        x.append(i)
        if i == 0:
            y.append(np.random.uniform(args.ymax/2 - 1 , args.ymax/2 + 1))
        else:
            y.append(np.random.uniform(max(0,y[i-1]-0.5),min(y[i-1]+0.5,args.ymax)))
    return x, y

def showPlot(x, y, args):

    plt.ion()
    plt.grid(linestyle='-.')

    if args.fixed is True:
        plt.xlim(0, args.xmax)
    plt.ylim(0, args.ymax)

    maxPrice = y[0]
    minPrice = y[0]

    for i in range(args.xmax):

        maxPrice = max(maxPrice, y[i])
        minPrice = min(minPrice, y[i])
        showStr = 'MaxPrice:    ' + '{0}'.format('%2.2f'%maxPrice) + '\n' + \
            'MinPrice:     ' + '{0}'.format('%2.2f'%minPrice) + '\n' + \
            'NewPrice:    ' + '{0}'.format('%2.2f'%y[i]) 

        plt.annotate( showStr, xy=(1, args.ymax-1.5), bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8)))
        plt.plot(x[i], y[i], 'b.')

        if i >= 1:
            c = getColor(x[i-1], y[i-1], x[i], y[i])
            plt.annotate("", xy=(x[i], y[i]), xytext=(x[i-1], y[i-1]), arrowprops=dict(arrowstyle="->", color=c))
        plt.pause(args.update)


    plt.savefig('picture.png', dpi=300)
    plt.ioff()
    plt.show()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--update", help="update", type=float, default=0.5)
    parser.add_argument("--xmax",   help="xmax", type=int, default=60)
    parser.add_argument("--ymax",   help="ymax", type=int, default=10)
    parser.add_argument("--fixed",  help="fix the x and y", action='store_true')

    args = parser.parse_args()
    print(args)

    x, y = creatDate(args)
    showPlot(x, y, args)