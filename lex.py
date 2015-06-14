__author__ = 'demathieu'
import ply.lex as lex

# List of reserved words
reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'length' : 'LENGTH',
   'while' : 'WHILE',
   'char' : 'CHAR',
   'return' : 'RETURN',
   'int' : 'INT',
   'write' : 'WRITE',
   'read' : 'READ'
}

# List of token names.   This is always required
tokens = [
   'NAME',
   'NUMBER',
   'QCHAR',
   'COMMENT',
   'NEQUAL',
   'LPAR',
   'RPAR',
   'LBRACE',
   'RBRACE',
   'LBRACK',
   'RBRACK',
   'ASSIGN',
   'SEMICOLON',
   'COMMA',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'EQUAL',
   'GREATER',
   'LESS',
   'QUOTE',
   'NOT'] + list(reserved.values())

# todo: t_comment
# Regular expression rules for simple tokens
t_QUOTE     = r'\''
t_LPAR      = r'\('
t_RPAR      = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LBRACK    = r'\['
t_RBRACK    = r'\]'
t_ASSIGN    = r'\='
t_NEQUAL    = r'!='
t_COMMA     = r'\,'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUAL     = r'=='
t_GREATER   = r'>'
t_LESS      = r'<'
t_NOT       = r'!'
t_SEMICOLON = r';'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


def giveInput(data):
    lexer.input(data)

def getToken():
    return lexer.token()

