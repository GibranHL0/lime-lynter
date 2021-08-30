"""Test the lambda assigning visitor."""

import ast
import pytest

from lime_lynter.Violations.correctness import LambdaAssigningViolation
from lime_lynter.Visitors.Correctness.correctness import LambdaAssigningVisitor

lambda_assigning = """
f = lambda x: 2 * x
"""


@pytest.mark.parametrize('code', [lambda_assigning])
def test_lambda_assigning(
    code,
):
    """
    Test lambda assigning.

    Args:
        code: Sample code.
    """
    tree = ast.parse(code)
    visitor = LambdaAssigningVisitor()
    visitor.run(tree)

    for violation in visitor.violations:
        isinstance(violation, LambdaAssigningViolation)

    assert len(visitor.violations) == 1
