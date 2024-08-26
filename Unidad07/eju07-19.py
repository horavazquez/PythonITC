import csv

with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['name', 'department', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'John Smith', 'department': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'name': 'Erica Meyers', 'department': 'IT', 'birth_month': 'March'})
    writer.writerow({'name': 'Jane Smooth', 'department': 'Sales', 'birth_month': 'July'})