import mysql.connector
from mysql.connector import Error

#disct u objeto para almacenar los atributos{nombre, categoria, clasificacion, genero, idioma}



pelicula = {}

def borrarPantalla():
    import os
    os.system("cls")  # Usa "cls" para Windows

def esperarTecla():
    input("\n\t\t... Oprima cualquier tecla para continuar ...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error que se presentó es: {e}")
        return None

def crearPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t.:: Crear Películas ::. \n")
        pelicula["nombre"] = input("Ingresa el nombre: ").upper().strip()
        pelicula["categoria"] = input("Ingresa la categoría: ").upper().strip()
        pelicula["clasificacion"] = input("Ingresa la clasificación: ").upper().strip()
        pelicula["genero"] = input("Ingresa el género: ").upper().strip()
        pelicula["idioma"] = input("Ingresa el idioma: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
        val = (
            pelicula["nombre"],
            pelicula["categoria"],
            pelicula["clasificacion"],
            pelicula["genero"],
            pelicula["idioma"]
        )
        cursor.execute(sql, val)
        conexionBD.commit()
        print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t.:: Mostrar las Películas ::. \n")
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas"
        cursor.execute(sql)
        registros = cursor.fetchall()
        if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print("-" * 80)
            for pelis in registros:
                print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
            print("-" * 80)
        else:
            print("\t .:: No hay películas en el sistema ::.")

def buscarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t.:: Buscar Películas ::. \n")
        nombre = input("Ingresa el nombre de la película a buscar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas WHERE nombre=%s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print("-" * 80)
            for pelis in registros:
                print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
            print("-" * 80)
        else:   
            print("\t .:: Películas no encontradas en el sistema ::.")
def borrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t.:: Borrar Películas ::. \n")
        nombre=input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()
        cursor=conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("Mostrar las Peliculas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
        for pelis in registros:
            print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
            print(f"-"*80) 
            resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): ").lower().strip()
        if resp=="si":
            sql="delete from peliculas where nombre = %s"
            val=(nombre,)
            cursor.execute(sql,val)
            conexionBD.commit()
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")
        else:
            print("\t .:: peliculas no encontradas en el sistema ::..")












































# El bloque de código proporcionado parece ser una versión alternativa de algunas funciones ya presentes en tu archivo.
# Para "acomodarlo bien", lo presento limpio, sin comentarios innecesarios, y adaptado para que puedas copiarlo y usarlo directamente si lo deseas.


