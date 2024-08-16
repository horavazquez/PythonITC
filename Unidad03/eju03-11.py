producto = input('Introduzca el nombre del producto: ')
precio = float(input('Introduzca el precio unitario: '))
unidades = int(input('Introduzca el número de unidades: '))
print('{prod}: {uni:3d} unidades x ${pr:5.2f} = ${total:8.2f}'.format(prod = producto, uni = unidades, pr = precio, total = unidades * precio))