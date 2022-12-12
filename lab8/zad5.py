# Program działający jako prosty kalkulator:

def dodawanie(a,b):
    return a+b


def odejmowanie(a,b):
    return a-b


def mnozenie(a,b):
    return a*b


def dzielenie(a,b):
    if b == 0:
        print("Dividing by zero")
        return None
    return a/b

operacje = { "+":dodawanie,
               "-":odejmowanie,
               "*":mnozenie,
               "/":dzielenie}

def kalkulator():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    operacja = input("Podaj jedną operację z +, -, *, /: ")
    wynik = operacje[operacja](a, b)
    print("Wynik działania to", wynik)
    return wynik

kalkulator()

