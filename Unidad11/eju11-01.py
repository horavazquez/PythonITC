array = []

for i in range(6):
    
    while True:
        try:
            array.append(int(input("Introduce el número de índice "+ str(i)+": ")))
            break  
        except:
            print("No has introducido un número entero. Inténtalo de nuevo.")

print("El número maximo introducido es el " + str(max(array)))