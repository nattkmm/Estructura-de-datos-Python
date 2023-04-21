import array
import random
#reto 2 día 21 de abril

num_aleatorio = random.randint(10,30)

arr = array.array('i', [0.0] * num_aleatorio)
for i in range(num_aleatorio):
    arr[i] = random.random()

print(arr)

search_val = input("Ingrese un valor para buscar en el arreglo: ")

found = False
for i in range(num_aleatorio):
    if arr[i] == float(search_val):
        print(f"El valor {search_val} se encuentra en el índice {i} del arreglo.")
        found = True
        break

if not found:
    print(f"El valor {search_val} no se encuentra en el arreglo.")
