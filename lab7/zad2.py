import numpy as np
tab = np.random.randint(low=0, high=11, size=(5, 5))
print(tab)

print("Największa wartość: ", tab.max())
print("Najmniejsza wartość:", tab.min())

print("Największe wartości wierszy", tab.max(axis=1))
print("Najmniejsze wartości wierszy", tab.min(axis=1))

print("Największe wartości kolumn", tab.max(axis=0))
print("Najmniejsze wartości kolumn", tab.min(axis=0))

print(tab.sum(axis=0)) #sumowanie kolumnami
print(tab.sum(axis=1)) #sumowanie wierszami

