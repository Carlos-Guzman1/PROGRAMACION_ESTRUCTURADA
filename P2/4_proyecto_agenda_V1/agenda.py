def borrarPantalla():
    import os
    os.system("cls")
    
def esperarTecla():
    input("Presione una tecla para continuar...")

def agregar_contacto(agenda):
    resp = True
    while resp: 
        borrarPantalla()
        print("\t\t\t.::: Agregar Contacto :::.")
        print("=" * 60)
        nombre = input("\t\tIngrese el nombre del contacto: ").upper().strip()
        if nombre == "":
            print("=" * 60)
            print("\t\t\t::: El nombre no puede estar vacio :::")
            opc = input("\n\tDesea volver a intentarlo (SI/NO)?: ").upper().strip()
            if opc == "NO":
                resp = False
        else:
            if nombre in agenda:
                print("Ya existe")
                resp = input("Desea volver a intentarlo (SI/NO)?: ").upper().strip()
            else:
                tel=input("Telefono: ").upper().strip()
                email=input("Email: ").upper().strip()
                if tel == "" or email == "":
                    print("=" * 60)
                    print("\t\t\t::: El Telefono y/o el Email no pueden estar vacios :::")
                    opc = input("\n\tDesea volver a intentarlo (SI/NO)?: ").upper().strip()
                    if opc != "SI":
                        resp = False
                else:
                    agenda[nombre] = [tel, email]
                    print("=" * 60)
                    print("Accion realizada con Exito")
                    resp = False
        
def mostrar_contactos(agenda):
    borrarPantalla()
    if not agenda:
        print("=" * 60)
        print(f"\t\tNo hay contactos")
        print("=" * 60)
    else:
        print("\t\t\t.::: Agenda :::.")
        print(f"{"Nombre":<15} {"Telefono":<15} {"Email":<15}")
        print("=" * 60)
        for nombre in agenda:
            tel, email = agenda[nombre]
            print(f"{nombre:<15} {tel:<15} {email:<15}")
        print("=" * 60)
        
def buscar_contacto(agenda):
    borrarPantalla()
    buscar = input("Ingrese el nombre del contacto a buscar: ").upper().strip()
    if buscar in agenda:
        persona = agenda[buscar]
        print("=" * 60)
        print(f"{"Nombre":<15} {"Telefono":<15} {"Email":<15}")
        print(f"{buscar:<15} {persona[0]:<15} {persona[1]:<15}")
        print("=" * 60)
    else:
        print("=" * 60)
        print("No existe el contacto... Vuelva a intentarlo por favor")
        
def modificar_contacto(agenda):
    borrarPantalla()
    print("\n\t.:: Modificar Característica de un contacto ::.\n")
    print(f"{"Nombre":<15} {"Telefono":<15} {"Email":<15}")
    print("=" * 60)
    for nombre in agenda:
        tel, email = agenda[nombre]
        print(f"{nombre:<15} {tel:<15} {email:<15}")
    print("=" * 60)
    buscar = input("Ingrese el nombre de la persona que quiere modificar: ").upper().strip()
    
    if buscar in agenda:
        persona = agenda[buscar]
        print(f"\n\t.:: Los datos de {buscar} son: ::.\n")
        print(f"\n\t\tTelefono: {persona[0]}")
        print(f"\n\t\tEmail: {persona[1]}")
        
        dato = input("\nIngresa el nombre de la característica que deseas modificar (Telefono/Email): ").upper().strip()
        
        if dato == "TELEFONO":
            resp = True
            while resp:
                nuevo_valor = input("Ingresa el nuevo numero telefonico: ").upper().strip()
                if nuevo_valor == "":
                    print("\n\tEl Telefono no puede estar vacio")
                else:
                    persona[0] = nuevo_valor
                    print("La operacion se realizo con exito")
                    resp = False
        elif dato == "EMAIL":
            resp = True
            while resp:
                nuevo_valor = input("Ingresa el nuevo email: ").upper().strip()
                if nuevo_valor == "":
                    print("\n\tEl Email no puede estar vacio")
                else:
                    persona[1] = nuevo_valor
                    print("=" * 60)
                    print("La operacion se realizo con exito")
                    resp = False
        else:
            print("\n\t\t::: La característica no existe :::")
    else:
        print("=" * 60)
        print("\t..:: No esta esa persona en la agenda ::..")
    
def borrar_contacto(agenda):
    borrarPantalla()
    buscar = input("Ingrese el nombre del contacto que desea borrar: ").upper().strip()
    if buscar in agenda:
        resp = input(f"Se encontro a {buscar}, deseas eliminarla de la agenda (Si/No)?: ").upper().strip()
        if resp == "SI":
            del agenda[buscar]
        print("=" * 60)
        print("La operacion se realizo con exito")
    else:
        print("=" * 60)
        print("No existe el contacto... Vuelva a intentarlo por favor")
