def matrix(n,m):
    A = [[-1] * n] * m
#no funciona
    for x in range(0,n):
        for y in range(0,m):
            A[x][y] = x + y
    print(A)
matrix(3,3)