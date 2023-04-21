#reto 1 dia 21 de abril
palabra = input ("ingrese una palabra: \n")

cantidad_vocales ={ 'a':0 , 'e':0 , 'i':0 , 'o':0 , 'u':0 }

for i in palabra:
    if i.lower() in cantidad_vocales:
        cantidad_vocales [i.lower()] +=1

print ("La cantidad de vocales en", palabra, "son:")
print ("a = ", cantidad_vocales ['a'])
print ("e = ", cantidad_vocales ['e'])
print ("i = ", cantidad_vocales ['i'])
print ("o = ", cantidad_vocales ['o'])
print ("u = ", cantidad_vocales ['u'])

# Integrantes: Natalia Carrillanca y Felipe Delgado 
