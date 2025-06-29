"""
Crear un programa que calcule e imprima la tabla de multiplicar del 2

Restricciones
1._Sin estructuras de control
2.-Sin funciones
"""

num=int(input("\n\t----Introducir el numero a multiplicar:")) 

multi=num*1
print(f"\n\t----{num}x1:{multi}")
multi=num*2
print(f"\n\t----{num}x2:{multi}")
multi=num*3
print(f"\n\t----{num}x3:{multi}")
multi=num*4
print(f"\n\t----{num}x4:{multi}")
multi=num*5
print(f"\n\t----{num}x5:{multi}")
multi=num*6
print(f"\n\t----{num}x6:{multi}")
multi=num*7
print(f"\n\t----{num}x7:{multi}")
multi=num*8
print(f"\n\t----{num}x8:{multi}")
multi=num*9
print(f"\n\t----{num}x9:{multi}")
multi=num*10
print(f"\n\t----{num}x10:{multi}")


#version 2
"""
Crear un programa que calcule e imprima la tabla de multiplicar del 2

Restricciones
1.-Con estructuras de control
2.-Sin funciones
"""

num=int(input("\n\t----Introducir el numero a multiplicar:"))
for i in range(1,11):
    multi=num+1
    print(f"{num}x{i}={multi}")


#version 3
"""
Crear un programa que calcule e imprima la tabla de multiplicar del 2

Restricciones
1.-Con estructuras de control
2.-Con funciones   
"""

def tabla (numero):
    num = numero
    respuesta = ""
    for i in range (1,11):
        multi = num * i
        respuesta += f"\t{num} x {i} = {multi}\n"

    return respuesta

num = int(input("Ingrese el numero de la tabla de multiplicar: "))
resultado = tabla(num)
print (f"{resultado}")