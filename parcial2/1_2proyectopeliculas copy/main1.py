"""
Proyecto1.-
crear un proyecto que permita gestionar(administrar peliculas).,
colocar un menu de opciones para agregar, borrar, modificar, consultar(mostrar 
todas las peliculas que hay),buscar,vaciar peliculas y salir 

Notas:
1.-Utilizar funciones y mandar llamar desde otro archivo
2.-utiliza una dict para almacenar los atributos o caracteristicas de las peliculas(nombre, categoria, clasificacion)

"""
#strip sirve para quitar el espacio de las cadenas de texto
import pelicula1

opcion=True
while opcion:
    pelicula1.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n..::: " \
    "\n\t\tSistema de Gestión de Peliculas :::...\n 1.- crear " \
    " \n 2.- Borrar \n 3.- Mostrar \n 4.- Agregar Caracteristicas " \
    "\n 5.- Modificar Caracteristicas \n 6.- Borrar Caracteristicas \n 7.- SALIR ")
    opcion=input("\t\t\t.::Elige una opción: ").upper()

    match opcion:
        case "1":
            pelicula1.crearPeliculas()
            pelicula1.esperarTecla()
        case "2":
            pelicula1.borrarpeliculas()
            pelicula1.esperarTecla()
        case "3":
            pelicula1.mostrarPeliculas()
            pelicula1.esperarTecla()
                
        case "4":
            pelicula1.agregarCaracteristicasPeliculas()
            pelicula1.esperarTecla()
        case "5": 
            pelicula1.ModificarCaracteristicasPeliculasDAG()
            pelicula1.esperarTecla()
        case "6": 
            pelicula1.borrarCaracteristicasPeliculas1()
            pelicula1.esperarTecla()
        case "7":
            opcion=False
            pelicula1.esperarTecla()    
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            opcion=True
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")

