#########################################
# 2019-08-31 Jiadai Sun
# sunjiadai@foxmail.com
# 
# python .\wordFrequency.py
#   countLetter = False
#   ifsort = True
#########################################
import re
import sys

def countletterfrequency(lineList, dic):
    for line in lineList:
        # line = line.strip('\n')
        # line = line.replace(' ','')
        # print(line)
        for letter in line:
            if letter.isalpha():
                dic[letter] += 1

def creatletterdic():
    letter = 'abcdefghijklmnopqrstuvwxyz'
    upletter = letter.upper()
    keyletter = letter + upletter
    dic = {}
    for key in keyletter:
        dic.update({ key : 0})
    return dic


def countwordfrequency(lineList, wordDic):
    for line in lineList:
        line = line.strip('\n')      
        # punctuation = ',{}()<.>/?;:\'"`~!@#$%^&*-=+'
        punctuation = '{}()<>.!,;:?"\''
        line = re.sub(r'[{}]+'.format(punctuation),'',line) # remove the punctuation
        line.strip().strip('-+')
        wordArr = line.split()
        # count the word 
        for key in wordArr:
            if (key in wordDic):
                wordDic[key] += 1
            else:
                wordDic[key] = 1

def mian():
    # filePath = sys.argv[1]
    wordDic = {}
    letterDic = creatletterdic()
    ansDic = {}

    file = open("../Data/bio.txt",'r')
    lineList = file.readlines()

    countLetter = False
    ifsort = True

    if countLetter:
        countletterfrequency(lineList, letterDic)
        ansDic = letterDic
    else:
        countwordfrequency(lineList, wordDic)
        ansDic = wordDic
    if ifsort:
        ansDic = sorted(ansDic.items(), key=lambda x: x[1], reverse=True)

    print(ansDic)

if __name__ == '__main__':
    mian()


