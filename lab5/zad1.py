values = [10, 20, 30]
keys = ["ten", "twenty", "thirty"]

# print(values)
# print(keys)

print(list(zip(keys, values)))

z1 = dict(zip(keys, values))
print(z1)

z1 = {}
for i in range(len(values)):
    z1[keys[i]] = values[i]
print(z1)

z2 = dict(thirty=30, forty=40, fifty=50)
print(z2)

z3 = z1.copy()
z3.update(z2) # z drugiego słownika są brane wartości przy update, giga ważne
print(z3)