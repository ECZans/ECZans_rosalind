"""Solutions related to the Fibonacci sequence"""


def recurrence_rabbits(n, k):
    """
    Rabbits and Recurrence Relations (FIB)

    Given a single pair of rabbits, compute the number of pairs of rabbits alive
    after n months given litter size k

    :return:
    """
    f1 = f2 = fnext = 1

    for _ in range(2, n):
        fnext = f2 + f1 * k
        f1, f2 = f2, fnext
    return fnext


def fibonacci_rabbits():
    """
    Mortal Fibonacci Rabbits (FIBD)

    :return:
    """


def increasing_subsequence():
    """
    Longest Increasing Subsequence (LGIS)

    :return:
    """