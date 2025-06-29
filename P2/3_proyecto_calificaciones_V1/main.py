"""Proyecto 3.
crear un proyecto que permita gestionar (Administrar) peliculas colocar un menu de opciones 
para agregar, mostrar, y calcular el promedio de calificaciones.
Notas: 1.- Utilizar Funciones y mandar llamar desde otro archivo
       2.- Utilizar listas para almacenar el nombre y 3 calificaciones de los alumnos."""

import calificaciones

def main():
    opcion = True
    datos=[]

    while opcion:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()
        
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
                opcion = False
                calificaciones.borrarPantalla()
                print("\tTerminaste la ejecución del SW")
                
            case _:
                opcion = True
                input("Opción invalida vuelva a intentarlo... por favor")
                calificaciones.esperarTecla()
                
if __name__=="__main__":
    main()

