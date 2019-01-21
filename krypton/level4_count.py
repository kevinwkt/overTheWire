#!/bin/python3

from collections import defaultdict
import vigenere
import pprint as pp
from itertools import combinations_with_replacement

#mp = defaultdict(int)

file1 = open("./level4_found1","r")
file2 = open('./level4_found2','r')

str = file1.read().replace(" ", "")
str2 = file2.read().replace(" ", "")

file1.close()
file2.close()

l = [defaultdict(int) for x in range(6)]
for i in range(len(str)):
    l[i%6][str[i]] += 1
for i in range(len(str2)):
    l[i%6][str2[i]] += 1

for i in range(len(l)):
    l[i] = sorted(l[i].items(), key=lambda x: x[1], reverse=True)

#pp.pprint(l)

file_ans = open("./level4_krypton5", "r")

s = file_ans.read()

#perms = map("".join, combinations_with_replacement("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3))
#i = 1
#for p in perms:
ans = vigenere.decrypt(s, "FREKEY")
print(ans)
