from operaciones import *

a, b, c, d = (10, 5, 0, "Hola")

print("\nSUMA:")
try:
    print( "{} + {} = {}".format(a, d, suma(a, d) ) )
except TypeError as e:
    print("El tipo de dato ingresado no es valido \n###",e, "###")

print("\nRESTA:")
try:
    print( "{} - {} = {}".format(b, a, resta(b, a) ) )
except TypeError as e:    
    print("El tipo de dato ingresado no es valido \n###",e, "###")

print("\nPRODUCTO:")
try:
    print( "{} * {} = {}".format(b, d, producto(b, d) ) )
except TypeError as e:    
    print("El tipo de dato ingresado no es valido \n###",e, "###")


#print( "{} / {} = {}".format(a, c, division(a, c) ) )