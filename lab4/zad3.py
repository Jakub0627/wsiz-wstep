zwierzeta = []
a = int(input("Podaj liczbę zwierząt: "))
for i in range(a):
    z = input("Podaj nazwę zwierzęcia ")
    zwierzeta.append(z)
print("Lista zwierzat przed sortowaniem ")
print(zwierzeta)
zwierzeta.sort()
print("Posortowana lista zwierząt: ")
print(zwierzeta)
print("Pierwsze zwierzę na liście: ")
print(zwierzeta[0])
print("Ostatnie 3 zwierzęta: ")
print(zwierzeta[-3:]) # tutaj jest coś ważnego, koniec listy
print("Rozmiar listy wynosi:", end=" ")
print(len(zwierzeta))
