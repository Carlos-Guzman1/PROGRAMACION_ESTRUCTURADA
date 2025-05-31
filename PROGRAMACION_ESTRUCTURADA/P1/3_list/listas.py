import os
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
os.system("cls")

numeros = [100, 34]
print(numeros)

variable = "["
for i in numeros:
    variable += f"{i} "
print(f"{variable}]")

variable = "["
for i in range(0, len(numeros)):
    variable += f"{i} "
print(f"{variable}]")


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

os.system("cls")

palabras = ["UTD", "2023", "logo", "TI", "2C clasica"]
print(palabras)
palabra_buscar = input ("Dame la palabra a buscar en la lista: ")

palabra_buscar in palabras

#1er forma
"""
if palabra_buscar in palabras:
    print("Si encontro la palabra en la lista")
else:
    print("No encontro la palabra en la lista")
"""

#2da forma
#Ejemplo 3 Añadir elementos a la lista
#["UTD", "2023", "logo", "TI", "2C clasica"]
"""
encontro = False

for i in palabras:
    if  i == palabra_buscar:
        encontro = True
        
if encontro:
    print("Si encontro la palabra en la lista")
else:
    print("No encontro la palabra en la lista")

#3er forma
encontro = False

for i in range(0, len(palabras)):
    if  palabras[i] == palabra_buscar:
        encontro = True
        
if encontro:
    print("Si encontro la palabra en la lista")
else:
    print("No encontro la palabra en la lista")
"""


#Ejemplo 4 Crear una lista multidimencional para almacenar los nombres y telefonos de unos contactos "Agenda"

agenda = [
            ["Carlos", "6181234567"],
            ["Carlos v", "6181234568"],
            ["Carlos vi", "6181234569"]
         ]

print(agenda)
lista = 0
for i in agenda:
    print(i)

for r in range(0, 3):
    for c in range(0,2):
        print(agenda [r] [c])

for r in range(0, 3):
    for c in range(0,2):
        lista += f"{agenda [r] [c]}, "
    lista += "\n"
print(lista)
