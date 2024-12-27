import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        
        token_spec = [
            ('NUMBER', r'\d+'),           
            ('ASSIGN', r'='),            
            ('IDENTIFIER', r'[a-zA-Z_]\w*'),  
            ('PRINT', r'print'),         
            ('OP', r'[+\-*/]'),          
            ('SKIP', r'[ \t]+'),         
            ('NEWLINE', r'\n'),          
            ('MISMATCH', r'.'),          
        ]

        
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)

        
        for match in re.finditer(token_regex, self.code):
            kind = match.lastgroup
            value = match.group()
            if kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f"Invalid character: {value}")
            self.tokens.append((kind, value))
        return self.tokens
