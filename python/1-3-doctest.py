import doctest


def add(a, b):
    """
    두 수를 더하는 함수입니다.

    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    """
    return a + b


if __name__ == "__main__":
    doctest.testmod()