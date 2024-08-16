age = int(input("Introduzca su edad: "))
# Decisión del precio en función de la edad
if age < 4:
    price = 0
elif age <= 18:
    price = 4
else:
    price = 10
# Mostrar precio
print(f'El precio de la entrada es ${price}.')