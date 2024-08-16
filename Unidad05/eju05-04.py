premiados = []
for i in range(6):
    premiados.append(int(input("Introduce un número ganador: ")))
premiados.sort()
print("Los números ganadores son " + str(premiados))