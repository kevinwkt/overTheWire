#!/bin/python3

from collections import defaultdict
import pprint as pp

mp = defaultdict(int)

file1 = open("./level3_found1","r")
file2 = open('./level3_found2','r')
file3 = open('./level3_found3','r')

str = file1.read()+file2.read()+file3.read()
#str2 = file2.read()
#str3 = file3.read()

file1.close()
file2.close()
file3.close()

for c in str:
    mp[c] += 1

# To print the list in freq order
#pp.pprint(sorted(mp.items(), key=lambda x: x[1], reverse=True))

ans = open("./level3_krypton4", "r")

s = ans.read()

for c in s:
    if c == 'S':
        print('E', end="")
    elif c == 'J':
        print('T', end="")
    elif c == 'D':
        print('H', end="")
    elif c == 'Q':
        print('A', end="")
    elif c == 'B':
        print('O', end="")
    elif c == 'U':
        print('S', end="")
    elif c == 'V':
        print('L', end="")
    elif c == 'I':
        print('V', end="")
    elif c == 'W':
        print('D', end="")
    elif c == 'G':
        print('N', end="")
    elif c == 'K':
        print('W', end="")
    elif c == 'X':
        print('F', end="")
    elif c == 'M':
        print('U', end="")
    elif c == 'N':
        print('R', end="")
    elif c == 'Y':
        print('P', end="")
    elif c == 'C':
        print('I', end="")
    elif c == 'A':
        print('B', end="")
