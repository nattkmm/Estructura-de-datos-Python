import random
import numpy as np
from numpy.linalg import inv, det

matrizA = []
for i in range (4):
    fila = []
    for j in range (4):
        fila.append(random.randint(0, 10))
    matrizA.append(fila)
matrizA = np.array(matrizA)
print("La primera matriz es: \n",matrizA)

matrizB = []
for i in range (4):
    fila = []
    for j in range (4):
        fila.append(random.randint(0, 10))
    matrizB.append(fila)
matrizB = np.array(matrizB)
print("la segunda matriz es: \n",matrizB)

matrizC = []
for i in range (4):
    fila = []
    for j in range (4):
        fila.append(random.randint(0, 10))
    matrizC.append(fila)
matrizC = np.array(matrizC)
print("la tercera matriz es: \n",matrizC)

determinanteB = det(matrizB)
print("el determinante de la matriz B es:", determinanteB)
matrizA3 = matrizA ** 3
determinanteA = det(matrizA3)
print("el determinante de la matriz A^3 es:", determinanteA)

if determinanteB == 0.0 :
    print("la matriz no B tiene inversa, por ende no se puede resolver la operación")
elif determinanteA == 0.0: 
    print("la matriz A^3 no tiene inversa, por ende no se puede resolver la operación")
else:
    inversaB = inv(matrizB)
    inversaA3 = inv(matrizA3)

    matrizResultado = matrizA3 @ inversaB @ matrizC + inversaA3
    print(matrizResultado)