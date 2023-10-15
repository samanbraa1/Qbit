class ParserError(Exception):
    pass


class Parser:
    def __init__(self):
        self.expression_parser = ExpressionParser()
        self.print_parser = PrintParser()
        self.assignment_parser = AssignmentParser()
        self.variable_store = {}
        self.if_parser = IfParser()
        self.whileparser = whileParser()

    def parse(self, tokens):
        if tokens[0][1] == "PRINT":

            return self.print_parser.parse_print(tokens)
        elif tokens[0][1] == "IF":

            return self.if_parser.parse_if(tokens)

        elif tokens[0][1] == "WHILE":

            return self.whileparser.parse_while(tokens)
        elif tokens[2][1] == "ASSIGNMENT":

            return self.assignment_parser.parse_assignment(tokens)

        else:
            return self.expression_parser.parse_expression(tokens)


class ExpressionParser:

    def parse_expression(self, tokens):
        if len(tokens) == 1 and tokens[0][1] == "INTEGER_LITERAL":

            return int(tokens[0][0])
        elif len(tokens) == 1 and tokens[0][1] == "VARIABLE":

            variable_name = tokens[0][0]

            return int(parser_ins.variable_store[variable_name])
        
        elif len(tokens) == 1 and tokens[0][1] == "BOOLEAN_LITERAL":

            return tokens[0][0] == "True"
        elif len(tokens) == 5:

            left_operand = self.parse_expression(tokens[:1])

            operator = tokens[2][1]

            right_operand = self.parse_expression(tokens[4:])

            if operator == "PLUS":
                return left_operand + right_operand
            
            elif operator == "MINUS":
                return left_operand - right_operand
            
            elif operator == "MULTIPLY":
                return left_operand * right_operand
            
            elif operator == "DIVIDE":
                return left_operand / right_operand
            
            elif operator == "LESS_THAN":
                return left_operand < right_operand
            
            elif operator == "EQUALS":
                return left_operand == right_operand
            
            elif operator == "NOT_EQUALS":
                return left_operand != right_operand
            elif operator == "LESS_THAN":
                return left_operand < right_operand
            elif operator == "LESS_THAN_EQUALS":
                return left_operand <= right_operand
            elif operator == "GREATER_THAN":
                return left_operand > right_operand
            elif operator == "GREATER_THAN_EQUALS":
                return left_operand >= right_operand
            if operator == "AND":
                return left_operand and right_operand
            if operator == "OR":
                return left_operand and right_operand

            else:
                raise ParserError("Invalid operator.")
        elif len(tokens) == 13:
            left_operand = self.parse_expression(tokens[:5])
            operator = tokens[6][1]
            right_operand = self.parse_expression(tokens[8:])
            if operator == "AND":
                return left_operand and right_operand
            elif operator == "OR":
                return left_operand or right_operand
            else:
                raise ParserError("Invalid operator.")
        else:
            raise ParserError("Invalid expression.")


class PrintParser:
    def parse_print(self, tokens):
        if tokens[0][1] == "PRINT":
            if tokens[1][1] == "STRING_LITERAL":
                return tokens[1][0][1:-1]  # Extract the string literal without quotes
            if tokens[2][1] == "VARIABLE":
                return parser_ins.variable_store[tokens[2][0]]

            else:
                raise ParserError("Invalid print statement. Expected string literal.")
        else:
            raise ParserError("Invalid statement. Expected print statement.")


class AssignmentParser:
    def parse_assignment(self, tokens):
        if tokens[2][1] == "ASSIGNMENT":
            variable_name = tokens[0][0]

            ex_p = ExpressionParser()

            value = tokens[4][0]
            parser_ins.variable_store[variable_name] = value
            # guests = {variable_name:value}
            # Parser.variable_store.update(guests)
            return None
        else:
            raise ParserError("Invalid assignment statement.")


class IfParser:
    def parse_if(
        self,
        tokens,
    ):
        # cheack if stetment exist
        if tokens[0][1] == "IF":
            ex_p = ExpressionParser()
            expres =  [item for item in tokens if item[0] != 'if']
            index = next((i for i, (token, _) in enumerate(expres) if token == ' '), None)

    # Delete the first 'WHITESPACE' token if found
        if index is not None:
            del expres[index]
            index = None


        for i, item in enumerate(expres):
            if item[0] == ':':
                index = i
                break

        if index is not None:
            # Print the rest of the list starting from the tuple with ':'
            expres=expres[:index]
        else:
            print("Key not found!")


        expression = ex_p.parse_expression(expres)


        if str(expression) == "True":
                print("if ")
                if tokens[16:]:
                    # if and or oprate exsit
                    ex_p2 = self.parse_block(tokens[16:])
                else:
                    ## if noramal exsit
                    ex_p2 = self.parse_block(tokens[8:])


                

                index = next((i for i, (token, _) in enumerate(ex_p2) if token == ' '), None)

                if index is not None:
                    
                    del ex_p2[index]
                    index = None

                expres2 = parser_ins.parse(ex_p2)

                return expres2
        else:
            
            raise ParserError("Invalid if statement.")
        


    def parse_block(self, tokens):
        block = []
        index = 0

        while index < len(tokens):
            if tokens[index][1] == "ENDIF":
                return block
            else:
                block.append(tokens[index])
                index += 1

        raise ParserError("Missing ENDIF statement.")




class whileParser:
    def parse_while(
        self,
        tokens,
    ):
        if tokens[0][1] == "WHILE":
            ex_p = ExpressionParser()
            expres = tokens[2:7]
            variable_name=tokens[2][0]
            value=tokens[6][0]
            expression = ex_p.parse_expression(expres)
            while str(expression) == "True":
                print("loop")
                sum =int (value )+1
                ex_p1 = ExpressionParser()
                x = self.parse_block(tokens[8:],variable_name,sum)
                expres2 = PrintParser.parse_print(self, x)
                return expres2
            else:
                return parser_ins.variable_store[variable_name]
        else:
            raise ParserError("Invalid WHILE statement.")

    def parse_block(self, tokens,name,value):
        block = []
        index = 0

        while index < len(tokens):
            if tokens[index][1] == "ENDW":
                return block
            else:
                block.append(tokens[index])
                
                parser_ins.variable_store[name] =value

                index += 1

        raise ParserError("Missing ENDIF statement.")




parser_ins = Parser()
