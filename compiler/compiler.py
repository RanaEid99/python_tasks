from typing import NamedTuple
import re


class Token(NamedTuple):
    # If u don't know what a class is think of this as a struct with 4 variables inside it.
    type: str
    value: str
    line: int
    column: int


def tokenize(code):
    # ToDo:add the rest of the keywords;
    keywords_cpp = {'auto', 'break', 'case', 'char',
                    'const', 'continue', 'default', 'do',
                    'double', 'else', 'enum', 'extern',
                    'float', 'for', 'goto', 'if','try',
                    'int', 'long','string', 'register', 'return',
                    'short', 'signed', 'sizeof', 'static',
                    'struct', 'switch', 'typedef', 'union',
                    'unsigned', 'void', 'volatile', 'while',
					'asm', 'dynamic_cast', 'namespace', 'reinterpret_cast',
                    'bool', 'explicit', 'new', 'static_cast','using',
                    'false', 'catch', 'operator', 'template',
					'friend', 'private', 'class', 'this','true',
                    'inline', 'public', 'throw', 'const_cast','delete',
                    'mutable', 'protected', 'typeid', 'typename','virtual','wchar_t'}
    # each element in the token_specification list is a named tuple that represents a possible token
    token_specification = [
        # ToDo: Check this example then complete the rest of the tokens.
        # I use a namedtuple in here. It's like a normal tuple but with named fields.
        # So i can get the values using names.
        ('assignment_operator', r'=|(\=)|\*=|\+=|\-=|\%=|\&=|\|=|\^=|\<<=|>>='),  # assignment-operator identifier
		('relational_operator', r'\>|\<|(\>=)|\<\=|\=\=|\!\='),  # relational_operator identifier
		('logical_operator', r'\&\&|\!|(\|\|)'),  # logical_operator identifier
		('binary_operator', r'\+|\-|\*|\/'),  # binary_operator identifier
		('unary_operator', r'\+\+|\-\-'),  # unary_operator identifier
		('bitwise_operator', r'\&|(\|)|\^|\~'),  # bitwise_operator identifier
		('identifier', r'[A-Za-z_]+([A-Za-z_]|[0-9])*'),  #  identifier
		('digits', r'[0-9][0-9]+'),  # digits
		('letter', r'[A-Za-z_]'),  # letter
		('digit', r'[0-9]'),  # digit
		('ternary_operator', r'\?|\:'),  # digit
        #('regular_exp',r'[A-z0-9_]+\s=\s(\w+|\([A-z]+)\s((>=)|>)\s(\d+|\w+)(\)?)\s\?\s("\w+"|\w+)\s:\s("\w+"|\w+);'),
    ]

    # This creates a regular expression that contains all the expressions u wrote in the token_specification list.
    # it uses the property that the regular expression a|b will get either a or b .
    # The syntax uses an idea called list comprehension to create a one line code.
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    line_num = 1
    line_start = 0
    # This for loop iterates over all the found matches in the input code and then creates a token for each match.
    # The finditer method can be found in the python documentation linked in the Task page.
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        # These lines give an example on some processing done to found tokens.
        # U can ignore them if u want.

        # if kind == 'NUMBER':
        #     value = float(value) if '.' in value else int(value)
        # elif kind == 'ID' and value in keywords_cpp:
        #     kind = value
        # elif kind == 'NEWLINE':
        #     line_start = mo.end()
        #     line_num += 1
        #     continue
        # elif kind == 'SKIP':
        #     continue
        # elif kind == 'MISMATCH':
        #     raise RuntimeError(f'{value!r} unexpected on line {line_num}')

        # The yield statement is part f a concept called generators in python.
        yield Token(kind , value , line_num , column)


def main():
    # ToDo: U have to add the file handling logic in here and then pass the code to the tokenize() function.
	file = open("ternary.txt","r")
	for token in tokenize(file.read()):
		print(token)


if __name__ == '__main__':
    main()