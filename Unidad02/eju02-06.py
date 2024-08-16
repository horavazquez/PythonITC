# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.")
print("Listado de pizzas")
print("\t 1 - Vegetariana")
print("\t 2 - No vegetariana")
print()
tipo = int(input("Introduzca el número correspondiente a la pizza que quiera: "))
if tipo >=1 and tipo <=2:
# Decisión sobre el tipo de pizza
    if tipo == 1:
        print("Ingredientes de pizzas vegetarianas")
        print("\t 1 - Pimiento")
        print("\t 2 - Tofu")
        print()
        ingrediente = int(input("Introduzca el ingrediente que desee: "))
        
        if ingrediente >= 1 and ingrediente <=2:
            print("Pizza vegetariana con mozzarella, tomate y ", end="")
            if ingrediente == 1:
                print("pimiento")
            else: 
                print("tofu")
        else:
            print("Ingreso un numero invalido de ingrediente")
    else:
        print("Ingredientes de pizzas no vegetarianas")
        print("\t 1 - Peperoni")
        print("\t 2 - Jamón")
        print("\t 3 - Salmón")
        print()
        ingrediente = int(input("Introduzca el ingrediente que desee: "))
        if ingrediente >= 1 and ingrediente <=3:
            print("Pizza no vegetarina con mozarrella, tomate y ", end="")
            if ingrediente == "1":
                print("peperoni")
            elif ingrediente == "2":
                print("jamón")
            else:
                print("salmón")
        else:
            print("Ingreso un numero invalido de Ingrediente")
else:
    print("Ingreso un numero invalido de Tipo de pizza")