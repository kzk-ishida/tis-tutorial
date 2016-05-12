#-*-coding:utf-8-*-
from collections import Counter

def count_col1(input_file):
    col1=[]
    with open(input_file) as ifile:
        l=ifile.readlines()
    for i in l:
        item_list=i[:-1].split('\t')
        col1.append(item_list[0])
        #  print item_list[0]

    count_dict=Counter(col1)
    for k,v in count_dict.most_common():
        print k,v

if __name__=="__main__":
    filename="address.txt"
    count_col1(filename)
