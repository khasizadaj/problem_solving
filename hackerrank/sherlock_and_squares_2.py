from math import sqrt, floor

# This is my second solution to same problem. In this solution
# we find square root of both ends to calculate number of perfect squares.
# Additionally, beginning value is also perfect square, we increment count to
# include that too. We don't want to lose any perfect ones, do we?

# Thanks to Nushaba for helping me out to improving the solution. <3

# link to problem: https://www.hackerrank.com/challenges/sherlock-and-squares/problem


def main():
  print(squares(3, 20))  # outputs: 3
  print(squares(180, 447))  # outputs: 8
  print(squares(384, 819))  # outputs: 9


def squares(a, b):
  # used floor() to get smallest near integer,
  # if number is not perfect square
  count_of_squares = floor(sqrt(b)) - floor(sqrt(a))

  a_is_square = a % sqrt(a) == 0
  if a_is_square:
    count_of_squares += 1

  return count_of_squares


if __name__ == '__main__':
  main()
