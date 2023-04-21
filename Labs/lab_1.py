import random

f1 = int (input ("ingrese la cantidad de filas: \n"))
c1 = int (input ("ingrese la cantidad de columnas: \n"))

m1 = []
for i in range(f1):
    fila = []
    for j in range(c1):
        fila.append(random.randint(0, 5))
    m1.append(fila)

m2 = []
for i in range(f1):
    fila = []
    for j in range(c1):
        fila.append(random.randint(0, 5))
    m2.append(fila)

print("La matriz 1 es:")
for fila in m1:
    print(fila)

print("La matriz 2 es:")
for fila in m2:
    print(fila)

msuma = []
for i in range(f1):
    fila = []
    for j in range(c1):
        fila.append(m1[i][j] + m2[i][j])
    msuma.append(fila)

print("La suma de matrices es:")
for fila in msuma:
    print(fila)

f2 = int (input ("ingrese la cantidad de filas: \n"))
c2 = int (input ("ingrese la cantidad de columnas: \n"))

m3 = []
for i in range(f2):
    fila = []
    for j in range(c2):
        fila.append(random.randint(0, 5))
    m3.append(fila)

print("La matriz 3 es:")
for fila in m3:
    print(fila)

mresta = []
for i in range(f2):
    fila = []
    for j in range(c2):
        fila.append(msuma[i][j] - m3[i][j])
    mresta.append(fila)

print("La resta de matrices es:")
for fila in mresta:
    print(fila)
