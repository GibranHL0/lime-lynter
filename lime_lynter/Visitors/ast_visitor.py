import abc
import ast
from typing import List
from lime_lynter.Violations.template import TemplateViolation


class Visitor(object, metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        self.violations: List[TemplateViolation] = []

    def add_violation(self, violation: TemplateViolation) -> None:
        """ Adds a violation to the visitor. """
        self.violations.append(violation)

    @abc.abstractmethod
    def run(self) -> None:
        """
        Runs a visitor.
        """

    def _post_visit(self) -> None:
        """ Executed after all nodes have been visited. """


class ASTVisitor(ast.NodeVisitor, Visitor, metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        super().__init__()

    def run(self, tree: ast.AST) -> None:
        self.visit(tree)
        self._post_visit()
