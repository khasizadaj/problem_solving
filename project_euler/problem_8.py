"""

Problem 8
---------

Find the thirteen adjacent digits in the 1000-digit number that have the 
greatest product. What is the value of this product?

Link to problem: https://projecteuler.net/problem=8


Sample
-------

The four adjacent digits in the 1000-digit number that have the greatest 
product are 9 × 9 × 8 × 9 = 5832.


Solution [pseudocode]
---------------------

initiate variable to save product of adjacent digits; default is 1
initiate variable to save starting position
loop through the given number
    get product of required amount digits
    if biggest so far:
        update the position

return position

calculate product of digits starting from position we found earlier

"""
from typing import Optional

THOUSAND = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450


def find_biggest_product(number: Optional[int] = None,
                         count_of_digits: Optional[int] = None) -> int:
    """
    Function returns the product of the required amount of adjacent digits 
    that has the largest product in the given number. 
    """
    
    if number is None or count_of_digits is None or count_of_digits < 1:
        return -1

    str_number = str(number)

    position = find_position(str_number, count_of_digits)
    adjacent_digits = str_number[position:position + count_of_digits]
    product = find_product(adjacent_digits)
    return product


def find_position(number: Optional[str] = None,
                  count_of_digits: Optional[int] = None) -> int:
    """
    Function returns the starting position of the required amount of adjacent 
    digits that has the largest product in the given number.
    """

    if number is None or count_of_digits is None or count_of_digits < 1:
        return -1

    prod = 1
    highest_pos = 0

    # removing parts (as many as count of digits) that we don't need to check
    modified_number = number[:count_of_digits * -1]

    for i, _ in enumerate(modified_number):
        curr_digits = number[i:i+count_of_digits]
        curr_prod = find_product(curr_digits)
        if curr_prod > prod:
            prod = curr_prod
            highest_pos = i

    return highest_pos


def find_product(number: Optional[str] = None) -> int:
    """
    Function returns the product of the digits in the given number. 
    """
    if number is None:
        return -1

    curr_prod = 1
    for i in number:
        curr_prod *= int(i)

    return curr_prod


prod = find_biggest_product(THOUSAND, 4)
print(prod)

prod = find_biggest_product(THOUSAND, 13)
print(prod)
