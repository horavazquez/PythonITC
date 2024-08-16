def main():
    dict = {'Arles': 'Java', 'Dennis' : 'C', 'Das':'Python'}
    try:
        print(dict['Ada'])
    except KeyError:
        print("Intenta acceder una llave que no se encuentra en el diccionario")
    
main()

