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
