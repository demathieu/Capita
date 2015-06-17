__author__ = 'demathieu'

import ply.yacc as yacc
import Scope as Sym
from Objects import *

# Get the token map from the lexer.  This is required.
import lex
tokens = lex.tokens

listTAC =[]

tempVariableCount = -1
tempLabelCount = -1
global scope
scope = Sym.Scope();

def newtemp(type = 'int'):
    global tempVariableCount
    tempVariableCount = tempVariableCount + 1
    tempVar = "_t" + str(tempVariableCount)
    entry = Sym.Entry(tempVar,type);
    scope.addVarToSymbolTable(entry)
    return tempVar

def newlabel():
    global tempLabelCount
    tempLabelCount = tempLabelCount + 1
    return "_L" + str(tempLabelCount)

def givecurrentlabel():
    return "_L" + str(tempLabelCount)

def GiveTAC(op, arg1 = None, arg2 = None, result = None ):
    listTAC.append(Quadruple(len(listTAC),op, arg1, arg2, result))


def p_program_declarations(p):
    'program		: declarations'
    #print'program'


def p_declarations_declaration_declarations(p):
    'declarations  	: declaration declarations'
    #print'declarations  	: declaration declarations'

def p_declarations_declaration(p):
    'declarations  	: declaration'
    #print'declarations  	: declaration'

def p_declaration_fun_declaration(p):
    'declaration	: fun_declaration'
    #print'declaration	: fun_declaration'

def p_declaration_var_declaration(p):
    'declaration	: var_declaration'
    #print'declaration	: var_declaration'

 #'fun_declaration	: type NAME LPAR formal_pars RPAR block'
def p_fun_declaration_type_formal_pars_block(p):
    'fun_declaration	: type functionName LPAR formal_pars RPAR block'
    GiveTAC('EndFunc')
    global scope
    scope.setCreator(Sym.Entry(p[2],p[1]))
    scope = scope.goBackToParentScope()
   # scope.addEntryToFunctionList(Sym.Entry(p[2],p[1]))

def p_functionName(p):
    'functionName : NAME'
    GiveTAC("function",None,None,p[1])
    GiveTAC("TO_CHECK_FunctionSize",'BeginFunc',p[1])
    global scope
    scope = scope.createSubScope();
    p[0]=p[1]

def p_formal_pars_formal_par_formal_pars(p):
    'formal_pars	: formal_par formal_pars'
    #print'formal_pars	: formal_par formal_pars'

def p_formal_pars_empty(p):
    'formal_pars    : '
    #print'formal_pars    : '

def p_formal_par(p):
    'formal_par	: type NAME'
    #print'formal_par	: type NAME'
    tempEntry = Sym.Entry(p[2],p[1])
    global scope
    scope.addFormalParamToSymbolTable(tempEntry)

def p_block_var_declarations_statements(p):
    'block		: LBRACE var_declarations statements RBRACE'
    #print'block		: LBRACE var_declarations statements RBRACE'

def p_var_declarations_var_declaration_var_declarations(p):
    'var_declarations : var_declaration var_declarations'
    #print'var_declarations : var_declaration var_declarations'


def p_var_declarations_empty(p):
    'var_declarations : '
    #print'var_declarations : '

def p_var_declaration_type(p):
    'var_declaration	: type NAME SEMICOLON'
    #print'var_declaration	: type NAME SEMICOLON'
    scope.addVarToSymbolTable(Sym.Entry(p[2],p[1]))


def p_type(p):
    '''type : INT
            | CHAR'''
    #print'''type : INT
            #| CHAR'''
    p[0]=p[1]


def p_type_type_exp_array(p):
    'type   :   type LBRACK exp RBRACK'
    #print'(array) type   :   type LBRACK exp RBRACK'

def p_statements_statement_statements(p):
    'statements	: statement SEMICOLON statements'
    #print'statements	: statement SEMICOLON statements'

def p_statements_statement(p):
    'statements :   statement'
    #print'statements :   statement'

def p_statements_empty(p):
    'statements : '
    #print'statements : '

def p_statement_exp_statement_if(p):
    'statement	: IF LPAR expTAC RPAR statement'
    #print'statement	: printIF LPAR exp RPAR statement'
    GiveTAC('Label',None,None,p[3])

def p_printtest(p):
    'expTAC : exp'
    labelTemp = newlabel()
    GiveTAC('IfNode',p[1],None,labelTemp)
    p[0] = labelTemp

def p_statement_exp_statement_statement(p):
    'statement  : IF LPAR expTAC RPAR statement else statement'
    #print'statement  : IF LPAR expTAC RPAR statement ELSE statement'
    GiveTAC('Label',None,None,p[6])

