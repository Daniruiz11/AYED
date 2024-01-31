#PROGRAMA 5 CUADRADO MAGICO

def crear_matriz(n):
    return[[0 for j in range(n)]for i in range(n)]
#LLENAR DE ARRIBA AL CENTRO DE LA MATRIZ
def arriba(inicio,n,matriz,conteo):
    for variable in range (n):
        matriz[inicio][variable]=conteo
        #print(inicio,variable,conteo)
    return matriz
   
#LLENAR DE ABAJO AL CENTRO DE LA MATRIZ
def abajo(inicio,n,matriz,conteo):
    for variable in range (n):
        matriz[inicio][variable]=conteo
        #print(inicio,variable,conteo)
    return matriz

#LLENAR DE DERECHA AL CENTRO DE LA MATRIZ
def derecha(inicio,n,matriz,conteo,nivel,limite,limite2):
    for variable in range (limite,limite2):
        matriz[variable][inicio]=conteo
        #print(variable,inicio,conteo,limite,limite2,n)
        
    return matriz

#LLENAR DE IZQUIERDA AL CENTRO DE LA MATRIZ
def izquierda(inicio,n,matriz,conteo,nivel,limite,limite2):
    for variable in range (limite,limite2):
        matriz[variable][inicio]=conteo
        #print(inicio,variable,conteo,limite,limite2,n)
        
    return matriz





nivel=int(input("Ingrese el nivel del cuadrado mágico: "))
#Por recurrencia el nivel nos da el tamaño de la matriz nxn
n=(2*nivel)-1
matriz = crear_matriz(n)
x=""
inicio=0
conteo=nivel
limite=0
limite2=n

#LLENAR DE ARRIBA AL CENTRO DE LA MATRIZ
for a in range (nivel):
    matriz=arriba(inicio,n,matriz,conteo)
    inicio=inicio+1
    conteo=conteo-1
conteo=conteo+1
#LLENAR DE ABAJO AL CENTRO DE LA MATRIZ
for b in range (nivel-1):
    conteo=conteo+1
    matriz=abajo(inicio,n,matriz,conteo)
    inicio=inicio+1
conteo=conteo+1
#LLENAR DE DERECHA AL CENTRO DE LA MATRIZ
for c in range (nivel-1):
    limite=limite+1
    limite2=limite2-1
    conteo=conteo-1
    inicio=inicio-1
    if ((limite2-limite)>0):
        matriz=derecha(inicio,n,matriz,conteo,nivel,limite,limite2)
conteo=nivel
inicio=0
limite=0
limite2=n
#print("ya casi",limite,limite2,conteo,inicio)
#LLENAR IZQUIERDA AL CENTRO DE LA MATRIZ
for d in range (nivel-1):
    limite=limite+1
    limite2=limite2-1    
    if ((limite2-limite)>0):
        #print("izquierda")
        matriz=izquierda(inicio,n,matriz,conteo,nivel,limite,limite2)
    inicio=inicio+1
    conteo=conteo-1

        
    
    
#IMPRIMIR LA MATRIZ    
for l in range (n):
    for m in range (n):
        x+=str(matriz[l][m])+'\t'
    print(x)
    x=""
        

#BY:@DANIRUIZ11_


    
