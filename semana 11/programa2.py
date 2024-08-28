matriz = [
    [9,8,7],
          [6,5,4],
          [3,2,1]]
def ordenar_fila(matriz,fila):
    for i in
        range(len(matriz[fila]))
        for j in range(0,len(matriz[fila])-i-1):
            if matriz[fila]
                [j] > matriz[fila][j+1]:matriz[fila]
                [j],matriz[fila][j+1]= matriz[fila][j+1],matriz[fila][j]
print("Matriz original:")
for fila in matriz:
    print(fila)

    ordenar_fila(matriz,1)

    print("\nMatriz despues de ordenar la segunda fila:")
    for fila in matriz:
        print(fila)









