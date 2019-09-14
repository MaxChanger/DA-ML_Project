#########################################
# 2019-09-07 Jiadai Sun
# sunjiadai@foxmail.com
# 
# python .\plotFrequencyGUI.py --filePath '../Data/test.txt' --showtype pie --sort --countLetter
# 
#########################################
import re
import sys
import tkinter
from tkinter import *
from tkinter import scrolledtext
import argparse
import matplotlib.pyplot as plt  

def countletterfrequency(lineList, dic):
    for line in lineList:
        # line = line.strip('\n')
        # line = line.replace(' ','')
        # print(line)
        for letter in line:
            if letter.isalpha():
                dic[letter] += 1
            else:
                dic['*'] += 1

def creatletterdic():
    letter = 'abcdefghijklmnopqrstuvwxyz'
    upletter = letter.upper()
    keyletter = letter + upletter + '*'
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

def main(window, args):

    wordDic = {}
    letterDic = creatletterdic()
    ansDic = {}
    
    file = open(args.filePath,'r')
    # file = open("./Data/test.txt",'r')
    lineList = file.readlines()
    file.close()

    ''' show srcText line '''
    srctext = scrolledtext.ScrolledText(window, width=100, height=40, font=('Arial',10))
    for line in lineList:
        srctext.insert(INSERT,line)
    srctext.pack(side = LEFT)

    ''' count the frequency of letter or word '''
    if args.countLetter is True:
        countletterfrequency(lineList, letterDic)   
        ansDic = letterDic
    else:
        countwordfrequency(lineList, wordDic)       
        ansDic = wordDic

    ''' if sort or not '''
    if args.sort is True:
        ansDic = sorted(ansDic.items(), key=lambda x: x[1], reverse=True)   # sort
    else:
        ansDic = ansDic.items() # not sort
    
    '''show the answer of countText line'''
    anstext = scrolledtext.ScrolledText(window, width=30, height=40, font=('Arial',10))
    for key, value in ansDic:
        tmp_str = key + ':\t' + str(value) + '\n'
        anstext.insert(INSERT,tmp_str)
    anstext.pack(side = RIGHT)

    return ansDic

def plotShow(ansdictItems, args):
    name_list = []
    num_list  = []
    
    ''' If the number of occurrences is 0, then remove '''
    for key, value in ansdictItems:
        if value != 0:
            name_list.append(key)
            num_list.append(value)

    if args.countLetter is True:

        if args.showtype == 'bar':
            plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)  
            plt.xlabel('letter')
            plt.ylabel('frequency')
            for x, y in zip( range(0,len(name_list)), num_list):
                plt.text(x, y+0.3, str(y), ha='center', va='bottom')
        elif args.showtype == 'pie':
            plt.axes(aspect=1)
            explode = [x * 0.02 for x in range(len(name_list))]
            plt.pie(x=num_list, labels=name_list, autopct='%0.2f %%', explode = explode, \
                shadow=False, labeldistance=1.1, startangle=0, pctdistance=0.8, center=(-1, 0))

    else:
        if args.showtype == 'bar':
            plt.barh(range(len(num_list)), num_list,color='rgb',tick_label=name_list)  
            plt.xlabel('frequency')
            plt.ylabel('word')
            for x, y in zip( num_list, range(0,len(name_list)), ):
                plt.text(x+0.05, y, str(x), ha='center', va='bottom')
        elif args.showtype == 'pie':
            plt.axes(aspect=1)
            explode = [x * 0.02 for x in range(len(name_list))]
            plt.pie(x=num_list, labels=name_list, autopct='%0.2f %%', explode = explode, \
                shadow=False, labeldistance=1.1, startangle=0, pctdistance=0.8, center=(-1, 0))
    # plt.legend(loc=7, bbox_to_anchor=(1.2, 0.80), ncol=3, fancybox=True, shadow=True, fontsize=8)
    plt.show()  

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--filePath",   help="path of textfile", type=str, default='./Data/test.txt')
    parser.add_argument("--sort",       help="if sort the answer", action='store_true')
    parser.add_argument("--countLetter",help="choose count Letter otr Word", action='store_true')
    parser.add_argument("--showtype",   help="choose count Letter otr Word",type=str, default='bar')
    args = parser.parse_args()
    print(args)
    
    window = tkinter.Tk()
    ansdictItems = main(window, args)
    
    window.title('count Frequency GUI')
    window.resizable(0,0)   

    plotShow(ansdictItems, args)
    window.mainloop()



