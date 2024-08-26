import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Las nombres de las Columnas son "{", ".join(row)}"')
            line_count += 1
        else:
            print(f'\t{row[0]} trabaja en el departmento {row[1]}, y nacio en {row[2]}.')
            line_count += 1
    print(f'Procesadas {line_count} lineas.')