#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    length_arr = len(s)
    total_sub = length_arr - (m - 1)
    # k = 0
    all_sub = {}
    for k in range(total_sub):
        all_sub[k] = []
        j = k
        for i in range(m):
            all_sub[k].append(s[j])
            j = j + 1

    sub_we_need = 0
    for v in all_sub.values():
        if sum(v) == d:
            sub_we_need += 1

    return sub_we_need


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
