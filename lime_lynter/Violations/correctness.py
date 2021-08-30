"""
Checks correctness antipatterns, which will litreally break code or make it
do the wrong intention.

--- Violations Summary ---

LambdaAssigningViolation

"""

from lime_lynter.Violations.template import TemplateViolation


class LambdaAssigningViolation(TemplateViolation):
    """
    Forbid lambda assigning.

    Reasoning:
    According to PEP207, you should always use a def statement instead of an
    assignment that binds a lambda expression directly to an identifier.

    Solution:
    According to the The Little Book of Python Anti-patterns (2020) "If you
    are going to assign a name to a `lambda`, you are better off just deffining
    it as a `def`"

    Example:
        #Correct:
            def f(x): return 2*x

        #Incorrect:
            f = lambda x: 2*x

    References:
    * Van Rossum G.(2016).PEP 207 Rich Comparisons. Legacy Python. Retrieved
    from: https://legacy.python.org/dev/peps/pep-0207/

    * Quantified Code.(2020). The Little Book of Python Anti-Patterns.
    Assigning a lambda expression to a variable. Retrieved from:
    shorturl.at/sDFLO
    """

    error = 'Found lambda assigning'
    code = 101
