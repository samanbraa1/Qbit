class IllegalCharError(Exception):
    pass

class ParserError(Exception):
    pass

import re
# Define the token patterns using regular expressions
operator = '=='
token_patterns = [
    (r'\bprint\b', 'PRINT'),                    # Matches the print keyword
    (r'\bif\b', 'IF'),                           # Matches the if keyword
    (r':', 'seperator'), 
    (r'\bFUNCTION\b', "FUNCTION"),
    (r'\b endif\b', 'ENDIF'),
    (r'\bwhile\b', 'WHILE'),                           # Matches the if keyword
    (r'\b endw\b', 'ENDW'), 
    (r'".*?"', 'STRING_LITERAL'),               # Matches string literals inside double quotes
    (r'\d+', 'INTEGER_LITERAL'),                 # Matches integer literals
    (r'\band\b', 'AND'),   
    (r'\bor\b', 'OR'),  
    (re.escape(operator), 'GREATER_THAN_EQUALS'), 
    (r'\+', 'PLUS'),                             # Matches the plus operator
    (r'-', 'MINUS'),                             # Matches the minus operator
    (r'\*', 'MULTIPLY'),                          # Matches the multiplication operator
    (r'/', 'DIVIDE'),                             # Matches the division operator
    (r'=', 'ASSIGNMENT'),                         # Matches the assignment operator
    (r'\b[A-Za-z]+\b', 'VARIABLE'),               # Matches variable names
    (r'\s+', 'WHITESPACE'),                       # Matches whitespace characters
    (r'==', 'EQUALS'),                            # Matches the equals operator
    (r'!=', 'NOT_EQUALS'),                        # Matches the not equals operator
    (r'<', 'LESS_THAN'),                          # Matches the less than operator
    (r'<=', 'LESS_THAN_EQUALS'),                   # Matches the less than or equals operator
    (r'>', 'GREATER_THAN'),                       # Matches the greater than operator
                  # Matches the greater than or equals operator
    (r'\band\b', 'AND'),                              # Matches the logical and operator
    (r'or', 'OR'),                                # Matches the logical or operator           
    (r'\bTrue\b|\bFalse\b', 'BOOLEAN_LITERAL'),  # Matches boolean literals        
]


class Interpreter:
    def __init__(self, lexer, parser):
        self.lexer = lexer
        self.parser = parser

    def interpret(self, input_string):
        try:

            tokens = self.lexer.tokenize(input_string)
            result = self.parser.parse(tokens)
            return result
        except IllegalCharError as e:
            return str(e)
        except ParserError as e:
            return str(e)

