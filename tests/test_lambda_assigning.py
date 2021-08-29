import pytest

from lime_lynter.Visitors.Correctness.correctness import LambdaAssigningVisitor
from lime_lynter.Violations.correctness import LambdaAssigningViolation

lambda_assigning = """
f = lambda x: 2 * x
"""


@pytest.mark.parametrize('code', [lambda_assigning])
def test_lambda_assigning(
    assert_errors,
    parse_ast_tree,
    code,
    mode,
):
    tree = parse_ast_tree(mode(code))
    visitor = LambdaAssigningVisitor(tree)
    visitor.run()

    assert_errors(visitor, [LambdaAssigningViolation])
