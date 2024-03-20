###Balanced Brackets

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def isBalanced(s):
    abiertos = "([{{"   # abiertos: Contiene los caracteres de apertura.
    cerrados = ")]}"    # cerrados: Contiene los caracteres de cierre.
    balance = 0         # Inicializa un contador `balance` en 0.
    for char in s:      # Recorre la cadena caracter por caracter.
        if char in abiertos:# Si el caracter es de apertura, se incrementa el contador.
          balance += 1

        elif char in cerrados:# Si el caracter es de cierre:
            if balance == 0 or abiertos[cerrados.index(char)] != char:
                return 'NO'
            balance -= 1 # Si el caracter de cierre coincide con el último caracter de apertura, se decrementa el contador.
    return 'YES' if balance == 0 else 'NO' # Se retorna 'YES' si el contador es 0 al final de la iteración, 'NO' en caso contrario.





    
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)
###By:@DaniRuiz11_
