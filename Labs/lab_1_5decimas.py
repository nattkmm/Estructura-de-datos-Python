import numpy as np

filas = int(input("Ingrese la cantidad de filas: \n"))
columnas  = int(input("Ingrese la cantidad de columnas: \n"))

matriz1 = np.empty((filas, columnas))
print("Ingrese el valor de los ementos de la matriz 1:")
for i in range (filas):
    for j in range (columnas):
        elemento = input("ingrese el valor del elemento:[{0}][{1}] ".format(i, j))
        matriz1 [i][j] = elemento

matriz2 = np.empty((filas, columnas))
print("A continuación ingrese el valor de los elementos de la matriz 2:")
for i in range (filas):
    for j in range (columnas):
        elemento = input("ingrese el valor del elemento:[{0}][{1}] ".format(i, j))
        matriz2 [i][j] = elemento

def sumar_matrices ():
    msuma = np.add(matriz1, matriz2)
    return msuma

def restar_matrices ():
    mresta = np.subtract(matriz1, matriz2)
    return mresta

print ("la matriz suma es: \n" , sumar_matrices())

print ("la resta de matrices es: \n", restar_matrices())


# np.add para sumar
# np.subtract para restar 