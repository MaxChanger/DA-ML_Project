#########################################
# 2019-08-31 Jiadai Sun
# sunjiadai@foxmail.com
# 
# python .\renamefilter.py myimage###.jpg
#                          imgDate###.png
# 
#########################################
import os
import re
import sys
import time

def rename(path, filename_list, filter):
    tmp_name = os.path.splitext(filter)[0]
    
    if 'Date' in tmp_name:
        str_time = time.strftime("%Y%m%d", time.localtime())
        tmp_name = tmp_name.replace('Date',str_time)
    _num = tmp_name.count('#')  # count the number of # 
    _tmp = '#' * _num           # generate _num '#' such as '####'
    _fmt = '%0{0}d'.format('%d'%_num)   # used for the format '%04d'% suffixdic[suffix]
    tmp_name = tmp_name.replace(_tmp, '{0}') # replace the #### with {0} . the formate
    suffix = os.path.splitext(filter)[1]
    suffixdic = {}
    suffixdic[suffix] = 0
    
    for file in filename_list:
        suffix = os.path.splitext(file)[1] # .jpg
        if suffix in suffixdic:
            new_filename = os.path.join(path, tmp_name.format(_fmt%suffixdic[suffix]) + suffix)
            suffixdic[suffix] += 1
            old_filepath = os.path.join(path, file)
            # print(old_filepath, new_filename)
            os.rename(old_filepath, new_filename)

def main():
    filter = sys.argv[1]
    # filter = 'imgDate###.png'
    path = "../Data/img/"
    filename_list = os.listdir(path)
    rename(path, filename_list, filter)

if __name__ == '__main__':
    main()

