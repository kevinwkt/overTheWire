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
#for c in str:
#    mp[c] += 1

# To print the list in freq order
#pp.pprint(sorted(mp.items(), key=lambda x: x[1], reverse=True))
#pp.pprint(sorted(l, key=lambda x:x.items()[1]), reverse=True)
pp.pprint(l.map(lambda x: sorted(x, lambda x: x.items()[1])))

#file_ans = open("./level4_krypton5", "r")
#
#s = file_ans.read()
#
#perms = map("".join, combinations_with_replacement("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 6))
#i = 1
#for p in perms:
#    ans = vigenere.decrypt(str, p)
#    if "THE" and "TO" and "OF" in ans:
#        print(p)
    #print(i)
    #print(ans)
    #i += 1

#for c in s:
#    if c == 'S':
#        print('E', end="")
