peliculas=["hola"]

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
    print(f"\n\t se borro {encontro} pelicula(s) con este titulo")