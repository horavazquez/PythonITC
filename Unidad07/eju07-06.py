def consultar_telefono(arch, nombre):
    f = open(arch, 'r')
    lista = f.readlines()
    f.close()
    for linea in lista:
        cli, tel = linea.split(',')
        if nombre == cli:
           return client
    return "El cliente no existe"

def agregar_telefono(arch, nombre, tel):
    return msg

def eliminar_telefono(arch, nombre):
    return msg

def crear_agenda(arch):
    import os
    if os.path.isfile(arch):
        if input("La agenda ya existe, Desea sobreescribirla? (S/N) ") =="N":
            msg = "La agenda ya existe y no fue sobreescrita"
        else:
            f = open("listado.txt",'w')
            f.close()
            msg = "La agenda fue sobreescrita"    
    else:
        f = open("listado.txt",'w')
        f.close()
        msg = "La agenda se creo con exito"
    return msg

def menu():
    print("Gestor de agenda telefonica")
    print("---------------------------")
    print("1 - Consultar un telefono")
    print("2 - Agregar un telefono")
    print("3 - Borrar un telefono")
    print("4 - Crear la agenda")
    print("0 - Finalizar")
    opcion = input("Ingrese la opcion deseada: ")
    return opcion


def principal():
    arch = "listado.txt"
    opcion = menu()
    while opcion != 0
        if opcion == '1':
            nombre = input("Ingrese el nombre del cliente: ")
            print(consultar_telefono(nombre))
        elif opcion == '2':
            nombre = input("Ingrese el nombre del cliente: ")
            tel = input("Ingrese el telefono del cliente: ")
            print(agregar_telefono(nombre,tel))
        elif opcion == '3':
            nombre = input("Ingrese el nombre del cliente: ")
            print(eliminar_telefono(nombre))
        elif opcion == '4':
            print(crear_agenda(arch))
        elif opcion == '4':
            print("Desea Salir (S/N) ")
            if input() == 'S':
                break
        else:
            print("Opcion invalida")     
        opcion = menu()
