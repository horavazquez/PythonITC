import re
ip = "216.08.094.196"
print("Direccion IP sin filtrar: ", ip)
string = re.sub(r'\.[0]*', '.', ip)
print("Direccion IP filtrada: ",string)