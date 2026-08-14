def add(a, b):
    """Return the sum of a and b."""
    return a + b


def is_palindrome(s):
    """Return True if s reads the same forwards and backwards (case-insensitive)."""
    s = s.lower()
    return s == s[::-1]


def factorial(n):
    """Return n! for n >= 0."""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
