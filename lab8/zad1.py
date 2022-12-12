#motywy zadań na kolokwium:
#funkcje
#listy/słowniki
#jedno zadanie bez list/słowników z danymi od użytkownika

#zadanie 1:

def find(list, a):
    for i in range(len(list)):
        if a == list[i]:
            print("Ta wartośćy występuje pod indeksami: ", i)
    return 0

find([2,3,4,5,2,3,4,2], 2)