def znaki(string):
    dict1 = {}
    string = string.replace(" ", "")
    while len(string) != 0:
        counter = 0
        for i in range(len(string)):
            if string[0] == string[i]:
                counter += 1
        dict1.update({string[0]:counter})
        string = string.replace(string[0], '')
    return sorted(dict1.items(), key=lambda x:x[1])

print(znaki("znaki napisu"))
