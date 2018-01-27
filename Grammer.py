non_terminals = {"Goal","Source","MainClass",
             "ClassDeclarations","ClassDeclaration",
             "Extension","FieldDeclarations",
             "FieldDeclaration","VarDeclarations",
             "VarDeclaration","MethodDeclarations",
             "MethodDeclaration","Parameters",
             "Parameter","Type","Statements",
             "Statement","GenExpression",
             "Expression","Term",
             "Factor","RelExpression",
             "RelTerm","Arguments",
             "Argument","Identifier",
             "Integer"
             }
added_non_terminals = {"C_PRIME",
                       "D_PRIME",
                       "E_PRIME",
                       "G_PRIME",
                       "H_PRIME",
                       "L_PRIME",
                       "N_PRIME"
                       }

terminals = {'EOF','public','{',
             'static','void','main',
             '(',')','}','class','extends',
             ';','return',',','boolean',
             'int','if','else','while',
             'for','=','+=','System.out.println',
             '+','-','*','.','true','false',
             '&&','==','<','identifier','integer'
             }

# Thanks to JFLAP for this parse table :)
# The parse table works as a dictionary with
# tuple type keys:
# ll1ParseTable = {("GenExpression",'('):["Expression","N_PRIME"],
#                 ("Expression",'('):["Term","C_PRIME"],
#                 ("Term",'('):["Factor","E_PRIME"],
#                 ("Factor",'('):['(',"Expression",')'],
#                 ("RelExpression",'('):["RelTerm","D_PRIME"],
#                 ("RelTerm",'('):["Expression","L_PRIME"],
#                 ("Arguments",'('):["GenExpression","Argument"],
#                 ("H_PRIME",'('):['(',"Arguments",')'],
#
#                 ("Parameters",')'):['epsilon'],
#                 ("Parameter",')'):['epsilon'],
#                 ("Arguments",')'):['epsilon'],
#                 ("Argument",')'):['epsilon'],
#                 ("C_PRIME",')'):['epsilon'],
#                 ("D_PRIME",')'):['epsilon'],
#                 ("E_PRIME",')'):['epsilon'],
#                 ("G_PRIME",')'):['epsilon'],
#                 ("H_PRIME",')'):['epsilon'],
#                 ("N_PRIME",')'):['epsilon'],
#
#                 ("E_PRIME",'*'):['*',"Factor","E_PRIME"],
#                 ("G_PRIME",'*'):['epsilon'],
#                 ("H_PRIME",'*'):['epsilon'],
#
#                 ("C_PRIME",'+'):['+',"Term","C_PRIME"],
#                 ("E_PRIME",'+'):['epsilon'],
#                 ("G_PRIME",'+'):['epsilon'],
#                 ("H_PRIME",'+'):['epsilon'],
#
#                 ("Parameter",','):[',',"Type","Identifier","Parameter"],
#                 ("Argument",','):[',',"GenExpression","Argument"],
#                 ("C_PRIME",','):['epsilon'],
#                 ("D_PRIME",','):['epsilon'],
#                 ("E_PRIME",','):['epsilon'],
#                 ("G_PRIME",','):['epsilon'],
#                 ("H_PRIME",','):['epsilon'],
#                 ("N_PRIME",','):['epsilon'],
#
#                 ("C_PRIME",'-'):['-',"Term","C_PRIME"],
#                 ("E_PRIME",'-'):['epsilon'],
#                 ("G_PRIME",'-'):['epsilon'],
#                 ("H_PRIME",'-'):['epsilon'],
#
#                 ("G_PRIME",'.'):['.','identifier',"H_PRIME"],
#
#                 ("C_PRIME",';'):['epsilon'],
#                 ("D_PRIME",';'):['epsilon'],
#                 ("E_PRIME",';'):['epsilon'],
#                 ("G_PRIME",';'):['epsilon'],
#                 ("H_PRIME",';'):['epsilon'],
#                 ("N_PRIME",';'):['epsilon'],
#
#                 ("C_PRIME",'<'):['epsilon'],
#                 ("E_PRIME",'<'):['epsilon'],
#                 ("G_PRIME",'<'):['epsilon'],
#                 ("H_PRIME",'<'):['epsilon'],
#                 ("L_PRIME",'<'):['<',"Expression"],
#                 ("N_PRIME",'<'):["L_PRIME","D_PRIME"],
#
#                 ("Goal",'public'):["Source",'EOF'],
#                 ("Source", 'public'): ["ClassDeclarations", "MainClass"],
#                 ("MainClass", 'public'): ['public', 'class',
#                                           "Identifier",'{','public',
#                                           'static','void','main','(',
#                                           ')','{',"VarDeclarations","Statements",
#                                           '}','}'],
#                 ("ClassDeclarations", 'public'): ['epsilon'],
#                 ("FieldDeclarations", 'public'): ['epsilon'],
#                 ("MethodDeclarations", 'public'): ["MethodDeclaration", "MethodDeclarations"],
#                 ("MethodDeclaration", 'public'): ['public','static',
#                                                   "Type","Identifier",
#                                                   '(',"Parameters",')',
#                                                   '{',"VarDeclarations",
#                                                   "Statements",'return',
#                                                   "GenExpression",';','}'],
#
#                 ("Goal",'class'):["Source",'EOF'],
#                 ("Source", 'class'): ["ClassDeclarations", "MainClass"],
#                 ("ClassDeclarations", 'class'): ["ClassDeclaration","ClassDeclarations"],
#                 ("ClassDeclaration", 'class'): ['class',"Identifier","Extension",
#                                                 '{',"FieldDeclarations","MethodDeclarations",
#                                                 '}'],
#
#                 ("GenExpression", 'true'): ["Expression", "N_PRIME"],
#                 ("Expression", 'true'): ["Term", "C_PRIME"],
#                 ("Term", 'true'): ["Factor", "E_PRIME"],
#                 ("Factor", 'true'): ['true'],
#                 ("RelExpression",'true'):["RelTerm","D_PRIME"],
#                 ("RelTerm",'true'):["Expression","L_PRIME"],
#                 ("Arguments",'true'):["GenExpression","Argument"],
#
#                 ("FieldDeclarations",'static'):["FieldDeclaration","FieldDeclarations"],
#                 ("FieldDeclaration",'static'):['static',"Type","Identifier",';'],
#
#                 ("GenExpression", 'false'): ["Expression", "N_PRIME"],
#                 ("Expression", 'false'): ["Term", "C_PRIME"],
#                 ("Term", 'false'): ["Factor", "E_PRIME"],
#                 ("Factor", 'false'): ['false'],
#                 ("RelExpression",'false'):["RelTerm","D_PRIME"],
#                 ("RelTerm",'false'):["Expression","L_PRIME"],
#                 ("Arguments",'false'):["GenExpression","Argument"],
#
#                 ("C_PRIME",'&&'):['epsilon'],
#                 ("D_PRIME",'&&'):['&&',"RelTerm","D_PRIME"],
#                 ("E_PRIME",'&&'):['epsilon'],
#                 ("G_PRIME",'&&'):['epsilon'],
#                 ("H_PRIME",'&&'):['epsilon'],
#
#                 ("C_PRIME",'=='):['epsilon'],
#                 ("E_PRIME",'=='):['epsilon'],
#                 ("G_PRIME",'=='):['epsilon'],
#                 ("H_PRIME",'=='):['epsilon'],
#                 ("L_PRIME",'=='):['==',"Expression"],
#                 ("N_PRIME",'=='):["L_PRIME","D_PRIME"],
#
#                 ("Extension",'extends'):['extends',"Identifier"],
#
#                 ("VarDeclarations",'return'):['epsilon'],
#                 ("Statements",'return'):['epsilon'],
#
#                 ("VarDeclarations",'boolean'):["VarDeclaration","VarDeclarations"],
#                 ("VarDeclaration",'boolean'):["Type","Identifier",';'],
#                 ("Parameters",'boolean'):["Type","Identifier","Parameter"],
#                 ("Type",'boolean'):['boolean'],
#
#                 ("VarDeclarations", 'int'): ["VarDeclaration", "VarDeclarations"],
#                 ("VarDeclaration", 'int'): ["Type", "Identifier", ';'],
#                 ("Parameters", 'int'): ["Type", "Identifier", "Parameter"],
#                 ("Type",'int'):['int'],
#
#                 ("VarDeclarations",'if'):['epsilon'],
#                 ("Statements",'if'):["Statement","Statements"],
#                 ("Statement",'if'):['if','(',"GenExpression",')',
#                                     "Statement",'else',"Statement"],
#
#                 ("VarDeclarations",'while'):['epsilon'],
#                 ("Statements",'while'):["Statement","Statements"],
#                 ("Statement",'while'):['while','(',"GenExpression",')',
#                                        "Statement"],
#
#                 ("VarDeclarations",'for'):['epsilon'],
#                 ("Statements",'for'):["Statement","Statements"],
#                 ("Statement",'for'):['for','(',"Identifier",
#                                      '=',"Integer",';',"RelTerm",';',
#                                      "Identifier",'+=',"Integer",')',
#                                      "Statement"],
#
#                 ("GenExpression", 'integer'): ["Expression", "N_PRIME"],
#                 ("Expression", 'integer'): ["Term", "C_PRIME"],
#                 ("Term", 'integer'): ["Factor", "E_PRIME"],
#                 ("Factor",'integer'):["Integer"],
#                 ("RelExpression",'integer'):["RelTerm","D_PRIME"],
#                 ("RelTerm",'integer'):["Expression","L_PRIME"],
#                 ("Arguments",'integer'):["GenExpression","Argument"],
#                 ("Integer",'integer'):['integer'],
#
#                 ("VarDeclarations",'System.out.println'):['epsilon'],
#                 ("Statements",'System.out.println'):["Statement","Statements"],
#                 ("Statement",'System.out.println'):['System.out.println','(',
#                                                     "GenExpression",')',';'],
#
#                 ("VarDeclarations",'identifier'):['epsilon'],
#                 ("Statements",'identifier'):["Statement","Statements"],
#                 ("Statement",'identifier'):["Identifier",'=',"GenExpression",';'],
#                 ("GenExpression",'identifier'):["Expression","N_PRIME"],
#                 ("Expression",'identifier'):["Term","C_PRIME"],
#                 ("Term",'identifier'):["Factor","E_PRIME"],
#                 ("Factor",'identifier'):['identifier',"G_PRIME"],
#                 ("RelExpression",'identifier'):["RelTerm","D_PRIME"],
#                 ("RelTerm",'identifier'):["Expression","L_PRIME"],
#                 ("Arguments",'identifier'):["GenExpression","Argument"],
#                 ("Identifier",'identifier'):['identifier'],
#
#                 ("Extension",'{'):['epsilon'],
#                 ("VarDeclarations",'{'):['epsilon'],
#                 ("Statements",'{'):["Statement","Statements"],
#                 ("Statement",'{'):['{',"Statements",'}'],
#
#                 ("FieldDeclarations",'}'):['epsilon'],
#                 ("VarDeclarations",'}'):['epsilon'],
#                 ("MethodDeclarations",'}'):['epsilon'],
#                 ("Statements",'}'):['epsilon']
#
#                 }


