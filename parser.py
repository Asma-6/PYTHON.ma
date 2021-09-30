# ------------------------------------------------------------
# Module: compiler_parser.py
# IT's about parsing with grammar rules
# ------------------------------------------------------------

import ply.yacc as yacc

# Get the token map from the lexer (it's required)
from lexer import tokens

############################ GRAMMAR_RULES ###########################

def p_lbdya(p):
    '''  lbdya  : lbdya STERJDID lbdya
                | lm3rofin
    '''
    if len(p) == 2:
        #if p[1] != None:  print(p[1])           # Showing the trees
        result = run(p[1])                       # Running the program
        if result != None:  print(result)

def p_lm3rofin(p):
    '''  lm3rofin : t3rif
                  | kteb
                  | 9ra
                  | ma7ed
                  | bnisbal
                  | ilakan
                  | ila
    '''
    p[0] = p[1]

def p_lkmala_dlm3rofin(p):
    '''  lm3rofin :
    '''


############ Concatenation :

def p_tjmi3(p):
    ''' tjmi3   : 7ARF
                | JOMLA
                | tjmi3 tjmi3
                | tjmi3 ZA2ID tjmi3
    '''
    if len(p) == 2:
        p[0] = p[1][1:-1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        # the parser just builds the tree up using the grammar rules
        p[0] = ('+', p[1], p[3])


############ Assignment operators :

def p_t3rif(p):
    '''  t3rif  : ISM KIYAKHOD t3rif1
                | ISM ZID3LIH t3rif2
                | ISM N9ESSMNO t3rif3
                | ISM DRBOFI t3rif3
                | ISM 9SMO3LA t3rif3
                | ISM BA9IH3LA t3rif3
    '''
    p[0] = (p[2], ('ISM', p[1]), p[3])

def p_lkmala_dt3rif(p):
    '''  t3rif  : var KIYAKHOD t3rif1
    '''
    p[0] = (p[2], p[1], p[3])

def p_t3rif1_t3rif2_t3rif3(p):
    '''  t3rif1  : 3ibara2
                 | mo9arana
                 | var
                 | t3rif2
                 | 9ra
         t3rif2  : t3rif3
                 | tjmi3
         t3rif3  : 3ibara1
                 | RA9MS7I7
                 | RA9M3ACHARI
    '''
    p[0] = p[1]


var = []

def p_var(p):
    '''  var : ISM var1
    '''
    p[0] = ('ISM', p[1], p[2])

def p_var1(p):
    '''  var1 : MA39OUFALISRIYA ldakhl MA39OUFALIMNIYA
              | var1 MA39OUFALISRIYA ldakhl MA39OUFALIMNIYA
    '''
    global var
    if len(p) == 4:
        var.append(p[2])
        p[0] = var
    else:
        var.append(p[3])
        p[0] = var

def p_ldakhl(p):
    '''  ldakhl : RA9MS7I7
                | tjmi3
                | ra9m JOJNO9AT ra9m
         ra9m   : RA9MS7I7
                |
    '''
    if len(p) == 1:
        p[0] = ''
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = {p[1]: p[3]}

def p_lkmala_dldakhl(p):
    '''  ldakhl : ISM
    '''
    p[0] = ('ISM', p[1])


l = []

def p_3ibara2(p):
    '''  3ibara2    : 9AWSLISER mjmo3a 9AWSLIMEN
    '''
    global l
    l = []
    p[0] = tuple(p[2])

def p_lkmala_d3ibara2_la2i7a(p):
    '''  3ibara2    : MA39OUFALISRIYA la2i7a MA39OUFALIMNIYA
         la2i7a     : mjmo3a
                    |
    '''
    global l
    l = []
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_lkmala1_d3ibara2(p):
    '''  3ibara2    : LAMMALISRIYA mo3jam LAMMALIMNIYA
    '''
    p[0] = p[2]

def p_mo3jam(p):
    '''  mo3jam     : lwel JOJNO9AT tani
                    | lwel JOJNO9AT tani FASILA mo3jam
                    |
    '''
    global l
    l = []
    if len(p) == 1:
        p[0] = {}
    elif len(p) == 4:
        p[0] = {p[1]:p[3]}
    else:
        p[0] = {**{p[1]:p[3]}, **p[5]}

def p_lkmala_dmjmo3a_tani(p):
    '''  mjmo3a     : tani FASILA tani
                    | tani FASILA mjmo3a
                    |
         tani       : lwel
    '''
    global l
    if len(p) == 1:
        p[0] = ()
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = l

def p_lkmala_dtani(p):
    ''' tani  : RA9MS7I7
              | RA9M3ACHARI
    '''
    global l
    l.append(p[1])
    p[0] = p[1]

def p_lwel(p):
    '''  lwel   : 7ARF
                | JOMLA
    '''
    global l
    l.append(p[1][1:-1])
    p[0] = p[1][1:-1]


############ Arithmetic operators :

precedence = (                       # Remove the ambiguity in grammar
             ('left','ZA2ID','NA9IS'),
             ('left','FI','M9SOUM3LA','9ISMAS7I7A','LBA9IDYALO3LA','OUS')
             )

def p_3ibara1_3ibara3(p):   # Spaces before and after (ZA2ID and NA9IS) are required due to [+-] in the regex
    '''  3ibara1 : 3ibara1 ZA2ID 3ibara3
                 | 3ibara1 NA9IS 3ibara3
                 | 3ibara3
         3ibara3 : 3ibara3 FI mo3amil
                 | 3ibara3 M9SOUM3LA mo3amil
                 | 3ibara3 9ISMAS7I7A mo3amil
                 | 3ibara3 LBA9IDYALO3LA mo3amil
                 | 3ibara3 OUS mo3amil
                 | mo3amil
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])


def p_mo3amil(p):
    '''  mo3amil : RA9MS7I7
                 | RA9M3ACHARI
                 | 9AWSLISER 3ibara1 9AWSLIMEN
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_lkmala_dmo3amil(p):
    '''  mo3amil : ISM
    '''
    p[0] = ('ISM', p[1])


############ Comparative operators :

def p_ma9arana(p):
    '''  mo9arana   : jiha KBARMN jiha
                    | jiha SGHARMN jiha
                    | jiha KAYSAWI jiha
                    | jiha KAYKHALF jiha
                    | jiha KBARMNWLAKAYSAWI jiha
                    | jiha SGHARMNWLAKAYSAWI jiha
    '''
    p[0] = (p[2], p[1], p[3])

def p_jiha(p):
    '''  jiha  : 3ibara1
               | tjmi3
    '''
    p[0] = p[1]


############ Function_Print :

ktab =[]

def p_kteb(p):
    '''  kteb  : ktab ktaba 9AWSLIMEN
    '''
    p[1].append(p[3])
    p[0] = tuple(p[1])

def p_ktab(p):
    '''  ktab  : KTEB 9AWSLISER
    '''
    global ktab
    ktab = ['KTEB', p[2]]
    p[0] = ktab

def p_ktaba(p):
    '''  ktaba    : var
                  | 3ibara1
                  | 3ibara2
                  | mo9arana
                  | RA9MS7I7
                  | RA9M3ACHARI
                  | tjmi3
                  | walo
                  | ktaba FASILA ktaba
    '''
    global ktab
    if len(p) == 2:
        ktab.append(p[1])
    else:
        ktab.append(p[3])

def p_walo(p):
    '''  walo :
    '''
    p[0] = ''


############ Function_Input :

def p_9ra(p):
    '''  9ra  : _9RA 9AWSLISER chi7aja 9AWSLIMEN
    '''
    p[0] = ('_9RA', p[2], p[3], p[4])

def p_chi7aja(p):
    '''  chi7aja  : tjmi3
                  | walo
    '''
    p[0] = p[1]

############ IF ONLY :

kmalat = []
def p_ila(p):
    '''   ila : bdyat dirr
    '''

    p[0] = tuple(p[1]) + tuple(p[2])


def p_bdyat(p):
    '''   bdyat : ILA mo9aranat JOJNO9AT
    '''
    p[0] = ['ILA',tuple(p[2]),p[3]]


def p_dirr(p):
    '''  dirr : lm3rofin
               | STERJDID LAMMALISRIYA dirr1 LAMMALIMNIYA
    '''
    global kmalat
    if len(p) == 2:
        kmalat.append(p[1])
        p[0] = kmalat
    else:
        p[0] = kmalat

def p_dirr1(p):
    '''   dirr1 : lm3rofin
               | dirr1 STERJDID dirr1
    '''
    global kmalat
    if len(p) == 2:
        kmalat.append(p[1])
        p[0] = kmalat
    else:
        p[0] = kmalat


############ IF ELSE :

kmala = []
kmalaIf = []
kmalaElse = []
def p_ilakan(p):
    '''   ilakan : bdya3 dir3 kmalaIf
    '''
    if len(p) == 4:
        p[0] = tuple(p[1]) + tuple(p[2]) + tuple(p[3])


def p_bdya3(p):
    '''   bdya3 : ILAKAN mo9aranat JOJNO9AT
    '''
    p[0] = ['ILAKAN',tuple(p[2]),p[3]]

def p_moqaranat(p):
    '''   mo9aranat : mo9arana
                    | mo9arana op mo9arana
                    | 9AWSLISER mo9aranat 9AWSLIMEN op mo9arana
                    | 9AWSLISER mo9aranat 9AWSLIMEN op 9AWSLISER mo9aranat 9AWSLIMEN
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = [p[2],p[1],p[3]]
    elif len(p) == 6:
        p[0] = [p[4],tuple(p[2]),tuple(p[5])]
    else:
        p[0] = [p[4],tuple(p[2]),tuple(p[6])]


def p_op(p):
    '''   op : WLA
             | W
    '''
    p[0] = p[1]

def p_dir3(p):
    '''  dir3 : lm3rofin
               | STERJDID LAMMALISRIYA dir4 LAMMALIMNIYA
    '''
    global kmala
    if len(p) == 2:
        kmala.append(p[1])
        p[0] = kmala
    else:
        p[0] = kmala

def p_dir4(p):
    '''   dir4 : lm3rofin
               | dir4 STERJDID dir4
    '''
    global kmala
    if len(p) == 2:
        kmala.append(p[1])
        p[0] = kmala
    else:
        p[0] = kmala

def p_kmalaIf(p):
    '''   kmalaIf : STERJDID bdya4 dir5


    '''
    if len(p) == 4:
        global kmalaElse
        kmalaElse.append(tuple(p[2]) + tuple(p[3]))
        p[0] = kmalaElse

def p_bdya4(p):
    '''   bdya4 : WILAMAKANCH JOJNO9AT'''
    p[0] = ['WILAMAKANCH', p[2]]

def p_dir5(p):
    '''  dir5 : lm3rofin
              | STERJDID LAMMALISRIYA dir6 LAMMALIMNIYA
    '''
    global kmalaElse
    if len(p) == 2:
        kmalaElse.append(p[1])
        p[0] = kmalaElse
    else:
        p[0] = kmalaElse

def p_dir6(p):
    '''   dir6 : lm3rofin
               | dir6 STERJDID dir6
    '''
    global kmalaElse
    if len(p) == 2:
        kmalaElse.append(p[1])
        p[0] = kmalaElse
    else:
        p[0] = kmalaElse


############ Loop_While :

bdya = []
tatima = []

def p_ma7ed(p):
    '''  ma7ed  : bdya STERJDID TAB LAMMALISRIYA dir LAMMALIMNIYA
                | bdya STERJDID TAB LAMMALISRIYA dir LAMMALIMNIYA tatima
    '''
    global bdya, tatima        # these 2 lists made just to manage ma7ed inside ma7ed
    bdya = []
    tatima = []
    if len(p) == 7:
        p[0] = p[1] + tuple(p[5])
    else:
        p[0] = p[1] + tuple(p[5]) + p[7]

def p_bdya(p):
    '''  bdya : MA7ED chart JOJNO9AT
    '''
    p[0] = ('MA7ED', p[2], p[3])

def p_tatima(p):
    '''  tatima : tatima1 LAMMALISRIYA dir1 LAMMALIMNIYA
    '''
    p[0] = p[1] + tuple(p[3])

def p_tatima1(p):
    '''  tatima1 : STERJDID ILAMAKANCH JOJNO9AT STERJDID TAB
    '''
    p[0] = (p[2], p[3])

def p_chart(p):
    '''  chart    : S7I7
                  | KHATE2
                  | RA9MS7I7
                  | mo9arana
    '''
    p[0] = p[1]

def p_dir(p):
    '''   dir : lm3rofin
              | KHREJ
              | KMEL
              | dir STERJDID TAB dir
    '''
    global bdya
    if len(p) == 2:
        bdya.append(p[1])
        p[0] = bdya
    else:
        p[0] = bdya

def p_dir1(p):
    '''   dir1 : lm3rofin
               | KHREJ
               | KMEL
               | dir1 STERJDID TAB dir1
    '''
    global tatima
    if len(p) == 2:
        tatima.append(p[1])
        p[0] = tatima
    else:
        p[0] = tatima


############ Loop_For :

list = []

def p_bnisbal(p):
    '''  bnisbal  : bdya1 STERJDID TAB LAMMALISRIYA dir2 LAMMALIMNIYA
    '''
    global list           # this list made just to manage bnisbal inside bnisbal
    list = []
    p[0] = p[1] + tuple(p[5])

def p_bdya1(p):
    '''  bdya1 : BNISBAL ISM KAYNF blasa JOJNO9AT
    '''
    p[0] = ('BNISBAL', ('ISM', p[2]), p[3], p[4], p[5])

def p_blasa(p):
    '''  blasa  : 3ibara2
                | tjmi3
                | NITA9 9AWSLISER lwast 9AWSLIMEN
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('NITA9', p[2], p[3], p[4])

def p_kmala_dblasa(p):
    '''  blasa  : ISM
    '''
    p[0] = ('ISM', p[1])

def p_lwast(p):
    '''  lwast   : RA9MS7I7
                 | RA9MS7I7 FASILA RA9MS7I7
                 | RA9MS7I7 FASILA RA9MS7I7 FASILA RA9MS7I7
    '''
    if len(p) == 2:
        p[0] = p[1],
    elif len(p) == 4:
        p[0] = p[1], p[3]
    else:
        p[0] = p[1], p[3], p[5]

def p_dir2(p):
    '''   dir2 : lm3rofin
               | KHREJ
               | KMEL
               | dir2 STERJDID TAB dir2
    '''
    global list
    if len(p) == 2:
        list.append(p[1])
        p[0] = list
    else:
        p[0] = list


############ Error_Handling_Rule :

def p_error(p):
    print("Kayn khata2 flktaba !!",p )


############################ RUN_FUNCTION ###########################

# Walk the trees and create the program

mjmo3at_t3rif = {}
kayn, khrej, kmel, khrej1, kmel1, khrej2, kmel2 = 0, 0, 0, 0, 0, 0, 0

def run(p):
    global mjmo3at_t3rif

    if type(p) == tuple:       # tuple here is the built trees

        # Empty tuple:
        if p == ():
            return p

        # ISM
        elif p[0] == 'ISM':
            if p[1] not in mjmo3at_t3rif:
                print(p[1], 'mam3roufch!')
                return None
            else:
                if len(p) == 2:
                    return mjmo3at_t3rif[p[1]]
                else:
                    ism = mjmo3at_t3rif[p[1]]
                    if len(p[2]) == 1:
                        if type(run(p[2][0])) == dict:
                            for a, b in run(p[2][0]).items():
                                if a == '':
                                    ism = ism[: b]
                                elif b == '':
                                    ism = ism[a:]
                                else:
                                    ism = ism[a: b]
                        else:
                            ism = ism[run(p[2][0])]
                    '''elif len(p[2]) == 2:
                        ism = ism[run(p[2][0])][run(p[2][1])]
                    elif len(p[2]) == 3:
                        ism = ism[run(p[2][0])][run(p[2][1])][run(p[2][2])]'''
                    return ism

        # Assignment operators
        elif p[0] == '=':
            if len(p[1]) == 2:
                mjmo3at_t3rif[p[1][1]] = run(p[2])
                # print(mjmo3at_t3rif)         # showing the dictionary of variabls
                return None
            else:
                issm = mjmo3at_t3rif[p[1][1]]
                issm[run(p[1][2][0])] = run(p[2])
                mjmo3at_t3rif[p[1][1]] = issm
                return None
        elif p[0] == '+=':
             mjmo3at_t3rif[p[1][1]] = run(p[1]) + run(p[2])
             return None
        elif p[0] == '-=':
            mjmo3at_t3rif[p[1][1]] = run(p[1]) - run(p[2])
            return None
        elif p[0] == '*=':
            mjmo3at_t3rif[p[1][1]] = run(p[1]) * run(p[2])
            return None
        elif p[0] == '/=':
            if run(p[2]) == 0:
                print("Maymkench t9sem 3la sifr!!")
                return None
            else:
                mjmo3at_t3rif[p[1][1]] = run(p[1]) / run(p[2])
                return None
        elif p[0] == '%=':
            mjmo3at_t3rif[p[1][1]] = run(p[1]) % run(p[2])
            return None

        # Arithmetic operators
        elif p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            if run(p[2]) == 0:
                print("Maymkench t9sem 3la sifr!!")
                return None
            else:
                return run(p[1]) / run(p[2])
        elif p[0] == '//':
            if run(p[2]) == 0:
                print("Maymkench t9sem 3la sifr!!")
                return None
            else:
                return run(p[1]) // run(p[2])
        elif p[0] == '%':
            return run(p[1]) % run(p[2])
        elif p[0] == '**':
            return run(p[1]) ** run(p[2])

        # Logical operators
        elif p[0] == '>':
            if run(p[1]) > run(p[2]):
                return 's7i7'
            else:
                return 'khate2'
        elif p[0] == '<':
            if run(p[1]) < run(p[2]):
                return 's7i7'
            else:
                return 'khate2'
        elif p[0] == '==':
            if run(p[1]) == run(p[2]):
                return 's7i7'
            else:
                return 'khate2'
        elif p[0] == '!=':
            if run(p[1]) != run(p[2]):
                return 's7i7'
            else:
                return 'khate2'
        elif p[0] == '>=':
            if run(p[1]) >= run(p[2]):
                return 's7i7'
            else:
                return 'khate2'
        elif p[0] == '<=':
            if run(p[1]) <= run(p[2]):
                return 's7i7'
            else:
                return 'khate2'

        # Functions
        elif p[0] == 'KTEB':
            if len(p) == 4:
                return run(p[2])
            else:
                for i in range(2, len(p)):
                    natija = run(p[i])
                    if natija != None and natija != ')':
                        print(run(p[i]), end=' ')
                print()

        elif p[0] == '_9RA':
           return input(run(p[2]))
        elif p[0] == 'NITA9':
            if len(p[2]) == 3:
                return range(p[2][0], p[2][1], p[2][2])
            elif len(p[2]) == 2:
                return range(p[2][0], p[2][1])
            else:
                return range(p[2][0])

        #IF ELSE

        elif p[0] == 'ILAKAN':
            res = []
            resu = []
            faux = False
            vrai = False
            vraie = False
            fausse = False
            if len(p)==4:
                if p[1][0] == 'w':
                    for i in range(1,len(p[1])):
                        if p[1][i][0] == 'wla':
                            for j in range(1, len(p[1][i])):
                                resu.append(run(p[1][i][j]))
                            for j in range(0, len(resu)):
                                if resu[j] == "s7i7":
                                    vraie = True
                                    break
                            if vraie == True:  # au moins une comparaison est vraie
                                res.append("s7i7")
                            else: res.append("khate2")
                        elif p[1][i][0] == 'w':
                            for j in range(1, len(p[1][i])):
                                resu.append(run(p[1][i][j]))
                            for j in range(0, len(resu)):
                                if resu[j] == "khate2":
                                    fausse = True
                                    break
                            if fausse == True:  # tout est vrai
                                res.append("khate2")
                            else: res.append("s7i7")
                        else:
                            res.append(run(p[1][i]))
                    for i in range(0,len(res)):
                        #print(res[i])
                        if res[i] == "khate2":
                            faux = True

                    if faux == False: #tout est vrai
                        print(run(p[3]))
                elif p[1][0] == 'wla':
                    for i in range(1,len(p[1])):
                        res.append(run(p[1][i]))
                    for i in range(0,len(res)):
                        if res[i] == "s7i7":
                            vrai = True
                            break
                    if vrai == True: #au moins une comparaison est vraie
                        print(run(p[3]))
                elif run(p[1]) == "s7i7":
                    print(run(p[3]))
            if len(p) > 4 :
                if p[1][0] == 'w':
                    for i in range(1,len(p[1])):
                        if p[1][i][0] == 'wla':
                            for j in range(1, len(p[1][i])):
                                resu.append(run(p[1][i][j]))
                            for j in range(0, len(resu)):
                                if resu[j] == "s7i7":
                                    vraie = True
                                    break
                            if vraie == True:  # au moins une comparaison est vraie
                                res.append("s7i7")
                            else: res.append("khate2")
                        elif p[1][i][0] == 'w':
                            for j in range(1, len(p[1][i])):
                                resu.append(run(p[1][i][j]))
                            for j in range(0, len(resu)):
                                if resu[j] == "khate2":
                                    fausse = True
                                    break
                            if fausse == True:  # tout est vrai
                                res.append("khate2")
                            else: res.append("s7i7")
                        else:
                            res.append(run(p[1][i]))
                    for i in range(0,len(res)):
                        #print(res[i])
                        if res[i] == "khate2":
                            faux = True

                    if faux == False: #tout est vrai
                        for i in range(3, len(p)):
                            natija = run(p[i])
                            if natija != None and natija != 'ILAKAN':
                                print(natija)
                elif p[1][0] == 'wla':
                    for i in range(1,len(p[1])):
                        res.append(run(p[1][i]))
                    for i in range(0,len(res)):
                        if res[i] == "s7i7":
                            vrai = True
                            break
                    if vrai == True: #au moins une comparaison est vraie
                        for i in range(3, len(p)):
                            natija = run(p[i])
                            if natija != None and natija != 'ILAKAN':
                                print(natija)
                elif run(p[1]) == "s7i7":
                    for i in range(3,len(p)):
                        natija = run(p[i])
                        if natija!=None and natija != 'ILAKAN':
                            print(natija)
            if p[len(p)-1][0] == 'WILAMAKANCH':
                if len(p) - 1 == 4:
                    if p[1][0] == 'w':
                        for i in range(1, len(p[1])):
                            if p[1][i][0] == 'wla':
                                for j in range(1, len(p[1][i])):
                                    resu.append(run(p[1][i][j]))
                                for j in range(0, len(resu)):
                                    if resu[j] == "s7i7":
                                        vraie = True
                                        break
                                if vraie == True:  # au moins une comparaison est vraie
                                    res.append("s7i7")
                                else:
                                    res.append("khate2")
                            elif p[1][i][0] == 'w':
                                for j in range(1, len(p[1][i])):
                                    resu.append(run(p[1][i][j]))
                                for j in range(0, len(resu)):
                                    if resu[j] == "khate2":
                                        fausse = True
                                        break
                                if fausse == True:  # tout est vrai
                                    res.append("khate2")
                                else:
                                    res.append("s7i7")
                            else:
                                res.append(run(p[1][i]))
                        for i in range(0, len(res)):
                            # print(res[i])
                            if res[i] == "khate2":
                                faux = True

                        if faux == True:  # condition non verifiee!
                            print(run(p[len(p)-1][2]))
                    elif p[1][0] == 'wla':
                        for i in range(1, len(p[1])):
                            res.append(run(p[1][i]))
                        for i in range(0, len(res)):
                            if res[i] == "s7i7":
                                vrai = True
                                break
                        if vrai == False:  # au moins une comparaison est vraie
                            print(run(p[len(p)-1][2]))
                    elif run(p[1]) == "khate2":
                        print(run(p[len(p)-1][2]))
                if len(p)-1 > 4:
                    if p[1][0] == 'w':
                        for i in range(1, len(p[1])):
                            if p[1][i][0] == 'wla':
                                for j in range(1, len(p[1][i])):
                                    resu.append(run(p[1][i][j]))
                                for j in range(0, len(resu)):
                                    if resu[j] == "s7i7":
                                        vraie = True
                                        break
                                if vraie == True:  # au moins une comparaison est vraie
                                    res.append("s7i7")
                                else:
                                    res.append("khate2")
                            elif p[1][i][0] == 'w':
                                for j in range(1, len(p[1][i])):
                                    resu.append(run(p[1][i][j]))
                                for j in range(0, len(resu)):
                                    if resu[j] == "khate2":
                                        fausse = True
                                        break
                                if fausse == True:  # tout est vrai
                                    res.append("khate2")
                                else:
                                    res.append("s7i7")
                            else:
                                res.append(run(p[1][i]))
                        for i in range(0, len(res)):
                            if res[i] == "khate2":
                                faux = True
                                break
                        if faux == True:  # condition non verifiee
                            for i in range(2, len(p[len(p)-1])):
                                natija = run(p[len(p)-1][i])
                                if natija != None and natija != 'ILAKAN':
                                    print(natija)
                    elif p[1][0] == 'wla':
                        for i in range(1, len(p[1])):
                            res.append(run(p[1][i]))
                        for i in range(0, len(res)):
                            if res[i] == "s7i7":
                                vrai = True
                                break
                        if vrai == False:  # condition non verifiee
                            for i in range(2, len(p[len(p)-1])):
                                natija = run(p[len(p)-1][i])
                                if natija != None and natija != 'ILAKAN':
                                    print(natija)
                    elif run(p[1]) == "khate2":
                        for i in range(2, len(p[len(p)-1])):
                            natija = run(p[len(p)-1][i])
                            if natija != None and natija != 'ILAKAN':
                                print(natija)

        # IF only
        elif p[0] == 'ILA':
            res = []
            resu = []
            faux = False
            vrai = False
            vraie = False
            fausse = False
            if len(p)==4:
                if p[1][0] == 'w':
                    for i in range(1,len(p[1])):
                        if p[1][i][0] == 'wla':
                            for j in range(1, len(p[1][i])):
                                resu.append(run(p[1][i][j]))
                            for j in range(0, len(resu)):
                                if resu[j] == "s7i7":
                                    vraie = True
                                    break
                            if vraie == True:  # au moins une comparaison est vraie
                                res.append("s7i7")
                            else: res.append("khate2")
                        elif p[1][i][0] == 'w':
                            for j in range(1, len(p[1][i])):
                                resu.append(run(p[1][i][j]))
                            for j in range(0, len(resu)):
                                if resu[j] == "khate2":
                                    fausse = True
                                    break
                            if fausse == True:  # tout est vrai
                                res.append("khate2")
                            else: res.append("s7i7")
                        else:
                            res.append(run(p[1][i]))
                    for i in range(0,len(res)):
                        #print(res[i])
                        if res[i] == "khate2":
                            faux = True

                    if faux == False: #tout est vrai
                        print(run(p[3]))
                elif p[1][0] == 'wla':
                    for i in range(1,len(p[1])):
                        res.append(run(p[1][i]))
                    for i in range(0,len(res)):
                        if res[i] == "s7i7":
                            vrai = True
                            break
                    if vrai == True: #au moins une comparaison est vraie
                        print(run(p[3]))
                elif run(p[1]) == "s7i7":
                    print(run(p[3]))
            if len(p) > 4 :
                if p[1][0] == 'w':
                    for i in range(1,len(p[1])):
                        if p[1][i][0] == 'wla':
                            for j in range(1, len(p[1][i])):
                                resu.append(run(p[1][i][j]))
                            for j in range(0, len(resu)):
                                if resu[j] == "s7i7":
                                    vraie = True
                                    break
                            if vraie == True:  # au moins une comparaison est vraie
                                res.append("s7i7")
                            else: res.append("khate2")
                        elif p[1][i][0] == 'w':
                            for j in range(1, len(p[1][i])):
                                resu.append(run(p[1][i][j]))
                            for j in range(0, len(resu)):
                                if resu[j] == "khate2":
                                    fausse = True
                                    break
                            if fausse == True:  # tout est vrai
                                res.append("khate2")
                            else: res.append("s7i7")
                        else:
                            res.append(run(p[1][i]))
                    for i in range(0,len(res)):
                        #print(res[i])
                        if res[i] == "khate2":
                            faux = True

                    if faux == False: #tout est vrai
                        for i in range(3, len(p)):
                            natija = run(p[i])
                            if natija != None and natija != 'ILAKAN':
                                print(natija)
                elif p[1][0] == 'wla':
                    for i in range(1,len(p[1])):
                        res.append(run(p[1][i]))
                    for i in range(0,len(res)):
                        if res[i] == "s7i7":
                            vrai = True
                            break
                    if vrai == True: #au moins une comparaison est vraie
                        for i in range(3, len(p)):
                            natija = run(p[i])
                            if natija != None and natija != 'ILAKAN':
                                print(natija)
                elif run(p[1]) == "s7i7":
                    for i in range(3,len(p)):
                        natija = run(p[i])
                        if natija!=None and natija != 'ILAKAN':
                            print(natija)

        # Loops
        elif p[0] == 'MA7ED':
            while True:
                if run(p[1]) != 'khate2':
                    for i in range(3, len(p)):
                        natija = run(p[i])
                        if natija!= None:
                            if natija == 'khrej':
                                global khrej
                                khrej = 1
                                break
                            elif natija == 'kmel':
                                global kmel
                                kmel = 1
                                break
                            elif natija != 'ilamakanch':
                                print(natija)
                            else:
                                break
                else:
                    for i in range(4, len(p)):
                        if p[i] == 'ilamakanch':
                            global kayn
                            kayn = 1
                            while True:
                                if run(p[1]) == 'khate2':
                                    for j in range(i+2, len(p)):
                                        natija1 = run(p[j])
                                        if natija1 != None:
                                            if natija1 == 'khrej':
                                                global khrej1
                                                khrej1 = 1
                                                break
                                            elif natija1 == 'kmel':
                                                global kmel1
                                                kmel1 = 1
                                                break
                                            else:
                                                print(natija1)
                                    if kmel1 == 1:
                                        continue
                                    elif khrej1 == 1:
                                        break
                                else:
                                    break
                    if kayn != 1:
                        break
                    if kmel1 == 1:
                        continue
                    elif khrej1 == 1:
                        break
                if kmel == 1:
                    continue
                elif khrej == 1:
                    break

        elif p[0] == 'BNISBAL':
            for var in run(p[3]):
                mjmo3at_t3rif[p[1][1]] = var
                for i in range(5, len(p)):
                    natija2 = run(p[i])
                    if natija2 != None:
                        if natija2 == 'khrej':
                            global khrej2
                            khrej2 = 1
                            break
                        elif natija2 == 'kmel':
                            global kmel2
                            kmel2 = 1
                            break
                        else:
                            print(natija2)
                if kmel2 == 1:
                    continue
                elif khrej2 == 1:
                    break

        # for mjmo3a which has the type of tuple but is not a tree
        else:
            return p

    # for some in 3ibara1, 3ibara2 and 7arfwlajomla which is not a tuple
    else:
        return p


############################ MAIN ###########################

# Build the parser
parser = yacc.yacc()    # --> the output produced by debugging here is parser.out

# Give the parser some input
codeSource = open('codeSource.py', 'r')
parser.parse(codeSource.read())
codeSource.close()
