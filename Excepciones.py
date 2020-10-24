#excepcion son errores
"""
try:
    num = int(input('Dame un numero:'))
    print(num)
except ValueError as e:
    #print (e._str_)
    print('No es un entero')
#un error enviarle un mensaje de su error, continua y no crakshea
#e es una variable para representar una clase


print('Continua...')
"""
x=[2,6]
try:
    num = int(input('Dame un numero:'))
    print(5/num)#no se puede dividir
    print(x[10])
except ValueError as e:
    print('No es un entero')
except ZeroDivisionError:
    print('No es puede dividir por cero')
except:
    print('Algo salio mal')#ponerlo hasta el final

print('Continua...')

error = False
while not error:
    try:
        num = int(input('dame un numero:'))
        error = True
    except ValueError:
        print('no es un entero')




