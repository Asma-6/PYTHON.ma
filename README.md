# PYTHON.ma "PYTHON maghribi"
![image](https://user-images.githubusercontent.com/77125092/135387880-f4e27a7c-1cd4-4f62-9d25-a46d28f5dab5.png)
   
PYTHON.ma is a simplified Python compiler in Darija created using Lex and Yacc from PLY library. 

## Why such a project :
This project was a brave idea, and an innovative one, it comes to solve the problem of people who has difficulties dealing with other languages besides their natal language. It is a way to encourage the young Moroccan people to code without the struggle of having a rich French or English vocabulary, or at least a good beginning for kids, to learn how to code from an early age, to help their mind stay awake, and learn how to solve problems on their own.


### `REGEX`
First thing, these are the regex used all along this project :

Variable’s Name:\
	$([0-9] | [A-Z] | [a-z]) 
  
Function’s Name:\
	([A-Z] | [a-z]) ([0-9]) | [A-Z] | [a-z])*
  
Integers:\
	(+ | - | ε) [0-9]+
  
Float:\
	 (+ | - | ε) [0-9]+ .[0-9] 
   
Comments:\
	 (( ( [0-9] | [A-Z] | [a-z] | & | | | ; | , | . | ? | ! | 	= | + | - | * | / | { | } | [ | ] | ( | ) | $ | < | > | _ | 	^ | % | # | ”| ’ )* ))
   
Symbols:\
	, | ; | . | : | \ | { | } | [ | ] | ( | ) | _ | # | ” | ’
  
Arithmetic Operators:\
	  * | + | - | / | %

Logical Operators:\
	 ! | && | || 

Assignment Operators:\
	 = , += , -= , *= , /= , %=

Comparative Operators:\
	 ( ( = | ! | < | > ) = ) | > | <

Keywords:\
	"Any string that is part of the syntax and can’t be used as an identifier, like : _9ra, kteb, ilakan, …" 
  

### `PROGRAMMING SIDE`
After building the Lexer in Darija Language, the parser was implemented also, by using the rules and the best way to construct a meaningful phrase.\
For example:

--> This function simply tells the program that these are the known identifiers, that are not allowed to be as variables:

def p_lm3rofin(p):\
'''  lm3rofin : t3rif\
              | kteb\
              | _9ra\
              | ma7ed\
              | bnisbal\
              | ilakan\
              | ila \
'''\
p[0] = p[1]


### `SOME MEANINGS`
 « kteb » means « print »\
 « _9ra » means « input »\
 « ma7ed » means « while »\
 « bnisbal » means « for »\
 « ilakan » means « if without else »\
 « ila » means « if with else »




