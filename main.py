#!/usr/bin/env python

# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyssosyhmMMMMMMMMMMMMMMMMMMMmdhyyyhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMh+.          `:sNMMMMMMMMMMMdo-`         -+hMMMMMMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMMMMs.                 /mMMMMMMMy-                `oNMMMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMMm.                     oMMMMm-    -::.            `hMMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMd`                       +MMd`  .yNMMMMNs`           sMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMM.                         hM.  .NMMMMMMMMm`           dMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMd             -ohhhs/`     :N   +MMMMMMMMMM-           +MMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMy           `dMMMMMMMm:    -N   `mMMMMMMMMh            :MMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMm           yMMMMMMMMMN    +m    `+dNMMNh/             oMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMM+          sMMMMMMMMMm   `mM:       ``               `NMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMM/         `yMMMMMMMd.  `dMMN-                      `hMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMMMs`         ./sss+-   :mMMMMN+                    -mMMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMMMMNo.              `/dMMMMMMMMm/`               :hMMMMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms/-`    `.:ohNMMMMMMMMMMMMNh+-`      `-/yNMMMMMMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMNmmmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
# Believe The eyes


import re
import TokenScanner,LL1_Parser

TScan = TokenScanner.tokenScanner()
my_parser = LL1_Parser.Parser()


f = open("testFile.txt", "r") #opens file with name of "test.txt"


while True:
    outprint = TScan.getChar(f.read(1))
    if outprint != None:
        #print outprint
        my_parser.get_token(outprint)
        if(outprint[1]=='EOF' or outprint[0]=="STOP"):
            break

f.close()
print "\nThe output will be like:"
for line,command in enumerate(my_parser.PB):
    print line,command

# tempset = {("omg","yay"):["Hi","iiii"],"holymoly":"funny","idfdf":"dead end"}
#
#
# new = tempset
# tempset["holymoly"] = "OKM"
# temp_list=[1,2,3,4,5]
# llist2=[434,56,74,422]
# llist2.extend(temp_list[::-1])
#
# print llist2


