#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def downToZero(n):
    # Write your code here
    m = [n] * (n+1)
    m[0:3] = [0,1,2]
    for i in range(2, n):
        m[i+1] = min(m[i+1], 1 + m[i])
        for j in range(2, i+1):
            if i * j > n: break
            m[i * j] = min(m[i * j], 1 + m[i])
    return m


if __name__ == '__main__':

    m = downToZero(10**6)   

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = m[n]
        print(result)

