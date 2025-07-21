import peliculas

peliculas1=True
while peliculas1: 
    
    peliculas1=input("Que opcion quieres hacer(agregar, borrar, modificar, consultar, bucar, vaciar y salir) :\n ").lower()

    match peliculas1:
    
        case "agregar":
            
            peliculas.agregarpelis()
        
        case "borrar":
            peliculas.eliminarpelis()
    
        case "modificar":
            peliculas.actualizarpelis() 
    
        case "consultar":
            peliculas.mostrarpelis()
        
        case "buscar":
            peliculas.buscarpelis()
    
        case "vaciar":
            peliculas.vaciarlista()
    
        case "salir":
            peliculas1=False    
            print("Terminaste la ejecucion del SW")
    
        case _: 
            input("Opción invalida vuelva a intentarlo ... por favor")