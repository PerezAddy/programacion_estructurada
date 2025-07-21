#ejemplo 1 crear una lista de un numero e imprimir
import os
numeros=[1,2,3,4,5]
print(numeros)

#2da forma
for  i in numeros:
    print(i)

#3ra forma
for i in range (0,len(numeros)):
    print(numeros[i])



#Ejemplo 2 crear unalista de palabras y posteriormente buacar 
# la coincidencia de una palabra
os.system("cls")
#palabras2=["","","",""] 
#palabras2[0]="hola"
#palabras2[2]="holaa"
#palabras2[3]="holaaa"



palabras=["hola","adios","como","si"] 
palabras_bus=input("que palabra buscas")

if palabras_bus in palabras:
    print ("se encontro")
else:
    print("no se enecotro la palabra")

#2da forma 
encontro=False
for i in palabras:
    if i==palabras_bus:
        encontro=True
if encontro:
    print("se encontro") 
else: 
    print("no lo encontro")




#3ra forma 
encontro=False
for i in range(0,len(palabras)):
    if palabras[i]==palabras_bus:
        encontro=True
if encontro:
    print("se encontro") 
else: 
    print("no lo encontro")






os.system("cls")
#ejemplo3 añadir elementos a una lista
numeros=[]
opc="si"
while opc=="si":
    numeros.append(float(input("dame un numero entero o decimal")))
    opc=input("deseas solicitar otro numero(si/no)").lower()#son para milusculas
print(numeros)

#ejemplo 4 crear una lista nal(matriz) que almacene el nombre y telefono de 4 personas

os.system("cls")
agenda=[
    ["carlos", "6183325001"],
    ["addy", "6182224101"],
    ["raul", "6195321455"]
]
print(agenda)


for r in agenda:
    print(i)



for r in range (0,3):
    for c in range(0,2):
        print(agenda[r][c])

cadena=""
for r in range(0,3):
    for c in range(0,2):
     cadena+=f"{agenda[r][c]}, "
    cadena+="\n"     
print(cadena) 


