#########################################
# 2019-08-31 Jiadai Sun
# sunjiadai@foxmail.com
# 
# python .\wordFrequency.py
# 
# will get  [('and', 25), ('in', 18), ('the', 14), ('of', 11), ('He', 10),....]
#########################################

import re

def countfrequency(lineList, wordDic):
    for line in lineList:
        line = line.strip('\n')      
        # punctuation = ',{}()<.>/?;:\'"`~!@#$%^&*-=+'
        punctuation = '{}()<>.!,;:?"\''
        line = re.sub(r'[{}]+'.format(punctuation),'',line) # 去除标点
        line.strip().strip('-+')
        wordArr = line.split()
        # 文字统计
        for key in wordArr:
            if (key in wordDic):
                wordDic[key] += 1
            else:
                wordDic[key] = 1

if __name__ == '__main__':

    wordDic = {}
    file = open("../Data/bio.txt",'r')
    lineList = file.readlines()
    countfrequency(lineList, wordDic)

    wordTup = sorted(wordDic.items(), key=lambda x: x[1], reverse=True)

    print(wordTup)

