import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def stepPerms(n,memoria={}):
    if n<0:
        print("Error, no se admiten números negativos")
    elif n in memoria:
        return memoria[n]
    elif n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        total=stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)
        memoria[n]=total
        return total

if __name__ == '__main__':
    

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)
        print(res)

       
