#!/bin/python3
####Coin change

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY c
#

def getWays(n, c, memoria={}):
    if n == 0:
        return 1
    if n < 0 or not c:
        return 0
    if (n, tuple(c)) in memoria:
        return memoria[(n, tuple(c))]#En memoria tengo que almacenar la cantidad n y la lista de monedas para que no repita procedimiento más adelante
    #Tuple convierte la lista en una estructura no editable
    resultado= getWays(n - c[-1], c, memoria) + getWays(n, c[:-1], memoria)#incluye y exluye la ultima moneda en el cálculo recursivamente
    memoria[(n, tuple(c))] = resultado #almacena resultado en memoria
    return memoria[(n, tuple(c))]

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))

    res = getWays(n, c)
    print(res)

    
#By:@DaniRuiz11_
