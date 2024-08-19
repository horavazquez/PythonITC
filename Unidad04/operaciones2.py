def suma(a, b):
    if (type(a) == int or type (a) == float) and (type(b) == int or type (b) == float):
        return a + b
    else:
        return "TypeError"
    
def resta(a, b):
    if (type(a) == int or type (a) == float) and (type(b) == int or type (b) == float):
        return a - b
    else:
        return "TypeError"

def producto(a, b):
    if (type(a) == int or type (a) == float) and (type(b) == int or type (b) == float):
        return a * b
    else:
        return "TypeError"

def division(a, b):
    if (type(a) == int or type (a) == float) and (type(b) == int or type (b) == float):
        if b != 0:
            return a / b
        else:
            return "ZeroDivisionError"
    else:
        return "TypeError"