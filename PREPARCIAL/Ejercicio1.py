####The Power Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def calculo(x, n, numeros):
    restante = (x - pow(numeros, n))
    #print("valores de restante, numeros: ",restante,nummeros)
    if (restante == 0): #Si llega a cero es porque ya se encontró la combinación que suma exactamente a X
        return 1
    if (restante < 0):
        return 0
   # print (calculo(restante,n,numeros+1))
    return calculo(restante, n, numeros + 1) + calculo(x, n, numeros + 1)


def powerSum(X, N):
    #print("valores de x,n: ",X,N)
    return calculo(X, N, 1)

if __name__ == '__main__':

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)
    print(result)

##By:@DaniRuiz11_

