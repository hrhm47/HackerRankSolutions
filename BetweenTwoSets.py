#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here

    # Step-1 Get range between two arrays
    # min=min(a)
    # max=max(b)

    mini = min(a)
    maxi = max(b)
    range_required = range(mini, maxi + 1)

    # Step-2 Divide every Range element by array1 elements(remainder==0)
    # range[1]%array1[i]==0

    choosen_r = []
    for r in range_required:

        choose_this_r = True
        for a_e in a:
            if r % a_e == 0:
                pass
            else:
                choose_this_r = False
                break

        if choose_this_r == True:
            choosen_r.append(r)

    # Step-3 Divide Every Element of Array2 by the range element(remainder==0)
    # array2[i]%range[i]==0


    final_r_array = []

    for each_choosen_r in choosen_r:

        we_need_this_r = True
        for each_b in b:
            if each_b % each_choosen_r == 0:
                pass
            else:
                we_need_this_r = False
                break

        if we_need_this_r == True:
            final_r_array.append(each_choosen_r)

    # Step-4 If both the Step 2 and 3 are satisfied return the element

    return len(final_r_array)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
