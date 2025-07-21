"""
list(array)
son colleciones o conjunto de datos/valores bajo un mismo
nombre, para acceder a los valores 
se hace con un indice numerico

Nota: sus valores si son modificables

la lista es una colecion ordenada y modificable
permite miembros duplicados

"""

import os
os.system ("clear")

#funciones mas comunes en las listas

paises=["Mexico","Brasil","España","canada"]

numeros=[23,12,100,34]

varios=["hola",True,33,3,12]


#ordenar las listas

print(numeros)
print(paises)
print(varios)


numeros.sort()#para ordenar cadena de caracterss y palabras
print(numeros)

paises.sort()
print(paises)




#agregar o insertar o añadir un elemento a la lista
print(paises)
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"honduras")#aqui se acomoda donde tu quieres
print(paises)

#eliminar o borrar o suprimir un elemneto de la lista
#1ra forma

paises.sort()
print(paises)

paises.pop(5)
print(paises)

#2da forma de borrar
paises.remove("Honduras")#se borra por nombre o numeros
print(paises)

#busca un elemento dentro de una lista

hola="Brasil" in paises #forma 1
print(hola)


print("Brasil" in paises )# forma 2 difrenetes fomas de hacer esto

#contar el numero de veces que un elemento 
#esta dentro de una de una lista

print(numeros)
print(numeros.count(12)) #forma para contar

numeros.insert(1,12)
print (numeros.count(12))

#dar la vuelta a los elementos de una  lista es decir decendentemente 
print(paises)
print(numeros)

paises.reverse()
print (paises)


numeros.reverse()
print (numeros)

#cononcer el indeice de la posicion de un valor de la lista
print(paises.index("España")) 

##
#posicion=paises.index("España")#sive para actualizar datos
#paises[posicion]="ESPAÑA"
#print(paises)

#unir el contenido de 2 o mas listas en una sola 
numeros2=[200,500,100]
print(numeros)
print(numeros2)
numeros.extend(numeros2)#sirve para unir las listas

print(numeros)


paises.extend(numeros2)
print(paises)