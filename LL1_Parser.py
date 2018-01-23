
import Grammer

# Thanks to JFLAP for this parse table :)
# The parse table works as a dictionary with
# tuple type keys:
ll1ParseTable = {("GenExpression",'('):["Expression","N_PRIME"],
                ("Expression",'('):["Term","C_PRIME"],
                ("Term",'('):["Factor","E_PRIME"],
                ("Factor",'('):['(',"Expression",')'],
                ("RelExpression",'('):["RelTerm","D_PRIME"],
                ("RelTerm",'('):["Expression","L_PRIME"],
                ("Arguments",'('):["GenExpression","Argument"],
                ("H_PRIME",'('):['(',"Arguments",')'],

                ("Parameters",')'):['epsilon'],
                ("Parameter",')'):['epsilon'],
                ("Arguments",')'):['epsilon'],
                ("Argument",')'):['epsilon'],
                ("C_PRIME",')'):['epsilon'],
                ("D_PRIME",')'):['epsilon'],
                ("E_PRIME",')'):['epsilon'],
                ("G_PRIME",')'):['epsilon'],
                ("H_PRIME",')'):['epsilon'],
                ("N_PRIME",')'):['epsilon'],

                ("E_PRIME",'*'):['*',"Factor","E_PRIME"],
                ("G_PRIME",'*'):['epsilon'],
                ("H_PRIME",'*'):['epsilon'],

                ("C_PRIME",'+'):['+',"Term","C_PRIME"],
                ("E_PRIME",'+'):['epsilon'],
                ("G_PRIME",'+'):['epsilon'],
                ("H_PRIME",'+'):['epsilon'],

                ("Parameter",','):[',',"Type","Identifier","Parameter"],
                ("Argument",','):[',',"GenExpression","Argument"],
                ("C_PRIME",','):['epsilon'],
                ("D_PRIME",','):['epsilon'],
                ("E_PRIME",','):['epsilon'],
                ("G_PRIME",','):['epsilon'],
                ("H_PRIME",','):['epsilon'],
                ("N_PRIME",','):['epsilon'],

                ("C_PRIME",'-'):['-',"Term","C_PRIME"],
                ("E_PRIME",'-'):['epsilon'],
                ("G_PRIME",'-'):['epsilon'],
                ("H_PRIME",'-'):['epsilon'],

                ("G_PRIME",'.'):['.','identifier',"H_PRIME"],

                ("C_PRIME",';'):['epsilon'],
                ("D_PRIME",';'):['epsilon'],
                ("E_PRIME",';'):['epsilon'],
                ("G_PRIME",';'):['epsilon'],
                ("H_PRIME",';'):['epsilon'],
                ("N_PRIME",';'):['epsilon'],

                ("C_PRIME",'<'):['epsilon'],
                ("E_PRIME",'<'):['epsilon'],
                ("G_PRIME",'<'):['epsilon'],
                ("H_PRIME",'<'):['epsilon'],
                ("L_PRIME",'<'):['<',"Expression"],
                ("N_PRIME",'<'):["L_PRIME","D_PRIME"],

                ("Goal",'public'):["Source",'EOF'],
                ("Source", 'public'): ["ClassDeclarations", "MainClass"],
                ("MainClass", 'public'): ['public', 'class',
                                          "Identifier",'{','public',
                                          'static','void','main','(',
                                          ')','{',"VarDeclarations","Statements",
                                          '}','}'],
                ("ClassDeclarations", 'public'): ['epsilon'],
                ("FieldDeclarations", 'public'): ['epsilon'],
                ("MethodDeclarations", 'public'): ["MethodDeclaration", "MethodDeclarations"],
                ("MethodDeclaration", 'public'): ['public','static',
                                                  "Type","Identifier",
                                                  '(',"Parameters",')',
                                                  '{',"VarDeclarations",
                                                  "Statements",'return',
                                                  "GenExpression",';','}'],

                ("Goal",'class'):["Source",'EOF'],
                ("Source", 'class'): ["ClassDeclarations", "MainClass"],
                ("ClassDeclarations", 'class'): ["ClassDeclaration","ClassDeclarations"],
                ("ClassDeclaration", 'class'): ['class',"Identifier","Extension",
                                                '{',"FieldDeclarations","MethodDeclarations",
                                                '}'],

                ("GenExpression", 'true'): ["Expression", "N_PRIME"],
                ("Expression", 'true'): ["Term", "C_PRIME"],
                ("Term", 'true'): ["Factor", "E_PRIME"],
                ("Factor", 'true'): ['true'],
                ("RelExpression",'true'):["RelTerm","D_PRIME"],
                ("RelTerm",'true'):["Expression","L_PRIME"],
                ("Arguments",'true'):["GenExpression","Argument"],

                ("FieldDeclarations",'static'):["FieldDeclaration","FieldDeclarations"],
                ("FieldDeclaration",'static'):['static',"Type","Identifier",';'],

                ("GenExpression", 'false'): ["Expression", "N_PRIME"],
                ("Expression", 'false'): ["Term", "C_PRIME"],
                ("Term", 'false'): ["Factor", "E_PRIME"],
                ("Factor", 'false'): ['false'],
                ("RelExpression",'false'):["RelTerm","D_PRIME"],
                ("RelTerm",'false'):["Expression","L_PRIME"],
                ("Arguments",'false'):["GenExpression","Argument"],

                ("C_PRIME",'&&'):['epsilon'],
                ("D_PRIME",'&&'):['&&',"RelTerm","D_PRIME"],
                ("E_PRIME",'&&'):['epsilon'],
                ("G_PRIME",'&&'):['epsilon'],
                ("H_PRIME",'&&'):['epsilon'],

                ("C_PRIME",'=='):['epsilon'],
                ("E_PRIME",'=='):['epsilon'],
                ("G_PRIME",'=='):['epsilon'],
                ("H_PRIME",'=='):['epsilon'],
                ("L_PRIME",'=='):['==',"Expression"],
                ("N_PRIME",'=='):["L_PRIME","D_PRIME"],

                ("Extension",'extends'):['extends',"Identifier"],

                ("VarDeclarations",'return'):['epsilon'],
                ("Statements",'return'):['epsilon'],

                ("VarDeclarations",'boolean'):["VarDeclaration","VarDeclarations"],
                ("VarDeclaration",'boolean'):["Type","Identifier",';'],
                ("Parameters",'boolean'):["Type","Identifier","Parameter"],
                ("Type",'boolean'):['boolean'],

                ("VarDeclarations", 'int'): ["VarDeclaration", "VarDeclarations"],
                ("VarDeclaration", 'int'): ["Type", "Identifier", ';'],
                ("Parameters", 'int'): ["Type", "Identifier", "Parameter"],
                ("Type",'int'):['int'],

                ("VarDeclarations",'if'):['epsilon'],
                ("Statements",'if'):["Statement","Statements"],
                ("Statement",'if'):['if','(',"GenExpression",')',
                                    "Statement",'else',"Statement"],

                ("VarDeclarations",'while'):['epsilon'],
                ("Statements",'while'):["Statement","Statements"],
                ("Statement",'while'):['while','(',"GenExpression",')',
                                       "Statement"],

                ("VarDeclarations",'for'):['epsilon'],
                ("Statements",'for'):["Statement","Statements"],
                ("Statement",'for'):['for','(',"Identifier",
                                     '=',"Integer",';',"RelTerm",';',
                                     "Identifier",'+=',"Integer",')',
                                     "Statement"],

                ("GenExpression", 'integer'): ["Expression", "N_PRIME"],
                ("Expression", 'integer'): ["Term", "C_PRIME"],
                ("Term", 'integer'): ["Factor", "E_PRIME"],
                ("Factor",'integer'):["Integer"],
                ("RelExpression",'integer'):["RelTerm","D_PRIME"],
                ("RelTerm",'integer'):["Expression","L_PRIME"],
                ("Arguments",'integer'):["GenExpression","Argument"],
                ("Integer",'integer'):['integer'],

                ("VarDeclarations",'System.out.println'):['epsilon'],
                ("Statements",'System.out.println'):["Statement","Statements"],
                ("Statement",'System.out.println'):['System.out.println','(',
                                                    "GenExpression",')',';'],

                ("VarDeclarations",'identifier'):['epsilon'],
                ("Statements",'identifier'):["Statement","Statements"],
                ("Statement",'identifier'):["Identifier",'=',"GenExpression",';'],
                ("GenExpression",'identifier'):["Expression","N_PRIME"],
                ("Expression",'identifier'):["Term","C_PRIME"],
                ("Term",'identifier'):["Factor","E_PRIME"],
                ("Factor",'identifier'):['identifier',"G_PRIME"],
                ("RelExpression",'identifier'):["RelTerm","D_PRIME"],
                ("RelTerm",'identifier'):["Expression","L_PRIME"],
                ("Arguments",'identifier'):["GenExpression","Argument"],
                ("Identifier",'identifier'):['identifier'],

                ("Extension",'{'):['epsilon'],
                ("VarDeclarations",'{'):['epsilon'],
                ("Statements",'{'):["Statement","Statements"],
                ("Statement",'{'):['{',"Statements",'}'],

                ("FieldDeclarations",'}'):['epsilon'],
                ("VarDeclarations",'}'):['epsilon'],
                ("MethodDeclarations",'}'):['epsilon'],
                ("Statements",'}'):['epsilon']
                }

