# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
import math
from ply.lex import TOKEN
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

tokens = [
    'ENTERO', 'DECIMAL', 'V_BOOLEAN','OCTAL' , 'NOTCIENT', 'FCIENT', 'SALTO', 'ID',
    'SEPARADOR', 'ASIGNACION', 'SIMBOLO',
    'BOOLEANO', 'LT','GT','LE','GE','EQ', 'VARTYPE','VECTOR'
]
literals = ['=', '+', '-', '*', '/', '(', ')', ';', ',', '[',']']

"""
# Tokens
t_OR = r'OR'
t_AND = r'AND'
t_NOT = r'NOT'
#t_LT = r'\<'
#t_GT = r'\>'
#t_LE = r'\<='
#t_GE = r'\>='
#t_EQ = r'\=='
operadoraritmeticologico = t_OR+r'|'+t_AND+r'|'+t_NOT+r'|'+t_LT+r'|'+t_GT+r'|'+t_LE+r'|'+t_GE+r'|'+t_EQ
"""
"""
def t_NOMBRE(t):
    r'\#\#[A-Z][a-z]+\s[A-Z][a-z]+\s[A-Z][a-z]+\n'
    return t
def t_MAIL(t):
    r'\#\#[a-zA-z\_\-\.]+\@[a-z]+\.[a-z]{2,3}'
    return t
def t_DNI(t):
    r'\#\#[0-9]{8}[A-Z]{1}'
    return t
def t_MATRICULA(t):
    r'\#\#[0-9]{4}[B-DF-HJ-NP-TV-Z]{3}'
    return t
"""


def t_multilinecomment(t):
    r'<!--'

    t.lexer.code_start = t.lexer.lexpos-4
    t.lexer.begin('multilinecomment')

def t_multilinecomment_end(t):
    r'.*-+->[\n]?'
    t.lexer.begin('INITIAL')
    t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos]
    t.type = 'MULTILINECOMMENT'
    #return t

def t_multilinecomment_lbrace(t):
    r'.*[^-->]'
    pass
"""
@TOKEN(operadoraritmeticologico)
def t_OPERADORARITMETICOLOGICO(t):
    return t
"""

t_LT = r'\<'
t_GT = r'\>'
t_LE = r'\<='
t_GE = r'\>='
t_EQ = r'\=='

def t_VARTYPE(t):
    r' ENTERO | FLOAT | REAL | BOOLEANO | LONG  '
    return t

def t_BOOLEANO(t):
    r'AND|NOT|OR'
    return t

def t_V_BOOLEAN(t):
    r'true|false'
    return t

def t_COMMENT(t):
    r'[\%\%|\#].*'
    #le he quitado lo del sato de linea al final
    pass

def t_VECTOR(t):
    r'VECTOR'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if reserved.get(t.value.lower()) is None:
        #t.type=t.value.lower()
        return t
    else:
        print("No es posible asignar ese nombre a la variable: Palabra reservada")


def t_SALTO(t):
    r'\n'
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

def t_BLANKSPACE(t):
    r'\s|\t'
    pass
    #return t
"""
def t_OPERADOR(t):
    r'\+|\-|\*|\/'
    return t

def t_ASIGNACION(t):
    r'\='
    return t
    
def t_SEPARADOR(t):
    r'\(|\)|\[|\]|\;|\:|\.'
    return t
"""
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules
#dictionary of names

names = {}


def p_statement_sl_statement(p):
    '''sentencias : statement SALTO sentencias
        | statement '''

def p_statement_declaration(p):
    '''statement : VARTYPE declaration'''

    if p[2] ==None:
        pass
    else:
        if type(p[2]) == str :
            if p[1] == "ENTERO":
                names[p[2]] = 0
            elif p[1] == "FLOAT":
                names[p[2]] = 0.0
            elif p[1] == "BOOLEANO":
                names[p[2]] = False
            else:
                names[p[2]]=0
        else:
            numeros=[]
            num=get_var(p[2],numeros)
            for var in num:

                if p[1] == "ENTERO":
                    names[var] = 0
                elif p[1] == "FLOAT":
                    names[var] = 0.0
                elif p[1] == "BOOLEANO":
                    names[var] = False
                else:
                    names[var]=0
            p[0]=p[2] #-----------------------------------------Necesario??????
        #print("----",p[0])

def get_var(vars,nums):

    #print(vars)
    if type(vars[1])==list:
        if vars[0] is not None: nums.append(vars[0])
        get_var(vars[1],nums)
    else:
        for num in vars:
            if num is not None:
                nums.append(num)
    return nums

