"""Visitors for the maintainability antipatterns type."""

import ast

from lime_lynter.Violations.maintainability import WithOpenViolation
from lime_lynter.Visitors.ast_visitor import ASTVisitor


class WithOpenVisitor(ASTVisitor):
    """Verify if the with statemen was used along the open one."""

    def visit_Assign(self, node: ast.Name):
        """
        Visit only the name ast type.

        Args:
            node: ast Name types.
        """
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'open':
            self.add_violation(WithOpenViolation(node))
