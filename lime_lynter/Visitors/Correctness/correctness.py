import ast

from lime_lynter.Violations.correctness import LambdaAssigningViolation
from lime_lynter.Visitors.ast_visitor import ASTVisitor


class LambdaAssigningVisitor(ASTVisitor):
    """
    Uses the Flake8 API to check all ast.Assign classes to verify
    whether it was an assignment of a Lambda function or not.
    """

    def visit_Assign(self, node: ast.Assign):
        if isinstance(node.value, ast.Lambda):
            self.add_violation(LambdaAssigningViolation(node))
