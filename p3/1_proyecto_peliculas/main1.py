"""
Proyecto1.-
crear un proyecto que permita gestionar(administrar peliculas).,
colocar un menu de opciones para agregar, borrar, modificar, consultar(mostrar 
todas las peliculas que hay),buscar  y salir de peliculas 

Notas:
1.-Utilizar funciones y mandar llamar desde otro archivo
2.-utiliza una dict para almacenar los atributos o caracteristicas de las peliculas(nombre, categoria, clasificacion)
3.-utilizar y impleentar una base de datos relacional en MySQL
"""
#strip sirve para quitar el espacio de las cadenas de texto
import pelicula1

opcion=True
while opcion:
    pelicula1.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n..::: " \
    "\n\t\tSistema de Gestión de Peliculas :::...\n 1.- crear " \
    " \n 2.- Borrar \n 3.- Mostrar \n 4.- Buscar " \
    "\n 5.- Modificar  \n 6.- SALIR ")
    opcion=input("\t\t\t.::Elige una opción: ").upper()

    match opcion:
        case "1":
            pelicula1.crearPeliculas()
            pelicula1.esperarTecla()
        case "2":
            pelicula1.borrarPeliculas()
            pelicula1.esperarTecla()
        case "3":
            pelicula1.mostrarPeliculas()
            pelicula1.esperarTecla()
                
        case "4":
            pelicula1.buscarPeliculas()
            pelicula1.esperarTecla()
        case "5": 
            pelicula1.modificarPeliculas()
            pelicula1.esperarTecla()
        case "6":
            opcion=False
            pelicula1.esperarTecla()    
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            opcion=True
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")

