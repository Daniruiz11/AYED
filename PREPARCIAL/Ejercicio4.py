#!/bin/python3
#####Closest Numbers

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    menor=float('inf')
    total=[]
    for i in range(len(arr)-1):
        menor=min(arr[i+1]-arr[i],menor)
    for i in range(len(arr)-1):
        if(arr[i+1]-arr[i] == menor):
            total.append(arr[i])
            total.append(arr[i+1])
    return total
# Write your code here

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)
    print(result)
 ##By:@DaniRuiz11





        
