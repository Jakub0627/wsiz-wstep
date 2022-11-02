# pierwszy wariant okazał się zakazany

char = input("Podaj literę, a program poda jej rozmiar. ")

if char.isupper() == True:
    print("Litera jest duża.")
else:
    print("Litera jest mała.")

# drugi wariant

char = input("Podaj literę, a program poda jej rozmiar. ")

if (char >= 'a') and (char < 'z'):
    print("Litera jest mała.")
else:
    print("Litera jest Duża.")