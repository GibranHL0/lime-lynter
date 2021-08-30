"""Test the with open visitor."""

import ast
import pytest

from lime_lynter.Violations.maintainability import WithOpenViolation
from lime_lynter.Visitors.Maintainability.mty import WithOpenVisitor

with_open = """
f = open("file.txt", "r")
"""


@pytest.mark.parametrize('code', [with_open])
def test_with_open(
    code,
):
    """
    Test with open.

    Args:
        code: Sample code.
    """
    tree = ast.parse(code)
    visitor = WithOpenVisitor()
    visitor.run(tree)

    for violation in visitor.violations:
        isinstance(violation, WithOpenViolation)

    assert len(visitor.violations) == 1
