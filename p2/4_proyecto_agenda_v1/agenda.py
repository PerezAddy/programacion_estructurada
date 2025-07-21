def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():

    print("\n\t\t...oprima cualquier tecla...")
    input()


def menu_principal():
    print("\n\t\t..::: Sistema de Gestion de Agenda de contactos :::...\n\n\t\t\t\t 1️⃣  Agregar contacto  \n\t\t\t\t 2️⃣  Mostrar todos los contactos \n\t\t\t\t 3️⃣  Buscar contacto con nombre \n\t\t\t\t 4️⃣  modificar contacto \n\t\t\t\t 5️⃣  Elimnar Contacto \n\t\t\t\t 6️⃣  Salir \n")
    opcion=input("\t\t\t 👉 Elige una opción (1-4): ").upper()
    return opcion 

def agregar_contacto(agenda) :
    borrarPantalla()
    print ("AgregarContactos")
    nombre=input ("Nombre:").upper () .strip()
    if nombre in agenda:
        print ("Contacto existente")
    else:
        tel=input("Telefono: ").strip()
        email=input ("Email: ").upper ().strip ()
    agenda [nombre]=[tel, email]
    print("Accion realizada con exito")

def mostrar_contacto (agenda):
    borrarPantalla()
    print("Mostrar Contactos")
    if not agenda : 
        print("No hay contactos")
    else:
        print(f"{'Nombre': <15} {'Telefono': <15}{'Email': <15}")
        print (f"-"*60)
    for nombre, datos  in agenda.items():
        print(f" {nombre: <15} {datos [0]: <15}{datos [1]: <15}")
        print(f"-"*60)

def buscar_contacto (agenda) :
    borrarPantalla()
    print("Buscar Contactos")
    if not agenda: 
        print ("No hay contactos")
    else:
        nombre=input ("Nombre:").upper().strip()
        if nombre in agenda:
            print(f"{ 'Nombre' : <15} {'Telefono' : <15} {'Email' : <15}")
            print(f"-"*40)
            print(f" {nombre: <15}{agenda[nombre][0]: <15} {agenda[nombre][1]:<15}")
            print(f"-"*40)
        else:
            print("No existente el  contacto")



def modificar_contacto(agenda):
    borrarPantalla()
    print("Modificar Contactos")
    if not agenda: 
        print ("No hay contactos")
    else:
        nombre=input("Nombre:") .upper().strip()
        if  nombre in agenda:
            print(f" {'Nombre': <15}{'Telefono' : <15}{'Email':<15}")
            print(f"-"*40)
            print(f" {nombre: <15}{agenda [nombre] [0]: <15} {agenda [nombre][1]: <15}")
            print(f"-"*40)
            resp=input ("Deseas modificar el contacto?  (S1/No)"). lower().strip()
            if resp=="si":
                tel=input("Telefono: ") .strip()
                email=input ("Email: "). upper().strip()
                agenda [nombre]=[tel, email]
                print("Accion realizada con exito")
            else:
                print("No•existente el contacto") 


def eliminar_contacto(agenda):
    borrarPantalla()
    print("Eliminar Contactos")
    if not agenda: 
        print ("No hay contactos")
    else:
        nombre=input("Nombre:") .upper().strip()
        if  nombre in agenda:
            print(f" {'Nombre': <15}{'Telefono' : <15}{'Email':<15}")
            print(f"-"*40)
            print(f" {nombre: <15}{agenda [nombre] [0]: <15} {agenda [nombre][1]: <15}")
            print(f"-"*40)
            resp=input ("Deseas elimnar contacto?  (S1/No)"). lower().strip()
            if resp=="si":
                del agenda[nombre]
                print("Accion realizada con exito")
            else:
                print("No•existente el contacto") 
