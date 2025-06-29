""" 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

import os
os.system("cls")

"""paises=["Mexico","Brasil","España","Canada"]
print(paises)
paises={"Mexico","Brasil","España","Canada","Canada"}
print(paises)

varios={True,"Cadena",23,3.1516}
print(varios)

paises.add("México")
print(paises)

varios.pop()
print(varios)

varios.remove("Cadena")
print(varios)
"""
"""Tarea
Ejemplo crear un programa que soliciete los emal de los alumnos de la utd alacenar en una lista y posteriormente mostrar en pantalla los enamil sin duplicados"""

email=[]
resp="si"

while resp=="si":
  email.append(input("Escribe tu Email"))
  resp==input("¿Quiere agregar otra dirreccion de Email?").lower()


email_set=set(email)
email=list(email_set)
print(email)