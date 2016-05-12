f=open("address.txt")

for line in f:
    print line.strip().replace('\t', ' ')

#  print f
#  print line