def p_else(p):
    'else : ELSE'
    #print'Else'
    currentlabel = givecurrentlabel()
    tempLabel = newlabel()
    GiveTAC('Goto',None,None,tempLabel)
    GiveTAC('Label',None,None,currentlabel)
    p[0] = tempLabel

def p_statement_exp_statement_while(p):
    'statement  : while LPAR  printWhile RPAR statement'
    #print'statement  : WHILE LPAR exp RPAR statement'
    GiveTAC('Goto',None,None,p[1])
    GiveTAC('Label',None,None,givecurrentlabel())

def p_while_getTacLoopCorrect(p):
    'printWhile : exp '
    #print'printWhile : '
    GiveTAC('IfNode',p[1],None,newlabel())

def p_while_label(p):
    'while  : WHILE'
    #print'while  : WHILE'
    label = newlabel()
    GiveTAC('Label',None,None,label)
    p[0] = label

def p_statement_lexp_exp(p):
    'statement  :   lexp ASSIGN exp'
    GiveTAC("assign exp",p[3],None,p[1])
    ##printp[3]

def p_statement_exp_return(p):
    'statement  : RETURN exp'
    GiveTAC('Return',p[2])

def p_statement_pars(p):
    'statement  : NAME LPAR pars RPAR'
    #print'statement  : NAME LPAR pars RPAR'
    GiveTAC('LCall',p[1],None)
    GiveTAC('PopParams','TO_CHECK_FormalParamsSize',p[1])

def p_statement_block(p):
    'statement : block'
    #print'statement : block'

def p_statement_exp_write(p):
    'statement  :   WRITE exp'
    #print'statement  :   WRITE exp'
    #print'kijk hier is'
    #printp[2]
    #printscope.giveBackTypeForVar(p[2])
    GiveTAC("PushParam", p[2])
    if scope.giveBackTypeForVar(p[2]) == 'int':
        GiveTAC('LCall', 'print_int')
        GiveTAC('PopParams', 4,'NoRecalculate')
    else:
        GiveTAC('LCall','print_char')
        GiveTAC('PopParams',1,'NoRecalculate')

def p_statement_lexp(p):
    'statement : READ lexp'
    #print'statement : READ lexp'
    if scope.giveBackTypeForVar(p[2]) == 'int':
        GiveTAC("= LCall", "read_int", None, p[2])
    else:
        GiveTAC("= LCall", "read_char", None, p[2])

def p_lexp_lexp_exp_array(p):
    'lexp		: lexp LBRACK exp RBRACK'
    #print'(array)lexp		: lexp LBRACK exp RBRACK'
    index = p[3]
    naamArray = p[1]
    width_one_element = 4
    assignValue = newtemp('int')
    GiveTAC('assign_number',width_one_element,None,assignValue)
    calculatedSize = newtemp('int')
    GiveTAC('*',assignValue,index,calculatedSize)
    tempToreferenceTo = newtemp('int')
    GiveTAC('+',naamArray,calculatedSize,tempToreferenceTo)
    GiveTAC('assign_address',tempToreferenceTo,None,newtemp('int'))


def p_lexp_var(p):
    'lexp   :   var'
    p[0]= p[1]
    #print'lexp   :   var'

def p_exp_lexp(p):
    'exp    :   lexp'
    p[0] = p[1]
    #print'exp    :   lexp'

def p_exp_exp_binop_exp(p):
    'exp    :   exp binop exp'
    temp = newtemp("int")
    GiveTAC(p[2],p[1],p[3],temp)
    #print'exp exp binop exp'
    p[0]=temp

def p_exp_unop_exp(p):
    'exp    :   unop exp'
    temp = newtemp("int")
    GiveTAC(p[1],p[2],None,temp)
    #print'exp unop exp'

def p_exp_exp(p):
    'exp    : LPAR exp RPAR'
    #print'exp_exp'

def p_exp_number(p):
    'exp : NUMBER'
    tempvar = newtemp("int")
    GiveTAC('assign_number',p[1],None,tempvar)
    p[0] = tempvar
    #print'exp_number'

def p_exp_pars(p):
    'exp    :  NAME LPAR pars RPAR'
    tempvar = newtemp("int")
    GiveTAC('LCall',p[1],None, tempvar)
    GiveTAC('PopParams','TO_CHECK_FormalParamsSize',p[1])
    p[0]=tempvar


def p_exp_qchar(p):
    'exp    :   QCHAR'
    #print'exp_Qchar'
    tempvar = newtemp("char")
    GiveTAC('assign_number',p[1],None,tempvar)
    p[0] = tempvar


def p_exp_lexp_lenght(p):
    ' exp   :  LENGTH lexp'