data_memory_iterator = 200 #The start of the dynamic memory is here
instruction_memory_block = 0
def alloc_4byte():
    global data_memory_iterator
    output = data_memory_iterator
    data_memory_iterator = data_memory_iterator + 4
    return output

def alloc_block():
    output = instruction_memory_block
    instruction_memory_block = instruction_memory_block + 1
    return instruction_memory_block

scop_list=[]# Where we keep all the scopes (class or functions)


class CLSscop():# For classes
    """Saves the elements of a CLASS in a clean structure"""

    pointer=[]# to point to other scopes by there INDEX in scop_list! (python has no pointers!!!)
    elems=[]# the Identifiers
    def __init__(self, name, parent_scop_index, extension_index = None):
        self.pointer.append(parent_scop_index)
        self.name=name
        if(extension_index):
            self.pointer.append(extension_index)

    def add_ID(self,type,token):# INT|BOOLEAN
        if(type=="int"):
            self.elems.append((token[1],"INT",alloc_4byte()))
        elif(type=="boolean"):
            self.elems.append((token[1],"BOOL",alloc_4byte()))
        else:# ERROR
            print "Undefined Type " + type

    def add_FUNC(self, token, function_scop_index):
        self.elems.append((token[1], "FUNC", function_scop_index))

    # def add_OBJ(self,token):
    #     self.elems.append(())
    # didn't mention that every thing was static :D

    def add_CLS(self,token,class_scop_index):
        self.elems.append((token[1],"CLS",class_scop_index))

