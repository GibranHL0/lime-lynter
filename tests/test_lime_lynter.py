import ast
from types import Set

import lime_lynter


def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = lime_lynter.lime_lynter.Plugin(tree)
    return {f'{line}:{col} {msg}' for line, col, msg, _ in plugin.run()}


def test_trivial_case():
    assert _results('') == set()
