#!/usr/bin/env python

import re
import TokenScanner

TScan = TokenScanner.tokenScanner()


f = open("testFile.txt", "r") #opens file with name of "test.txt"


while True:
    outprint = TScan.getChar(f.read(1))
    if outprint != None:
        print outprint
        if(outprint[0]=="STOP"):
            break;

f.close()

# tempset = {"omg","holymoly","idfdf"}
#
# temp = 'A'
# print int("12334324")+1


