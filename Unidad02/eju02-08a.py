name = input("Ingrese su nombre ")
gender = input("Ingrese su sexo (M o F) ")
if gender == "F":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)