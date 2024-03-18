#!/bin/python3
###poisonousPlants
import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    pila = []
    maximo = 0 
    
    for pesticida in p:
        dias = 0 
        while pila and pila[-1][0] >= pesticida:
            dias = max(dias, pila.pop()[1])
        if pila:
            dias += 1
        else:
            dias = 0
        maximo = max(maximo, dias)
        pila.append((pesticida, dias))
    
    return maximo



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()

##By: DaniRuiz11_
