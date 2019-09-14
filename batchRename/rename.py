import os
import re

def rename(path, filename_list):

    suffixdic = {}

    # for file in filename_list:
    #     suffix = os.path.splitext(file)[1] # .jpg
    #     if suffix not in suffixdic:
    #         suffixdic[suffix] = 0
    # print(suffixdic)

    for file in filename_list:
        suffix = os.path.splitext(file)[1] # .jpg
        if suffix not in suffixdic:
            suffixdic[suffix] = 0

        if suffix in suffixdic:
            new_filename = os.path.join(path,"aa=bud__{0}".format('%03d'%suffixdic[suffix]) + suffix)
            suffixdic[suffix] += 1
            old_filepath = os.path.join(path, file)
            print(old_filepath, new_filename)
            os.rename(old_filepath, new_filename)

def main():
    path = "./Data/img/"
    filename_list = os.listdir(path)
    rename(path, filename_list)

if __name__ == '__main__':
    main()

