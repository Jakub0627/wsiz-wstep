import numpy as np

#potegi = []
#for i in range(7, -1, -1):
#    potegi.append(2**i)
#
#print(potegi)

potegi = [2**i for i in range(7, -1, -1)]

wagi = np.array(potegi)
print(wagi)

liczba_bin = np.random.randint(low=0, high=2, size=8)
print(liczba_bin)

tab = wagi * liczba_bin
print(tab)
print(tab.sum())