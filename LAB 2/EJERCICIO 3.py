#!/bin/python3
####Luck Balance
import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    #suma de la columna 1 se contests
    suma=0
    suerte=0
    for i in range(0,len(contests)):
                   suma=suma+contests[i][1]
                   suerte=suerte+contests[i][0]
    #print(suma, suerte, k)
    
    for j in range(0,len(contests)):
        if k < suma :
           # print("asi,",suerte,contests[j][0])
            if contests[j][1]==1:
                suerte=suerte-(2*contests[j][0])
                k=k+1
              #  print("CONSTANTE Y SUERTE", k, suma, suerte)
        
        else:
            return suerte
    return suerte
        
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    contests.sort()
    #print(contests)
    result = luckBalance(k, contests)
    #print("el resultado es")
    print(result)
#by: @DANIRUIZ11_

    
