#########################################
# 2019-08-31 Jiadai Sun
# sunjiadai@foxmail.com
# 
# python .\letterFrequency.py
# 
#########################################
def countfrequency(lineList, dic):
    for line in lineList:
        # line = line.strip('\n')
        # line = line.replace(' ','')
        # print(line)
        for letter in line:
            if letter.isalpha():
                dic[letter] += 1

def creatdic():
    letter = 'abcdefghijklmnopqrstuvwxyz'
    upletter = letter.upper()
    keyletter = letter + upletter
    dic = {}
    for key in keyletter:
        dic.update({ key : 0})
    return dic

if __name__ == '__main__':

    dic = creatdic()
    file = open("./Data/bio.txt",'r')
    lineList = file.readlines()
    countfrequency(lineList, dic)

    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    print(dic)

