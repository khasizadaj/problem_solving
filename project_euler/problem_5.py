"""
Link to problem: https://projecteuler.net/problem=5

Problem 5
---------

2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

"""

from typing import Iterable, Optional
from math import gcd


def least_common_multiple_two(num_1: int, num_2: int) -> int:
    multiple = num_1 * num_2

    # LCM can only be smallest positive integer.
    if multiple < 0:
        multiple = abs(multiple)

    # LCM of 0 and any integer is undefined in math.
    if multiple == 0:
        return None

    return multiple // gcd(num_1, num_2)


"""
- Steps to calculate LCM of numbers until given number (`n`)
    - initiate least common multiple (in short, LCM) as 1
    - numbers = half of the list that strats from 1 to `n` (as they are already multiple of 
    previous)
    - loop through the list of numbers until given number:
        - find least common multiple (current LCM) of current number and LCM
        - if current LCM is not equal to LCM:
            - update LCM with current LCM
    - return LCM
"""


def least_common_multiple_many(num: int) -> Iterable[int]:
    nums = list(range(num // 2 + 1, num + 1))
    lcm = 1
    for num in nums:
        curr_lcm = least_common_multiple_two(num, lcm)
        if lcm != curr_lcm:
            lcm = curr_lcm

    return lcm


# Simple testing

assert least_common_multiple_two(2, 3) == 6
assert least_common_multiple_two(2, 3) != 7
assert least_common_multiple_two(0, 3) == None

assert least_common_multiple_many(10) == 2520
assert least_common_multiple_many(20) == 232792560
