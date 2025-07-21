""" peliculas=["hola"]

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    print("\n\t\t...oprima cualquier tecla...")
    input()

def agregarPelicula():
    borrarPantalla()
    print("\n\t...Agregar Pelicula:: \n")
    peliculas.append(input("ingrese el nombre: ").upper().strip())
    print("\n\t... La operacion se realizo con exito...")


def consultarPeliculas():
    borrarPantalla()
    print("\n\t .::consultar o Mostrar las peliculas::.\n")
    if len(peliculas)>0:
        for i in range(0,len(peliculas)):
            print(f"\t{i+1}: {peliculas [i]}")
    else:
        print("\n\t ho hay peliculas el sistema")

def vaciarPeliculas():
    borrarPantalla()
    print("\n\t vaciar o quitar Todas las peliculas: ")
    res=input("deseas quitar Todos las peliculas del sistema (SI/NO): ").lower().strip()
    if res=="clear":
        peliculas.clear()
        print("se borro")
        print("\n\t\t:::La operacion se realizo con exito:::")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t.:: Buscar peliculas ::.\n")
    pelicula_buscar=input("ingrese el nombre de la pelicula a bucar").lower().strip()
    encontro=0
    if not {pelicula_buscar in peliculas}:
        print("\n\t\t ¡No se encontro la pelicula!")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"\nLa pelicula{pelicula_buscar} si la tenemos y esta en la casilla {i+1} ")
                encontro+=1
        print(f"\nTenemos {encontro} pelicula(s) con este titulo")
        print("\n\t\t:::La operacion se realizo con exito:::")


def eliminarpelis():
    
    borrarPantalla()
    print("\n\t.:: Buscar peliculas ::.\n")
    pelicula_buscar=input("ingrese el nombre de la pelicula a borrar").lower().strip()
    encontro=0
    if not {pelicula_buscar in peliculas}:
        print("\n\t\t ¡No se encontro la pelicula!")
    else:
        res="si"
        while pelicula_buscar in peliculas and res=="si":
            res=input("¿Desea borrar la pelicula del sistema? (si/no)")
            if res=="si":
                posicion= peliculas.index(pelicula_buscar)
                print(f"\nLa pelicula que se borro es {pelicula_buscar} y estaba en la casilla {posicion+1} ")
                peliculas.remove(pelicula_buscar)
                encontro+=1
                print("\n\t\t:::La operacion se realizo con exito:::")
    print(f"\n\t se borro {encontro} pelicula(s) con este titulo")         """

from conexion import conectar
import os
def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperaTecla():
    input("\n🔘 Oprima cualquier tecla para continuar ...")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t🎞️ .:: Agregar Películas ::.")
    nombre = input("🎬 Ingresa el nombre: ").upper().strip()
    categoria= input("🎬ingrese categoria de pelicula").upper().strip()
    clasificacion=input("🎬ingrese clasificaion de pelicula").upper().strip()
    genero= input("🎬ingrese genero de pelicula ").upper().strip()
    idioma= input("🎬ingrese idioma de pelicula: ").upper().strip()

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO peliculas( nombre, categoria, clasificacion, genero, idioma,) VALUES (%s, %s, %s, %s, %s)", (nombre, categoria, clasificacion, genero, idioma))
    conexion.commit()
    conexion.close()

    print("\n\t✅ ::: ¡Película guardada en la base de datos! :::")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t📋 .:: Lista de Películas ::.")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM peliculas")
    peliculas = cursor.fetchall()
    conexion.close()

    if peliculas:
        for peli in peliculas:
            print(f"{peli[0]}. {peli[1]}")
    else:
        print("⚠️ No hay películas registradas.")

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t❌ .:: Eliminar Película ::.")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM peliculas")
    peliculas = cursor.fetchall()

    if peliculas:
        for peli in peliculas:
            print(f"{peli[0]}. {peli[1]}")
        try:
            id_a_eliminar = int(input("\n👉 Ingresa el ID de la película a eliminar: "))
            cursor.execute("DELETE FROM peliculas WHERE id = %s", (id_a_eliminar,))
            conexion.commit()
            print("\n✅ ::: Película eliminada.")
        except ValueError:
            print("❌ Entrada inválida.")
    else:
        print("⚠️ No hay películas registradas.")
    conexion.close()

def actualizarPeliculas():
    borrarPantalla()
    print("\n\t🔁 .:: Actualizar Película ::.")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM peliculas")
    peliculas = cursor.fetchall()

    if peliculas:
        for peli in peliculas:
            print(f"{peli[0]}. {peli[1]}")
        try:
            id_a_actualizar = int(input("\n👉 Ingresa el ID de la película a actualizar: "))
            nuevo_nombre = input("🎬 Ingresa el nuevo nombre: ").upper().strip()
            cursor.execute("UPDATE peliculas SET nombre = %s WHERE id = %s", (nuevo_nombre, id_a_actualizar))
            conexion.commit()
            print("\n✅ ::: Película actualizada.")
        except ValueError:
            print("❌ Entrada inválida.")
    else:
        print("⚠️ No hay películas registradas.")
    conexion.close()

def buscarPeliculas():
    borrarPantalla()
    print("\n\t🔍 .:: Buscar Película ::.")

    conexion = conectar()
    cursor = conexion.cursor()
    busqueda = input("🔎 Ingresa parte del nombre a buscar: ").upper().strip()
    cursor.execute("SELECT id, nombre FROM peliculas WHERE nombre LIKE %s", ('%' + busqueda + '%',))
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        print("\n🎯 Resultados encontrados:")
        for peli in resultados:
            print(f"{peli[0]}. {peli[1]}")
    else:
        print("❌ No se encontraron coincidencias.")

def vaciarPelicula():
    borrarPantalla()
    print("\n\t🧹 .:: Vaciar Lista de Películas ::.")
    confirmacion = input("¿Estás seguro que deseas borrar todas las películas? (si/no): ").lower()
    if confirmacion == "si":
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM peliculas")
        conexion.commit()
        conexion.close()
        print("✅ Todas las películas fueron eliminadas.")
    else:
        print("⏹️ Operación cancelada.")