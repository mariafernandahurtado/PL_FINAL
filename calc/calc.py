# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
import math
from ast import literal_eval
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

reserved = (
    'true', 'boileano', 'entonces', 'false', 'vector', 'sino', 'entero', 'long', 'finsi', 'real', 'mientras', 'and', 'finmientras',
    'si', 'or', 'not'
)
tokens = reserved+(
    'NAME', 'ENTERO', 'DECIMAL' , 'HEXADECIMAL', 'OCTAL' , 'NOTCIENT', 'FCIENT', 'SALTO'
)

literals = ['=', '+', '-', '*', '/', '(', ')']

# Tokens

def t_NAME(t):
    r'MEM_'
    return t


def t_SALTO(t):
    r'\n+'
    return t

def t_FCIENT(t):
    r'log|exp|sin|cos'
    return t

def t_NOTCIENT(t):
    r'\d+(\.\d*)?[e|E]-?\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Number is wrong", t.value)
        t.value = 0
    return t


def t_HEXADECIMAL(t):
    r'0[x|X][0-9a-fA-F]+'
    try:
        t.value = int(t.value, 16)
    except ValueError:
        print("Hexadecimal number is wrong", t.value)
        t.value = 0
    return t

def t_OCTAL(t):
    r'0[o|O][0-7]+'
    try:
        t.value = int(t.value,8)
    except ValueError:
        print("Octal number is wrong", t.value)
        t.value = 0
    return t


def t_DECIMAL(t):
    r'[\d+]?\.[\d+]?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

def t_wrong(t):
    r'[A-Za-z]+\_?[A-Za-z]+?[1-9]+?\=.+'
    print("Error de asignación")
    t.lexer.skip(1)

def t_comment(t):
    r'[ ]*%%.*[^\n]?'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules
#dictionary of names
names = {}
for i in range(1,11): #inicializamos las variables a 0
    names['MEM_'+str(i)]=0


def p_statement_sl_statement(p):
    '''sentencias : statement SALTO sentencias
        | statement'''

def p_statement_assign(p):
    """statement : NAME ENTERO "=" expressionSR"""
    if p[2]<0 or p[2]>10:
        print("Error el nombre de la variable ", p[1]+str(p[2])," no es aceptado")
    else:
        p[1]=p[1]+str(p[2])
        names[p[1]] = p[4]

def p_statement_expr(p):
    'statement : expressionSR'
    print(p[1])

def p_statement_sl(p):
    'statement : \n'

def p_expression_binop(p):
    '''expressionSR : expressionSR '+' expressionMD
                  | expressionSR '-' expressionMD'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expressionSR_expressionMD(p):
    'expressionSR : expressionMD'
    p[0] = p[1]

def p_expression_opmd(p):
    '''expressionMD : expressionMD '*' expression
                  | expressionMD '/' expression'''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expressionMD_expression(p):
    'expressionMD : expression'
    p[0] = p[1]


def p_expression_group(p):
    "expression : '(' expressionSR ')'"
    p[0] = p[2]


def p_expression_signo(p):
    """expression : '-' expression
                | '+' expression
                """
    if p[1]=='-':
        p[0]= -p[2]
    elif p[1]=='+':
        p[0] = p[2]


def p_expression_basica(p):
    """expression : ENTERO
                | DECIMAL
                | HEXADECIMAL
                | NOTCIENT
                | OCTAL
    """
    p[0] = p[1]

def p_expression_fcient(p):
    """expression : FCIENT '(' expressionSR ')'"""
    if p[1]=='log':
        p[0] = math.log(p[3], 10)
    elif p[1]=='exp':
        p[0] = math.exp(p[3])
    elif p[1]=='sin':
        p[0] = math.sin(p[3])
    elif p[1]=='cos':
        p[0] = math.cos(p[3])


def p_expression_name(p):
    "expression : NAME ENTERO"
    p[1]=p[1]+str(p[2])
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
        print(p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

fname="Pruebas.txt"
try:
    f= open(fname, 'r')
except IOError:
    print ("Archivo no encontrado:", fname)
while 1:
    try:
        s = f.read()
    except EOFError:
        break
    if not s:
        break
    yacc.parse(s)