def escalera(n):
    for x in range(1,n+1):
        print("".join([str(y) for y in range(1,x+1)]))

escalera(5)