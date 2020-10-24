"""
datos = [0,1,2,3,4]
print(datos)
#datos2 = [i for i in range(1,51)] #agregar i es 0 y traerla a for que vas se
#print(datos2)

#multiplosde5 = [i for i in range(1,101) if i%5==0]
multiplosde5 = [i for i in range(65,90)]

multiplosde5 =[]
for i in range(1,101):
    if 1%5==0:
        multiplosde5.append(i)

print(multiplosde5)
#multiplos solo que se vean los dos son iguales
"""
#abcedario = [chr(i) for i in range (65,91)] #poner siempre un numero mas
#print(abcedario)

#print(ord('A')) #imprimir letra a numero con ord
#print(chr(65)) #imprime un numero a la letra con chr

d = {i:i for i in range(1,51)} # i:i es para crear diccionarios por un key:valor
print(d)
import random as rm
#m = [(i,j) for j in range(1,6) for i in range(1,11)] (1,1)
#m = [[i for j in range(1,6)] for i in range(1,11)] #lista dentro de otra lista [1,1,1,1]
#m = [[rm.randint(1,10) for j in range(1,6)] for i in range(1,11)] #[8,7,3,5,7]
m = [[rm.randint(1,10) for j in range(1,6) if j%2==0] for i in range(1,11)] #dos columnas [2,1]

print (m)
print(len(m))
