#while
#for

n=1
while n<5:
 print(n,'mensaje')
 n+=1

for n in range(2,10,2):
    print(n,'Mensaje')
# si quieres que inicie de 1 pon (1,5)
# (2,10,2) seria de 2,4,6,8 porque va de dos en dos hasta el 10

import math

resp = 'si'

while resp == 'si':
    a=int(input('Dame a:'))
    b=int(input('Dame b:'))
    c=int(input('Dame c:'))

    if a!=0:
       d = b**2 - 4*a*c
       if d>=0:
         x1 = (-b+math.sqrt(d))/(2*a)
         x2 = (-b + math.sqrt(d))/(2*a)
        print('x1=',x1,'\nx2=', x2)
       else:
        print('sol compleja')
    else:
        print('No es una ecuacion cuadratica. Es lineal')
    resp =input('Desea la solucion de otra ec.cuadratica:')
print('Continúa')