# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex  # inside lex there is import re for regex

# List of token names.   This is always required
tokens = [
   'ID'     , 'INT'    , 'FLOAT'   , 'CHAR'   , 'STR'    ,
    # Operators
   'PLUS'   , 'MINUS'  , 'MUL'     , 'DIV'   , 'FLOORDIV', 'MOD'     , 'POW',
   'ASSIGN' , 'PLUSASS', 'MINUSASS', 'MULASS', 'DIVASS'  , 'MODASS'  ,
   'GTHAN'  , 'LTHAN'  , 'EQUAL'   , 'NOTEQ' , 'GTORE'   , 'LTORE'   ,
   # Symbols
   'LPAREN' , 'RPAREN' , 'LBRACE'  , 'RBRACE' , 'LBRACKET', 'RBRACKET',
   'SLICE'  , 'COMMA'  , 'PERIOD'  , 'QUOTE'  , 'SINGLQ'  , 'CONDOP'  ,
   'DECORAT', 'CARET'  , 'TILDE'       
]

reserved = {
   # Regex for logical operators
   'w'         : 'W',
   'wla'       : 'WLA',
   'machi'     : 'MACHI',
   # Regex for identity operators
   'howa'      : 'HOWA',
   'howamachi' : 'HOWAMACHI',
   # Regex for membership operators
   'kaynf'     : 'KAYNF',
   'makaynchf' : 'MAKAYNCHF',
   # Boolean values
   's7i7'      : 'S7I7,
   'khate2'    : 'KHATE2',
   # Loops
   '3la9bel'   : '3LA9BEL',
   'ma7ed'     : 'MA7ED',
   # Functions 
   'kteb'      : 'KTEB',
   '9ra'       : '9RA',
   'rjja3'     : 'RJJA3',
   'mjmo3a'    : 'MJMO3A',
   'nou3'      : 'NOU3',
   '7el'       : '7EL',
   'sed'       : 'SED',
   # Reserved words
   'ilakan'    : 'ILAKAN',
   'wilakan'   : 'WILAKAN',
   'ilamakanch': 'ILAMAKANCH',
   'men'       : 'MEN',
   'jib'       : 'JIB',
   '3lachkel'  : '3LACHKEL',
   '3rref'     : '3RREF',
   '7iyed'     : '7IYED',
   'ta7aja'    : 'TA7AJA',
   'khrej'     : 'KHREJ',
   'kmel'      : 'KMEL',
   'douz'      : 'DOUZ',
   '3iyet3la'  : '3IYET3LA',
   'jreb'      : 'JREB'
   #class?
}

tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens (defined by strings)
t_CHAR       = r'.'

  # Regex for arithmetic operators
t_PLUS       = r'\+'   # or enclose it inside a character class as [+]
t_MINUS      = r'-'
t_MUL        = r'\*'
t_DIV        = r'/'
t_FLOORDIV   = r'/{2}'  # integer division
t_MOD        = r'%'
t_POW        = r'\*{2}'

  # Regex for assignment operators
t_ASSIGN     = r'\='
t_PLUSASS    = r'\+='
t_MINUSASS   = r'-='
t_MULASS     = r'\*='
t_DIVASS     = r'/='
t_MODASS     = r'%='

  # Regex for comparison operators
t_GTHAN      = r'\>'
t_LTHAN      = r'\<'
t_EQUAL      = r'={2}'
t_NOTEQ      = r'!\='
t_GTORE      = r'>\=' 
t_LTORE      = r'<\='

  # Regex for symbols
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'{'
t_RBRACE     = r'}'
t_LBRACKET   = r'\['
t_RBRACKET   = r']'
t_SLICE      = r'\:'
t_COMMA      = r',' 
t_PERIOD     = r'\.'
t_QUOTE      = r'\"'
t_SINGLQ     = r'\''
t_CONDOP     = r'\?'
t_DECORAT    = r'\@'
t_CARET      = r'\^'
t_TILDE      = r'\~'


# A regular expression rule with some action code for tokens (defined by functions)
  # the ordre of the regex is so important here
def t_FLOAT(t):
    r'\d+\.\d*'                  
    t.value = float(t.value) 
    return t

def t_INT(t):
    r'\d+'                  
    t.value = int(t.value)
    return t


 
'''def t_NUMBER(t):
    r'\d+'                   # is equivalent to [0-9]+
    t.value = float(t.value) if '.' in t.value else int(t.value)  # converts the string into a Python float or integer
    return t  ''' 

def t_ID(t):
    r'[a-zA-Z_]\w*'          # \w* is equivalent to [a-zA-Z0-9_]*
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded, it's not necessary to define it in tokens

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# EOF handling rule
def __init__(self):
    def t_eof(t):
        # Get more input (Example)
        more = input('... ')
        if more:
            self.lexer.input(more)
            return self.lexer.token()
        return None

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
2. + 5 = 12

ma7ed a < b:
    kteb('6')
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
'''while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

for tok in lexer:
    print(tok)'''

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)





