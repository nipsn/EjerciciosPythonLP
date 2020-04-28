def noRepite():
    lista = [1, 2, 1, 3, 4, 5, 2, 8, 3]
    noRepes = [x for x in lista if lista.count(x) < 2]
    print(noRepes)

noRepite()

            

