asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobadas = []
for asignatura in asignaturas:
    nota = float(input("Qué nota sacaste en " + asignatura + "?"))
    if nota >= 5:
        aprobadas.append(asignatura)
for asignatura in aprobadas:
    asignaturas.remove(asignatura)
print("Tenes que repetir " + str(sorted(asignaturas)))