# The parse table works as a dictionary with
# tuple type keys:
ll1ParseTable_with_codegens = {("GenExpression",'('):["Expression","N_PRIME"],
                ("Expression",'('):["Term","C_PRIME"],
                ("Term",'('):["Factor","E_PRIME"],
                ("Factor",'('):['(',"Expression",')'],
                ("RelExpression",'('):["RelTerm","D_PRIME"],
                ("RelTerm",'('):["Expression","L_PRIME"],
                ("Arguments",'('):["GenExpression","Argument"],
                ("H_PRIME",'('):["#callFUNC",'(',"Arguments",')',"#endCallFUNC"],

                ("Parameters",')'):['epsilon'],
                ("Parameter",')'):['epsilon'],
                ("Arguments",')'):['epsilon'],
                ("Argument",')'):['epsilon'],
                ("C_PRIME",')'):['epsilon'],
                ("D_PRIME",')'):['epsilon'],
                ("E_PRIME",')'):['epsilon'],
                ("G_PRIME",')'):["#insIDadd"],
                ("H_PRIME",')'):["#pCLS_ID"],#OK
                ("N_PRIME",')'):['epsilon'],

                ("E_PRIME",'*'):['*',"Factor","#MULT","E_PRIME"],
                ("G_PRIME",'*'):["#insIDadd"],
                ("H_PRIME",'*'):["#pCLS_ID"],#OK

                ("C_PRIME",'+'):['+',"Term","#ADD","C_PRIME"],
                ("E_PRIME",'+'):['epsilon'],
                ("G_PRIME",'+'):["#insIDadd"],
                ("H_PRIME",'+'):["#pCLS_ID"],#OK

                ("Parameter",','):[',',"Type","Identifier","#insIDadd","Parameter"],
                ("Argument",','):[',',"GenExpression","Argument"],
                ("C_PRIME",','):['epsilon'],
                ("D_PRIME",','):['epsilon'],
                ("E_PRIME",','):['epsilon'],
                ("G_PRIME",','):["#insIDadd"],
                ("H_PRIME",','):["#pCLS_ID"],#OK
                ("N_PRIME",','):['epsilon'],

                ("C_PRIME",'-'):['-',"Term","#SUB","C_PRIME"],
                ("E_PRIME",'-'):['epsilon'],
                ("G_PRIME",'-'):["#insIDadd"],
                ("H_PRIME",'-'):["#pCLS_ID"],#OK

                ("G_PRIME",'.'):['.',"Identifier","H_PRIME"],# Changed "identifier" to "Identifier" and #OK

                ("C_PRIME",';'):['epsilon'],
                ("D_PRIME",';'):['epsilon'],
                ("E_PRIME",';'):['epsilon'],
                ("G_PRIME",';'):["#insIDadd"],
                ("H_PRIME",';'):["#pCLS_ID"],#OK
                ("N_PRIME",';'):['epsilon'],

                ("C_PRIME",'<'):['epsilon'],
                ("E_PRIME",'<'):['epsilon'],
                ("G_PRIME",'<'):["#insIDadd"],
                ("H_PRIME",'<'):["#pCLS_ID"],#OK
                ("L_PRIME",'<'):['<',"Expression","#LT"],
                ("N_PRIME",'<'):["L_PRIME","D_PRIME"],

                ("Goal",'public'):["Source",'EOF'],
                ("Source", 'public'): ["ClassDeclarations", "MainClass"],
                ("MainClass", 'public'): ['public', 'class',
                                          "Identifier",'{','public',
                                          'static','void','main','(',
                                          ')','{',"#enteredMain","VarDeclarations","Statements",#OK !
                                          '}',"#GenTheCode",'}'],
                ("ClassDeclarations", 'public'): ['epsilon'],
                ("FieldDeclarations", 'public'): ['epsilon'],
                ("MethodDeclarations", 'public'): ["MethodDeclaration", "MethodDeclarations"],
                ("MethodDeclaration", 'public'): ['public','static',
                                                  "Type","Identifier","#genFunc",
                                                  '(',"Parameters",')',
                                                  '{',"VarDeclarations",
                                                  "Statements",'return',
                                                  "GenExpression",';',"#endFunc",'}'],

                ("Goal",'class'):["Source",'EOF'],
                ("Source", 'class'): ["ClassDeclarations", "MainClass"],
                ("ClassDeclarations", 'class'): ["ClassDeclaration","ClassDeclarations"],
                ("ClassDeclaration", 'class'): ['class',"Identifier","Extension","#newCLSscope",#OK
                                                '{',"FieldDeclarations","MethodDeclarations",
                                                '}',"#endCLSscope"],#OK

                ("GenExpression", 'true'): ["Expression", "N_PRIME"],
                ("Expression", 'true'): ["Term", "C_PRIME"],
                ("Term", 'true'): ["Factor", "E_PRIME"],
                ("Factor", 'true'): ["#pBOOLconst",'true'],
                ("RelExpression",'true'):["RelTerm","D_PRIME"],
                ("RelTerm",'true'):["Expression","L_PRIME"],
                ("Arguments",'true'):["GenExpression","Argument"],

                ("FieldDeclarations",'static'):["FieldDeclaration","FieldDeclarations"],
                ("FieldDeclaration",'static'):['static',"Type","Identifier","#addIDToSymTable",';'],#OK

                ("GenExpression", 'false'): ["Expression", "N_PRIME"],
                ("Expression", 'false'): ["Term", "C_PRIME"],
                ("Term", 'false'): ["Factor", "E_PRIME"],
                ("Factor", 'false'): ["#pBOOLconst",'false'],
                ("RelExpression",'false'):["RelTerm","D_PRIME"],
                ("RelTerm",'false'):["Expression","L_PRIME"],
                ("Arguments",'false'):["GenExpression","Argument"],

                ("C_PRIME",'&&'):['epsilon'],
                ("D_PRIME",'&&'):['&&',"RelTerm","#andRelTerms","D_PRIME"],
                ("E_PRIME",'&&'):['epsilon'],
                ("G_PRIME",'&&'):["#insIDadd"],
                ("H_PRIME",'&&'):["#pCLS_ID"],#OK

                ("C_PRIME",'=='):['epsilon'],
                ("E_PRIME",'=='):['epsilon'],
                ("G_PRIME",'=='):["#insIDadd"],#OK ['epsilon']
                ("H_PRIME",'=='):["#pCLS_ID"],#OK
                ("L_PRIME",'=='):['==',"Expression","#EQ"],
                ("N_PRIME",'=='):["L_PRIME","D_PRIME"],

                ("Extension",'extends'):['extends',"Identifier"],

                ("VarDeclarations",'return'):['epsilon'],
                ("Statements",'return'):['epsilon'],

                ("VarDeclarations",'boolean'):["VarDeclaration","VarDeclarations"],
                ("VarDeclaration",'boolean'):["Type","Identifier","#addIDToSymTable",';'],#OK !
                ("Parameters",'boolean'):["Type","Identifier","#insIDadd","Parameter"],#OK
                ("Type",'boolean'):["#BOOL",'boolean'],

                ("VarDeclarations", 'int'): ["VarDeclaration", "VarDeclarations"],
                ("VarDeclaration", 'int'): ["Type","Identifier","#addIDToSymTable", ';'],#OK !
                ("Parameters", 'int'): ["Type", "Identifier","#insIDadd", "Parameter"],#OK
                ("Type",'int'):["#INT",'int'],

                ("VarDeclarations",'if'):['epsilon'],
                ("Statements",'if'):["Statement","Statements"],
                ("Statement",'if'):['if','(',"GenExpression",')',"#genIf",
                                    "Statement",'else',"#genElse","Statement","#endIf"],

                ("VarDeclarations",'while'):['epsilon'],
                ("Statements",'while'):["Statement","Statements"],
                ("Statement",'while'):['while','(',"#SAVE_PC","GenExpression",')',"#genWhile",
                                       "Statement","#endWhile"],

                ("VarDeclarations",'for'):['epsilon'],
                ("Statements",'for'):["Statement","Statements"],
                ("Statement",'for'):['for','(',"Identifier","#insIDadd",#OK
                                     '=',"Integer","#assign",';',"#SAVE_PC","RelTerm","#genFor",';',
                                     "Identifier","#insIDadd",'+=',"Integer",')',#OK
                                     "Statement","#endFor"],

                ("GenExpression", 'integer'): ["Expression", "N_PRIME"],
                ("Expression", 'integer'): ["Term", "C_PRIME"],
                ("Term", 'integer'): ["Factor", "E_PRIME"],
                ("Factor",'integer'):["Integer"],
                ("RelExpression",'integer'):["RelTerm","D_PRIME"],
                ("RelTerm",'integer'):["Expression","L_PRIME"],
                ("Arguments",'integer'):["GenExpression","Argument"],
                ("Integer",'integer'):["#pconst",'integer'],#OK

                ("VarDeclarations",'System.out.println'):['epsilon'],
                ("Statements",'System.out.println'):["Statement","Statements"],
                ("Statement",'System.out.println'):['System.out.println','(',
                                                    "GenExpression",')',"#systemPrint",';'],#OK

                ("VarDeclarations",'identifier'):['epsilon'],
                ("Statements",'identifier'):["Statement","Statements"],
                ("Statement",'identifier'):["Identifier","#insIDadd",'=',"GenExpression","#assign",';'],#OK
                ("GenExpression",'identifier'):["Expression","N_PRIME"],
                ("Expression",'identifier'):["Term","C_PRIME"],
                ("Term",'identifier'):["Factor","E_PRIME"],
                ("Factor",'identifier'):["#pid",'identifier',"G_PRIME"],#OK !
                ("RelExpression",'identifier'):["RelTerm","D_PRIME"],
                ("RelTerm",'identifier'):["Expression","L_PRIME"],
                ("Arguments",'identifier'):["GenExpression","Argument"],
                ("Identifier",'identifier'):["#pid",'identifier'],#OK

                ("Extension",'{'):["#none"],#OK ['epsilon']
                ("VarDeclarations",'{'):['epsilon'],
                ("Statements",'{'):["Statement","Statements"],
                ("Statement",'{'):['{',"Statements",'}'],

                ("FieldDeclarations",'}'):['epsilon'],
                ("VarDeclarations",'}'):['epsilon'],
                ("MethodDeclarations",'}'):['epsilon'],
                ("Statements",'}'):['epsilon'],

                ##### For Panic Mode:
                ("Goal",'$'):["--SYNCH--"],

                ("Source",'EOF'):["--SYNCH--"],

                ("MainClass", 'EOF'):["--SYNCH--"],

                ("ClassDeclaration", 'public'): ["--SYNCH--"],

                ("FieldDeclaration", 'public'): ["--SYNCH--"],
                ("FieldDeclaration", '}'): ["--SYNCH--"],

                ("VarDeclaration", 'if'): ["--SYNCH--"],
                ("VarDeclaration", 'while'): ["--SYNCH--"],
                ("VarDeclaration", 'for'): ["--SYNCH--"],
                ("VarDeclaration", 'System.out.println'): ["--SYNCH--"],
                ("VarDeclaration", 'identifier'): ["--SYNCH--"],
                ("VarDeclaration", '{'): ["--SYNCH--"],
                ("VarDeclaration", '}'): ["--SYNCH--"],
                ("VarDeclaration", 'return'): ["--SYNCH--"],

                ("MethodDeclaration", '}'): ["--SYNCH--"],

                ("Type", 'identifier'): ["--SYNCH--"],

                ("Statement", 'else'): ["--SYNCH--"],
                ("Statement", '}'): ["--SYNCH--"],
                ("Statement", 'return'): ["--SYNCH--"],

                ("GenExpression", ')'): ["--SYNCH--"],
                ("GenExpression", ';'): ["--SYNCH--"],
                ("GenExpression", ','): ["--SYNCH--"],

                ("Expression", ')'): ["--SYNCH--"],
                ("Expression", '&&'): ["--SYNCH--"],
                ("Expression", '=='): ["--SYNCH--"],
                ("Expression", ';'): ["--SYNCH--"],
                ("Expression", '<'): ["--SYNCH--"],
                ("Expression", ','): ["--SYNCH--"],

                ("Term", ')'): ["--SYNCH--"],
                ("Term", '&&'): ["--SYNCH--"],
                ("Term", '=='): ["--SYNCH--"],
                ("Term", ';'): ["--SYNCH--"],
                ("Term", '+'): ["--SYNCH--"],
                ("Term", '<'): ["--SYNCH--"],
                ("Term", ','): ["--SYNCH--"],
                ("Term", '-'): ["--SYNCH--"],

                ("Factor", ')'): ["--SYNCH--"],
                ("Factor", '&&'): ["--SYNCH--"],
                ("Factor", '*'): ["--SYNCH--"],
                ("Factor", '=='): ["--SYNCH--"],
                ("Factor", ';'): ["--SYNCH--"],
                ("Factor", '+'): ["--SYNCH--"],
                ("Factor", '<'): ["--SYNCH--"],
                ("Factor", ','): ["--SYNCH--"],
                ("Factor", '-'): ["--SYNCH--"],

                ("RelTerm", ')'): ["--SYNCH--"],
                ("RelTerm", '&&'): ["--SYNCH--"],
                ("RelTerm", ';'): ["--SYNCH--"],
                ("RelTerm", ','): ["--SYNCH--"],

                ("Identifier", '+='): ["--SYNCH--"],
                ("Identifier", '('): ["--SYNCH--"],
                ("Identifier", ')'): ["--SYNCH--"],
                ("Identifier", '{'): ["--SYNCH--"],
                ("Identifier", 'extends'): ["--SYNCH--"],
                ("Identifier", ';'): ["--SYNCH--"],
                ("Identifier", ','): ["--SYNCH--"],
                ("Identifier", '='): ["--SYNCH--"],

                }


