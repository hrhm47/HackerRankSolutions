#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
"""
leap_months = [31,29,31,30,31,30,31,31]
not_leap_months = [31,28,31,30,31,30,31,31]
nine_eighten_month = [32,14,31,30,31,30,31,31]
#1700-1917
    if 1700<=year<=1917:
        if year%4==0:
        dd=256-sum(leap_months)
        return (dd,".","09",year)
        else:
        dd=256-sum(not_leap_months)
        return (dd,".","09",year)
    elif year == 1918:
        # if year%4==0:
        dd=256-sum(leap_months)
        return (dd,".","09",year)        
    else:
        if 1919<=year<=2700:
            if year%400==0:
                dd=256-sum(leap_months)
                return (dd,".","09",year)

            elif year%4==0 and year%100!=0:
                dd=256-sum(leap_months)
                return (dd,".","09",year)

            else:
                dd=256-sum(not_leap_months)
                return (dd,".","09",year)

"""


def dayOfProgrammer(year):
    # Write your code here
    leap_months = [31, 29, 31, 30, 31, 30, 31, 31]
    not_leap_months = [31, 28, 31, 30, 31, 30, 31, 31]
    nine_eighten_month = [32, 14, 31, 30, 31, 30, 31, 31]
    dd = 0
    sep = "09"
    # 1700-1917
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            dd = 256 - sum(leap_months)
            return (str(dd) + "." + sep + "." + str(year))
        else:
            dd = 256 - sum(not_leap_months)
            return (str(dd) + "." + sep + "." + str(year))
    if year == 1918:
        # if year%4==0:
        # print(256-sum(nine_eighten_month))
        dd = 256 - sum(nine_eighten_month)
        return (str(dd) + "." + sep + "." + str(year))
    else:
        if 1919 <= year <= 2700:
            if year % 400 == 0:
                dd = 256 - sum(leap_months)
                return (str(dd) + "." + sep + "." + str(year))

            elif year % 4 == 0 and year % 100 != 0:
                dd = 256 - sum(leap_months)
                return (str(dd) + "." + sep + "." + str(year))

            else:
                dd = 256 - sum(not_leap_months)
                return (str(dd) + "." + sep + "." + str(year))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

fptr.close()