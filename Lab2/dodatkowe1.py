liczba = input("Podaj liczbę: ")
baza = int(input("Podaj bazę od 2 do 9: "))

# Fragment odpowiedzialny za rozłączenie liczby w ciąg znaków

def stringtolist(string):
    list1 = []
    list1[:0] = string
    return list1

fragmenty = stringtolist(liczba)

wynik = 0

for i in range(len(fragmenty)):
    wynik += int(fragmenty.pop())*(baza**(i))
print(wynik)

#Program kuleje bo nie ma zabezpieczeń na niepoprawne inputy oraz składniowo jest zrobiony na szybko...