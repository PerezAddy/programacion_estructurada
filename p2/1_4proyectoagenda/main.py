import agenda

def main():
    opcion=True
    datos=[]
    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menu_principal()#regresa el valor del return
        
        match opcion:
                case "1":
                    agenda.agregar_contacto(datos)
                    agenda.esperarTecla()
                case "2":
                    agenda.mostrar_contacto(datos)
                    agenda.esperarTecla()
                case "3":
                    agenda.buscar_contacto(datos)
                    agenda.esperarTecla()    
                case "4":
                    agenda.modificar_contacto(datos)
                    agenda.esperarTecla()    
                case "5":
                    agenda.eliminar_contacto(datos)
                    agenda.esperarTecla()    
                case "6":
                    opcion=False    
                    agenda.esperarTecla()
                    print("\n\tTerminaste la ejecucion del SW")
                case _: 
                    input("\n\tOpción invalida vuelva a intentarlo ... por favor")

if __name__ == "__main__":#siempre parte de aqui

    main()