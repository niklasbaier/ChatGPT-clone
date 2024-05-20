# src/instant_repo/mkdocstrings_example.py

"""Quick description about contents of module.

This module allows the user to make mathematical calculations.

Examples:
    >>> from instant_repo import mkdocstrings_example
    >>> mkdocstrings_example.function_mkdocstrings_example(2, 4)
    6.0

The module contains the following functions:

- `function_mkdocstrings_example(a, b)` - Returns the sum of two numbers.
"""

import typing as t


def function_mkdocstrings_example(
    a: t.Union[float, int], b: t.Union[float, int]
) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)
