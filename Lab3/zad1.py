a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if (a>b):
    a,b = b,a

while (a <= b):
    print(a, end=" ")
    a = a + 1