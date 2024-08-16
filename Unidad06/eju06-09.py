facturas = {}
cobrado = 0
pendiente = 0
menu = ''
while menu != 'T':
    if menu == 'A':
        clave = input('Introduce el número de la factura: ')
        costo = float(input('Introduce el costo de la factura: '))
        facturas[clave] = costo
        pendiente += costo
    if menu == 'P':
        clave = input('Introduce el número de la factura a pagar: ')
        costo = facturas.pop(clave, 0)
        cobrado += costo
        pendiente -= costo
    print('Recaudado:', cobrado)
    print('Pendiente de cobro: ', pendiente)
    menu = input('¿Desea añadir una nueva factura (A), pagarla (P) o terminar (T)? ')
