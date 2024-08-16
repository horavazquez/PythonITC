age = int(input("Ingrese su edad "))
income = float(input("Ingrese los ingresos mensuales?"))
if age > 16 and income >= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")