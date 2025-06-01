#crear un programa que calcule e imprima tabla de mutliplicar del 2 numero=input(int("ingrese el numero que quiere multiplicar"))


numero=int(input("ingrese el numero que quiere multiplicar"))

mult=numero*1
print(f" [{numero}x 1= {mult}")
mult=numero*2
print(f" {numero} x 2= {mult}")
mult=numero*3
print(f" {numero} × 3= {mult}")
mult=numero*4
print(f" {numero} × 4= {mult}")
mult=numero*5
print (f" {numero} x 5= {mult}")
mult=numero*6
print (f" {numero} x 6= {mult}")
mult=numero*7
print(f" {numero} x 7= {mult}")
mult=numero*8
print (f" {numero} x 8= {mult}")
mult=numero*9
print(f" {numero} x 9= {mult}")
mult=numero*10
print(f" {numero} x 10= {mult}")

#caso 2
numero=int(input("ingrese el numero que quiere multiplicar"))
for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")


#caso 3
#usando funciones y estruturas de control

def multi(numero):
 for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")



#aqui le pide al usuario que quiere multiplicar 
pedirmulti=int(input("ingrese usted el numero que multiplicar"))


#aqui llamo ala funion
multi(pedirmulti)