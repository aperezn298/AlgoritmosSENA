# agenda = {}

# # Funcion para agregar un nuevo contacto a la agenda
# def agregar_contacto(nombre, telefono, ubicacion):
#     if telefono in agenda:
#         print("Contacto ya existe en la agenda.")
#     else:
#         datos = [nombre, telefono, ubicacion]
#         agenda[telefono] = datos
#         print("Contacto agregado con exito.")
        

# # Funcion para listar todos los contactos en la agenda
# def listar_contactos():
#     cont = 1
#     if len(agenda) == 0:
#         print("No hay contactos en la agenda.")
#     else:
#         print("Lista de contactos:")
#         for valor in agenda.values():
#             print(f"Usuario {cont} => {valor[0]}, telefono: {valor[1]}, ubicacion: {valor[2]}")
#             cont += 1

# # Funcion para buscar un contacto en la agenda y modificar su numero de telefono
# def modificar_contacto(clave, nombre, telefono, ubicacion):
#     if clave in agenda:
#         del agenda[clave]
#         datos = [nombre, telefono, ubicacion]
#         agenda[telefono] = datos
#         print("Contacto modificado con exito.")
#     else:
#         print("El contacto no se encontro en la agenda.")

# # Funcion para eliminar un contacto de la agenda
# def eliminar_contacto(telefono):
#     if telefono in agenda:
#         del agenda[telefono]
#         print("Contacto eliminado con exito.")
#     else:
#         print("El contacto no se encontro en la agenda.")

# # Menu principal y opciones del menu
# while True:
#     print("\nBienvenido a la agenda telefonica.")
#     print("Seleccione una opcion:")
#     print("1. Agregar un nuevo contacto")
#     print("2. Listar todos los contactos")
#     print("3. Modificar un contacto existente")
#     print("4. Eliminar un contacto existente")
#     print("5. Salir")
#     opcion = int(input("Opcion seleccionada: "))
    
#     if opcion == 1:
#         nombre = input("Ingrese el nombre del nuevo contacto: ")
#         telefono = input("Ingrese el numero de telefono del nuevo contacto: ")
#         ubicacion = input("Ingrese la ubicacion del nuevo contacto: ")
#         agregar_contacto(nombre, telefono, ubicacion)
        
#     elif opcion == 2:
#         listar_contactos()
        
#     elif opcion == 3:
#         clave = input("Ingrese el numero de telefono del contacto que desea modificar: ")
#         print()
#         nombre = input("Ingrese el nuevo nombre del contacto: ")
#         telefono = input("Ingrese el nuevo telefono del contacto: ")
#         ubicacion = input("Ingrese la nueva ubicacion del contacto: ")
#         modificar_contacto(clave, nombre, telefono, ubicacion)
        
#     elif opcion == 4:
#         telefono = input("Ingrese el numero de telefono del contacto que desea eliminar: ")
#         eliminar_contacto(telefono)
        
#     elif opcion == 5:
#         print("Gracias por utilizar la agenda telefonica. ¡Hasta pronto!")
#         break
        
#     else:
#         print("Opcion invalida. Por favor seleccione una opcion valida.")


agenda = {}   

while True:
    print("\nBienvenido a la agenda telefonica.")
    print("Seleccione una opcion:")
    print("1. Agregar un nuevo contacto")
    print("2. Listar todos los contactos")
    print("3. Modificar un contacto existente")
    print("4. Eliminar un contacto existente")
    print("5. Salir")
    opcion = int(input("Opcion seleccionada: "))
    
    if opcion == 1:
        nombre = input("Ingrese el nombre del nuevo contacto: ")
        telefono = input("Ingrese el numero de telefono del nuevo contacto: ")
        ubicacion = input("Ingrese la ubicacion del nuevo contacto: ")
        if telefono in agenda:
            print("Contacto ya existe en la agenda.")
        else:
            datos = [nombre, telefono, ubicacion]
            agenda[telefono] = datos
            print("Contacto agregado con exito.")
        
    elif opcion == 2:
        cont = 1
        if len(agenda) == 0:
            print("No hay contactos en la agenda.")
        else:
            print("Lista de contactos:")
            for valor in agenda.values():
                print(f"Usuario {cont} => {valor[0]}, telefono: {valor[1]}, ubicacion: {valor[2]}")
                cont += 1

        
    elif opcion == 3:
        clave = input("Ingrese el numero de telefono del contacto que desea modificar: ")
        print()
        nombre = input("Ingrese el nuevo nombre del contacto: ")
        telefono = input("Ingrese el nuevo telefono del contacto: ")
        ubicacion = input("Ingrese la nueva ubicacion del contacto: ")
        if clave in agenda:
            del agenda[clave]
            datos = [nombre, telefono, ubicacion]
            agenda[telefono] = datos
            print("Contacto modificado con exito.")
        else:
            print("El contacto no se encontro en la agenda.")
        
    elif opcion == 4:
        telefono = input("Ingrese el numero de telefono del contacto que desea eliminar: ")
        if telefono in agenda:
            del agenda[telefono]
            print("Contacto eliminado con exito.")
        else:
            print("El contacto no se encontro en la agenda.")
        
    elif opcion == 5:
        print("Gracias por utilizar la agenda telefonica. ¡Hasta pronto!")
        break
        
    else:
        print("Opcion invalida. Por favor seleccione una opcion valida.")