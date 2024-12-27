import sys
from src.lexer import Lexer
from src.parser import Parser
from src.ast_nodes import AssignmentNode, PrintNode, BinaryOpNode


class Interpreter:
    def __init__(self):
        self.variables = {}  # Store variables here

    def interpret(self, nodes):
        for node in nodes:
            self.execute(node)

    def execute(self, node):
        if isinstance(node, AssignmentNode):
            self.variables[node.variable] = node.value
        elif isinstance(node, PrintNode):
            value = self.evaluate(node.expression)
            print(value)
        elif isinstance(node, BinaryOpNode):
            return self.evaluate(node)

    def evaluate(self, node):
        if isinstance(node, BinaryOpNode):
            left = self.get_value(node.left)
            right = self.get_value(node.right)
            if node.operator == '+':
                return left + right
            elif node.operator == '-':
                return left - right
            elif node.operator == '*':
                return left * right
            elif node.operator == '/':
                return left / right
        elif isinstance(node, str):  # Variable name
            return self.variables.get(node, 0)  # Default to 0 if variable not found
        elif isinstance(node, int):  # Literal value
            return node

    def get_value(self, operand):
        # Resolve variables or return the literal directly
        if isinstance(operand, str):  # Variable name
            if operand not in self.variables:
                raise NameError(f"Variable '{operand}' is not defined.")
            return self.variables[operand]
        return operand

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.interpreter <file>.olav")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            code = file.read()

        # Tokenize, parse, and interpret
        lexer = Lexer(code)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        interpreter = Interpreter()
        interpreter.interpret(ast)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()