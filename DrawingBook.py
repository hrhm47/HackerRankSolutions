#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here

    # From Front
    # book_pages = []
    # right_page = 1
    # left_page =0
    # count = 0
    # for i in range(n):
    #     book_pages.append([left_page,right_page])
    #     left_page += 2
    #     right_page += 2
    # # print(book_pages)

    # #From Back
    # arr_back = []
    # right = 0
    # left = 0
    # if p%2!=0:
    #     right = p
    #     left = p - 1
    # else:
    #     left = p
    #     right = p-1
    # for i in range(5):
    #     arr_back.append([left,right])
    #     left  -= 2
    #     right -= 2
    # print(arr_back)
    # #array for to retrun minimum
    # ar_min = []
    # count = 0
    # #From Front Counting How Many Pages We Need
    # for i in range(n):
    #     if p in book_pages[i]:
    #         ar_min.append(count)
    #         break
    #     else:
    #         count += 1
    # ar_min.append(count)
    # count = 0
    # #From Back Counting

    # for i in range(n):
    #     if p in arr_back[i]:
    #         ar_min.append(count)
    #         return min(ar_min)
    #     else:
    #         count += 1

    # if p%2!=0:
    # Left =  0
    # Right = 1
    # countR = 0
    # arr_final = []
    # #Front loop (from front flipping)
    # for i in range(n):
    #     # print(Left,Right)
    #     if Left==p or Right ==  p:
    #         # print(countR)  # return i
    #         arr_final.append(countR)
    #         # return countR
    #         break
    #     Right +=2
    #     Left +=2
    #     countR +=1
    # arr_final.append(countR)

    # #Back Fliping
    # # else:
    # Left =  0
    # Right = 0
    # countL = 0

    # if p%2==0:
    #     Left = p
    #     Right = p+1
    # else:
    #     Right = p
    #     Left = p-1

    # for j in range(n):
    #     # print(j)
    #     # print(Left,Right)
    #     if Left or Right ==  p:
    #         arr_final.append(countL)
    #         # print(countL)  # return i
    #         # return countL
    #         break
    #     Right -=2
    #     Left -=2
    #     countL +=1
    #     # print("else")
    # if n%2==1:
    #     return min(arr_final)
    # else:
    #     return max(arr_final)
    # # arr_final.append(countL)
    # # return (min(arr_final))

    # n=6 p=2
    #  p//2     2//2 =  1  front
    # n//2 - p//2   , 6//2 = 3 2//2 =1    3-1   = 2  //back
    # min(1,2)

    if (p <= n):
        return min(p // 2, n // 2 - p // 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
