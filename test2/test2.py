import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

path = 'result.txt'
f = open(path, 'w+')

content = "Hello welcome to Cathay 60th year anniversary"
tmp=content.upper()
result_dic={}
for i in tmp:
    if i==' ':
        continue
    result_dic[i]=tmp.count(i)

result_List=[]
for key,value in result_dic.items():
    result_List.append('{} {}'.format(key,value))

result_List.sort()
for i in result_List:
    f.writelines(i+'\n')
    print(i)

f.close()