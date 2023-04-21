#reto 1 del día 21 abril 
#LEI MAL EL PROBLEMA, ESTE NO CUENTA
#pero funciona, hemos fallado con exito :D

palabra = input ("ingrese una palabra")

vocal = ["a", "e", "i", "o", "u"]

cantidad_vocales = 0

for i in palabra:
    if i.lower() in vocal:
        cantidad_vocales +=1

print ("La cantidad de vocales en", palabra, "son", cantidad_vocales)
