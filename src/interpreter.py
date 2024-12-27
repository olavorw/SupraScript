import sys
import random
from src.lexer import Lexer
from src.parser import Parser
from src.ast_nodes import AssignmentNode, PrintNode, BinaryOpNode, LoopNode, VariableNode, NumberNode

# Random insults to roast the programmer
INSULTS = [
    "Wow, you're bad at this.",
    "Did you even read the docs?",
    "SupraScript is disappointed in you.",
    "Olav is disappointed in you.",
    "You're a disgrace to programmers everywhere.",
    "Did you even think?",
    "SupraScript expected more from you.",
    "You're a failure.",
    "Stop embarrassing yourself.",
    "This is why we can't have nice things.",
]

class Interpreter:
    def __init__(self):
        self.variables = {}  # Store variables here

    def interpret(self, nodes):
        """Interpret each node in the AST."""
        for node in nodes:
            self.execute(node)

    def execute(self, node):
        """Execute an AST node."""
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

    def evaluate_condition(self, condition_node):
        """Evaluate a loop condition."""
        left_value = self.evaluate(condition_node.left)
        right_value = self.evaluate(condition_node.right)
        if condition_node.operator == '<':
            return left_value < right_value
        elif condition_node.operator == '>':
            return left_value > right_value
        elif condition_node.operator == '==':
            return left_value == right_value
        elif condition_node.operator == '!=':
            return left_value != right_value
        else:
            raise ValueError(f"Unsupported comparison operator: {condition_node.operator}")


    # noinspection PyMethodMayBeStatic
    def handle_error(self, message):
        """Roast the programmer with a random insult."""
        roast = random.choice(INSULTS)
        raise RuntimeError(f"{message} - {roast}")

    def evaluate(self, node):
        """Evaluate an expression node."""
        if isinstance(node, BinaryOpNode):
            left_value = self.evaluate(node.left)
            right_value = self.evaluate(node.right)
            if node.operator == '+':
                return left_value + right_value
            elif node.operator == '-':
                return left_value - right_value
            elif node.operator == '*':
                return left_value * right_value
            elif node.operator == '/':
                return left_value / right_value
            else:
                raise ValueError(f"Unsupported operator: {node.operator}")
        elif isinstance(node, VariableNode):
            return self.get_variable_value(node.name)
        elif isinstance(node, NumberNode):
            return node.value
        else:
            raise TypeError(f"Unsupported node type: {type(node)}")



    def get_value(self, operand):
        """Get the value of a variable or literal."""
        if isinstance(operand, str):  # Variable name
            if operand not in self.variables:
                self.handle_error(f"Variable '{operand}' is not defined.")
            return self.variables[operand]
        return operand


def main():
    """Main function for running .olav files."""
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
