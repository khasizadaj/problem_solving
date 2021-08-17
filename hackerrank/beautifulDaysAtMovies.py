# Given a range of numbered days,  and a number , determine
# the number of days in the range that are beautiful. Beautiful
# numbers are defined as numbers where  is evenly divisible by . 
# If a day's value is a beautiful number, it is a beautiful day. 
# Return the number of beautiful days in the range.

def beautifulDays(i, j, k):
    countOfBeautifulDays = 0

    for day in range(i, j + 1):
        isBeautiful = checkIfDayIsBeautiful(day, k)
        if isBeautiful:
            print('beautiful')
            countOfBeautifulDays += 1
    return countOfBeautifulDays


def checkIfDayIsBeautiful(day, beautyMeasurement):
    reversedNumber = getReverseOfNumber(day)
    difference = abs(day - reversedNumber)

    if difference % beautyMeasurement == 0:
        return True
    return False


def getReverseOfNumber(number):
    reversedNumber = str(number)[::-1]
    return int(reversedNumber)


if __name__ == '__main__':
    print("test 1")
    print(beautifulDays(20, 23, 6))
    
    print("test 2")
    print(beautifulDays(20, 23, 4))
    
    print("test 3")
    print(beautifulDays(23, 23, 6))
