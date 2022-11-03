# Jakub Gładysz grupa 1
# Grupa 1. Użytkownik podaje dwie liczby zmiennoprzecinkowe. Wypisz na ekranie większą z nich

a = float(input("Podaj pierwszą liczbę zmiennoprzecinkową: "))
b = float(input("Podaj drugą liczbę zmiennoprzecinkową: "))

if(a==b):
    print("Te liczby są sobie równe.")
    print("a")
elif(a>b):
    print(a)
else:
    print(b)