class FUNCscop():
    """Saves the elements of a FUNCTION and its subcode in a clean structure"""

    code_block=[]# contains the output code :D
    pass






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

    # using a list as stack:
    stack = ['$',"Goal"]

    def get_token(self,token):
        input_term = token_to_terminal(token)
        print token,input_term
        while(self.stack[-1] != '$'):
            if(self.stack[-1] in Grammer.terminals):
                if(self.stack[-1] == input_term):
                    print "accepted: " + self.stack.pop()
                    break
                else:# Oh no an ERROR!!!
                    print "ERROR stack top is: " + self.stack[-1]
                    print "and input term is: " + input_term
                    break
            elif(self.stack[-1] in Grammer.non_terminals or self.stack[-1] in Grammer.added_non_terminals):
                if( ll1ParseTable.has_key((self.stack[-1],input_term)) ):
                    temp_to_get_in_stack = ll1ParseTable[(self.stack[-1],input_term)]
                    print "Reduced " + self.stack.pop()
                    self.stack.extend(temp_to_get_in_stack[::-1])
                    if(self.stack[-1] == 'epsilon'):
                        self.stack.pop()
                    print self.stack[-1]
                else:# ERROR we the LL(1) table is empty :(
                    print "LL(1) is empty..."
                    print (self.stack[-1],input_term)
                    break
            else:
                print "ERROR top of the stack is neither terminal nor non-terminal :" + self.stack[-1]
                break













