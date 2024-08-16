def operar(a, b):
    return a+b
        
    
def main():
        a = int(input())
        b = 'hola'
        try:
             operar(a, b)
        except TypeError:
             print("Los tipos de datos no cuadran para hacer la operación")

main()

