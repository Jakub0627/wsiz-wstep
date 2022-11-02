a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if (a>b):
    a,b = b,a

while (a <= b):
    if a%2==1:
        a += 1
        continue
    print(a, end=" ")
    a = a + 1
