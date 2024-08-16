lista = [1, 2, 3, 4]

n = int(input("Ingrese la posicion a la que desea acceder: "))
try:
    lista[n]
except IndexError:
    print('Intenta acceder una posición que no está en el arreglo:')
else:
    print(f'El valor de la posicion {n} de la lista es: {lista[n]}')