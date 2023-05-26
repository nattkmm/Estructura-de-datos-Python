import random
import numpy as np

matrizA = []
for i in range (3):
    fila = []
    for j in range (3):
        fila.append(random.randint(1,10))
    matrizA.append(fila)
matrizA = np.array(matrizA)
print("La matriz A es:\n", matrizA)

matrizB = []
for i in range (3):
    fila = []
    for j in range (3):
        fila.append(random.randint(11,30))
    matrizB.append(fila)
matrizB = np.array(matrizB)
print("La matriz B es:\n",matrizB)

matrizC = []
for i in range (3):
    fila = []
    for j in range (3):
        fila.append(random.randint(-10,-1))
    matrizC.append(fila)
matrizC = np.array(matrizC)
print("La matriz C es:\n",matrizC)

SumaAB = matrizA + matrizB
print("El resultado de la Suma de la matriz A con la matriz B es:\n",SumaAB)

###Resultado 1
MulABC = SumaAB @ matrizC
print("El resultado de la Multiplicación de la matriz A + B con la matriz C es:\n",MulABC)

MulAC = matrizA @ matrizC
print("El resultado de la Multiplicación de la matriz A con la matriz C es: \n",MulAC)

MulBC = matrizB @ matrizC
print("El resultado de la Multiplicación de la matriz B con la matriz C es: \n",MulBC)

###resultado 2
SumaAC_BC = MulAC + MulBC
print("El resultado de la Suma de la matriz AxB con la matriz BxC es: \n",SumaAC_BC)


if MulABC[i][j] == SumaAC_BC[i][j]:
    print("la propiedad se cumple")
else:
    print("la propiedad no se cumple") 

