import pytest
import ast

from lime_lynter.Visitors.Correctness.correctness import LambdaAssigningVisitor
from lime_lynter.Violations.correctness import LambdaAssigningViolation

lambda_assigning = """
f = lambda x: 2 * x
"""


@pytest.mark.parametrize('code', [lambda_assigning])
def test_lambda_assigning(
    code,
):
    tree = ast.parse(code)
    visitor = LambdaAssigningVisitor()
    visitor.run(tree)

    for violation in visitor.violations:
        isinstance(violation, LambdaAssigningViolation)

    assert len(visitor.violations) == 1
