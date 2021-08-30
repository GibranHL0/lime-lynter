"""Visitors for the readability antipatterns type."""

import ast

from lime_lynter.Violations.readability import TypeUsageViolation
from lime_lynter.Visitors.ast_visitor import ASTVisitor


class TypeUsageVisitor(ASTVisitor):
    """Verify if type was used."""

    def visit_Call(self, node: ast.Call):
        """
        Visit only the call ast type.

        Args:
            node: ast Call types.
        """
        if isinstance(node.func, ast.Name) and node.func.id == 'type':
            self.add_violation(TypeUsageViolation(node))
