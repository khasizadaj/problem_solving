#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratorybirds(arr):
    cnt = [0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        if arr[i] in arr:
            cnt[arr[i]] += 1

    return cnt.index(max(cnt))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
