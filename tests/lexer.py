from src.lexer import Lexer

code = """
let x = 5
loop x < 10:
    print x
    let x = x + 1
"""

lexer = Lexer(code)
tokens = lexer.tokenize()
print("Tokens:", tokens)

# Output:
# Tokens: [('IDENTIFIER', 'let'), ('IDENTIFIER', 'x'), ('ASSIGN', '='),
#          ('NUMBER', '5'), ('IDENTIFIER', 'loop'), ('IDENTIFIER', 'x'),
#          ('COMP_OP', '<'), ('NUMBER', '10'), ('NEWLINE', '\n'),
#          ('PRINT', 'print'), ('IDENTIFIER', 'x'), ('NEWLINE', '\n'),
#          ('IDENTIFIER', 'let'), ('IDENTIFIER', 'x'), ('ASSIGN', '='),
#          ('IDENTIFIER', 'x'), ('OP', '+'), ('NUMBER', '1'), ('NEWLINE', '\n')]
