import json


f=open('item.json','r')
out = open('out.json','w')

line=f.read()
line=line.replace('index','id')
line=line.replace('answer','answers')
out.write(line)
f.close()
out.close()