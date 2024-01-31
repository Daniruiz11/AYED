#PROGRAMA 4 PROBLEMA DE NÚMEROS PRIMOS GEMELOS


def primo(num):
    resultado=1
    for n in range(2, num):
        if num % n == 0:
            #print("Entré a la función if",num,n,resultado)
            resultado=0
            
    return resultado
print("Se le pedirá un rango para poder encontrar los números primos gemelos")
rango1=int(input("Ingrese el número menor del rango: "))
rango2=int(input("Ingrese el número mayor del rango: "))
rango=rango1
a=0
b=0
#POR SI ES MENOR EL SEGUNDO NUMERO QUE EL PRIMERO
if rango1>rango2:
    rango1=rango2
    rango2=rango
print ("Su rango es: ", rango1, "-", rango2)
print("Primos Gemelos")
#Para no generar error por fórmula
if rango1<5:
    rango1=5
    print("3 - 5")
#LIMITES TENIENDO EN CUENTA 6N-1 Y 6N+1 PARA ENCONTRAR PRIMOS GEMELOS
rango1=rango1+1
rango2=rango2+1
#print(rango1)
#print(rango2)
lim1 = int(rango1/6)
lim2 = int(rango2/6)
#print (lim1)
#print (lim2)
for i in range (lim1,lim2+1):
    a=(6*i)-1
    b=(6*i)+1
    #print (a)
    #print (b)
    if primo(a)==1 and primo(b)==1:
        print(a,"-",b)
#BY:@DANIRUIZ11_
    
