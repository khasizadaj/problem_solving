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

"""

# don't forget possibility of input number to  be odd number


def calc_difference(num: int) -> int:
    sum_of_squares = calc_sum_of_squares(num)
    square_of_sum = calc_square_of_sum(num)

    return abs(sum_of_squares - square_of_sum)


def calc_sum_of_squares(num: int) -> int:
    """
    formula: n/2*(n+1)^2 - 2(n*1 + n-1*2 + ... + (n/2 + 1)*(n/2))
    
    formula derived from: a^2 + b^2 = (a+b)^2 + 2*a*b
    """

    part_1 = num // 2 * (num + 1) ** 2
    part_2 = 2 * calc_sum_of_multiplied(start=1, end=num)

    return part_1 - part_2


def calc_sum_of_multiplied(start: int = 1, end: int = 1) -> int:
    numbers = range(start, end + 1)
    total = 0
    for i, num in enumerate(numbers):
        total += num * numbers[end - 1 - i]
        if num == end // 2:
            break
    
    return total


def calc_square_of_sum(num: int) -> int:
    numbers = range(1, num + 1)
    return sum(numbers)**2

assert calc_difference(10) == 2640
assert calc_difference(4) == 70
print(calc_difference(100))
print(calc_difference(10))