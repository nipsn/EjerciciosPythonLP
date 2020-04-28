def bisiesto(ano):
    if ano % 4 == 0:
        if ano % 100 != 0 or ano % 400 == 0: return True
    return False

print(bisiesto(2000))
