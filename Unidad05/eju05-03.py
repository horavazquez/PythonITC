asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = input("Qué nota sacaste en " + asignatura + "?")
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " sacaste " + notas[i])