name = input("Ingrese su nombre ")
gender = input("Ingrese su sexo (M o F) ")
if (gender == "F" and name.lower() < 'm') or (gender == "M" and name.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)