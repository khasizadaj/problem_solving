"""
This module is solution for Problem 2 in Project Euler.

Link to problem: https://projecteuler.net/problem=2
"""

from typing import Iterable, Optional

def get_even_fib_nums(end: Optional[int] = None) -> Iterable[int]:
    """
    Functions returns iterable of fibonacci numbers that are 
    divisor of 2 until given number (end value)

    Args
        end: ending point | default value is None

    Output
        1. returns iterable of integers
        2. if end value is not provided, it returns nothing, i.e. empty iterable

    """
    if end is None:
        return 

    curr_fib = 2
    prev_fib = 1
    while curr_fib <= end:

        if curr_fib % 2 == 0:
            yield curr_fib

        next_fib = curr_fib + prev_fib
        prev_fib, curr_fib = curr_fib, next_fib


# expected results
assert list(get_even_fib_nums()) == []
assert list(get_even_fib_nums(1)) == []
assert list(get_even_fib_nums(2)) == [2]
assert list(get_even_fib_nums(3)) == [2]
assert list(get_even_fib_nums(10)) == [2, 8]
assert list(get_even_fib_nums(100)) == [2, 8, 34]
assert sum(get_even_fib_nums(10)) == 10


if __name__ == "__main__":
    even_fib_nums = sum(get_even_fib_nums(4_000_000))
    print(even_fib_nums)
