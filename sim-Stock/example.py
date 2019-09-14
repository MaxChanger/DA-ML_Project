import matplotlib.pyplot as plt
import numpy as np

ax=[]   #保存图1数据
ay=[]
bx=[]   #保存图2数据
by=[]
num=0   #计数
plt.ion()    # 开启一个画图的窗口进入交互模式，用于实时更新数据
# plt.rcParams['savefig.dpi'] = 200 #图片像素
# plt.rcParams['figure.dpi'] = 200 #分辨率
plt.rcParams['figure.figsize'] = (10, 10)        # 图像显示大小
plt.rcParams['font.sans-serif']=['SimHei']   #防止中文标签乱码，还有通过导入字体文件的方法
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 0.5   #设置曲线线条宽度
plt.xlim(0,100)
while num<100:
    plt.clf()    #清除刷新前的图表，防止数据量过大消耗内存
    plt.suptitle("总标题",fontsize=30)             #添加总标题，并设置文字大小
    g1=np.random.random()  #生成随机数画图
	#图表1
    ax.append(num)      #追加x坐标值
    ay.append(g1)       #追加y坐标值
    agraphic=plt.subplot(2,1,1)
    agraphic.set_title('子图表标题1')      #添加子标题
    agraphic.set_xlabel('x轴',fontsize=10)   #添加轴标签
    agraphic.set_ylabel('y轴', fontsize=20)
    plt.plot(ax,ay,'g-')                #等于agraghic.plot(ax,ay,'g-')
	
    #图表2
    bx.append(num)
    by.append(g1)
    bgraghic=plt.subplot(2, 1, 2)
    bgraghic.set_title('子图表标题2')
    bgraghic.plot(bx,by,'r^')
    if num > 1:
        plt.arrow(bx[num],by[num],bx[num]-bx[num-1],by[num]-by[num-1],head_width=0.1,color="black",alpha=0.9) 
    plt.pause(0.4)     #设置暂停时间，太快图表无法正常显示
    if num == 15:
        plt.savefig('picture.png', dpi=300)  # 设置保存图片的分辨率
        #break
    num=num+1

plt.ioff()       # 关闭画图的窗口，即关闭交互模式
plt.show()       # 显示图片，防止闪退



#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jinriqiang'

import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# set up matplotlib
is_ipython = 'inline' in matplotlib.get_backend()
if is_ipython:
    from IPython import display

plt.ion()
Frequency = 1
DataSize = 100
DataType = 4
Max_number = 20
Min_number = 0

def createRandomNumber():
    number = []
    for i in range(DataSize):
        num = random.uniform(Min_number, Max_number)
        number.append(round(num, 2))

    return number

def createDate(Data):
    number = createRandomNumber()
    Data[1:len(Data)] = number

def designColor(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    if k > 0:
        return "red"
    if k <= 0:
        return 'green'

def draw(i, Data):
    plt.figure(DataType)
    for j in range(DataType):
        plt.subplot((DataType)*100+10+(j+1))
        plt.title(str(Data[j][0])+"Share")
        plt.plot(i, Data[j][i], '.')
        plt.xlim(0, DataSize)
        plt.ylim(0, Max_number)
        if i >= 2:
            #plt.arrow(i-1, Data[j][i-1], 1, Data[j][i]-Data[j][i-1], length_includes_head=True, head_width=0.25, head_length=0.5, fc='r', ec='b')
            color = designColor(i-1, Data[j][i-1], i, Data[j][i])
            plt.annotate("", xy=(i, Data[j][i]), xytext=(i-1, Data[j][i-1]), arrowprops=dict(arrowstyle="->", color=color))

    plt.pause(Frequency)  # pause a bit so that plots are updated
    if is_ipython:
        display.clear_output(wait=True)
        display.display(plt.gcf())

def main():
    Data = [[0 for i in range(DataSize + 1)]for j in range(DataType)]
    for k in range(DataType):
        Data[k][0] = chr(k + 65)
        createDate(Data[k])
    for i in range(DataSize):
        draw(i+1, Data)


if __name__ == '__main__':
    main()