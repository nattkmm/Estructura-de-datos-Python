import random

fila = int (input ("ingrese la cantidad de filas: \n"))
columna = int (input ("ingrese la cantidad de columnas: \n"))

matriz = []
for i in range(fila):
    fila = []
    for j in range(columna):
        fila.append(random.randint(0, 10))
    matriz.append(fila)

print("La matriz es:")
for fila in matriz:
    print(fila)

esc = int(input("ingrese un escalar: \n"))

for i in range(fila):
    for j in range(columna):
        matriz[i][j] = matriz[i][j] * esc



