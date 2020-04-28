def cercano():
    n = int(input())
    lista = [-1] * 4
    lista[0] = int(input())
    lista[1] = int(input())
    lista[2] = int(input())
    lista[3] = int(input())
    
    print(lista)
    # termina input

    distancia = 100000
    mascercano = -1
    for x in lista:
        if abs(n - x) < distancia: 
            mascercano = x
            distancia = abs(n - x)
    
    print(mascercano)

cercano()
