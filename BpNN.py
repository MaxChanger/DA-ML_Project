#########################################
# 2019-09-14 Jiadai Sun
# sunjiadai@foxmail.com
# Ref:   https://blog.csdn.net/huakai16/article/details/77479127?utm_source=blogxgwz7
# 
# python .\BpNN.py
# 
#########################################

from sklearn.datasets import load_digits                # 数据集
from sklearn.preprocessing import LabelBinarizer        # 标签二值化
from sklearn.model_selection import train_test_split    # 数据集分割
import numpy as np
import matplotlib.pyplot as plt  


def sigmoid(x):  # 激活函数
    return 1/(1+np.exp(-x))

def dsigmoid(x):  # sigmoid的导数 其中的x应该是sigmod(x)
    return x*(1-x)

def normalize(x):
    ''' 数据归一化,一般是x=(x-x.min)/x.max-x.min '''
    x -= x.min()
    x /= x.max()
    # min_ = x.min()
    # max_ = x.max()
    # x = (x - min_) / (max_ - min_)

class NeuralNetwork:
    
    def __init__(self, layers): 
        self.V = np.random.random((layers[0]+1, layers[1])) * 2 - 1  # (65,100)  -0.5?
        self.W = np.random.random((layers[1], layers[2]))   * 2 - 1  # (100,10)

    def train(self, data_train, label_train, data_test, label_test, lr=0.1, epochs=3000):
        # lr为学习率，epochs为迭代的次数
        # 为数据集添加偏置
        temp = np.ones([data_train.shape[0], data_train.shape[1]+1]) # 1347 * 65
        temp[:, 0:-1] = data_train
        data_train = temp  # 这里最后一列为偏置 1347 * 65

        # 进行权值训练更新
        for n in range(epochs+1):
            i = np.random.randint(data_train.shape[0])  # 随机选取一行数据(一个样本)进行更新
            x = data_train[i]
            x = np.atleast_2d(x)  # 转为二维数据 [[1,12,21,...]] 1*65

            L1 = sigmoid(np.dot(x, self.V))  # 隐层输出(1,100)    1*65 x 65*100 = 1*100
            L2 = sigmoid(np.dot(L1, self.W))  # 输出层输出(1,10)  1*10 x 100*10 = 1*10

            # delta
            L2_delta = (label_train[i]-L2)*dsigmoid(L2)  # (1,10)
            # (1,100)，这里是数组的乘法，对应元素相乘
            L1_delta = L2_delta.dot(self.W.T)*dsigmoid(L1)

            # 更新 反向传播 
            self.W += lr * L1.T.dot(L2_delta)  # (100,10)
            self.V += lr * x.T.dot(L1_delta)

            # 每训练1000次预测准确率
            if n % 1000 == 0:
                predictions = []
                for j in range(data_test.shape[0]):
                    out = self.predict(data_test[j])    # 用验证集去测试 64
                    predictions.append(np.argmax(out))  # 返回预测结果
                accuracy = np.mean(np.equal(predictions, label_test))  # 求平均值
                print('epoch:', n, 'accuracy:', accuracy)
        
        # 测试和可视化
        # for tmp in range(10):
        #     j = np.random.randint(data_test.shape[0])
        #     out = self.predict(data_test[j])    # 用验证集去测试 64
        #     b = np.array(data_test[j]).reshape(8,8)
        #     pred_num = np.argmax(out)
        #     print(pred_num)
        #     showStr = 'pred_num:{0}   true_label:{1}'.format('%d'%pred_num, '%d'%label_test[j])
        #     fig = plt.figure()
        #     ax = fig.add_subplot(331)
        #     plt.title(showStr)
        #     ax.matshow(b, cmap='viridis') 
        #     plt.pause(1)    # 显示秒数
        #     plt.close()     # 关闭   
        for _ in range(10):
            fig = plt.figure()
            for tmp in range(331,340):
                j = np.random.randint(data_test.shape[0])
                out = self.predict(data_test[j])    # 用验证集去测试 64
                b = np.array(data_test[j]).reshape(8,8)
                pred_num = np.argmax(out)
                # print(pred_num)
                showStr = 'P:{0}   T:{1}'.format('%d'%pred_num, '%d'%label_test[j])
                ax = fig.add_subplot(tmp)
                plt.title(showStr)
                plt.axis('off')
                ax.matshow(b) 
            plt.pause(3)    # 显示秒数
            plt.close()     # 关闭  


    def predict(self, x):
        # 添加转置,这里是一维的
        temp = np.ones(x.shape[0]+1)
        temp[0:-1] = x
        x = temp
        x = np.atleast_2d(x)

        L1 = sigmoid(np.dot(x, self.V))  # 隐层输出
        L2 = sigmoid(np.dot(L1, self.W))  # 输出层输出
        return L2


# def main():
if __name__ == '__main__':
    digits = load_digits()  # 使用sklearn中自带的手写数字数据集（digits），这个数据集中并没有图片，而是经过提取得到的手写数字特征和标记
    data   = digits.data    # 数据 1797 * 64
    label  = digits.target  # 标签 1797 * 1
    normalize(data)

    data_train, data_test, label_train, label_test = train_test_split(data, label)  # 默认分割：3:1 1347/450

    label_train = LabelBinarizer().fit_transform(label_train)  # 标签二值化 0001000
    # label_test = LabelBinarizer().fit_transform(label_test)

    net = NeuralNetwork([64, 100, 10])
    net.train(data_train, label_train, data_test, label_test, epochs=20000)
