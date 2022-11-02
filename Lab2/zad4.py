def sizeswapper(char):
    if char.isupper() == True:
        print(char.lower())
    else:
        print(char.upper())
    return

char = input("Podaj literę, a program zmieni jej rozmiar: ")
sizeswapper(char)