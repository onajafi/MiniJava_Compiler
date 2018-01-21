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

class scop():
    """Saves the elements in a clean structure"""


    pointer=[]# to point to other scopes!
    elems=[]# the Identifiers
    def __init__(self, name, parent_scop, extension = None):
        self.pointer.append(parent_scop)
        self.name=name
        if(extension):
            self.pointer.append(extension)

    def add_ID(self,type,token):# INT|BOOLEAN
        if(type=="int"):
            self.elems.append((token[0],"INT",))
        elif(type=="boolean"):
            self.elems.append()
        else:# ERROR
            print "Undefined Type " + type


    def add_OBJ(self,token):
        pass

    def add_FUNC(self,token):
        pass






def token_to_terminal(token):
    pass

class Parser():
    """Receives every token and parses the inputs"""

    # using a list as stack:
    stack = ['$',"Goal"]

    def get_token(self,token):
        pass







