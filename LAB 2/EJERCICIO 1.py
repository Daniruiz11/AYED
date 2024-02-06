# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    resumen=[]
    #print("creado resumen")
    # Write your code here
    for i in range(len(orders)):
        #print("entre",i)
        resumen.append(list((i+1, orders[i][0]+orders[i][1])))
        #print("llené ",i)
    return resumen

def InsertionSort(result):
    for j in range (1,len(result)):
        key = result[j][1]
        cliente = result[j][0]
      #  print("Key: ",key)
      #  print(result)
        i = j-1
        #print("I: ", i)
        while i >= 0 and result[i][1] > key :
           # print("llegue",result[i][1],key)
            result[i + 1][1] = result[i][1]
            result[i + 1][0] = result[i][0]
            i=i-1
        result[i+1][1] = key
        result[i+1][0] = cliente


if __name__ == '__main__':


    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

print(orders)
result = jimOrders(orders)
print(result)
ordenado =InsertionSort(result)
print(result)
result = [fila[0] for fila in result]
print("Esto es salida")
print(result)

