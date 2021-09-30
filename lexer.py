# ------------------------------------------------------------
# Module: lexer.py
# IT's about a tokenizer
# ------------------------------------------------------------

import ply.lex as lex

############################ RULES ###########################

# List of token names.   This is always required
# tuple
tokens = [
    # Identifiers
    'ISM'                  ,
    # Numbers
    'RA9MS7I7'             ,
    'RA9M3ACHARI'          ,
    # Characters and Strings
    '7ARF'                 ,
    'JOMLA'                ,
    # Arithmetic operators
    'ZA2ID'                ,
    'NA9IS'                ,
    'FI'                   ,
    'M9SOUM3LA'            ,
    '9ISMAS7I7A'           ,
    'LBA9IDYALO3LA'        ,
    'OUS'                  ,
    # Comparative operators
    'KBARMN'               ,
    'SGHARMN'              ,
    'KAYSAWI'              ,
    'KAYKHALF'             ,
    'KBARMNWLAKAYSAWI'     ,
    'SGHARMNWLAKAYSAWI'    ,
    # Assignment operators
    'KIYAKHOD'             ,
    'ZID3LIH'              ,
    'N9ESSMNO'             ,
    'DRBOFI'               ,
    '9SMO3LA'              ,
    'BA9IH3LA'             ,
    # Symbols
    '9AWSLISER'            ,
    '9AWSLIMEN'            ,
    'LAMMALISRIYA'         ,
    'LAMMALIMNIYA'         ,
    'MA39OUFALISRIYA'      ,
    'MA39OUFALIMNIYA'      ,
    'JOJNO9AT'             ,
    'FASILA'               ,
    # Newline
    'STERJDID'             ,
    'TAB'                  ,
]

# Dictionary for reserved words
reserved = {
    # Regex for membership operators
    'kaynf'         : 'KAYNF'      ,
    # Boolean values
    's7i7'          : 'S7I7'       ,
    'khate2'        : 'KHATE2'     ,
    # Loops
    'bnisbal'       : 'BNISBAL'    ,
    'ma7ed'         : 'MA7ED'      ,
    'ilamakanch'    : 'ILAMAKANCH' ,
    # Functions
    'kteb'          : 'KTEB'       ,
    '_9ra'          : '_9RA'       ,
    # Reserved words
    'ilakan'        : 'ILAKAN'     ,
    'ila'           : 'ILA'        ,
    'wilamakanch'   : 'WILAMAKANCH',
    'khrej'         : 'KHREJ'      ,
    'kmel'          : 'KMEL'       ,
    'nita9'         : 'NITA9'      ,
    'wla'           : 'WLA'        ,
    'w'             : 'W'
}


tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens
# Regex for arithmetic operators
t_ZA2ID              = r'\+'
t_NA9IS              = r'-'
t_FI                 = r'\*'
t_M9SOUM3LA          = r'/'
t_LBA9IDYALO3LA      = r'\%'
t_9ISMAS7I7A         = r'/{2}'
t_OUS                = r'\*{2}'

# Regex for assignment operators
t_KIYAKHOD           = r'='
t_ZID3LIH            = r'\+='
t_N9ESSMNO           = r'-='
t_DRBOFI             = r'\*='
t_9SMO3LA            = r'/='
t_BA9IH3LA           = r'\%='

# Regex for comparative operators
t_KBARMN             = r'\>'
t_SGHARMN            = r'\<'
t_KAYKHALF           = r'\!='
t_KAYSAWI            = r'\=='
t_KBARMNWLAKAYSAWI   = r'\>='
t_SGHARMNWLAKAYSAWI  = r'\<='


# Regex for symbols
t_9AWSLISER          = r'\('
t_9AWSLIMEN          = r'\)'
t_MA39OUFALISRIYA    = r'\['
t_MA39OUFALIMNIYA    = r'\]'
t_LAMMALISRIYA        = r'\{'
t_LAMMALIMNIYA        = r'\}'
t_JOJNO9AT           = r':'
t_FASILA             = r','

literals = "?@."


# A regular expression rule with some action code

# Regex for identifiers and numbers
def t_ISM(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ISM')  # Check for reserved words
    return t

def t_RA9M3ACHARI(t):
    r'[+-]?[0-9]+\.[0-9]*'
    t.value = float(t.value)
    return t

def t_RA9MS7I7(t):
    r'[+-]?[0-9]+'
    t.value = int(t.value)
    return t

# Ignore comments (comment's rule should be before 7ARF and JOMLA, otherwise it'll not be considered)
def t_T3LI9(t):
    r'\#.*|\'{3}.*\'{3}'
    pass

# Regex for characters and strings
def t_7ARF(t):
    r'\'[^\']?\''
    return t

def t_JOMLA(t):
    r'\'[^\']*\'|\"[^\"]*\"'
    return t

# Define a rule so we can track line numbers
def t_STERJDID(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Rule for tabs
def t_TAB(t):
    r'([ \f]{4})+'
    return t

# Ignore spaces
def t_FARAGH(t):
    r'[ \f]+'
    pass


# Error handling rule
def t_error(t):
    print("Had 7arf khate2 '%s'" % t.value[0])
    t.lexer.skip(1)



############################ MAIN ###########################
# Build the lexer
lexer = lex.lex()


# Give the lexer some input
codeSource = open('codeSource.py', 'r')
lexer.input(codeSource.read())

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    #print(tok.type, tok.value, tok.lineno, tok.lexpos)   # Showing the tokens

codeSource.close()
