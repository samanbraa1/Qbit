from sys import *
from interpreter import *
from Lexer import *
from Parser import *
to=[('if', 'IF'), (' ', 'WHITESPACE'), ('x', 'VARIABLE'), (' ', 'WHITESPACE'), ('>', 'GREATER_THAN'), (' ', 'WHITESPACE'), ('1', 'INTEGER_LITERAL'), (':', 'seperator'), (' ', 'WHITESPACE'), ('print', 'PRINT'), (' ', 'WHITESPACE'), ('y', 'VARIABLE'), (' endif', 'ENDIF')]

# Example usage
lexer = Lexer(token_patterns)
parser = Parser()
#print(parser.parse(to))
interpreter = Interpreter(lexer, parser)


ss= 'x = 4'
result = interpreter.interpret(ss)


ss= 'y = 25'
result = interpreter.interpret(ss)


input_string = 'if x > 1 and y > 10: print y endif'
result = interpreter.interpret(input_string)
print(result)   

inputL_string = 'while x < 19 print x endw'
result = interpreter.interpret(inputL_string)
print(result)   