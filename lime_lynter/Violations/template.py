import abc


class TemplateViolation(object, metaclass=abc.ABCMeta):
    def __init__(self, error: str, code: int) -> None:
        self.error = error
        self.code = code
