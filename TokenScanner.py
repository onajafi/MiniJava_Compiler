

keys={"EOF","public","class","Identifier","static",
      "void","main","extends","return","boolean",
      "int","if","else","while","for","Integer",
      "true","false","identifier","integer"}

class tokenScanner():
    """Receives every character and
    gives out the token"""

    state=0
    tempStr=""
    def getChar(self,inputChar):
        if(self.state==0):
            if(inputChar.isdigit()):
                self.tempStr += inputChar
                self.state = 1
            elif(inputChar.isalpha()):
                self.state = 2
        elif(self.state==1):
            pass
        elif(self.state==2):
            pass

