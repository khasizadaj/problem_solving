"""
Link to problem: https://projecteuler.net/problem=1
"""


from typing import Iterable, Optional


def get_numbers(start:int = 1, end: Optional[int] = None) -> Iterable[int]:
    """
    Functions returns iterable of integers that are divisor of
    3 or 5 within given interval.
    
    Args
        start: beginning point of interval | default value is 1
        end: ending point of interval | default value is None

    Output
        1. returns iterable of integers
        2. if end value is not provided, it returns nothing, i.e. empty iterable
        3. if start is bigger than end, it returns -1.

    """

    if end is None:
        return

    if start > end:
        yield -1
        return 'start value is bigger than end value'

    for num in range(start, end):
        if num % 3 == 0 or num % 5 == 0:
            yield num


assert list(get_numbers(end=10)) == [3, 5, 6, 9] 
assert sum(get_numbers(end=10)) == 23
assert sum(get_numbers()) == 0
assert next(get_numbers(start=10, end=5)) == -1

print(sum(get_numbers(end=1000)))
