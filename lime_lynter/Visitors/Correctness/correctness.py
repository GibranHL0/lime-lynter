from lime_lynter.Violations.correctness import LambdaAssigningViolation
from lime_lynter.Visitors.ast_visitor import Visitor


class LambdaAssigningVisitor(Visitor):
    """
    Something
    """

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        self.add_violation(LambdaAssigningViolation)
