#!/usr/bin/env python

import re
import TokenScanner,LL1_Parser

TScan = TokenScanner.tokenScanner()


# f = open("testFile.txt", "r") #opens file with name of "test.txt"
#
#
# while True:
#     outprint = TScan.getChar(f.read(1))
#     if outprint != None:
#         print outprint
#         if(outprint[1]=='EOF' or outprint[0]=="STOP"):
#             break
#
# f.close()

# tempset = {("omg","yay"):["Hi","iiii"],"holymoly":"funny","idfdf":"dead end"}
#
# temp = tempset.has_key(("omg","yay"))
# print len(tempset[("omg","yay")])


