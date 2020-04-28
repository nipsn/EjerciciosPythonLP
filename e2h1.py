def desglose(eur):
    cantidades = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    resultados = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    i = 0
    while eur > 0:
        eur -= cantidades[i]
        resultados[i] += 1
        if 0 > eur < cantidades[i]:
            i += 1


# no funciona



    print(resultados)

desglose(434)