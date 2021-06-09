"""
Link to problem: https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt


def greatest_prime_factor(num):
    factors = get_factors(num)
    return max(factors)


def get_factors(num):
    if is_prime(num):
        yield 1
        yield num
        return

    curr_num = num
    factor = 1
    while 1 < curr_num <= num and factor <= curr_num:
        # print(curr_num, factor)
        if curr_num % factor != 0:
            factor += 1
            continue
        elif is_prime(factor):
            yield factor
            curr_num /= factor
            factor = 1

        factor += 1


def is_prime(num: int):
    if num == 1:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


assert list(get_factors(5)) == [1, 5]
assert list(get_factors(11)) == [1, 11]
assert list(get_factors(12)) == [1, 2, 2, 3]
assert list(get_factors(15)) == [1, 3, 5]
assert list(get_factors(25)) == [1, 5, 5]
assert list(get_factors(24)) == [1, 2, 2, 2, 3]
assert list(get_factors(98)) == [1, 2, 7, 7]

assert greatest_prime_factor(5) == 5
assert greatest_prime_factor(8) == 2
assert greatest_prime_factor(15) == 5
assert greatest_prime_factor(119) == 17
assert greatest_prime_factor(13195) == 29

if __name__ == "__main__":
    ans = greatest_prime_factor(600851475143)
    print(ans)
