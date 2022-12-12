import random
punkty = []
for i in range(15):
    punkty.append(round(random.uniform(0, 50), 2))
print("Punkty uzyskane przez studentów: ")
print(punkty)

# najmniejsza liczba punktów
pomoc = 50
for i in range(len(punkty)):
    if punkty[i] < pomoc:
        pomoc = punkty[i]
print("Najmniejsza liczba uzyskanych punktów to:", end=" ")
print(pomoc)
print(min(punkty))  # lepsza opcja


# największa liczba punktów
pomoc = 0
for i in range(len(punkty)):
    if punkty[i] > pomoc:
        pomoc = punkty[i]
print("Największa liczba uzyskanych punktów to:", end=" ")
print(pomoc)
print(max(punkty))  # lepsza opcja

# podpunkt 2 - wyłapanie indeksu pierwszego wystąpienia podanej wartości
wartosc = float(input("Podaj wartość punktową: "))

try:
    print(punkty.index(wartosc))
except:  # powinienem określić błąd chyba, bo nie łapie co jest nie tak
    print("Takiej wartości nie ma na liśćie. ")

# na zajęciach poprawną metodą było sprawdzenie czy element jest w liście i dopiero wtedy wyszukiwanie

# średnia
srednia = 0
for i in range(len(punkty)):
    srednia = srednia + punkty[i]

srednia = srednia/15
print("Srednia wynosi:", end=" ")
print(round(srednia, 2))

# liczba ludzi powyżej średniej

nop = 0
for i in range(len(punkty)):
    if punkty[i] > srednia:
        nop += 1
print("Ilosc osob z wynikiem powyzej sredniej:", end=" ")
print(nop)

# lista punktów powyżej średniej

above = []
for i in range(len(punkty)):
    if punkty[i] > srednia:
        above.append(punkty[i])

print("Lista punktow powyzej sredniej:", end=" ")
print(above)

# lista punktów ponizej średniej

under = []
for i in range(len(punkty)):
    if punkty[i] < srednia:
        under.append(punkty[i])


'''
alternatywny wariant z zajęć:
under = [p for p in punkty if p < srednia]
'''

print("Lista punktow poniej sredniej:", end=" ")
print(under)


