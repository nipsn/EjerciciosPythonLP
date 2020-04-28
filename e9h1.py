def histograma():
    vector = (8,1,4,4,0,1,8,5,1,2,9,6,3,3,4,4,1,4,0,3)
    hist = [0] * (max(vector)+1)
    for i in vector:
        hist[i] += 1
    print(hist)

    for index,i in enumerate(hist):
        print(index, end='')
        print("| ", end='')
        for j in range(i):
            print("|**|", end='')
        print("\n", end='')

histograma()