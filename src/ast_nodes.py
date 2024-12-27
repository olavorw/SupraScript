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
    def __init__(self, condition_var, comp_op, condition_value, body):
        self.condition_var = condition_var
        self.comp_op = comp_op
        self.condition_value = condition_value
        self.body = body

    def __repr__(self):
        return f"Loop({self.condition_var} {self.comp_op} {self.condition_value}, {self.body})"

class VariableNode(ASTNode):
    """Represents a variable in the AST."""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Variable({self.name})"

class NumberNode(ASTNode):
    """Represents a number in the AST."""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"