def p_binop(p):
    '''binop		: MINUS
		| PLUS
		| TIMES
		| DIVIDE
		| EQUAL
		| NEQUAL
		| GREATER
		| LESS
		'''
    p[0] = p[1]

def p_unop(p):
    '''unop		: MINUS
		| NOT'''
    p[0] = p[1]


def p_pars_exp(p):
    'pars   :   exp'
    GiveTAC('PushParam',p[1])

def p_pars_exp_exp(p):
    'pars   :   exp COMMA exp'
    #print'pars   :   exp COMMA exp'

def p_var(p):
    'var    :   NAME'
    p[0]= p[1]



# Error rule for syntax errors
def p_error(p):
    ##print("Syntax error in input!")
    raise SyntaxError('Syntax error in input!')

def forTesting(data):
    global listTAC
    listTAC = []
    global tempLabelCount
    tempLabelCount = -1
    global tempVariableCount
    tempVariableCount = -1
    parser = yacc.yacc()
    yacc.parse(data)
    TAC = calculateSizes(listTAC,scope)
    return TAC;


def parsers(data):
    p = parser.parse(data)
    return p

# Build the parser
parser = yacc.yacc()

def calculateSizes(list,SymbolTable):
    for i, codeLine in enumerate(list):
        if codeLine.op=='TO_CHECK_FunctionSize':
            #list[i]= Quadruple(codeLine.id,'BeginFunc',SymbolTable.giveBackSizeForFunction(codeLine.arg2),None,codeLine.arg2)
            list[i]= Quadruple(codeLine.id,'BeginFunc',0,None,codeLine.arg2)
        elif codeLine.arg1 == 'TO_CHECK_FormalParamsSize':
            #list[i]= Quadruple(codeLine.id,'PopParams',SymbolTable.giveBackSizeForFormalParam(codeLine.arg2),None,codeLine.arg2)
            list[i]= Quadruple(codeLine.id,'PopParams',0,None,None)
        elif codeLine.op == 'BeginFunc' and codeLine.arg2 != 'NoRecalculate':
            #list[i]= Quadruple(codeLine.id,'BeginFunc',SymbolTable.giveBackSizeForFunction(codeLine.result),None,None)
            list[i]= Quadruple(codeLine.id,'BeginFunc',0,None,None)
        elif codeLine.op == 'PopParams' and codeLine.arg2 != 'NoRecalculate':
            #list[i]= Quadruple(codeLine.id,'PopParams',SymbolTable.giveBackSizeForFormalParam(codeLine.result),None,None)
            list[i]= Quadruple(codeLine.id,'PopParams',0,None,None)
    return list

def PrintQuadruplesToTac(listOfQuadruples):
    #print'start printing \n'
    resultString = ''
    for quad in listOfQuadruples:
        resultString += str(quad.result) + " = " + str(quad.arg1) + " " + str(quad.op) + " " + str(quad.arg2)+ " \n"
    return resultString
    #print(resultString);

def show_TAC(code):
    #print'start tac code printing \n'
    return_string = ''
    for item in code:
        op = str(item.op or None)
        arg1 = str(item.arg1 or None)
        arg2 = str(item.arg2  or None)
        result = str(item.result or None)
        if item.op and item.arg1 and item.arg2 and item.result:
            return_string = return_string + "\t" +  result + " = " + arg1 + " " + op + " " + arg2 + ";\n"
        elif op == "BeginFunc":
                #if not item.arg1:
                    return_string = return_string + "\t" + "BeginFunc" + ' '+ arg1 + ";\n"
        elif item.op == "IfNode":
            return_string = return_string + "\t" + "IfZ " + arg1 + " Goto " + result + ";\n"

        elif item.op and item.arg1 is not None and item.result:
            return_string = return_string + "\t" +  result + " = "
            if op == "-":
                return_string = return_string + "-" + arg1 + ";\n"
            elif op == "assign_address":
                return_string = return_string +  "&" + arg1 + ";\n"
            else:
                return_string = return_string +  str(item.arg1) + ";\n"
        elif item.op and item.arg1:
            return_string = return_string + "\t" + op + " "+ arg1 + ";\n"
        elif item.op:
            if op == "EndFunc":
                return_string = return_string + "\t" + "EndFunc" + ";\n"
            elif op == "Label":
                return_string = return_string + result + ":\n"
            elif op == "Goto":
                return_string = return_string + "\t" +  "Goto " + result + ";\n"
            elif op == "function":
                return_string = return_string + result + ":\n"
            elif op == "Return":
                if not item.arg1:
                    return_string = return_string + "\t" + "Return 0" + ";\n"

    #printreturn_string