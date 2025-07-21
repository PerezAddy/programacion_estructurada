#todas las funciones 

Peliculas_1=["spiderman","conjuro","spiderman"]

#funcion para agregar peliculas
def agregarpelis():
    res="si"
    while res=="si":
        Peliculas_1.append(input("Que pelicula quiere agregar:\n"))
        res=input("Desea Agregar mas peliculas:\n").lower()#son para milusculas
    for i in Peliculas_1:
        print(f"Pelicula: {i}")

#funcion para eliminar peliculas
def eliminarpelis():
    
    for i in Peliculas_1:
        print(f"Pelicula: {i}")
    
    res="si"
    while res=="si":
        Peliculas_1.remove(input("Que pelicula quieres eliminar:\n"))
        res=input("Desea eliminar otra pelicula?:\n").lower()
    for i in Peliculas_1:
        print(f"Pelicula: {i}")


#funcion para eliminar peliculas
def actualizarpelis():
    
    for i in Peliculas_1:
        print(f"Pelicula: {i}")
    
    res="si"
    while res=="si":
        actualizar = Peliculas_1.index(input("Que pelicula quieres Actualizar:\n"))
        Peliculas_1[actualizar]=input("A que lo quieres actulizar:\n")
        res=input("Deseas Actualizar otra pelicula?:\n").lower()
    for i in Peliculas_1:
        print(f"Pelicula: {i}")

#funcion para consultar las peliculas que hay 

def mostrarpelis():
    contador=0
    
    if len(Peliculas_1)==0:
        print("no hay peliculas")
    else:
        print("Peliculas que se encuentran: ")
        for i in Peliculas_1:
            contador+=1
            
            print(f"{contador}: {i}")
        res="si" 
        res=input("quieres saber que pelicula se repite?:\n").lower()   
        while res=="si":
            veces_peli=Peliculas_1.count(input("que pelicula quires saber si se repite:\n"))
            print(f"Pelicula({i}): {veces_peli} veces se repite ")
            res=input("quieres saber que otra pelicula se repite?:\n")

#funcion para buscar las peliculas que hay 

def buscarpelis():
    palabras_bus=input("que palabra buscas:\n")
    encontro=False
    for i in range(0,len(Peliculas_1)):
        if Peliculas_1[i]==palabras_bus:
            encontro=True
    if encontro:
        print("se encontro\n")
    
        for i in Peliculas_1:
            print(f"Pelicula: {i}")
    else: 
        print("no lo encontro")

#funcion para vaciar las peliculas que hay 

def vaciarlista():
    Peliculas_1.clear()
    print("se borro todo")



