"""
Checks maintainability antipatterns. A program is maintainable if it is easy
to understand and modify the code even for someone that is unfamiliar with
the code base.

--- Violations Summary ---

WithOpenViolation

"""


from lime_lynter.Violations.template import TemplateViolation


class WithOpenViolation(TemplateViolation):
    """
    Forbid using open without the `with` statement.

    Reasoning:
    According to The Little Book of Python Anti-Patterns (2020) the file class
    was equipped with special methods that are automatically called whenever a
    file is oppened via a `with` statemen. These special methods enxure that
    the file is properly and safely opened and closed. Even if the programmer
    remembers to call close() the code is still dangerous, because if an
    exception occurs before the call to `close()` then `close()` will not be
    called and the memory issues can occur, or the file can be corrupted.

    Solution:
    According to the The Little Book of Python Anti-patterns (2020) Use a
    `with` statement whenever a file is oppened.

    Example:
        #Correct:
            with open("file.txt", "r") as f:
                content = f.read()

        #Incorrect:
            f = open("file.txt", "r")
            content = f.read()

    References:
    * Quantified Code.(2020). The Little Book of Python Anti-Patterns.
    Not using with to open files. Retrieved from:
    shorturl.at/imAQW
    """

    error = 'Found open without `with` statement'
    code = 201
