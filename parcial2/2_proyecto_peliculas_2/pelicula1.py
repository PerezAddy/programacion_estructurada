
#disct u objeto para almacenar los atributos{nombre, categoria, clasificacion, genero, idioma}
peliculas={ }

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    print("\n\t\t...oprima cualquier tecla...")
    input()

def crearPeliculas():
    borrarPantalla()
    print("\n\t...Agregar Pelicula:: \n")
    # otra forma de hacerlo  peliculas ("nombre")=input("Ingrese el nombre: ") .upper().lower()
    peliculas.update({"nombre":input("ingrese el nombre: ").upper().strip()})
    peliculas.update({"categoria":input("ingrese la categoria: ").upper().strip()})
    peliculas.update({"clasificacion":input("ingrese la clasificaion: ").upper().strip()})
    peliculas.update({"genero":input("ingrese el genero: ").upper().strip()})
    peliculas.update({"idioma":input("ingrese el idioma: ").upper().strip()})

    print("\n\t... La operacion se realizo con exito...")


def borrarpeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar o Quitar Todas las peliculas::.\n")
    resp=input("¿Desea quitar o borrar todas las peliculas del sistema?(Si/No)")
    if resp=="si":
        peliculas.clear()
        print("\n\t... La operacion se realizo con exito...")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t .::Mostrar las caracteristicas de peliculas::.\n")
    if len(peliculas)>0:
        for i in peliculas:
            print(f"\t{i} : {peliculas[i]}")
    else:
        print("\n\t ho hay peliculas el sistema")


def agregarCaracteristicasPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Caracteristicas a peliculas::.\n")
    atributo=input("ingrese la nueva caracteristicas de la pelicula: ").lower().strip()
    valor=input("ingrese el valor de la caracteristica de la pelicula: ").upper() .strip()
    #peliculas.update({atributo:valor})
    peliculas[atributo]=valor
    print("\n\t... La operacion se realizo con exito...")


def ModificarCaracteristicasPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Características de Películas ::.")
    for i in peliculas:
        print(f".::\t{(i)} : {peliculas[i]} ")
    
        atributo = input("\t\nIngresa la caracteristica a modificar: ").lower().strip()
        if atributo in peliculas:
            valor = input("\tIngresa el nuevo valor: ").upper().strip()
            peliculas[atributo] = valor
            print("\n\t\t::: ¡OPERACION EXITOSA! :::")
        else:
            print("\n\t\t::: La caracteristica no fue encontrada :::")
    else:
        print("\t .:: No hay peliculas ::.")

def ModificarCaracteristicasPeliculasDAG():
    borrarPantalla()
    print("\n\t.:: Modificar Características a Películas  ::. \n")

    if len(peliculas)>0:
        print(f"\n\tValor actuales: \n ")
        for i in peliculas:
            print(f"\t {(i)} : {peliculas[i]}")
            resp=input(f"\t¿Deseas cambiar el valor de {i}? (Si/No) ")
            if resp=="si":
                peliculas.update({f"{i}":input("\t \U0001F501 el nuevo valor: ").upper().strip()})
                print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXÍTO!  :::") 
    else:
        print("\t..:: No hay peliculas en Sistema  ::..")
        esperarTecla()

def borrarCaracteristicasPeliculas():
    borrarPantalla()

    print("\n\t.:: Borrar Caracteristicas de peliculas::.\n") 
    
    atributo =input("\tIngresa la caracteristica a borrar: ").lower().strip()
        
    del peliculas[atributo]

    print("\n\t\t::: ¡OPERACION EXITOSA! :::")

def borrarCaracteristicasPeliculas1():
    borrarPantalla()
    print("\n\t.:: Borrar una Característica de la Película ::.\n")
    
    for i, pelis in peliculas.items():
        print(f"{i} : {pelis}")
    
    confirmacion = input(f"\t¿Deseas Borar alguna Caracteristica? (Si/No) ").lower().strip()
    
    if confirmacion == "si":
        atributo = input("¿Que caracteristica quieres elimnar?").lower().strip()
        if atributo in peliculas:
                
        
                del peliculas[atributo]
                print(f"\n.:: La característica {atributo} fue eliminada con éxito.")
        else:
                print(".:: Esa característica no existe.")
        
    else:
        print("::Operación cancelada.")













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
