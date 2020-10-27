import math


a=int(input("Dame a:"))
b=int(input("Dame b:"))
c=int(input("Dame c:"))

if a!=0:
  d = b**2 - 4*a*c
  if d>=0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b + math.sqrt(d))/(2*a)
    print('x1=',x1,'\nx2:', x2)8
  else:
    print('sol compleja')
else:
 print('No es una ecuacion cuadratica. Es lineal')
print('Continúa')

#SC SECUENCIALES
#SC CONDICIONALES (IF, IF-ELSE, ELIF)
#SC CICLITICAS(WHILE, FOR)