persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato queres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
