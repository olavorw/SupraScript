import sys
from src.lexer import Lexer
from src.parser import Parser
from src.ast_nodes import AssignmentNode, PrintNode, BinaryOpNode, LoopNode
import random

INSULTS = [
    "Wow you're bad at this",
    "You're worse than my grandma",
    "You're a disgrace to programmers everywhere",
    "You're a failure",
    "You're a joke",
    "You're a disappointment",
    "You're a waste of space",
    "You're a waste of time",
    "You're a waste of oxygen",
    "You're a waste of atoms",
    "You're a waste of matter",
    "You're a waste of energy",
    "You're a waste of life",
    "You're a waste of potential",
    "You're a waste of potential energy",
    "You're a waste of kinetic energy",
    "You're a waste of thermal energy",
    "You're a waste of electromagnetic energy",
    "You're a waste of nuclear energy",
    "You're a waste of gravitational potential energy",
    "You're a waste of elastic potential energy",
    "You're a waste of chemical energy",
    "You're a waste of electrical energy",
    "You're a waste of mechanical energy",
    "You're a waste of radiant energy",
    "You're a waste of sound energy",
    "Did you even read the docs?",
    "Did you even try?",
    "Did you even think?",
    "Did you even care?",
    "Did you even look?",
    "Did you even listen?",
    "Did you even watch?",
    "SupraScript is disappointed in you",
    "Olav is disappointed in you",
    "Olavorw is disappointed in you",
    "You should be ashamed of yourself",
]

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
        elif isinstance(node, LoopNode):
            while self.evaluate_condition(node):
                for statement in node.body:
                    self.execute(statement)

    def evaluate_condition(self, node):
        left = self.variables.get(node.condition, 0)
        right = node.value
        if node.operator == '<':
            return left < right
        elif node.operator == '>':
            return left > right
        elif node.operator == '==':
            return left == right
        elif node.operator == '!=':
            return left != right
        return False

    def handle_error(self, message):
        roast = random.choice(INSULTS)
        raise RuntimeError(f"{message} - {roast}")

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