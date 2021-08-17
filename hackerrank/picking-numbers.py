#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    x = []
    for i in range(len(a)):
        m = [a[i]]
        for j in range(len(a)):
            if abs(a[i] - a[j]) <= 1:
                m.append(a[j])
            if max(m) - min(m) > 1:
                m.remove(a[j])
        x.append(len(m)-1)

    return max(x)   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
