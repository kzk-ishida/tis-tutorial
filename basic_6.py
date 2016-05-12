#-*-coding:utf-8-*-

import sys


def bottom_output(input_file):
    try:
        row=int(sys.argv[1])

    except IndexError:
        print 'Usage:%s N(nutral_number)'%sys.argv[0]

    else:
        with open(input_file) as ifile:
            l=ifile.readlines()
        row_max=len([None for k in l])
        for i in range(row_max-row,row_max):
            print l[i],



if __name__=="__main__":
    filename="address.txt"
    bottom_output(filename)
