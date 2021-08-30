"""Visitors for the correctness antipatterns type."""

import ast

from lime_lynter.Violations.correctness import LambdaAssigningViolation
from lime_lynter.Visitors.ast_visitor import ASTVisitor


class LambdaAssigningVisitor(ASTVisitor):
    """Verify whether it was an assignment of a Lambda function or not."""

    def visit_Assign(self, node: ast.Assign):
        """
        Visit only the assign ast type.

        Args:
            node: ast Assign types
        """
        if isinstance(node.value, ast.Lambda):
            self.add_violation(LambdaAssigningViolation(node))
