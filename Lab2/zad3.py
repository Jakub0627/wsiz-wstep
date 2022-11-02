print("Wybierz operację: ")
print("Dodawanie - 1 ")
print("Odejmowanie - 2 ")
print("Mnożenie - 3 ")
print("Dzielenie - 4 ")
print("Potęgowanie - 5 ")
a = float(input("Podaj numer operacji: "))
b = float(input("Podaj pierwsza liczbe: "))
c = float(input("Podaj druga liczbe: "))

if a == 1:
    print(b+c)
elif a == 2:
    print(b-c)
elif a == 3:
    print(b*c)
elif a == 4:
    print(b/c)
elif a == 5:
    print(b**c)
else:
    print("Podano zły numer operacji")