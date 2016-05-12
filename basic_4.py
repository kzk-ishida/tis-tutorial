fcol1=open("col1.txt","r")
fcol2=open("col2.txt","r")
f=open("address1.txt","w")




col1=fcol1.readlines()
col2=fcol2.readlines()

for i in range(len(col1)):
    col=col1[i].replace("\n","\t")+col2[i]
    f.write(col)

    print col,


#  print f
fcol1.close()
fcol2.close()
f.close()

