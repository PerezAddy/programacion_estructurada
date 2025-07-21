"""


  Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("cls")
paises={"Mexico","Brasil","España","Canada"}
print(paises)

#Funciones u operaciones 
for i in paises:
    print(i)

paises.add("México")
print(paises)

paises.pop()
print(paises)

paises.remove("México")
print(paises)

#ejemplo crar un programa que solicite los email de los alumons de la UTD
#almacenar en una lista y posteriormente mostrar en pantalla sin duplicados

lista_email=[]
res="si"
while res=="si":
    lista_email.append(input("dame que email que quieres almacenar"))
    res=input("deseas alamacenar mas email?").lower()#son para milusculas
print(lista_email)

#Para impirmir con set sin duplicados


email_set=set(lista_email)
lista_email=list(email_set)
print(lista_email)














