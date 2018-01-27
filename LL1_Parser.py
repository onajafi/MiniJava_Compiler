
PARSE_DBG = False
CODE_GENERATE_DBG = True

USING_PanicMode = True

data_memory_iterator = 2000 #The start of the dynamic memory is here
stack_memory_start = 4000 #The start of the stack in memory
stack_pointer = 3996#The stack pointer (SP)

import Grammer
from Grammer import ll1ParseTable_with_codegens

codegen_inputs = {"#pid","#assign","#addIDToSymTable",
                  "#systemPrint","#pconst","#BOOL","#INT","#popSS","#enteredMain",
                  "#newCLSscope","#endCLSscope","#newFUNCScope","#endFUNCScope","#none",
                  "#insIDadd","#GenTheCode","#pCLS_ID","#pCLS_FUNC",
                  "#MULT","#ADD","#SUB",
                  "#genIf","#genElse","#endIf",
                  "#LT","#EQ","#andRelTerms",
                  "#pBOOLconst",
                  "#SAVE_PC","#genWhile","#endWhile",
                  "#genFor","#endFor",
                  "#genFunc","#endFunc",
                  "#callFUNC","#endCallFUNC"

}


def alloc_4byte():
    global data_memory_iterator
    output = data_memory_iterator
    data_memory_iterator = data_memory_iterator + 4
    return output



CLSscop_list = []  # Where we keep all the scopes (class)
FUNCscop_list = []  # Where we keep all the scopes (function)

def give_CLS_index(CLS_name):
    for index,elem in enumerate(CLSscop_list):
        if elem.name == CLS_name:
            return index
    return None

class CLSscop():# For classes
    """Saves the elements of a CLASS in a clean structure"""

    def __init__(self, name, extension_index = None):
        # To point to other scopes by there INDEX in CLSscop_list! (python has no pointers!!!)
        self.pointer=[]# These scopes share there identifier and functions with this scop
        self.id_elems=[]# the Identifiers
        self.func_indx = []  # the Identifiers
        self.name=name
        if(extension_index):
            self.pointer.append(extension_index)

    def add_ID(self,type,id_name):# INT|BOOLEAN
        if(type=="int"):
            self.id_elems.append((id_name,"INT",alloc_4byte()))
        elif(type=="boolean"):
            self.id_elems.append((id_name,"BOOL",alloc_4byte()))
        else:# ERROR
            print "Undefined Type " + type

    def give_ID_elem(self, id_name):  # Find an ID
        output = None  # the element tuple goes here
        for elem in self.id_elems:# Check in current scope
            if (elem[0] == id_name):
                output = elem
                break
        if (output == None):# Check in parents
            for index in self.pointer:
                output = CLSscop_list[index].give_ID_elem(id_name)
                if (output != None):
                    break
        return output

    def add_FUNC_idx(self,function_scop_index):
        self.func_indx.append(function_scop_index)

    def give_FUNC_Index(self,func_name):
        output = None
        for idx in self.func_indx:
            if (FUNCscop_list[idx].name == func_name):
                output = idx
                break
        if (output == None):
            for index in self.pointer:
                output = CLSscop_list[index].give_FUNC_Index(func_name)
                if (output != None):
                    break
        return output

    # def give_FUNC_elem(self,func_name):# Find a FUNC
    #     output = None
    #     for elem in self.func_elems:
    #         if (elem[0] == func_name):
    #             output = elem
    #             break
    #     if(output == None):
    #         for index in self.pointer:
    #             output = CLSscop_list[index].give_FUNC_elem(func_name)
    #             if (output != None):
    #                 break
    #     return output

    # def add_OBJ(self,token):
    #     self.elems.append(())
    # didn't mention that every thing was static :D

    #We do not use this function in a class scope :)
    # def add_CLS(self,token,class_scop_index):
    #     self.elems.append((token[1],"CLS",class_scop_index))

