from .ast_nodes import AssignmentNode, PrintNode, BinaryOpNode, LoopNode, VariableNode


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
        elif token[0] == "IDENTIFIER" and token[1] == "loop":
            return self.parse_loop()
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def parse_assignment(self):
        """Parse an assignment like 'let x = 42' or 'let x = y + 1'."""
        self.consume("IDENTIFIER")  # 'let'
        var_name = self.consume("IDENTIFIER")[1]  # Variable name
        self.consume("ASSIGN")  # '='
        value = self.parse_expression()  # Parse the right-hand side as an expression
        return AssignmentNode(var_name, value)

    def parse_value(self):
        """Parse a single value (variable or number)."""
        if self.match("NUMBER"):
            return int(self.consume("NUMBER")[1])
        elif self.match("IDENTIFIER"):
            return VariableNode(self.consume("IDENTIFIER")[1])
        else:
            raise SyntaxError(f"Expected value, got {self.tokens[self.current]}")


    def parse_print(self):
        """Parse a print statement like 'print x + 5'."""
        self.consume("PRINT")  # 'print'
        expr = self.parse_expression()
        return PrintNode(expr)

    def parse_expression(self):
        """Parse expressions like 'x + 5' or just 'x'."""
        left = self.parse_value()  # Parse the left-hand side

        # Check for an operator
        if self.match("OP"):
            op = self.consume("OP")[1]
            right = self.parse_value()  # Parse the right-hand side
            return BinaryOpNode(left, op, right)

        return left  # Single value or variable

    def consume_value(self):
        """Consume either a NUMBER or an IDENTIFIER (variable)."""
        if self.match("NUMBER"):
            return int(self.consume("NUMBER")[1])  # Literal number
        elif self.match("IDENTIFIER"):
            return self.consume("IDENTIFIER")[1]  # Variable name
        else:
            raise SyntaxError(f"Expected a value (NUMBER or IDENTIFIER), got {self.tokens[self.current]}")


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

    def parse_loop(self):
        """Parse a loop like 'loop x < 10:'."""
        self.consume("IDENTIFIER")  # 'loop'
        condition_var = self.consume("IDENTIFIER")[1]  # Variable name
        comp_op = self.consume("COMP_OP")[1]  # Comparison operator (e.g., <)
        condition_value = self.consume("NUMBER")[1]  # Comparison value
        self.consume("COLON")  # The colon after the condition

        # Parse the body of the loop (statements indented under the loop)
        body = []
        while self.current < len(self.tokens) and self.tokens[self.current][0] != "NEWLINE":
            body.append(self.parse_statement())

        return LoopNode(condition_var, comp_op, int(condition_value), body)

