from math import sqrt

# returns number of perfect squares in given
# list of integers. It uses isPerfectSquare()
# to determine first perfect square. then uses
# math to find the rest of perfect squares without
# checking them directly.

# link to problem: https://www.hackerrank.com/challenges/sherlock-and-squares/problem


def squares(a, b):
  countOfPerfectSquares = 0
  firstSquareFound = False
  currNum = a

  while currNum <= b:
    if firstSquareFound == False:
      if isPerfectSquare(currNum):
        countOfPerfectSquares += 1
        firstSquareFound = True
        continue

      currNum += 1
      continue

    # n^2 -> (n+1)^2 : in every step increase is equal to "2 * n + 1"
    currNum += int(sqrt(currNum)) * 2 + 1
    if currNum <= b:
      countOfPerfectSquares += 1
  return countOfPerfectSquares


# chekcing if it is perfect square
def isPerfectSquare(num):
  roundedRoot = int(sqrt(num))
  if roundedRoot**2 == num:
    return True
  return False


if __name__ == "__main__":
  firstNumber = int(input('Tell me first number: '))
  lastNumber = int(input('Tell me last number: '))
  countOfPerfectSquares = squares((firstNumber), lastNumber)

  print(
      f'There are {countOfPerfectSquares} perfect squares between {firstNumber} and {lastNumber}.'
  )
