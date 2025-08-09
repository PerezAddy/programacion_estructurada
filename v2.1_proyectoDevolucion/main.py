import funciones
import conexionBD
from usuarios import usuario
from notas import productos
import getpass
def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            lista_usuarios = usuario.registrar(nombre, apellidos, email, password, id_roles=1)
            if lista_usuarios:
                print(f"\n {nombre} {apellidos} se a registrado correctamente con el email: {email}")
            else:
                print(f"\n no fue posible registrar al usuario {nombre} {apellidos}, intentelo mas tarde")
            funciones.esperarTecla()

        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=input("\t Ingresa tu contraseña: ").strip()
            lista_usuarios=usuario.iniciarSesion(email,password)
            if lista_usuarios:
                if lista_usuarios[3]== 2:
                    menu_UsuariosAdministrador(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2], lista_usuarios[3])
                else:
                    menu_Usuarios(lista_usuarios[0], lista_usuarios[1], lista_usuarios[2], lista_usuarios[3])

            else:
                print(f"Email y/o password incorrectos, por favor verifica y vielve a intentar ")
            
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_Usuarios(id_usuario,nombre,apellidos,id_categoria):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_Usuarios()

        if opcion == '1' or opcion=="Devolver Producto":
            funciones.borrarPantalla()
            print(f"\n \t .:: Devolver Producto ::. ")
            nombre1=input("\tnombre del producto: ")
            problema=input("\tDescripción del problema: ")
            precio=float(input("\tPrecio del producto: "))
            productos.categorias()
            id_categoria=int(input("\tID de la categoria del producto: "))
            resultado=productos.devolver(nombre1, problema, precio, id_categoria, id_usuario)
            if resultado:
                print(f"\n\t\tse hizo correctamente su devolucion {nombre}")
            else:
                print(f"\n\t\tNo fue posible la devolucion , intenta mas tarde")

            funciones.esperarTecla()    
        
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            

            lista_producto=productos.mostrar(id_usuario)
            if len(lista_producto) >= 1:
                print(f"Mostrar Productos devueltos de {nombre}")
                print(f"{'ID':<10}{'Nombre':<25}{'Problema':<25}{'Precio':<15}{'Categoría':<30}{'Fecha'}")
                print("-" * 120)
                
                for fila in lista_producto:
                    print(f"{fila[0]:<10}{fila[1]:<25}{fila[2]:<25}${fila[3]:<15}{fila[4]:<30}{fila[5]}")
                
                print("-" * 120)
            else:
                print("\t .:: No hay producto devueltos  ::..")


            funciones.esperarTecla()
        


        elif opcion == '3' or opcion=="MENSAJES":
            funciones.borrarPantalla()
            lista_notas=productos.mensajes(id_usuario) 
            if len(lista_notas)>=1:
                print(f"\n\tMostrar los mensajes de eliminacion")
                print(f"{'ID':<10}{'Mnesaje':<35}{'producto':<20}{'id_usuario':<20}")
                print("-" * 80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10}{fila[1]:<35}{fila[4]:<20}{fila[2]:<10}")
                print("-" * 80)
            else:
                print("\n\t..No existen mensajes para ti..")
            funciones.esperarTecla()    
        
        
        elif opcion == '4' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()



