import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

path = 'result.txt'
f = open(path, 'w+')

num = int(input("輸入一個整數:"))
f.writelines("輸入的數字為:{}\n".format(num))
if (num % 2) == 0 and 2<=num<=5:
   f.writelines("輸入的數字為偶數且在2到5之間 輸出O\n")
   print('輸入的數字為偶數且在2到5之間 輸出O')
elif (num % 2) == 0 and 6<=num<=20:
   f.writelines("輸入的數字為偶數且在6到20之間 輸出X\n")
   print('輸入的數字為偶數且在6到20之間 輸出X')
elif (num % 2) == 0 and num>20:
   f.writelines("輸入的數字為偶數且大於20 輸出O\n")
   print('輸入的數字為偶數且大於20 輸出O')
else:
   f.writelines("輸入的數字為奇數 輸出X\n")
   print('輸入的數字為奇數 輸出X')
f.close()