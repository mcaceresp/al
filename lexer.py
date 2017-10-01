import ply.lex as lex
import re

tokens = ('WHILE',
          'LBRACE',
          'RBRACE',
          'STRING',
          'NUMBER')


def t_WHILE(t):
    r'(?i)while'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t


def t_LBRACE(t):
    r'{'
    return t


def t_EQU(t):
    r'='
    return t


def t_RBRACE(t):
    r'}'
    return t


def t_STRING(t):
    r'(\"[^"]*\"|\'[^\']*\')'
    # Esto acepta strings de la forma "..." y '...'. Notar las negaciones!
    t.value = t.value[1:-1]  # Elimino las comillas.
    return t


def t_NUMBER(t):
    r'[0-9]*\.[0-9]+|[0-9]+'
    # Numeros enteros y decimales con al menos un numero despues de la coma.
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    # Salto de linea (contar)
    return t


t_ignore = ' \t\n'  # Ignorar esto!


def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    # Tratamiento de errores.
    t.lexer.skip(1)


lexer = lex.lex()

with open('sample.txt', 'r') as f:
    contents = f.read()
    lex.input(contents)
    for tok in iter(lex.token, None):
        print repr(tok.type), repr(tok.value)
