"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("cls")


pais={
      "nombre":"México", 
      "capital":"CDMX", 
      "poblacion":"1200000",
      "idioma":"Español",
      "status":True,
      }

pais2={
      "nombre":"Brasil", 
      "capital":"CDMX", 
      "poblacion":"1250000",
      "idioma":"Portugues",
      "status":True,
      }

pais3={
  "nombre":"Canada", 
      "capital":"Otawua", 
      "poblacion":"500000",
      "idioma":{"ingles","frances"},
      "status":True,
      }


#Funciones u Operaciones con los diccionarios u objetos

#print(pais)

"""for i in pais:
  print (f"{i}={pais[i]}")
  
#agregar un atribujo a un objeto
  
pais ["altitud"]=3000
for i in pais:
  print (f"{i}={pais[i]}")  
"""
#quitar atributo en particular
pais.pop("status")
for i in pais:
  print (f"{i}={pais[i]}")  