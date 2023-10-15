my_list = [('if', 'IF'), (' ', 'WHITESPACE'), ('x', 'VARIABLE'), (' ', 'WHITESPACE'), ('>', 'GREATER_THAN'), (' ', 'WHITESPACE'), ('1', 'INTEGER_LITERAL'), (':', 'seperator'), (' ', 'WHITESPACE'), ('print', 'PRINT'), (' ', 'WHITESPACE'), ('y', 'VARIABLE'), (' endif', 'ENDIF')]


my_list = [item for item in my_list if item[0] != 'if']
# Find the index of the tuple containing ':'
index = None
for i, item in enumerate(my_list):
    if item[0] == ':':
        index = i
        break


if index is not None:
    # Print the rest of the list starting from the tuple with ':'
    for item in my_list[:index]:
        final=my_list[:index]
else:
    print("Key not found!")


[('if', 'IF'), (' ', 'WHITESPACE'), ('x', 'VARIABLE'), (' ', 'WHITESPACE'), ('>', 'GREATER_THAN'), (' ', 'WHITESPACE'), ('1', 'INTEGER_LITERAL'), (':', 'seperator'), (' ', 'WHITESPACE'), ('print', 'PRINT'), (' ', 'WHITESPACE'), ('y', 'VARIABLE'), (' endif', 'ENDIF')]
    

index = next((i for i, (token, _) in enumerate(my_list) if token == ' '), None)

# Delete the 'WHITESPACE' token if found
if index is not None:
    del my_list[index]
    
print(my_list)


interpreter = Interpreter(lexer, parser)
#print(parser.parse(to))


ss= 'x = 4'
result = interpreter.interpret(ss)


ss= 'y = 25'
result = interpreter.interpret(ss)






input_string = 'if x > 1: print y endif'
result = interpreter.interpret(input_string)
print(result)   

inputL_string = 'while x < 19 print x endw'
result = interpreter.interpret(inputL_string)
print(result)   
