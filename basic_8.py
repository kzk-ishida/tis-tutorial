#-*-coding:utf-8-*-

def sort_col2(input_file):
    with open(input_file) as ifile:
        lines=sorted([line.split('\t')for line in ifile],key=lambda x:x[1])
        for line in lines:
            print '\t'.join(line),


if __name__=='__main__':
    filename="address.txt"
    sort_col2(filename)