class FUNCscop():
    """Saves the elements of a FUNCTION and its subcode in a clean structure"""

    def __init__(self, name, parent_scop_index):
        self.pointer = []  #To point to other scopes by there INDEX in CLSscop_list! (python has no pointers!!!)
        self.id_elems = []  #The Identifiers
        self.code_block = []  #Contains the output code :D
        self.param_inputs_CNT = 0
        self.vars_CNT = 0
        self.return_type = None
        self.name=name
        self.address=0

        self.pointer.append(parent_scop_index)

    def add_ID(self,type,id_name):# INT|BOOLEAN
        if(type=="int"):
            self.id_elems.append((id_name,"INT",alloc_4byte()))
        elif(type=="boolean"):
            self.id_elems.append((id_name,"BOOL",alloc_4byte()))
        else:# ERROR
            print "Undefined Type " + type

    def give_ID_elem(self,id_name):# Find an ID
        output = None# the element tuple goes here
        for elem in self.id_elems:
            if(elem[0]==id_name):
                output = elem
                break
        if(output == None and self.name != "_MAIN"):
            for index in self.pointer:
                output=CLSscop_list[index].give_ID_elem(id_name)
                if (output != None):
                    break
        return output


    # def give_FUNC_elem(self,func_name):# Find a FUNC
    #     output = None
    #     # We don't have a function in a function scope!
    #     for index in self.pointer:
    #         output = CLSscop_list[index].give_FUNC_elem(func_name)
    #         if(output != None):
    #             break


def token_to_terminal(token):
    if(token[0]=='Key'):
        return token[1]
    elif(token[0]=='ID'):
        return 'identifier'
    elif(token[0]=='INT'):
        return 'integer'
    elif(token[0]=='Opr'):
        return token[1]
    elif(token[0]=='ST'):
        return token[1]
    return None

