monedas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
moneda = input("Introduce el nombre de una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está en la lista."))