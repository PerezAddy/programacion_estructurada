
#lista=[
#        ["Ruben",10,8,10,0,10,0],
#        ["Diana",10,0,9,8,8,0],
#       ["Jose",5,0,6,7,8]
#   ]

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():

    print("\n\t\t...oprima cualquier tecla...")
    input()

def menu_principal():
    print("\n\t\t\t..::: CALIFICACIONES :::... \n\t\t..::: Sistema de administracion de calificaciones :::...\n\t\t 1.- Agregar  \n\t\t 2.- Mostrar \n\t\t 3.- Cálcular Promedios \n\t\t 4.- SALIR ")
    opcion=input("\t\t\t Elige una opción (1-4): ").upper()
    return opcion 

def agregar_calificaciones(datos):
    borrarPantalla()
    print("\n\t...Agregar calificaion numerica:: \n") 
    datos.append(input("ingrese el nombre del alumno: ").upper().strip())
    datos.append(float(input("ingrese la calificacion 1: ")))
    datos.append(float(input("ingrese la calificacion 2: ")))
    datos.append(float(input("ingrese la calificacion 3: ")))
    print("\n\t... La operacion se realizo con exito...")

def mostrar_calificaciones(datos):
        borrarPantalla()
        print("\n\t...Calificaciones capturadas:: \n")
        if datos>0:
            print (f"Alumno    Calificaciones:\t")
            print ("--------------------------------------")
            print (f"{datos[0]}      {datos[1]}  {datos[2]}  {datos[3]}\t")
        else:
            print("No hay calificaciones")

def calcular_promedios(datos):
    borrarPantalla()
    print("\n\t...Promedio del alumno:: \n")
    suma_totalPromedio=(datos[1]+datos[2]+datos[3])/3
    print (f"Alumno     Promedio\t")
    print ("--------------------------------------")
    print (f"{datos[0]}      {suma_totalPromedio}\t")




def agregar_calificaciones1(lista):
    borrarPantalla()
    print("Agregar Calificaciones")
    nombre=input("Nombre del Alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"Calificación {i}: "))
                if cal>=0 and cal<11:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("Ingresa un número valido") 
            except ValueError:
                    print("Ingresa un valor númerico")
    lista.append([nombre]+calificaciones)
    print("Acción realizada con exíto")

def mostrar_calificaciones1(lista):
    borrarPantalla()
    print("Mostrar Calificaciones") 
    if len(lista)>0:
        print(f"{'Nombre':<15}{'Calf. 1':<10}{'Calf. 2':<10}{'Calf. 3':<10}")
        print(f"{'-'*40}")
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
            print(f"{'-'*40}")  
            cuantos=len(lista)
            print(f"Son {cuantos} alumnos")
    else:
        print("No hay calificaciones registradas en el sistema")    

def calcular_promedios2_1(lista):
    borrarPantalla()
    print(".:: PROMEDIOS ::. ")
    if len(lista)>0:
        print(f"{'Alumno':<15}{'Promedio':<10}")
        print(f"{'-'*30}")
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            i=1
            suma=0
            promedio=0
            while i<=3:
                suma+=fila[i]
                i+=1
            promedio=suma/3
            print(f"{nombre:<15}{promedio:.2f}")  
            promedio_grupal+=promedio 
            print(f"{'-'*30}")
        promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio grupal es: {promedio_grupal} ")
    else:
        print("No hay calificaciones registradas en el sistema")     

def calcular_promedios1(lista):
    borrarPantalla()
    print(".:: PROMEDIOS ::. ")
    if len(lista)>0:
        print(f"{'Alumno':<15}{'Promedio':<10}")
        print(f"{'-'*30}")
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            promedio=sum(fila[1:])/3
            print(f"{nombre:<15}{promedio:.2f}")  
            promedio_grupal+=promedio 
            print(f"{'-'*30}")
            promedio_grupal=promedio_grupal/len(lista)
            print(f"El promedio grupal es: {promedio_grupal} ")
    else:
        print("No hay calificaciones registradas en el sistema")    
