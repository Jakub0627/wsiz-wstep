dict1 = {'data1':10, 'data2':-4, 'data3':2}
def sum_of_values(dict):
    suma = 0
    for i in dict.values():
        suma += i
    return suma

print(sum_of_values(dict1))

#keys
#values
#items tutaj są pary, zamiast values można dać items i dodawać item[1]