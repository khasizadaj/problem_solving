"""
Question

An integer `d` is a divisor of an integer n if the remainder of `n % d == 0`.

Given an integer, for each digit that makes up the integer determine whether 
it is a divisor. Count the number of divisors occurring within the integer.

link: https://www.hackerrank.com/challenges/find-digits/problem

---------
========
---------

Steps of solution:
    Get number
    convert number to str to be able iterate easily
    loop  through digits, i.e. digits as a string
        convert string digit to integer
        omit 0 as divisor
        check if digit is divisor of number
        if digit is divisor:
            increase the count of divisors

    return count of the divisiors
"""


def find_count_of_divisor_digits(num: int = None) -> int:
    """
    Returns count of divisor digits in the given number
    """
    if num is None or num == 0:
        return 0

    count_of_divisors = 0
    str_num = str(num)

    for i in str_num:
        curr_digit = int(i)

        if curr_digit == 0:
            continue

        is_divisor = check_divisor(num, curr_digit)

        if is_divisor:
            count_of_divisors += 1

    return count_of_divisors


def check_divisor(number: int, digit: int) -> bool:
    """
    Returns boolean value if digit is divisor of number
    """

    try:
        if number % digit == 0:
            return True
        return False
    except ZeroDivisionError:
        return False


assert find_count_of_divisor_digits(0) == 0
assert find_count_of_divisor_digits() == 0
assert find_count_of_divisor_digits(124) == 3
assert find_count_of_divisor_digits(10) == 1