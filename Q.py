from sys import *
from interpreter import *
from Lexer import *
from Parser import *

# Example usage
lexer = Lexer(token_patterns)
parser = Parser()
interpreter = Interpreter(lexer, parser)



ss= 'x = 4'
result = interpreter.interpret(ss)


ss= 'y = 25'
result = interpreter.interpret(ss)






input_string = 'if x > 1 print y endif'
result = interpreter.interpret(input_string)
print(result)  # Output: False

inputL_string = 'while x < 19 print x endw'
result = interpreter.interpret(inputL_string)
print(result)  # Output: False

