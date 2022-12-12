#Grupa 1. Użytkownik podaje 5 liczb. Zapisz do listy tylko liczby nieparzyste.
list = []
for i in range(0, 5):
    a = int(input("Podaj liczbę: "))
    if a%2 == 1:
        list.append(a)

print("Nieparzyste liczby z podanych to:")
print(list)