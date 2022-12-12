def z5(**kwargs):
    if 'end' in kwargs:
        pom = kwargs['end']
    else:
        pom = "\n"
    print(kwargs)
    for k in kwargs:
        print(k, ' = ', kwargs[k], end=pom)


z5(dom=1, ulica="Lwowska", kodpocztowy="35-202")


z5(dom=1, ulica="Lwowska", kodpocztowy="35-202", end=' ')
