#########################################
# 2019-08-31 Jiadai Sun
# sunjiadai@foxmail.com
# 
# python .\countFrequencyGUI.py --filePath '../Data/bio.txt' --sort --countLetter
# 
#########################################
import re
import sys
import tkinter
from tkinter import *
from tkinter import scrolledtext
import argparse

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

    # btn1 = tkinter.Button(window, text='Open File',font =('Arial',10,'bold'),width=20, command=openfiles(filename))
    # print(filename)
    # btn1.pack(side='top')

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


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--filePath",   help="path of textfile", type=str, default='../Data/test.txt')
    parser.add_argument("--sort",       help="if sort the answer", action='store_true')
    parser.add_argument("--countLetter",  help="choose count Letter otr Word", action='store_true')
    args = parser.parse_args()
    print(args)
    
    window = tkinter.Tk()
    main(window, args)
    window.title('count Frequency GUI')
    window.resizable(0,0)   
    window.mainloop()


