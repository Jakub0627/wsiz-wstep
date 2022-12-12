def oblicz(a, b):
    print(f'Suma:', a+b)
    print(f'Różnica:', a-b)
    return a+b, a-b

wynik = oblicz(5, 10)

print(wynik[0], wynik[1])

a, b = oblicz(1.1, 2.3)
print(a)
print(b)

'''def oblicz(liczba1,liczba2):
    x = liczba1 + liczba2
    y = liczba1 - liczba2
    return x, y
z = oblicz(5,5)
print(z[0],z[1])
a,b = oblicz(7.5,5.5)
print(a,b)'''