class Parser():
    """Receives every token and parses the inputs"""

    abort = False# Will go True if there is an error

    # Find the memory address of a given ID
    # We assume that this method is called in a function scope (it really is)
    def findaddr(self,input_ID,func_scop_index):
        elem = FUNCscop_list[func_scop_index].give_ID_elem(input_ID)
        if(elem == None):
            return None
        return elem[2]# the address given from alloc_4byte()

    CLSscope_index = -1
    FUNscope_index = -1

    Error_CNT = 0#Counting the errors (which are recovered by panic mode)

    in_func_scope = False
    PB=[]# Program Block
    PC=0
    SS=[]# Semantic Stack

    #These codes have to be called at the start of the program (start of main CLS)
    def gen_initial_code(self):
        self.PB.append(("ASSIGN",'#' + str(stack_memory_start),stack_pointer,None))
        self.PC = self.PC + 1

    #Generates a code that pushes the value in the src address to the stack
    def gen_push_stack(self,src):
        self.PB.append(("ASSIGN",src,"@"+str(stack_pointer),None))
        self.PC = self.PC + 1
        self.PB.append(("ADD",stack_pointer,"#4",stack_pointer))
        self.PC = self.PC + 1
    def gen_pop_stack(self,dst):
        self.PB.append(("SUB", stack_pointer, "#4", stack_pointer))
        self.PC = self.PC + 1
        self.PB.append(("ASSIGN","@"+str(stack_pointer),dst,None))
        self.PC = self.PC + 1
    def gen_read_stack(self,dst_add,index):#index should be minus and -1 shows the top of stack
        tempaddr = alloc_4byte()
        self.PB.append(("ADD", stack_pointer, '#'+str(4*index), tempaddr))
        self.PC = self.PC + 1
        self.PB.append(("ASSIGN", '@'+str(tempaddr), dst_add, None))
        self.PC = self.PC + 1



    def codegen(self,action):# Generate the final code and save in PB[]
        if CODE_GENERATE_DBG:
            print "___________________"
            print "called " + action
            print "Current token:" , self.current_token
            print "SS:" , self.SS
            # print "Parser stack:", self.stack

        if(action=="#pid"):# the input could be a class name or a functon name or an ID name...
            self.SS.append(self.current_token[1])
        elif(action=="#insIDadd"):# Put the address of an Id in the scope instead of there name
            if (self.in_func_scope):
                ID_tuple=FUNCscop_list[self.FUNscope_index].give_ID_elem(self.SS[-1])
            else:
                ID_tuple=CLSscop_list[self.CLSscope_index].give_ID_elem(self.SS[-1])

            if(ID_tuple==None):#ERROR semantic
                print "Undefined identifier: " + self.SS[-1] + "\nAborted parsing..."
                self.abort = True
                return
            self.SS.pop()
            self.SS.append(ID_tuple[1])# Here we put the address
            self.SS.append(ID_tuple[2])# Here we put the address
        elif(action=="#pconst"):
            self.SS.append("INT")
            self.SS.append("#" + str(self.current_token[1]))
        elif(action=="#assign"):
            if(self.SS[-2] not in ("BOOL","INT") or self.SS[-4] not in ("BOOL","INT")
               or self.SS[-2] == self.SS[-4]):# Chaecking the types!!! ("BOOL","INT")
                self.PB.append(("ASSIGN",self.SS[-1],self.SS[-3],None))
                self.PC = self.PC + 1
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
            else:#ERROR semantic
                print "can't assign two different type: BOOL and INT"
                print "Aborted parsing..."
                self.abort=True
        elif(action=="#addIDToSymTable"):# Add an entry to the symbol table
            if(self.in_func_scope):
                FUNCscop_list[self.FUNscope_index].add_ID(self.SS[-2],self.SS[-1])
            else:
                CLSscop_list[self.CLSscope_index].add_ID(self.SS[-2],self.SS[-1])
            self.SS.pop()
            self.SS.pop()
        elif(action=="#systemPrint"):
            self.PB.append(("PRINT",self.SS[-1],None,None))
            self.PC = self.PC + 1
            self.SS.pop()
            self.SS.pop()
        elif(action=="#INT"):
            self.SS.append("int")
        elif(action=="#BOOL"):
            self.SS.append("boolean")
        elif(action=="#popSS"):
            # self.SS.pop()
            pass
        elif(action=="#enteredMain"):
            self.in_func_scope = True
            FUNCscop_list.append(FUNCscop(self.SS[-1],None))
            self.SS.pop()
            self.CLSscope_index = self.CLSscope_index + 1
            self.FUNscope_index = self.FUNscope_index + 1
            #Cleaning the Code Block to put the new function codes in it
            self.PB = []
            self.PC = 0
            #Now we should add the init codes:
            self.gen_initial_code()
        elif(action=="#newCLSscope"):
            if(self.SS[-1] != None):# The class has an extension
                the_parent_CLS_index = give_CLS_index(self.SS[-1])
                if(the_parent_CLS_index != None):
                    CLSscop_list.append(CLSscop(self.SS[-2],the_parent_CLS_index))
                else:# ERROR semantic
                    print "The extension " + self.SS[-1] + " was not found\nAborted parsing..."
                    self.abort = True

            else:
                CLSscop_list.append(CLSscop(self.SS[-2]))
            self.CLSscope_index = self.CLSscope_index + 1
            self.SS.pop()
            self.SS.pop()
        elif(action=="#none"):
            self.SS.append(None)
        elif(action=="#GenTheCode"):
            self.PB.append((None,None,None,None))
            CodeLength=len(self.PB)
            Exit_comm_index = CodeLength - 1

            start_list = [0]
            for i in range(0,len(FUNCscop_list)):
                FUNCscop_list[i].address = CodeLength
                self.PB.extend(FUNCscop_list[i].code_block)
                CodeLength=len(self.PB)
                start_list.append(CodeLength)

            print "Code length:",CodeLength

            i = 0
            while (i < start_list[1]):
                if (isinstance(self.PB[i][1], tuple)):
                    if (self.PB[i][1][0] == '^'):
                        self.PB[i] = (
                        self.PB[i][0], "#" + str(self.PB[i][1][1]),
                        self.PB[i][2],
                        self.PB[i][3])
                    elif (self.PB[i][1][0] == '*'):
                        self.PB[i] = (
                        self.PB[i][0], FUNCscop_list[self.PB[i][1][1]].address,
                        self.PB[i][2],
                        self.PB[i][3])
                if (isinstance(self.PB[i][2], tuple)):
                    if (self.PB[i][2][0] == '^'):
                        self.PB[i] = (
                        self.PB[i][0],
                        self.PB[i][1], "#" + str(self.PB[i][2][1]),
                        self.PB[i][3])
                    elif (self.PB[i][2][0] == '*'):
                        self.PB[i] = (
                        self.PB[i][0],
                        self.PB[i][1], FUNCscop_list[self.PB[i][2][1]].address,
                        self.PB[i][3])
                i = i + 1
                print i
            for idx in range(1,len(FUNCscop_list)):
                while(i<start_list[idx+1]):
                    if(isinstance(self.PB[i][1],tuple)):
                        if(self.PB[i][1][0]=='^'):
                            self.PB[i] = (self.PB[i][0], "#"+str(FUNCscop_list[idx].address+self.PB[i][1][1]),self.PB[i][2],self.PB[i][3])
                        elif(self.PB[i][1][0]=='*'):
                            self.PB[i] = (self.PB[i][0], FUNCscop_list[self.PB[i][1][1]].address, self.PB[i][2], self.PB[i][3])
                        # elif(self.PB[i][1][0]=='#^'):
                        #     self.PB[i] = (self.PB[i][0], "#"+str(FUNCscop_list[idx].address + self.PB[i][1][1]), self.PB[i][2], self.PB[i][3])
                    if (isinstance(self.PB[i][2], tuple)):
                        if (self.PB[i][2][0] == '^'):
                            self.PB[i] = (self.PB[i][0], self.PB[i][1], "#"+str(FUNCscop_list[idx].address + self.PB[i][2][1]),self.PB[i][3])
                        elif (self.PB[i][2][0] == '*'):
                            self.PB[i] = (self.PB[i][0], self.PB[i][1], FUNCscop_list[self.PB[i][2][1]].address, self.PB[i][3])
                        # elif (self.PB[i][2][0] == '#^'):
                        #     self.PB[i] = (self.PB[i][0], self.PB[i][1], "#"+str(FUNCscop_list[idx].address + self.PB[i][2][1]), self.PB[i][3])
                    i = i+1
            self.PB[Exit_comm_index] = ("JP",CodeLength,None,None)

            print "\nFinished Compilation with " + str(self.Error_CNT) \
                  + " warnings (Panic mode recoveries)"
        elif(action=="#pCLS_ID"):# For finding the address of: identifier.identifier
            the_CLS_index = give_CLS_index(self.SS[-2])
            if (the_CLS_index != None):
                the_elem = CLSscop_list[the_CLS_index].give_ID_elem(self.SS[-1])
                if(the_elem != None):
                    self.SS.pop()
                    self.SS.pop()
                    self.SS.append(the_elem[1])
                    self.SS.append(the_elem[2])
                else:#ERROR semantic
                    print "There is no variable or function in the class " + self.SS[-2] \
                          + " scope, named: " + self.SS[-1]
                    print "Aborted parsing..."
                    self.abort = True
            else:#ERROR semantic
                print "There is no defined class named " + self.SS[-2] + "\nAborted parsing..."
                self.abort = True
        elif(action=="#MULT"):
            if(self.SS[-2] != "BOOL" and self.SS[-4] != "BOOL"):
                temp_WORD = alloc_4byte()
                self.PB.append(("MULT", self.SS[-1], self.SS[-3], temp_WORD))
                self.PC = self.PC + 1
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.append("INT")
                self.SS.append(temp_WORD)
            else:#ERROR semantic
                print "Can't multiply booleans !!!"
                print "Aborted parsing..."
                self.abort=True
        elif(action=="#ADD"):
            if (self.SS[-2] != "BOOL" and self.SS[-4] != "BOOL"):
                temp_WORD = alloc_4byte()
                self.PB.append(("ADD", self.SS[-1], self.SS[-3], temp_WORD))
                self.PC = self.PC + 1
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.append("INT")
                self.SS.append(temp_WORD)
            else:  # ERROR semantic
                print "Can't do addition on booleans !!!"
                print "Aborted parsing..."
                self.abort = True
        elif(action=="#SUB"):
            if (self.SS[-2] != "BOOL" and self.SS[-4] != "BOOL"):
                temp_WORD = alloc_4byte()
                self.PB.append(("SUB", self.SS[-3], self.SS[-1], temp_WORD))
                self.PC = self.PC + 1
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.append("INT")
                self.SS.append(temp_WORD)
            else:  # ERROR semantic
                print "Can't do subtraction on booleans !!!"
                print "Aborted parsing..."
                self.abort = True
        elif(action=="#LT"):
            if (self.SS[-2] != "BOOL" and self.SS[-4] != "BOOL"):
                temp_WORD = alloc_4byte()
                self.PB.append(("LT", self.SS[-3], self.SS[-1], temp_WORD))
                self.PC = self.PC + 1
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.append("BOOL")
                self.SS.append(temp_WORD)
            else:  # ERROR semantic
                print "Can't comapare booleans !!!"
                print "Aborted parsing..."
                self.abort = True
        elif(action=="#EQ"):
            temp_WORD = alloc_4byte()
            self.PB.append(("EQ", self.SS[-3], self.SS[-1], temp_WORD))
            self.PC = self.PC + 1
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
            self.SS.append("BOOL")
            self.SS.append(temp_WORD)
        elif(action=="#andRelTerms"):
            if (self.SS[-2] != "INT" and self.SS[-4] != "INT"):
                temp_WORD = alloc_4byte()
                self.PB.append(("AND", self.SS[-3], self.SS[-1], temp_WORD))
                self.PC = self.PC + 1
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.pop()
                self.SS.append("BOOL")
                self.SS.append(temp_WORD)
            else:  # ERROR semantic
                print "Can't use an integer in a logical operation"
                print "Aborted parsing..."
                self.abort = True
        elif(action=="#genIf"):
            self.SS.append(self.PC)# Saving the address space for JPF command
            self.PB.append(None)# We will fill this in #genElse
            self.PC = self.PC + 1
        elif(action=="#genElse"):
            self.PB[self.SS[-1]] = ("JPF",('^',self.SS[-2]),self.PC+1,None)# We want it to jump to PC+1 because this line should not be called if we go in else
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
            self.SS.append(self.PC)# Saving the address space for JP command
            self.PB.append(None)# We will fill this in #endIf
            self.PC = self.PC + 1
        elif(action=="#endIf"):
            self.PB[self.SS[-1]] = ("JP",('^',self.PC),None,None)
            self.SS.pop()
        elif(action=="#pBOOLconst"):
            self.SS.append("BOOL")
            if(self.current_token[1]=='false'):
                self.SS.append("#0")
            else:# self.current_token[1]=='true'
                self.SS.append("#1")
        elif(action=="#SAVE_PC"):
            self.SS.append(self.PC)
        elif(action=="#genWhile"):
            self.SS.append(self.PC)  # Saving the address space for JPF command
            self.PB.append(None)  # We will fill this in #endWhile
            self.PC = self.PC + 1
        elif(action=="#endWhile"):
            self.PB[self.SS[-1]] = ("JPF",('^',self.SS[-2]),self.PC+1,None)#We want it to jump to PC+1 when the RelTerm is false
            self.PB.append(("JP",('^',self.SS[-4]),None,None))
            self.PC = self.PC + 1
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
        elif(action=="#genFor"):
            self.SS.append(self.PC)  # Saving the address space for JPF command
            self.PB.append(None)  # We will fill this in #endFor
            self.PC = self.PC + 1
        elif(action=="#endFor"):
            self.PB.append(("ADD",self.SS[-3],self.SS[-1],self.SS[-3]))
            self.PC = self.PC + 1
            self.PB[self.SS[-5]] = ("JPF",('^',self.SS[-6]),self.PC+1,None)#We want it to jump to PC+1 when the RelTerm is false
            self.PB.append(("JP",('^',self.SS[-8]),None,None))
            self.PC = self.PC + 1
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
            self.SS.pop()
        elif(action=="#genFunc"):
            self.in_func_scope = True
            #Adding function to FUNC list
            FUNCscop_list.append(FUNCscop(self.SS[-1], None))
            self.FUNscope_index = self.FUNscope_index + 1
            #Adding FUNC to the class
            CLSscop_list[self.CLSscope_index].add_FUNC_idx(self.FUNscope_index)

            if(self.SS[-2]=="int"):
                FUNCscop_list[self.FUNscope_index].return_type = "INT"
            else:#if(self.SS[-2]=="boolean"):
                FUNCscop_list[self.FUNscope_index].return_type = "BOOL"
            self.SS.pop()
            self.SS.pop()
            # Cleaning the Code Block to put the new function codes in it; will be saved later in endFunc
            self.PB = []
            self.PC = 0
            # generate the parameter reading code:
            pass
        elif(action=="#endFunc"):
            #Check if return type is same with the function output type:
            if((self.SS[-2] in ("BOOL","INT")) and FUNCscop_list[self.FUNscope_index].return_type != self.SS[-2]):#ERROR semantic
                print "In " + FUNCscop_list[self.FUNscope_index].name + " the return type is diffrent with the specified one"
                print "Aborted parsing..."
                self.abort = True
            self.gen_push_stack(self.SS[-1])#Saving the return value of the function
            self.SS.pop()
            self.SS.pop()

            temp_ret_add=alloc_4byte()
            self.gen_read_stack(temp_ret_add,-2)
            #Now we just need to jump to where <temp_ret_add> is showing
            self.PB.append(("JP","@"+str(temp_ret_add),None,None))
            self.PC = self.PC + 1

            #The code has been completed we just have to copy it to the function scope:
            FUNCscop_list[self.FUNscope_index].code_block = self.PB
            self.in_func_scope = False
        elif(action=="#callFUNC"):
            #Generate code for storing params in the stack:
            pass
            #Saving the return place after calling the function
            self.gen_push_stack(("^",self.PC+3))# '^' means to add the start of the current function block address to the next param

            the_CLS_index = give_CLS_index(self.SS[-2])
            if(the_CLS_index != None):
                the_FUNC_idx = CLSscop_list[the_CLS_index].give_FUNC_Index(self.SS[-1])
                if(the_FUNC_idx != None):
                    # Saving function index we have to change the tuple with the start of functions block address
                    self.PB.append(("JP", ("*", the_FUNC_idx), None,None))
                    self.PC = self.PC + 1
                    self.SS.pop()
                    self.SS.pop()
                else:#ERROR semantic
                    print "There is no function defenition in class " + self.SS[-2] + " named " + self.SS[-1]
                    print "Aborted parsing..."
                    self.abort = True
            else:#ERROR semantic
                print "There is no defined class called: " + self.SS[-2]
                print "Aborted parsing..."
                self.abort = True


        elif(action=="#endCallFUNC"):
            temp_ret_val = alloc_4byte()
            self.gen_pop_stack(temp_ret_val)
            self.SS.append(None)  # Don't know the return type
            self.SS.append(temp_ret_val)




    # using a list as stack:
    stack = ['$',"Goal"]
    current_token = None

    def get_token(self,token):
        if(token[0]=='STOP'):
            print token[1]
            return

        self.current_token = token
        input_term = token_to_terminal(token)

        while((not self.abort) and self.stack[-1] != '$'):
            if(self.stack[-1] in Grammer.terminals):
                if(self.stack[-1] == input_term):
                    if PARSE_DBG:
                        print "accepted: " + self.stack[-1]
                    self.stack.pop()
                    break
                else:# Oh no an ERROR!!!
                    self.Error_CNT = self.Error_CNT + 1
                    print "\nERROR stack top is: " + self.stack[-1]
                    print "and input term is: " + input_term
                    if USING_PanicMode:
                        print "Using Panic Mode error recovery:"
                        print "Poping: " + self.stack.pop()
                    else:
                        break
            elif(self.stack[-1] in Grammer.non_terminals or self.stack[-1] in Grammer.added_non_terminals):
                if( ll1ParseTable_with_codegens.has_key((self.stack[-1],input_term))
                    and ll1ParseTable_with_codegens[(self.stack[-1],input_term)] != ["--SYNCH--"]):
                    temp_to_get_in_stack = ll1ParseTable_with_codegens[(self.stack[-1],input_term)]
                    if PARSE_DBG:
                        print "Reduced " + self.stack[-1]
                    self.stack.pop()
                    self.stack.extend(temp_to_get_in_stack[::-1])
                    if(self.stack[-1] == 'epsilon'):
                        self.stack.pop()
                    # print self.stack[-1]
                elif(ll1ParseTable_with_codegens.has_key((self.stack[-1],input_term))
                    and ll1ParseTable_with_codegens[(self.stack[-1],input_term)] == ["--SYNCH--"]):# LL(1) table shows a SYNCH
                    self.Error_CNT = self.Error_CNT + 1
                    print "\nERROR LL(1) table is shows Synch"
                    print "The table Entry is:", (self.stack[-1], input_term)
                    if USING_PanicMode:
                        print "Using Panic Mode error recovery:"
                        print "Poping: " + self.stack.pop()
                    else:
                        break
                else:# ERROR we the LL(1) table is empty :(
                    self.Error_CNT = self.Error_CNT + 1
                    print "\nERROR LL(1) table is empty..."
                    print "The table Entry is:", (self.stack[-1],input_term)
                    if USING_PanicMode:
                        print "Using Panic Mode error recovery:"
                        print "Skipping input token:", self.current_token
                        break#Getting out of the loop
                    else:
                        break
            elif(self.stack[-1] in codegen_inputs):
                self.codegen(self.stack.pop())
                # print "GOT " + self.stack[-1]
            else:#If we reach here, there is a problem from the compiler
                print "ERROR top of the stack is neither a codegen_input, terminal nor non-terminal :" + self.stack[-1]
                break
















