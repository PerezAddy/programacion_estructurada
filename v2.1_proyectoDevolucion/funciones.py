def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_usurios():
    print("\n \t.:: Sistema de Gestión de devoluciones ::.. \n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir ")
    opcion=input("\t\t Elige una opción: ").upper().strip() 
    return opcion

def  menu_Usuarios():
    while True:
        print("\n\t\t\t..::: Devoluciones :::... \n\t\t..::: Sistema de administracion de Devoluciones :::...\n\t\t 1.- Devolver Producto  \n\t\t 2.- Mostrar Productos devueltos \n\t\t 3.- mensajes \n\t\t 4.- SALIR ")
        opcion=input("\t\t\t Elige una opción (1-4): ").upper()
        return opcion

def menu_principalAdmin():
  
        print("\n\t\t\t..::: Devoluciones :::... \n\t\t..::: Sistema de administracion de Devoluciones (admin) :::...\n\t\t 1.- Mostrar todos los Productos devueltos \n\t\t 2.- Buscar pruductos devueltos \n\t\t 3.- eliminar pruductos devueltos \n\t\t 4.- SALIR ")
        opcion=input("\t\t\t Elige una opción (1-4): ").upper()
        return opcion