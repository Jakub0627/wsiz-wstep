def potega(list1, list2):
    wyniki = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            wyniki.append(list1[i] ** list2[i])
        return wyniki
    else:
        print("Podane listy mają różne długości!")


print(potega([2, 2, 2, 2], [0, 1, 2, 3, 4]))  #różne długości
print(potega([2, 2, 2, 2], [0, 1, 2, 3]))  #te same długości