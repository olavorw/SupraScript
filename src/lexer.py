import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        # Define patterns for tokens (order matters: keywords before identifiers)
        token_spec = [
            ('PRINT', r'print'),         # Print keyword
            ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Variable names
            ('ASSIGN', r'='),            # Assignment operator
            ('NUMBER', r'\d+'),          # Integer or float
            ('OP', r'[+\-*/]'),          # Arithmetic operators
            ('COMP_OP', r'[<>!=]=?|=='), # Comparison operators (<, >, <=, >=, ==, !=)
            ('COLON', r':'),             # Colon (used for loops and conditionals)
            ('SKIP', r'[ \t]+'),         # Skip spaces/tabs
            ('NEWLINE', r'\n'),          # Line endings
            ('MISMATCH', r'.'),          # Catch all other errors
        ]



        # Create the regex for tokenizing
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)

        # Match tokens line by line
        for match in re.finditer(token_regex, self.code):
            kind = match.lastgroup
            value = match.group()
            if kind in ('SKIP', 'NEWLINE'):  # Skip spaces/tabs and newlines
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f"Invalid character: {value}")
            self.tokens.append((kind, value))
        return self.tokens
