#-*-coding:utf-8-*-
import sys

def before_output(input_file):

    with open(input_file) as ifile:
        
        
        print ifile
        param=int(sys.argv[1])
        count=0
        l=ifile.readlines()
        for i in range(0,param):
            
            #  if  count<=int(param[1]):
            print l[i],

            #  print count



if  __name__=="__main__":
    filename="address.txt"
    before_output(filename)

    
