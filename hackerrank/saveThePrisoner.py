# functions returns position of poisoned prisoner.
# it uses modulo to figure out poisoned prisoner and

# if modulo is equal to 0 it returns countOfPrisoner
# (means countofCandies is divisor of countOfProsners),
# because last cycle will end at position of last prisoner

# source of problem: https://www.hackerrank.com/challenges/save-the-prisoner/problem


def saveThePrisoner(countOfPrisoners, countOfCandies, startingPosition):
  currPosition = startingPosition + countOfCandies % countOfPrisoners - 1
  return currPosition % countOfPrisoners or countOfPrisoners


if __name__ == '__main__':
  t1 = saveThePrisoner(7, 6, 2)
  print("Test 1:", t1)

  t2 = saveThePrisoner(7, 7, 1)
  print("Test 2:", t2)

  t3 = saveThePrisoner(5, 7, 5)
  print("Test 3:", t3)
