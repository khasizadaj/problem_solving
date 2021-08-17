#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
            "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]

    twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

    def num99(n):
        c = n % 10  # singles digit
        b = int(((n % 100) - c) / 10)  # tens digit
        if b <= 1:
            st = ones[n % 100]
        elif b > 1:
            st = twenties[b] + ones[c]
        return st

    if m > 30:
        if m == 45:
            return 'quarter to %s' % num99(h+1)
        else:
            return '%sminutes to %s' % (num99(60 - m), num99(h+1))
    elif m == 30:
        return 'half past %s' % (num99(h))
    elif m == 00:
        return "%so' clock" % (num99(h))
    elif m < 30:
        if m == 1:
            return 'one minute past one'
        if m == 15:
            return 'quarter past %s' % num99(h)
        else:
            return '%sminutes past %s' % (num99(m), num99(h))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
