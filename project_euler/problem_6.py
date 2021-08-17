"""
Link to problem: https://projecteuler.net/problem=6

Problem 6
---------

Find the difference between the sum of the squares of the first 100 
natural numbers and the square of the sum.


Sample
---------

The sum of the squares of the first 10 natural numbers is,
   1^2 + 2^2 + 3^2 + ... + 10^2 = 385

The square of the sum of the first 10 natural numbers is,
   (1 + 2 + 3 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first 10 natural 
numbers and the square of the sum is `3025 - 385 = 2640`.


Solution
---------

= sum of squares
    - group squares that sum of bases are equal (in case of first 10 natural 
    numbers this sum is 11 and grouped numbers are 1-10, 2-9, etc.)
    - use `a^2 + b^2 = (a+b)^2 + 2*a*b` function to do much simpler groupings
    - last version after all simplifications: 
        - n/2*(n+1)^2 - 2(n*1 + n-1*2 + ... + (n/2 + 1)*(n/2))
    - apply this formula to find end result
"""


def calc_sum_of_squares(n: int) -> int:
    """
    Function returns sum of squares of the first `n` natural numbers by using 
    formula explained below and considering `n` is even. 
    
    | Formula: n/2*(n+1)^2 - 2(n*1 + n-1*2 + ... + (n/2 + 1)*(n/2))

    If `n` is odd, returns `-1`.
    
    
    Explanation of the formula:
        - grouping squares that sum of bases are equal (in case of first 10 
        natural numbers this sum is 11 and grouped numbers are 1-10, 2-9, etc.)
        - using `a^2 + b^2 = (a+b)^2 + 2*a*b` equality to have much simpler 
        groupings
        - applying this formula to find end result
        
    """

    if n % 2 != 0:
        return -1

    part_1 = n // 2 * (n + 1)**2
    part_2 = 2 * calc_sum_of_multiplied(n)

    return part_1 - part_2


def calc_sum_of_multiplied(end: int = 1) -> int:
    """
    Calculates second part of formula that is explained in calculation of the sum
    of the squares:
        (n*1 + n-1*2 + ... + (n/2 + 1)*(n/2)
    
    `n` is equal to `end` in this formula, i.e. given integer number
    """
    numbers = range(1, end + 1)
    total = 0
    for i, num in enumerate(numbers):
        total += num * numbers[end - 1 - i]
        if num == end // 2:
            break

    return total


def calc_square_of_sum(n: int) -> int:
    """
    Functions returns the square of the sum of numbers until given number.
    """

    numbers = range(1, n + 1)
    return sum(numbers)**2


def calc_difference(n: int) -> int:
    """
    Functions returns the absolute difference between the sum of the squares 
    of the first 100 natural numbers and the square of the sum.
    """
    sum_of_squares = calc_sum_of_squares(n)
    square_of_sum = calc_square_of_sum(n)

    return abs(sum_of_squares - square_of_sum)


assert calc_difference(10) == 2640
assert calc_difference(4) == 70