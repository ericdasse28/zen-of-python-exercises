"""Readability & Simplicity.

Refactor the following code to:
1. Improve readability
2. Minimize nesting
3. Use meaningful names
"""

def f(a, b):
    """Calculate bonus.

    Args:
        a (int): Customer points
        b (int): Items in cart

    Returns:
        int: Bonus
    """
    if a > 10:
        if b < 5:
            return a*b
        else:
            return a+b
    else:
        if b < 5:
            return a-b
        else:
            return b-a