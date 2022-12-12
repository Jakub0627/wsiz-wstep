import numpy as np
tab = np.zeros((3, 3))
print(tab)

#tab[1:,:2] = 1 #wycinek1
tab[0:, 2:] = 1 #wycinek2
tab[:2, ] = 1 #wycinek3
print(tab)