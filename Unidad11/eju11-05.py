agenda = {}

def process_numbers(person, number):
    if len(str(number)) <20:
        agenda[person] = number
    else:
        raise Exception("Ingreso un nro telefonico >20 digitos")    

def main():
    n = int(input('Digite el número de contactos:'))
    print('Agregando ' + str(n) + ' personas...')
    for i in range(n):
        nombre = input('Digite el nombre del contacto {}:'.format(i+1))
        numero = int(input('Digite el número de contacto {}:'.format(i+1)))
        try:
            process_numbers(nombre, numero)
        except Exception as e:
            print(e.args[0])
    print('Así va la agenda:' + str(agenda))

main()
    