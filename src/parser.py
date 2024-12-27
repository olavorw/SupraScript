class ASTNode:
    """Base class for all AST nodes."""
    pass

class AssignmentNode(ASTNode):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def __repr__(self):
        return f"Assignment({self.variable}, {self.value})"

class PrintNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"Print({self.expression})"

class BinaryOpNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryOp({self.left}, {self.operator}, {self.right})"


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        """Entry point for parsing a program."""
        nodes = []
        while self.current < len(self.tokens):
            token = self.tokens[self.current]
            if token[0] == "NEWLINE":  # Skip NEWLINE tokens
                self.current += 1
                continue
            node = self.parse_statement()
            nodes.append(node)
        return nodes

    def parse_statement(self):
        """Parse a single statement (e.g., assignment or print)."""
        token = self.tokens[self.current]
        if token[0] == "IDENTIFIER" and token[1] == "let":
            return self.parse_assignment()
        elif token[0] == "PRINT":
            return self.parse_print()
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def parse_assignment(self):
        """Parse an assignment like 'let x = 42'."""
        self.consume("IDENTIFIER")  # 'let'
        var_name = self.consume("IDENTIFIER")[1]  # Variable name
        self.consume("ASSIGN")  # '='
        value = self.consume("NUMBER")[1]  # Value
        return AssignmentNode(var_name, int(value))

    def parse_print(self):
        """Parse a print statement like 'print x + 5'."""
        self.consume("PRINT")  # 'print'
        expr = self.parse_expression()
        return PrintNode(expr)

    def parse_expression(self):
        """Parse expressions like 'x + 5'."""
        left = self.consume("IDENTIFIER")[1]
        if self.match("OP"):
            op = self.consume("OP")[1]
            right = self.consume("NUMBER")[1]
            return BinaryOpNode(left, op, int(right))
        return left

    def consume(self, expected_type):
        """Consume the next token if it matches the expected type."""
        if self.current < len(self.tokens) and self.tokens[self.current][0] == expected_type:
            token = self.tokens[self.current]
            self.current += 1
            return token
        raise SyntaxError(f"Expected {expected_type}, got {self.tokens[self.current]}")

    def match(self, expected_type):
        """Check if the next token matches the expected type."""
        return self.current < len(self.tokens) and self.tokens[self.current][0] == expected_type
