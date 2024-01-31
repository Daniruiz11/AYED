#PROGRAMA 1 NÚMERO PALINDROMO

print("Por favor escriba una palabra o frase, el programa verificará cada palabra escrita (pueden ser números) y dirá si es palíndromo o no.")
texto=input("Ingresar texto aquí: ")
cantidad=0
palabra=""
#print(len(texto))
for c in texto:
    #print (c)
    palabra=palabra+c
    if c==" ":
        cantidad=cantidad+1 #Cuenta el número de palabras
        palabra=palabra[:-1]
        #print(palabra)
        palabrainvertida=palabra[::-1]
        #print(palabrainvertida)
        if palabra==palabrainvertida:
            print('La palabra', palabra , 'es palindroma')
            palabra="";
            palabrainvertida="";
        else:
            print('La palabra', palabra , 'no es palindroma')
            palabra="";
palabrainvertida=palabra[::-1]
cantidad=cantidad+1
if palabra==palabrainvertida:
    print('La palabra', palabra , 'es palindroma')
    palabra="";
    palabrainvertida="";
else:
    print('La palabra', palabra , 'no es palindroma')
    palabra="";
print('Se analizaron', cantidad ,'palabras');
#BY:@DANIRUIZ11_

        
