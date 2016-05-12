
#-*-coding:utf-8-*-
#  import  codecs

f=open("address.txt","r")
col1=open("col1.txt","w")
col2=open("col2.txt","w")

#  f=codecs.open("address.txt","rb","utf-8")
#  fcol1=codecs.open("col1.txt","w","utf-8")
#  fcol2=codecs.open("col2.txt","w","utf-8")


for i in f:
    itemList=i[:-1].split('\t')
    col1.writelines(itemList[0]+"\n")
    col2.writelines(itemList[1]+"\n")

#  print f
test_list=['あ','い','う']

for i in range(len(test_list)):
    print test_list[i],

print test_list

col1.close()
col2.close()
f.close()

