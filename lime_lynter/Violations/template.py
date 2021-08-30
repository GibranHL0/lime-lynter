"""Provides the blueprint for Violations"""

import abc
from ast import AST
from typing import Tuple


class TemplateViolation(object, metaclass=abc.ABCMeta):
    """Template from all the Violations."""
    def __init__(self, node: AST) -> None:
        """Initialize the space of where the violation was found."""
        self.line = node.lineno
        self.column = node.col_offset
    
    def get_space(self) -> Tuple[int, int]:
        """Retrieve the position of the violation."""
        return (self.line, self.column)
