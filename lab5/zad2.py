sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

#podpunkt 1
for k in sample_dict:
    print(f'{k:<10} =  {sample_dict[k]:>8}') # to jest fajne

# mój wariant:
print("Mój wariant przez krotki dostosowany do zajęć.")
for item in sample_dict.items():
    print(f'{item[0]:<10} = {item[1]:>8}')

#podpunkt 2

print("Podpunkt 2:")

b = ["age", "name"]
second_sample_dict = {}

# for i in b:
#     for j in sample_dict:
#         if i == j:
#             second_sample_dict[i] = sample_dict[i]
#             break
# print(second_sample_dict)

#mocniejsza metoda

# for i in b:
#     if i in sample_dict:
#         second_sample_dict[i] = sample_dict[i]
# print(second_sample_dict)

#najmocniejsza metoda
second_sample_dict={i:sample_dict[i] for i in b if i in sample_dict.keys()}
print(second_sample_dict)

D = sample_dict.copy()

#podpunkt 3
print("Podpunkt 3:")
for k in b:
    if k in D.keys():
        D.pop(k)
print(D)