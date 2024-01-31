#PROGRAMA 3 PROBLEMA DE SUBCADENAS DISTINTAS

texto1=input("Ingrese la cadena original: ")
#print (texto1)
textorotado=texto1
cantidad=0;
for i in range (0,len(texto1)):
    textorotado= textorotado[1:]+textorotado[:1]
    print(textorotado)
    cantidad=cantidad +1

print ("La cantidad de cadenas posibles es: ",cantidad)
#BY:@DANIRUIZ11_
