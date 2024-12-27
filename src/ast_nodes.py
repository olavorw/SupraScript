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

class LoopNode(ASTNode):
    def __init__(self, condition, operator, value, body):
        self.condition = condition
        self.operator = operator
        self.value = value
        self.body = body

    def __repr__(self):
        return f"Loop({self.condition} {self.operator} {self.value}, {self.body})"
