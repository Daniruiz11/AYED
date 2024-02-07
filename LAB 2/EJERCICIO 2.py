#!/bin/python3
#Minimum Absolute Difference in an Array

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    momento = abs(arr[1]-arr[0])
    for j in range (0,len(arr)):
        for i in range (j+1,len(arr)):
            key = abs(arr[j]-arr[i])
            print("Key=",arr[j],"-",arr[i],key)
            if i != j and momento>key:
                momento=key
                print("MOMENTO:",momento)
    return momento   
    

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)

#By:@DANIRUIZ11_
