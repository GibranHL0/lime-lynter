"""Module that is going to be exuted by the Flake8 API."""

import ast
import sys
from typing import Any, Generator, Tuple, Type

from lime_lynter.Visitors.Correctness.correctness import LambdaAssigningVisitor

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


class Plugin(object):
    """Class that executes all the Visitors within the lime lynter."""

    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        """
        Obtain the AST from the code.

        Args:
            tree: Abstract Syntax Tree from the code.
        """
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        """
        Perform all the visitors within the lime lynter.
        """
        visitor = LambdaAssigningVisitor()
        visitor.visit(self._tree)

        for violation in visitor.violations:
            line = violation.line
            col = violation.column
            msg = f'LML{violation.code} {violation.error}'
            yield line, col, msg, type(self)
