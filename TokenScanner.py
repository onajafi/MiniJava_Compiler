
# Terminals that will be recognized as Identifiers but they are keys!!!
keys={"EOF","public","class","static","void",
      "main","extends","return","boolean",
      "int","if","else","while","for","true",
      "false","identifier","integer","System.out.println"}

# Other Terminals
simpleTerms={"{","}","(",")",";",",","=","+=","+","-",
             "*",".","&&","==","<"}
# Start of Simple terms:
startOfST = {"{","}","(",")",";",",","=","+","-",
             "*",".","&","<"}
# Second char of Simple terms(if there is):
endOfST = {"=","&"}

class tokenScanner():
    """Receives every character and
    gives out the token"""

    state=0
    tempStr=""
    last_constructed_token=(None,None)

    lastChar=""# When Character is not proccessed
    we_already_have_a_char=False

    # For comments: When we see a '/' it means we have a comment...
    last_state=-1# The state before entering a comment (we have to get back to this state after the comment

    def constructToken(self,lastChar):
        output = None
        if(self.state==0):
            pass
        elif(self.state==1):#Identifier
            if(self.tempStr in keys):
                output = ("Key", self.tempStr)
            elif('.' not in self.tempStr):
                output = ("ID", self.tempStr)
        elif(self.state==2):
            output=("INT",int(self.tempStr))
        elif (self.state == 3):
            output = ("Opr",self.tempStr)
        elif(self.state ==4 or self.state==5):
            if(self.tempStr in simpleTerms):# ST: Simple Term
                output = ("ST",self.tempStr)


        # Reseting the vars
        self.tempStr = ""
        self.state=0

        if(lastChar not in (" ","\n")):
            self.we_already_have_a_char=True
            self.lastChar = lastChar

        if(output != None):
            self.last_constructed_token=output

        return output

    def getChar(self,inputChar):

        if(self.we_already_have_a_char):# There is a char left for process!
            self.we_already_have_a_char = False # We don't want to get in a loop!
            self.getChar(self.lastChar)

        if(self.state==0):
            if(inputChar=='/'):#Check for comments
                self.last_state=self.state
                self.state = 6
            elif(inputChar.isdigit()):
                self.tempStr += inputChar
                self.state = 2
            elif(inputChar.isalpha()):
                self.tempStr += inputChar
                self.state = 1
            elif (inputChar=='+' or inputChar=='-'):
                self.tempStr += inputChar
                self.state = 3
            elif (inputChar in startOfST):
                self.tempStr += inputChar
                self.state = 4
            elif (inputChar == "" or inputChar == None):
                return ("STOP","END OF FILE")
            else:
                self.tempStr = ""

        elif(self.state==1):#ID
            if (inputChar == '/'):  # Check for comments
                self.last_state = self.state
                self.state = 6
            elif(inputChar.isalpha() or inputChar.isdigit() or inputChar=='.'):
                self.tempStr += inputChar
            else:
                return self.constructToken(inputChar)

        elif(self.state==2):#Digit
            if (inputChar == '/'):  # Check for comments
                self.last_state = self.state
                self.state = 6
            elif (inputChar.isdigit()):
                self.tempStr += inputChar
            else:
                return self.constructToken(inputChar)

        elif(self.state==3):# +|-
            if (inputChar == '/'):  # Check for comments
                self.last_state = self.state
                self.state = 6
            elif (inputChar.isdigit() and not (self.last_constructed_token[0] == "ID" or
                                               self.last_constructed_token[0] == "INT")):# example c=1+1
                self.tempStr += inputChar
                self.state = 2
            elif(inputChar == '='):
                self.tempStr +=inputChar
                self.state = 4
            else:
                return self.constructToken(inputChar)

        elif(self.state==4):
            if (inputChar == '/'):  # Check for comments
                self.last_state = self.state
                self.state = 6
            elif (inputChar in endOfST):
                self.tempStr += inputChar
                self.state = 5
            else:
                return self.constructToken(inputChar)

        elif(self.state==5):
            if (inputChar == '/'):  # Check for comments
                self.last_state = self.state
                self.state = 6
            else:
                return self.constructToken(inputChar)

        # here is the comments section:
        elif(self.state==6):
            if(inputChar=='/'):
                self.state = 7
            elif (inputChar=='*'):
                self.state = 8
            else:# ERROR
                print "Error maybe in defining the comment"
                self.state = self.last_state

        elif(self.state==7):
            if(inputChar == '\n'):# back to work...
                self.state = self.last_state

        elif(self.state==8):
            if(inputChar == '*'):
                self.state = 9

        elif(self.state==9):
            if(inputChar == '/'):# back to work...
                self.state = self.last_state
            else:
                self.state = 8






