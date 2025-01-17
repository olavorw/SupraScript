from src.lexer import Lexer
from src.parser import Parser

code = """
let x = 42
print x + 5
"""

# Tokenize the code
lexer = Lexer(code)
tokens = lexer.tokenize()
print("Tokens:", tokens)

# Parse the tokens
parser = Parser(tokens)
ast = parser.parse()
print("AST:", ast)

# Output:
# Tokens: [('IDENTIFIER', 'let'), ('IDENTIFIER', 'x'), ('ASSIGN', '='), ('NUMBER', '42'), ('PRINT', 'print'), ('IDENTIFIER', 'x'), ('OP', '+'), ('NUMBER', '5')]
# AST: [Assignment(x, 42), Print(BinaryOp(x, +, 5))]
