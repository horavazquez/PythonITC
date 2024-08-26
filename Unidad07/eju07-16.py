import csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Los nombres de las columnas son "{", ".join(row)}"')
            line_count += 1
        print(f'\t{row["name"]} trabaja en el departmento {row["department"]}, y nacio en {row["birthday month"]}.')
        line_count += 1
    print(f'Procesadas {line_count} lineas.')