import re

class IllegalCharError(Exception):
    pass

class Lexer:
    def __init__(self, token_patterns):
        self.token_patterns = token_patterns

    def tokenize(self, input_string):
        tokens = []
        position = 0

        while position < len(input_string):
            match = None

            # Try to match each token pattern with the input string
            for pattern, token_type in self.token_patterns:
                regex = re.compile(pattern)
                match = regex.match(input_string, position)
                if match:
                    value = match.group(0)
                    tokens.append((value, token_type))
                    position = match.end()
                    break

            # If no token pattern matches, raise an IllegalCharError
            if not match:
                raise IllegalCharError('Illegal character at position {}'.format(position))

        return tokens
