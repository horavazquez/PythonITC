from operaciones2 import *

a, b, c, d = (10, 5, 0, "Hola")

print("\nSUMA:")
if suma(a,b) != "TypeError":
    print( "{} + {} = {}".format(a, b, suma(a, b) ) )
else:
    print("El tipo de dato ingresado no es valido \n")

print("\nRESTA:")
if resta(b,d) != "TypeError":
    print( "{} - {} = {}".format(b, d, resta(b, d) ) )
else:    
    print("El tipo de dato ingresado no es valido \n")

print("\nPRODUCTO:")
if producto(b,b) != "TypeError":
    print( "{} * {} = {}".format(b, b, producto(b, b) ) )
else:    
    print("El tipo de dato ingresado no es valido \n")

print("\nDIVISION:")
if division(a,c) != "TypeError" and division(a,c) != "ZeroDivisionError" :
    print( "{} * {} = {}".format(a, c, division(a, c) ) )
else:    
    if division(a,c) == "TypeError":
        print("El tipo de dato ingresado no es valido \n")
    else:
        print("No es posible dividir por cero \n")