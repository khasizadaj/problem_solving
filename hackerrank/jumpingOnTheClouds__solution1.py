# function calculates remaining energy until it lands
# to starting position again. it uses least common multiple
# to find out minimum required moves to go back to starting
# position


def main(listOfClouds, countOfSteps):
  currentPosition = 0
  countOfClouds = len(listOfClouds)
  energy = 100
  countOfMinimumRequiredMoves = calculateMinimumRequiredMoves(
      countOfSteps, countOfClouds)

  for i in range(countOfMinimumRequiredMoves):
    nextPosition = findNextPosition(currentPosition, countOfSteps,
                                    countOfClouds)
    decreasedEnergyAmount = calculateDecreasedEnergy(nextPosition,
                                                     listOfClouds)
    energy -= decreasedEnergyAmount
    currentPosition = nextPosition

  return energy


# returns next position to be moved
def findNextPosition(currentPosition, countOfSteps, countOfClouds):
  return (currentPosition + countOfSteps) % countOfClouds


# depending type of cloud, functions returns amount of
# energy that will be decreased after each move
def calculateDecreasedEnergy(nextPosition, listOfClouds):
  if listOfClouds[nextPosition] == 1:
    return 3
  return 1


# returns number of moves needed to land on starting
# position again
def calculateMinimumRequiredMoves(countOfSteps, countOfClouds):
  leastCommonMultiple = calculateLeastCommonMultiple(countOfSteps,
                                                     countOfClouds)
  return int(leastCommonMultiple / countOfSteps)


# It calculates greatest common multiple first to find out LCM.
# This function was taken from mathematics (lcm = a * b / gcm)
def calculateLeastCommonMultiple(n, m):
  greatestCommonMultiple = getGreatestCommonMultiple(n, m)
  leastCommonMultiple = n * m / greatestCommonMultiple
  return leastCommonMultiple


def getGreatestCommonMultiple(n, m):
  gcm = 1
  commonPrimeFactors = getCommonFactors(n, m)

  for i in commonPrimeFactors:
    gcm *= i

  return gcm


# returns list of common factors of given numbers
def getCommonFactors(n, m):
  factorsOfFirst = getAllPrimeFactorsOfNumber(n)
  factorsOfSecond = getAllPrimeFactorsOfNumber(m)

  return [fac for fac in factorsOfFirst if fac in factorsOfSecond]


# returns list of prime factors for a given number
def getAllPrimeFactorsOfNumber(n):
  divisors = []

  while n > 1:
    smallestPrimeFactor = findSmallestPrimeFactor(n)
    divisors.append(smallestPrimeFactor)
    n = n / smallestPrimeFactor

  return divisors


# returns smallest divisor of number e.g., smallest divisors
# for 6 and 9, are 2 and 3 respectively
def findSmallestPrimeFactor(n):
  n = int(n)
  if n == 1:
    return 1

  for i in range(2, n + 1):
    if n % i == 0:
      return i


# extra info and credits
def furtherInfoAboutProblem():
  link = 'https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem'
  problemName = 'Jumping on the Clouds: Revisited'
  return f'Further inforamtion about problem called {problemName} can be found in this link: {link}'


if __name__ == '__main__':
  # TEST 1
  c1 = [0, 0, 1, 0, 0, 1, 1, 0]
  k1 = 2
  res1 = main(c1, k1)

  print('Test 1:')
  print('Clouds:', c1)
  print('Count of steps:', k1)
  print(res1, end='\n\n')

  # TEST 2
  c2 = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
  k2 = 3
  res2 = main(c2, k2)

  print('Test 2:')
  print('Clouds:', c2)
  print('Count of steps:', k2)
  print(res2, end='\n\n')

  # EXTRA INFO
  extraInfo = furtherInfoAboutProblem()
  print(extraInfo)
