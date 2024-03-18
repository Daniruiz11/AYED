#!/bin/python3

####GAME OF TWO STACKS

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b,atop,btop,suma,cantidad):
    
    # Write your code here
    if atop<0 and btop<0: ##Cuando ambos INDICES llegan a cero
        print("llego a cero",atop, btop)
        return cantidad
    elif atop<0: ##Cuando el INDICE de a llega a cero
        print("llego a cero a",atop, btop)
        if a[btop]+suma<maxSum:
            cantidad=cantidad+1
            print("sumando contador",cantidad)
            suma=b[btop]+suma
            btop=btop-1
            print("derecha en cero",suma)
            cantidad=twoStacks(maxSum, a, b,atop,btop,suma,cantidad)
        else: return cantidad

    elif btop<0: ##Cuando el INDICE de b llega a cero
        print("llego a cero b",atop, btop)
        if a[atop]+suma<maxSum:
            cantidad=cantidad+1
            print("sumando contador",cantidad)
            suma=suma+a[atop]
            atop=atop-1
            print("izquierda en cero",suma)
            cantidad=twoStacks(maxSum, a, b,atop,btop,suma,cantidad)
        else: return cantidad
    elif a[atop]+suma<=b[btop]+suma: ##Comparando ambas sumas para saber cual coger LADO IZQUIERDO
        if a[atop]+suma<maxSum:
            cantidad=cantidad+1
            print("sumando contador",cantidad)
            suma=suma+a[atop]
            atop=atop-1
            print("izquierda",suma)
            cantidad=twoStacks(maxSum, a, b,atop,btop,suma,cantidad)            
    elif a[atop]+suma > b[btop]+suma :
        if a[btop]+suma<maxSum:
            cantidad=cantidad+1
            print("sumando contador",cantidad)
            suma=b[btop]+suma
            btop=btop-1
            print("derecha",suma)
            cantidad=twoStacks(maxSum, a, b,atop,btop,suma,cantidad)
        else: return cantidad 
 
    
    

if __name__ == '__main__':
    g = int(input().strip())


    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))
    atop=n-1
    btop=m-1
    suma=min(a[atop],b[btop])
    print (atop,btop,suma)
    cantidad=0
    if(a[atop]<b[btop]):
        atop=atop-1
        cantidad=cantidad+1
    elif(a[atop]>b[btop]):
        btop=btop-1
        cantidad=cantidad+1
    result = twoStacks(maxSum, a, b,atop,btop,suma,cantidad)
    print("salida",result)
        
###BY: DaniRuiz11_
