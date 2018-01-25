
PARSE_DBG = False
CODE_GENERATE_DBG = True

import Grammer
from Grammer import ll1ParseTable_with_codegens

codegen_inputs = {"#pid","#assign","#addIDToSymTable",
                  "#systemPrint","#pconst","#BOOL","#INT","#popSS","#enteredMain",
                  "#newCLSscope","#endCLSscope","#newFUNCScope","#endFUNCScope","#none",
                  "#insIDadd"

}

data_memory_iterator = 200 #The start of the dynamic memory is here
instruction_memory_block = 0
def alloc_4byte():
    global data_memory_iterator
    output = data_memory_iterator
    data_memory_iterator = data_memory_iterator + 4
    return output

def alloc_block():
    global instruction_memory_block
    output = instruction_memory_block
    instruction_memory_block = instruction_memory_block + 1
    return instruction_memory_block


CLSscop_list = []  # Where we keep all the scopes (class)
FUNCscop_list = []  # Where we keep all the scopes (function)


class CLSscop():# For classes
    """Saves the elements of a CLASS in a clean structure"""

    # To point to other scopes by there INDEX in CLSscop_list! (python has no pointers!!!)
    pointer=[]# These scopes share there identifier and functions with this scop
    id_elems=[]# the Identifiers
    func_elems = []  # the Identifiers

    def __init__(self, name, extension_index = None):
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
        for elem in self.id_elems:
            if (elem[0] == id_name):
                output = elem
                break
        if (output == None):
            for index in self.pointer:
                output = CLSscop_list[index].give_ID_elem(id_name)
                if (output != None):
                    break
        return output

    def add_FUNC(self, token, function_scop_index):
        self.func_elems.append((token[1], "FUNC", function_scop_index))

    def give_FUNC_elem(self,func_name):# Find a FUNC
        output = None
        for elem in self.func_elems:
            if (elem[0] == func_name):
                output = elem
                break
        if(output == None):
            for index in self.pointer:
                output = CLSscop_list[index].give_FUNC_elem(func_name)
                if (output != None):
                    break
        return None

    # def add_OBJ(self,token):
    #     self.elems.append(())
    # didn't mention that every thing was static :D

    #We do not use this function in a class scope :)
    # def add_CLS(self,token,class_scop_index):
    #     self.elems.append((token[1],"CLS",class_scop_index))

class FUNCscop():
    """Saves the elements of a FUNCTION and its subcode in a clean structure"""

    pointer=[]# to point to other scopes by there INDEX in CLSscop_list! (python has no pointers!!!)
    id_elems = []# The Identifiers
    func_elems = []# The functions
    code_block = []# contains the output code :D

    def __init__(self, name, parent_scop_index):
        self.pointer.append(parent_scop_index)
        self.name=name

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
        if(output == None):
            for index in self.pointer:
                output=CLSscop_list[index].give_ID_elem(id_name)
                if (output != None):
                    break
        return output

    def give_FUNC_elem(self,func_name):# Find a FUNC
        output = None
        # We don't have a function in a function scope!
        for index in self.pointer:
            output = CLSscop_list[index].give_FUNC_elem(func_name)
            if(output != None):
                break




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

    # Find the memory address of a given ID
    # We assume that this method is called in a function scope (it really is)
    def findaddr(self,input_ID,func_scop_index):
        elem = FUNCscop_list[func_scop_index].give_ID_elem(input_ID)
        if(elem == None):
            return None
        return elem[2]# the address given from alloc_4byte()

    CLSscope_index = -1
    FUNscope_index = -1

    in_func_scope = False
    PB=[]# Program Block
    PC=0
    start_writing_in_PB = False
    SS=[]# Semantic Stack

    def codegen(self,action):# Generate the final code and save in PB[]
        if(action=="#pid"):# the input could be a class name or a functon name or an ID name...
            self.SS.append(self.current_token[1])
        elif(action=="#insIDadd"):
            if (self.in_func_scope):
                ID_tuple=FUNCscop_list[self.FUNscope_index].give_ID_elem(self.SS[-1])
            else:
                ID_tuple=CLSscop_list[self.CLSscope_index].give_ID_elem(self.SS[-1])

            if(ID_tuple==None):#ERROR semantic
                print "Undefined identifier: " + self.SS[-1]
                return
            self.SS.pop()
            self.SS.append(ID_tuple[2])
        elif(action=="#pconst"):
            self.SS.append("#" + str(self.current_token[1]))
        elif(action=="#assign"):
            self.PB.append(("ASSIGN",self.SS[-1],self.SS[-2],None))
            self.PC = self.PC + 1
            self.SS.pop()
            self.SS.pop()
        elif(action=="#addIDToSymTable"):
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
        elif(action=="#INT"):
            self.SS.append("int")
        elif(action=="#BOOL"):
            self.SS.append("boolean")
        elif(action=="#popSS"):
            # self.SS.pop()
            pass
        elif(action=="#enteredMain"):
            self.start_writing_in_PB = True
            self.in_func_scope = True
            FUNCscop_list.append(FUNCscop("_MAIN",None))
            self.CLSscope_index = self.CLSscope_index + 1
        elif(action=="#newCLSscope"):
            if(self.SS[-1] != None):# The class has an extension
                CLSscop_list.append(CLSscop(self.SS[-2],CLSscop(self.SS[-1])))
            else:
                CLSscop_list.append(CLSscop(self.SS[-2]))
            self.CLSscope_index = self.CLSscope_index + 1
            self.SS.pop()
            self.SS.pop()
        elif(action=="#none"):
            self.SS.append(None)


        if CODE_GENERATE_DBG:
            print "called " + action
            print self.current_token


    # using a list as stack:
    stack = ['$',"Goal"]
    # last2_token = None
    # last1_token = None
    current_token = None

    def get_token(self,token):
        if(token[0]=='STOP'):
            print token[1]
            return

        # self.last2_token = self.last1_token
        # self.last1_token = self.current_token
        self.current_token = token
        input_term = token_to_terminal(token)
        # print token,input_term

        while(self.stack[-1] != '$'):
            if(self.stack[-1] in Grammer.terminals):
                if(self.stack[-1] == input_term):
                    if PARSE_DBG:
                        print "accepted: " + self.stack[-1]
                    self.stack.pop()
                    break
                else:# Oh no an ERROR!!!
                    print "ERROR stack top is: " + self.stack[-1]
                    print "and input term is: " + input_term
                    break
            elif(self.stack[-1] in Grammer.non_terminals or self.stack[-1] in Grammer.added_non_terminals):
                if( ll1ParseTable_with_codegens.has_key((self.stack[-1],input_term)) ):
                    temp_to_get_in_stack = ll1ParseTable_with_codegens[(self.stack[-1],input_term)]
                    if PARSE_DBG:
                        print "Reduced " + self.stack[-1]
                    self.stack.pop()
                    self.stack.extend(temp_to_get_in_stack[::-1])
                    if(self.stack[-1] == 'epsilon'):
                        self.stack.pop()
                    # print self.stack[-1]
                else:# ERROR we the LL(1) table is empty :(
                    print "ERROR LL(1) is empty..."
                    print (self.stack[-1],input_term)
                    break
            elif(self.stack[-1] in codegen_inputs):
                self.codegen(self.stack.pop())
                # print "GOT " + self.stack[-1]
            else:
                print "ERROR top of the stack is neither a codegen_input, terminal nor non-terminal :" + self.stack[-1]
                break

            # Check for a code generator element on top of the stack (with #)
        print self.SS













