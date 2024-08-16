clientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        cuit = input('Introduce CUIT del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        telefono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
        clientes[cuit] = cliente
    if opcion == '2':
        cuit = input('Introduce CUIT del cliente: ')
        if cuit in clientes:
            del clientes[cuit]
        else:
            print('No existe el cliente con el CUIT', cuit)
    if opcion == '3':
        cuit = input('Introduce CUIT del cliente: ')
        if cuit in clientes:
            print('cuit:', cuit)
            for clave, valor in clientes[cuit].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el CUIT', cuit)
    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')