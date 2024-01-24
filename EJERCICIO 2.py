#PROGRAMA 2 CADENAS ROTADAS
texto1=input("Ingrese la primera cadena: ")
texto2=input("Ingrese la segunda cadena: ")
#print (texto1)
textorotado=texto1
estado=0;
for i in range (0,len(texto1)):
    textorotado= textorotado[1:]+textorotado[:1]
    #print(textorotado)
    if(textorotado==texto2):
        print('La cadena 2 ',texto2,' es rotación de la cadena 1 ',texto1)
        estado=1;
if (estado==0):
    print('La cadena 2 ',texto2,' NO es rotación de la cadena 1 ',texto1)