def p_statement_vector(p):
    """statement : VECTOR VARTYPE declaration"""
    if p[2] != 'ENTERO' and p[2] != 'REAL' and p[2] != 'BOOLEANO':
        print(" No se puede declarar un vector con ese tipo")
    else:

        if type(p[3])==str and p[3]!=None:
            names[p[3]]=[]
        else:
            vectors=[]
            vectors=get_var(p[3],vectors)
            for vec in vectors:
                names[vec]=[]

def p_statement_dec_assign(p):
    """statement : VARTYPE ID '=' expressionSR"""
    if p[2] not in names.keys():
        names[p[2]]=p[4]
        p[2] = p[4]
    else:
        print("Variable definida anteriormente: ",p[2])

def p_statement_assign(p):
    """statement : ID '=' expressionSR
                | ID '=' boolean"""
    if p[1] in names.keys():
        names[p[1]] = p[3]
        p[1] = p[3]
    else:
        print("Declare primero la variable")


    
def p_statement_expr(p):
    '''statement : expressionSR
                    | boolean'''
    print(p[1])

def p_statement_sl(p):
    'statement : \n'

def p_boolean_single(p):
    '''boolean : expressionLOG'''
    p[0] = p[1]

def p_statement_boolean(p):
    '''boolean :  expressionLOG BOOLEANO boolean'''
    if p[2] == "AND":
        if p[1] is True and p[3] is True:
            p[0]=True
        else:
            p[0]=False
    elif p[2] == "OR":
        if p[1] is True or p[3] is True:
            p[0]=True
        else:
            p[0]=False
    elif p[2] == "NOT":
        if p[1] is not p[3]:#REVIIIISAR PORQUE TE MIRA QUE EL NOMBRE NO SEA EL MISMO NO EL CONTENIDO.
            p[0]=True
        else:
            p[0]=False
    print(p[1])


def p_declaration_vectors(p):
    '''declaration : vector
                        |  vector ',' declaration '''
    print("Heyyyy",p[0])
    if len(p) == 4:
        # print("Multiple declaracion")
        p[0] = []
        p[0].append(p[1])
        p[0].append(p[3])
    else:
        p[0] = p[1]
        # print("Declaration ",p[0])


def p_declaracion_variables(p):
    '''declaration : identificador
                    |  identificador ',' declaration '''

    if len(p)==4:
        #print("Multiple declaracion")
        p[0]=[]
        p[0].append(p[1])
        p[0].append(p[3])
    else:
        p[0]=p[1]
        #print("Declaration ",p[0])

def p_vector(p):
    """vector : ID '[' ENTERO ']' """
    # Preguntar sobre el tamaño, en python no se pueden declarar arrays con un tamaño determinado
    if p[1] in names.keys():
        print("Variable definida anteriormente: ", p[1])
        p[0] = None
    else:
        p[0] = p[1]


def p_statement_declarationSimple(p):
    """identificador : ID"""

    if p[1] in names.keys():
        print("Variable definida anteriormente: ",p[1])
        p[0]=None
    else:
        p[0]=p[1]
    #print("ID: ",p[0:])


def p_expressionLOG(p):
    '''expressionLOG : expressionSR LT expressionSR
                        | expressionSR GT expressionSR
                        | expressionSR LE expressionSR
                        | expressionSR GE expressionSR
                        | expressionSR EQ expressionSR'''

    if p[2]=='<':
        if p[1] < p[3]:
            p[0]=True #no se si hay que poner esto o return True
        else:
            p[0]= False
    elif p[2]=='>':
        if p[1] > p[3]:
            p[0]=True #no se si hay que poner esto o return True
        else:
            p[0]= False
    elif p[2]=="<=":
        if p[1] <= p[3]:
            p[0] = True  # no se si hay que poner esto o return True
        else:
            p[0] = False
    elif p[2]==">=":
        if p[1] >= p[3]:
            p[0] = True  # no se si hay que poner esto o return True
        else:
            p[0] = False
    elif p[2]=="==":
        if p[1] == p[3]:
            p[0] = True  # no se si hay que poner esto o return True
        else:
            p[0] = False


def p_expression_binop(p):
    '''expressionSR : expressionSR '+' expressionMD
                  | expressionSR '-' expressionMD'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expressionSR_expressionMD(p):
    '''expressionSR : expressionMD'''

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
                | V_BOOLEAN
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
    "expression : ID "

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

fname="PruebasOficiales.txt"
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
    print(names)