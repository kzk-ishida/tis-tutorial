#-*-coding:utf-8-*-
def sort_col1_2(input_file):
    with open(input_file) as ifile:
        lines=sorted([line.split('\t')for line in ifile],key=lambda x:x[0],reverse=True)
        lines2=sorted(lines,key=lambda x:x[1],reverse=True)
    for i in lines2:
        print '\t'.join(i),

        #  for line in lines:
            #  print '\t'.join(line),
if __name__=='__main__':
    filename="address.txt"
    sort_col1_2(filename)

