monedas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
moneda = input("Introduce el nombre de una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está en la lista.")