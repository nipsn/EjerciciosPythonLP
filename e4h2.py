def cuentaMayus(cadena):
    print("Mayus:", sum(1 for c in cadena if c.isupper()))
    print("Minus:", sum(1 for c in cadena if c.islower()))
cuentaMayus("AaAaAAAAAA")