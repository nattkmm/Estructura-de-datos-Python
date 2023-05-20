import random

fila1 = random.randint(2,5)
print(fila1)

columna1 = random.randint(2,5)
print(columna1)

matriz1 = []
for i in range(fila1):
    fila = []
    for j in range(columna1):
        fila.append(0)
    matriz1.append(fila)
print(matriz1)

print("Ingrese los valores de la matriz 1:")
for i in range (fila1):
    for j in range (columna1):
        elemento1 = int(input("ingrese el elemento:[{0}][{1}] ".format(i, j)))
        matriz1 [i][j] = elemento1
print(matriz1)

matriz2 = []
for i in range(fila1):
    fila = []
    for j in range(columna1):
        fila.append(0)
    matriz2.append(fila)

print("Ingrese los valores de la matriz 2:")
for i in range (fila1):
    for j in range (columna1):
        elemento2 = int(input("ingrese el elemento:[{0}][{1}] ".format(i, j)))
        matriz2 [i][j] = elemento2
print(matriz2)

mresta = []
for i in range(fila1):
    fila = []
    for j in range(columna1):
        fila.append(matriz1[i][j] - matriz2[i][j])
    mresta.append(fila)

print("La resta es:")
for fila in mresta:
    print(fila)

fila2 = int (input ("ingrese la cantidad de filas de la matriz a multiplicar: \n"))
columna2 = int (input ("ingrese la cantidad de columnas de la matriz a multiplicar: \n"))

##multiplicación de matricesss
if columna2 == fila1:
    pass

##transpuestassss


