import ast
from Violations.correctness import LambdaAssigningViolation
from Visitors.ast_visitor import ASTVisitor


class LambdaAssigningVisitor(ASTVisitor):
    """
    Something.
    """

    def __init__(self) -> None:
        super().__init__()

    def visit_Assign(self, node: ast.Assign):
        if isinstance(node.value, ast.Lambda):
            self.add_violation(LambdaAssigningViolation)

    def run(self) -> None:
        self.add_violation(LambdaAssigningViolation)
