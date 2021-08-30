"""Test the type usage visitor."""

import ast
import pytest

from lime_lynter.Violations.readability import TypeUsageViolation
from lime_lynter.Visitors.Readability.read import TypeUsageVisitor

type_usage = """
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

r = Rectangle(3, 4)

if type(r) is types.ListType:
    print("Object r is a list")
"""


@pytest.mark.parametrize('code', [type_usage])
def test_type_usage(
    code,
):
    """
    Test type usage.

    Args:
        code: Sample code.
    """
    tree = ast.parse(code)
    visitor = TypeUsageVisitor()
    visitor.run(tree)

    for violation in visitor.violations:
        isinstance(violation, TypeUsageViolation)

    assert len(visitor.violations) == 1
