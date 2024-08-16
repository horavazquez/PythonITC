def ingreso(x) :
    print("Ingrese un nro")
    x = input()
    if type(x) is int:
        print("OK")
    '''if type(x) is int:
        return int(x)
    else:
        raise TypeError("Ingrese un valor numerico")
   '''
nros =[]
i = 0
while i < 2 :
    
    try:
        nros.append(ingreso(x))
    except TypeError:
        print("El valor ingresado no es un nro")
    i += 1
print(nros)
