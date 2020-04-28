def invertDict():
    d1 = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
    set1 = set(d1.values())
    d2 = dict()

    for elem in set1:
        lista = list()
        for key,value in d1.items():
            if value == elem:
                lista.append(key)
        d2[elem] = lista
    print(d2)

invertDict()