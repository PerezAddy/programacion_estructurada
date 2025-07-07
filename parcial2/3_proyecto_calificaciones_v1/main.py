#PROYECTO 3
#Crear un proyecto que permita gestionar (administrar calificaciones; colocar un menu de opciones para
#agregar, mostrar y calcular promedios de las calificaciones de los alumnos

#NOTAS
#1.- Utilizar funciones y mandar llamar desde otro archivo
#2.- Utilizar listas para almacenar el nombre de un alumno y 3 calicaciones

import calificaciones

def main():
    opcion=True
    datos=[]
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()#regresa el valor del return
        
        match opcion:
                case "1":
                    calificaciones.agregar_calificaciones(datos)
                    calificaciones.esperarTecla()
                case "2":
                    calificaciones.mostrar_calificaciones(datos)
                    calificaciones.esperarTecla()
                case "3":
                    calificaciones.calcular_promedios(datos)
                    calificaciones.esperarTecla()    
                case "4":
                    opcion=False    
                    calificaciones.esperarTecla()
                    print("\n\tTerminaste la ejecucion del SW")
                case _: 
                    input("\n\tOpción invalida vuelva a intentarlo ... por favor")

if __name__ == "__main__":#siempre parte de aqui
    main()

    