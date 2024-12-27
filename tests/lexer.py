from src.lexer import Lexer

code = """
let x = 42
print x + 5
"""

lexer = Lexer(code)
tokens = lexer.tokenize()
print(tokens)

# Output:
# [('IDENTIFIER', 'let'), ('IDENTIFIER', 'x'), ('ASSIGN', '='), ('NUMBER', '42'), ('PRINT', 'print'), ('IDENTIFIER', 'x'), ('OP', '+'), ('NUMBER', '5')]