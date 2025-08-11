def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_usurios():
    print("\n \t🛠️ .:: Sistema de Gestión de Devoluciones ::..")
    print("\n\t\t1️⃣  Registro 📝")
    print("\t\t2️⃣  Login 🔐")
    print("\t\t3️⃣  Salir 🚪")
    opcion = input("\n\t👉 Elige una opción: ").upper().strip()
    return opcion

def menu_Usuarios():
    while True:
        print("\n\t\t📦 ..::: Devoluciones :::...")
        print("\t\t📋 ..::: Sistema de administración de Devoluciones :::...")
        print("\t\t1️⃣  Devolver Producto ↩️")
        print("\t\t2️⃣  Mostrar Productos devueltos 📄")
        print("\t\t3️⃣  Mensajes ✉️")
        print("\t\t4️⃣  Salir 🚪")
        opcion = input("\n\t👉 Elige una opción (1-4): ").upper()
        return opcion

def menu_principalAdmin():
    print("\n\t\t👑 ..::: Devoluciones :::...")
    print("\t\t📋 ..::: Sistema de administración de Devoluciones (Admin) :::...")
    print("\t\t1️⃣  Mostrar todos los Productos devueltos 📦")
    print("\t\t2️⃣  Buscar productos devueltos 🔍")
    print("\t\t3️⃣  Eliminar productos devueltos 🗑️")
    print("\t\t4️⃣  Salir 🚪")
    opcion = input("\n\t👉 Elige una opción (1-4): ").upper()
    return opcion
