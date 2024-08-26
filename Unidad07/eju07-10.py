import re
filename = input("Ingrese el archivo a buscar: ")
text_file = open(filename, "r")
pattern = input("Ingrese el texto a buscar: ")
i = 0
for line in text_file:
    if re.search(pattern, line):
        print(line)
        i += 1
print (f'El archivo {filename} contiene {i} lineas que coinciden con {pattern}')