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

#Palabras reservadas
reserved = {
        'true': 'true',
        'booleano': 'booleano',
        'entonces': 'entonces',
        'false': 'false',
        'vector': 'vector',
        'sino': 'sino',
        'entero': 'entero',
        'long': 'long',
        'finsi': 'finsi',
        'real': 'real',
        'mientras': 'mientras',
        'and': 'and',
        'finmientras': 'finmientras',
        'si': 'si',
        'or': 'or',
        'not': 'not'
}

states=(
    ('multilinecomment', 'inclusive'),
)

tokens = list(reserved.values()) + [
    'ENTERO', 'DECIMAL' , 'HEXADECIMAL', 'OCTAL' , 'NOTCIENT', 'FCIENT', 'SALTO', 'NOMBRE', 'MAIL', 'DNI', 'MATRICULA', 'ID',
    'OPERADOR', 'OPERADORARITMETICOLOGICO', 'SEPARADOR', 'ASIGNACION', 'SIMBOLO', 'OR', 'AND', 'NOT', 'XOR', 'LOR', 'LAND', 'LNOT',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE', 'AUTORES', 'BLANKSPACE', 'MULTILINECOMMENT', 'COMMENT', 'RESERVADAS'
]


# Tokens
t_OR = r'\O\R'
t_AND = r'\A\N\D'
t_NOT = r'\N\O\T'
t_LT = r'\<'
t_GT = r'\>'
t_LE = r'\<='
t_GE = r'\>='
t_EQ = r'\=='
operadoraritmeticologico = t_OR+r'|'+t_AND+r'|'+t_NOT+r'|'+t_LT+r'|'+t_GT+r'|'+t_LE+r'|'+t_GE+r'|'+t_EQ+r'|'

def t_NOMBRE(self,t):
    r'\#\#[A-Z][a-z]+\s[A-Z][a-z]+\s[A-Z][a-z]+\n'
    return t
def t_MAIL(self,t):
    r'\#\#[a-zA-z\_\-\.]+\@[a-z]+\.[a-z]{2,3}'
    return t
def t_DNI(self,t):
    r'\#\#[0-9]{8}[A-Z]{1}'
    return t
def t_MATRICULA(self,t):
    r'\#\#[0-9]{4}[B-DF-HJ-NP-TV-Z]{3}'
    return t
def t_multilinecomment(self, t):
    r'<!--'
    t.lexer.code_start = t.lexer.lexpos-4
    t.lexer.begin('multilinecomment')

def t_multilinecomment_end(self, t):
    r'.*-+->[\n]?'
    t.lexer.begin('INITIAL')
    t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos]
    t.type = 'MULTILINECOMMENT'
    return t

def t_multilinecomment_lbrace(self, t):
    r'.*[^-->]'

@lex.TOKEN(operadoraritmeticologico)
def t_OPERADORARITMETICOLOGICO(self, t):
    return t

def t_COMMENT(self, t):
    r'[\%\%|\#].*[^\n]?'
    return t

def t_ID(self, t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if self.reserved.get(t.value.lower()) is not None:
        t.type=t.value.lower()
    return t

def t_SALTO(self, t):
    r'\n'
    return t

def t_FCIENT(self, t):
    r'log|exp|sin|cos'
    return t

def t_NOTCIENT(self, t):
    r'\d+(\.\d*)?[e|E]-?\d+'
    return t

def t_HEXADECIMAL(self, t):
    r'0[x|X][0-9a-fA-F]+'
    return t

def t_OCTAL(self, t):
    r'0[o|O][0-7]+'
    return t

def t_DECIMAL(self, t):
    r'[\d+]?\.[\d+]'
    return t

def t_ENTERO(self, t):
    r'\d+'
    return t

def t_BLANKSPACE(self, t):
    r'\s|\t'
    return t

def t_OPERADOR(self, t):
    r'\+|\-|\*|\/'
    return t

def t_ASIGNACION(self, t):
    r'\='
    return t

def t_SEPARADOR(self, t):
    r'\(|\)|\[|\]|\;|\:|\.'
    return t

def t_error(self, t):
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
    'statement : expressionSR || expressionSR OPERADORARITMETICOLOGICO expressionSR'
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