def palabraMasLarga(filename):
    with open(filename) as file_object:
        lines = file_object.readlines()
    
    print(sorted(lines, key=len)[-1])

palabraMasLarga("file_e8h2")