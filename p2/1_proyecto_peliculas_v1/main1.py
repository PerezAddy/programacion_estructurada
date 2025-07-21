"""
Proyecto1.-
crear un proyecto que permita gestionar(administrar peliculas).,
colocar un menu de opciones para agregar, borrar, modificar, consultar(mostrar 
todas las peliculas que hay),buscar,vaciar peliculas y salir 

Notas:
1.-Utilizar funciones y mandar llamar desde otro archivo
2.-utiliza una lista para almacenar los nombres de las peliculas

"""
#strip sirve para quitar el espacio de las cadenas de texto
import pelicula1

opcion=True
while opcion:
    pelicula1.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n..::: \n\t\tSistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion=input("\t\t\t.::Elige una opción: ").upper()

    match opcion:
        case "1":
            pelicula1.agregarPeliculas()
            pelicula1.esperaTecla()
        case "2":
            pelicula1.eliminarPeliculas()
            pelicula1.esperaTecla()
        case "3":
            pelicula1.actualizarPeliculas()
            pelicula1.esperaTecla()
                
        case "4":
            pelicula1.consultarPeliculas() 
            pelicula1.esperaTecla()
        case "5": 
            pelicula1.buscarPeliculas()
            pelicula1.esperaTecla()
        case "6": 
            pelicula1.vaciarPelicula()
            pelicula1.esperaTecla()
        case "7":
            opcion=False
            pelicula1.esperaTecla()    
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            opcion=True
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")

