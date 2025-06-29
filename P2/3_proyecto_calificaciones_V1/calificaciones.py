
"""lista=[
        ["Ruben", 10.0,8.9,9.2],
        ["Andres", 10.0,10.0,10.0],
        ["Maria", 10.0,10.0,10.0]

      ]"""


def borrarPantalla():
    import os
    os.system("cls")
    
def esperarTecla():
    input("Oprima cualquier tecla para continuar")

def menu_principal():
        print("Sistema de Gestión de Calificaciones " \
        "\n1.- Agregar " \
        "\n2.- Mostrar " \
        "\n3.- Cálcular Promedios " \
        "\n4.- SALIR")
        opcion = input("Elige una opción (1-4): ")
        return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print(".::Agregar Calificaciones::.")
    nombre = input("Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1,4):
        bandera = True
        while bandera:
            try:
                cal = float(input(f"Calificación {i}: "))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    bandera = False
                else:
                    print("Ingrese un valor comprendido entre 0 y 10")
            except ValueError:
                print("Ingrese un valor numerico")
    lista.append([nombre] + calificaciones)
    print("Acción realizada con éxito")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\t\t.::Mostrar Calificaciones::.")
    if len(lista) > 0:
        print(f"{"Nombre":<15} {"Cali.1":<10} {"Cali.2":<10} {"Cali.3":<10}")
        print("=" * 60)
        for fila in lista:
            print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10}")
        print("=" * 60)
        print(f"Son {len(lista)} alumnos")
    else:
        print("No hay calificaciones en el sistema")

def calcular_promedios(lista):
    borrarPantalla()
    print("\t.::Promedios de Alumnos::.")
    if len(lista) > 0:
        print(f"{"Nombre":<15} {"Promedio":<10}")
        print("=" * 60)
        for fila in lista:
            promedio = (fila[1] + fila[2] + fila[3]) / 3
            print(f"{fila [0]:<15} {promedio:<10:.2f}")
        print("=" * 60)
        suma_total = sum((fila[1] + fila[2] + fila[3]) for fila in lista)
        promedio_general = suma_total / (len(lista) * 3)
        print(f"Promedio general: {promedio_general:.2f}")
        print("=" * 60)
        print(f"Son {len(lista)} alumnos")
    else:
        print("No hay calificaciones en el sistema")
        