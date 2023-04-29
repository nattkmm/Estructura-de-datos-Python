import random

filas = int (input ("ingrese la cantidad de filas: \n"))
columnas = int (input ("ingrese la cantidad de columnas: \n"))

matriz1 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(random.randint(1, 5))
    matriz1.append(fila)

matriz2 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(random.randint(1, 5))
    matriz2.append(fila)

print("La matriz 1 es:")
for fila in matriz1:
    print(fila)

print("La matriz 2 es:")
for fila in matriz2:
    print(fila)

msuma = [[0] * filas, [0] * columnas]
def Suma_de_Matrices(matriz1, matriz2, msuma):
    for i in range(filas):
        for j in range(columnas):
            msuma[i][j] = (matriz1[i][j] + matriz2[i][j])
    return msuma

mresta = [[0] * filas, [0] * columnas]
def Resta_de_Matrices(matriz1, matriz2, mresta):
    for i in range(filas):
        for j in range(columnas):
            mresta[i][j] = (matriz1[i][j] - matriz2[i][j])
    return mresta

print("El resultado de la suma de matrices es:\n", Suma_de_Matrices(matriz1, matriz2, msuma))

print("El resultado de la resta de matrices es:\n", Resta_de_Matrices(matriz1, matriz2, mresta))
