def esPrimo(n):
    return not n % 2 == 0

def muestraPrimos(n):
    for i in range(1,n):
        if esPrimo(i): print(i)


muestraPrimos(10)