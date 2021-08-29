"""
Checks readability antipatterns, the ease with which a developer can understand
and read a code base.

--- Violations Summary ---

TypeUsageViolation

"""


from Violations.template import TemplateViolation


class TypeUsageViolation(TemplateViolation):
    """
    Forbid using `type()` to compare types.

    Reasoning:
    According to The Little Book of Python Anti-Patterns (2020) checking for
    equality of `type` does not caters for inheritance.

    Solution:
    According to the The Little Book of Python Anti-patterns (2020) The
    function `isinstance` is the best-equipped to handle type checking because
    it supports inheritance.

    Example:
        #Correct:
            class Rectangle():
                def __init__(self, width, height):
                    self.width = width
                    self.height = height

            r = Rectangle(3, 4)

            if isinstance(r, types.ListType):
                print("Object r is a list")

        #Incorrect:
            class Rectangle():
                def __init__(self, width, height):
                    self.width = width
                    self.height = height

            r = Rectangle(3, 4)

            if type(r) is types.ListType:
                print("Object r is a list")

    References:
    * Quantified Code.(2020). The Little Book of Python Anti-Patterns.
    Using type() to compare types. Retrieved from:
    shorturl.at/fyBE8
    """
    def __init__(self) -> None:
        super().__init__('Found type() usage', 301)
