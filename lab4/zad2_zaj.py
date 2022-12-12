import random
a = int(input("Podaj liczbę: "))
zestaw_1 = []
zestaw_1 = [random.randint(1, 10) for f in range(a)]
print(zestaw_1)

a = int(input("Podaj liczbę: "))
zestaw_2 = []
zestaw_2 = [random.randint(5, 15) for g in range(a)]
print(zestaw_2)

a = int(input("Podaj liczbę całkowitą, a program powie Ci o przynależności do zestawów. "))

if a in zestaw_1:
    print("Ta liczba należy do zestawu 1.")
elif a in zestaw_2:
    print("Ta liczba należy do zestawu 2")
else:
    print("Ta liczba nie należy do obu zestawów.")

zestaw_12 = zestaw_1 + zestaw_2
print("Połączone zestawy: ")
print(zestaw_12)
print("Po posortowaniu: ")
zestaw_12.sort()
print(zestaw_12)