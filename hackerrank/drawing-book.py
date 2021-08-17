#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    a = int(p/2)
    b = int((n-p)/2)
    if n % 2 == 0 and n-p == 1:
        b += 1
    if a < b:
        return a
    else:
        return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
