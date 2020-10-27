
def leerEntero(cad):
    error = False
    while not error:
        try:
            n = int(input(cad))
            error = True
        except ValueError:
            print('no es un entero')
    return n

def leerFloat(cad):
    error = False
    while not error:
        try:
            n = float(input(cad))
            error = True
        except ValueError:
            print('no es un float')
    return n
    