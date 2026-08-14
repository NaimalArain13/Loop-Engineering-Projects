from utils import add, is_palindrome, factorial


def test_add():
    assert add(2, 3) == 5


def test_is_palindrome():
    assert is_palindrome("RaceCar") is True
    assert is_palindrome("hello") is False


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
