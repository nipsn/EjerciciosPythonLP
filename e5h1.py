def exp(n):
    sum = 0
    for x in range(1,n):
        sum += ((x * x) + 1) / x
    print(sum)

exp(4)