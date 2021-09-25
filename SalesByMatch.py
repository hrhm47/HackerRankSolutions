#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    arr_count = []
    arr_unique = []
    for i in range(n):
        if ar[i] not in arr_unique:
            arr_unique.append(ar[i])
            arr_count.append(ar.count(ar[i]))

    count = 0
    final_arr = []
    for i in arr_count:
        # if i % 2 == 0:
        count = i / 2
        # print(count)
        final_arr.append(int(count))
        count = 0
    return (sum(final_arr))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
