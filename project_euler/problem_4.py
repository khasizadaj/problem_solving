"""
Link to problem: https://projecteuler.net/problem=4

* Note: Usage of Numba is optional. I used to increase speed of code. You
can check it out from link below.

  - link to module: https://github.com/numba/numba
  - link to tutorial: https://youtu.be/x58W9A2lnQc

"""

from numba import njit
import time
from typing import Optional

@njit
def is_palindrome(num: int) -> bool:
    """
    it checks if number is palindrome. it converts number to string
    and compares string with reverse of the same string.
    """
    string = str(num)

    return string == string[::-1] # xyz m zyx


assert is_palindrome(9009) == True
assert is_palindrome(9008) == False
assert is_palindrome(90109) == True
assert is_palindrome(901109) == True
assert is_palindrome(9019109) == True


@njit
def get_max_pal_product(start: int = 1, end: Optional[int] = 1) ->  tuple:
    """
    Function returns the biggest palindrome number and factors of it
    within given interval.

    For fast calculation we start from end of interval
    and go backwards. If current product is less than maximum
    product so far, without checking if it's palindrome, we continue
    to next number pair.

    Args
        start: beginning point of interval | default value is 1
        end: ending point of interval | default value is 1

    Output
        tuple of biggest palindrome and tuple of numbers created it.
            (9009, (91, 99))
              |      |
              |      --> num_1 and num_2
              --> max_product or biggest palindrome
    """
    
    if end == 1:
        return 1, (1, 1)

    count = 0
    max_product = 1
    factor_1 = 1
    factor_2 = 1

    for num_1 in range(end, start, -1):
        for num_2 in range(num_1, start, -1):
            if num_1 <= factor_1 and num_2 <= factor_2:
                break

            curr_product = num_1 * num_2
            count += 1
            if curr_product < max_product:
                continue

            is_pal = is_palindrome(curr_product)

            if is_pal:
                max_product = curr_product
                factor_1 = num_1
                factor_2 = num_2
    print(count)
    return max_product, (factor_1, factor_2)


assert get_max_pal_product() == (1, 1, 1)
assert get_max_pal_product(end=100) == (9009, 91, 99)
assert get_max_pal_product(start=80, end=100) == (9009, 91, 99)
assert get_max_pal_product(end=1000) == (906609, 913, 993)

start = time.time()
pal, factors = get_max_pal_product(start=1, end=1000)
end = time.time()
print(f'{pal} is the greatest palindrome number within given interval and product of {factors[0]} and {factors[1]}.')
print(f"Elapsed (with compilation) = {(end - start)}")

start = time.time()
pal, factors = get_max_pal_product(start=1, end=1000)
end = time.time()
print(f'{pal} is the greatest palindrome number within given interval and product of {factors[0]} and {factors[1]}.')
print(f"Elapsed (after compilation) = {(end - start)}")
