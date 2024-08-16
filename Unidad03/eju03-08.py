price = input("Introduzca el precio del producto con dos decimales:  ")
print(price[:price.find(',')], 'pesos con', price[price.find(',')+1:], 'centavos.')