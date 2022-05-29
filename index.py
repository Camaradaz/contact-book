agenda = {}

while True:
    print("\t Menú ")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Elija una opción del menú: "))

    print()

    if opcion == 1:
        nombre = input("Nombre del contacto: ")
        telefono = input("Numero de telefono: ")

        if telefono not in agenda:
            agenda[telefono] = telefono 
            print("Contacto agregado")
        else:
            print("Ese contacto ya existe")

    elif opcion == 2:
        nombre = input("Nombre del contacto a borrar: ")

        if nombre in agenda:
            del(agenda[nombre])
            print("Contacto eliminado")
        else:
            print("Contacto no existente")

    elif opcion == 3:
        print("Contactos agregados")
        for clave,valor in agenda.items:
            print(f"Nombre: {clave}, Telefono: {valor}")
    
    elif opcion == 4:
        print("Gracias por utilizar la agenda")
        break
    
    else:
        print("Se equivocó de opción de menú")

    print()



