import random

# podpunkt 1
zestaw_1 = []

a = int(input("Podaj liczbę liczb zestawu 1: "))

for i in range(a):
    zestaw_1.append(random.randint(1, 10))

print(zestaw_1)

#podpunkt 2
zestaw_2 = []

a = int(input("Podaj liczbę liczb zestawu 2: "))

for i in range(a):
    zestaw_2.append(random.randint(5, 15))

print(zestaw_2)
#podpunkt 3
a = int(input("Podaj liczbę całkowitą, a program powie Ci o przynależności do zestawów. "))

pomoc = 0

if a in zestaw_1:
    print("Ta liczba należy do zestawu 1 ")
    pomoc = 1

if (pomoc == 0) and (a in zestaw_2):
    print("Ta liczba należy do zestawu 2 ")
    pomoc = 1

if pomoc == 0:
    print("Ta liczba nie znajduje się w tych listach.")
