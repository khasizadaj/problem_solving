import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    small = scores[0]
    big = scores[0]
    max = 0
    min = 0
    for i in range(len(scores)):
        if scores[i]>big:
            max+=1
            big = scores[i]
        elif scores[i]<small:
            min+=1
            small = scores[i]
    return (max, min)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
