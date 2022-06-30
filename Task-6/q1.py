import os
h=open('onelinefile.txt')
content=h.readlines()
string=content[0]
for i in range(1,len(content[0])):
    j=string[i]
    if j.isnumeric():
        content[0]=content[0][:i]+" "+content[0][i:]
content