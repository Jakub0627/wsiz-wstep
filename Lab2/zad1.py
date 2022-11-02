a = int(input("Podaj wiek klienta: "))
if a < 4:
    print("Wejście bezpłatne")
elif a < 18:
    print("Bilet kosztuje: 10pln.")
else:
    print("Bilet kosztuje 20pln.")