#!/bin/python3
#Minimum Absolute Difference in an Array

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    momento = abs(arr[1]-arr[0])
    combinaciones = list(combinations(arr, 2))
    print("combinaciones",combinaciones)
    for comb in combinaciones:
        i, j = comb
        print("comb",comb)
        if (abs(i-j))< momento:
            momento=abs(i-j)
            print("momento",momento)
    return momento   
    

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)


