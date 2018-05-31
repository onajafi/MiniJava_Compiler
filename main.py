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

goodbye=False

while not goodbye:
    outprint = TScan.getChar(f.read(1))
    if outprint != None:
        #print outprint
        my_parser.get_token(outprint)
        if(outprint[1]=='EOF' or outprint[0]=="STOP"):
            break
        if(outprint[0]=="ERROR"):
            print "ERROR: " + outprint[1]
            goodbye = True

f.close()
if(not goodbye):
    print "\nThe output will be like:"
    for line,command in enumerate(my_parser.PB):
        print line, command


    output_file = open("output.txt","w")
    for line,command in enumerate(my_parser.PB):
        output_file.write(str(line) + "\t" + '(')
        if (command[0] != None):
            output_file.write(str(command[0])+ ', ')
        if (command[1] != None):
            output_file.write(str(command[1]) + ', ')
        if (command[2] != None):
            output_file.write(str(command[2]) + ', ')
        if (command[3] != None):
            output_file.write(str(command[3]))
        output_file.write(')\n')

    output_file.close()

    print "Done"
    if(my_parser.abort or my_parser.Error_CNT):
        if(my_parser.abort):
            print "But with error(s) and " + str(my_parser.Error_CNT) + " warning(s)"
        else:
            print str(my_parser.Error_CNT) + " warning(s)"
    else:
        print "With no errors :)"



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