def menu_UsuariosAdministrador(id_usuario,nombre,apellidos,id_categoria):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión como Administrador ...")
        opcion=funciones.menu_principalAdmin()  
        
        if opcion == '1' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            lista_productos=productos.mostrarAdmin()
            if lista_productos:

                print(f"Mostrar Productos devueltos")
                print(f"{'Nombre':<20}{'Producto':<25}{'Problema':<25}{'Precio':<15}{'Categoría':<30}{'Fecha'}")
                print("-" * 120)
                
                for fila in lista_productos:
                    print(f"{fila['nombre_usuario']:<20}{fila['nombre_producto']:<25}{fila['problema']:<25}${fila['precio']:<15}{fila['nombre_categoria']:<30}{fila['fecha']}")

                print("-" * 120)
            else:
                print("\t .:: No hay producto devueltos  ::..")

            funciones.esperarTecla()




        elif opcion == '2' or opcion=="BUSCAR":
            funciones.borrarPantalla()
            lista_usuarios = productos.mostrarUsuarios()
            if len(lista_usuarios) >= 1:
                print(f"\n\tMostrar los Usuarios")
                print(f"{'ID':<10}{'Nombre':<25}{'Apellido':<20}")
                print("-" * 80)
                for fila in lista_usuarios:
                    print(f"{fila[0]:<10}{fila[1]:<25}{fila[2]:<20}")
                print("-" * 80)
                resp = input("¿Deseas buscar los productos de un usuario? (Si/No): ").lower().strip()
                if resp == "si":
                    id_usuario=input("\n\t..Ingresa el ID del usuario: ")
                    productos_usuario = productos.mostrarProductosPorUsuario(id_usuario)
                
                    if len(productos_usuario) >= 1:
                        print(f"Mostrar Productos devueltos de {nombre}")
                        print(f"{'ID':<10}{'Nombre':<25}{'Problema':<25}{'Precio':<15}{'Categoría':<30}{'Fecha'}")
                        print("-" * 120)
                        
                        for fila in productos_usuario:
                            print(f"{fila[0]:<10}{fila[1]:<25}{fila[2]:<25}${fila[3]:<15}{fila[4]:<30}{fila[5]}")
                        
                        print("-" * 120)
                        input("\n\t..salir de la busqueda..")
                    else:
                        input("\n\tNo se encontraron productos para ese usuario.")
                        
                else:
                    print("\n\t..Id invalida..")
            else:
                print("\n\t..No existen usuarios..")
        
        
        elif opcion == '3' or opcion=="ELIMINAR":
            lista_usuarios = productos.mostrarUsuarios() 
            if lista_usuarios and len(lista_usuarios) >= 1:
                print("\n\tMostrar los Usuarios")
                print(f"{'ID':<10}{'Nombre':<25}{'Apellido':<20}")
                print("-" * 80)
                for fila in lista_usuarios:
                    print(f"{fila[0]:<10}{fila[1]:<25}{fila[2]:<20}")
                print("-" * 80)

                # Preguntar si desea eliminar
                resp = input("¿Deseas eliminar algún producto? (Si/No): ").lower().strip()
                if resp == "si":
                    id_usuario = input("\n\t..Ingresa el ID del usuario: ").strip()
                    
                    if id_usuario:
                        productos_usuario = productos.mostrarProductosPorUsuario(id_usuario)
                        
                        if productos_usuario and len(productos_usuario) >= 1:
                            print(f"\nMostrar Productos devueltos")
                            print(f"{'ID':<10}{'Nombre':<25}{'Problema':<25}{'Precio':<15}{'Categoría':<30}{'Fecha'}")
                            print("-" * 120)
                            for fila in productos_usuario:
                                print(f"{fila[0]:<10}{fila[1]:<25}{fila[2]:<25}${fila[3]:<15}{fila[4]:<30}{fila[5]}")
                            print("-" * 120)

                            # Eliminar producto
                            id_producto = input("\t \t ID del producto a eliminar: ").strip()
                            razon = input("\t \t ¿Cuál es la razón de la eliminación?: ").strip()

                            if id_producto and razon:
                                resultado1 = productos.motivoEliminacion(razon, id_producto, id_usuario)
                                if resultado1:
                                    print("\n\t✅ El motivo de eliminación fue guardado correctamente.")
                                    respuesta = productos.borrar(id_producto)
                                    if respuesta:
                                        print(f"\n\t✅ Se eliminó correctamente el producto con ID {id_producto}.")
                                    else:
                                        print(f"\n\t❌ No fue posible eliminar el producto. Inténtalo de nuevo.")
                                else:
                                    print("\n\t❌ No se pudo guardar el motivo de eliminación.")
                            else:
                                print("\n\t❌ Debes ingresar un ID y una razón válida.")
                        else:
                            print("\n\t❌ No se encontraron productos para ese usuario.")
                    else:
                        print("\n\t❌ ID de usuario no válido.")
                else:
                    print("\n\tOperación cancelada.")
            else:
                print("\n\t❌ No existen usuarios registrados.")

            funciones.esperarTecla()
        

        elif opcion == '4' or opcion=="SALIR":
            break           

if __name__ == "__main__":
    main()    


