def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia (base, exponente - 1)
base=int(input("Introduce una base "))
exponente=int(input("Introduce un exponente "))

print(potencia(base, exponente))