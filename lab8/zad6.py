import numpy as np
tab = np.zeros((5,5))
print("Utworzenie tablicy 5x5 z samych zer:")
print(tab)
tab[0, 0] = 1
tab[0, 4] = 1
tab[4, 0] = 1
tab[4, 4] = 1
print("Zamiana wartości w rogach na 1:")
print(tab)

#funkcja zamieniająca zera na jedynki i odwrotnie
def swap(tab):
    for i in range(tab.shape[0]):
        for j in range(tab.shape[1]):
            if tab[i][j] == 0:
                tab[i][j] = 1
            else:
                tab[i][j] = 0
    return tab
print("Po odwróceniu zer i jedynek:")
print(swap(tab))