import math
import os
opc=0
while opc != 6:
  os.system('cls')
  print('MENU')
 print('1.Area Triangulo')
 print('2.Salario Trabajador')
 print('3.Solucion de una ecuación cuadratica')
 print('4.Edad')
 print('5.while')
 print('6.salir')

 opc =int(input('Dame una opcion:'))

  if opc == 1:
    print('Area de un triangulo')

  elif opc ==2:
        nombre = input('Nombre:')
    ht = int(input('Horas trabajadas:'))
    ph = float(input('Pago por Hora:'))

    salario = ht*ph

    print('El salario de', nombre, 'es $', salario)

  elif opc == 3:

        a=int(input("Dame a:"))
    b=int(input("Dame b:"))
    c=int(input("Dame c:"))

    if a!=0:
      d = b**2 - 4*a*c
      if d>=0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b + math.sqrt(d))/(2*a)
        print('x1=',x1,'\nx2:', x2)
      else:
        print('sol compleja')
    else:
    print('No es una ecuacion cuadratica. Es lineal')
    print('Continúa')

    
  elif opc ==4:
  
        edad = 25

    condicion = edad>=18
    print(condicion)
    if condicion:
      print('Ya puedes votar, mayor de edad')
    else:
        print('no puedes votar, menor de edad')

    print('Algo') 
    """"""

    #and/or/not
    n=int(input('Numero entre 1 y 30:'))

    if n>=0 and n<=10:
        print('Rango 0 al 10')
    elif n>10 and n<=20:
        print('Rango 11 al 20')
    elif n>20 and n<=30:
        print('Rango 21 al 30')
    else:
        print('Fuera del Rango')
    print('Terminó')

  elif opc == 5:
      n=1
    while n<=5:
    print('mensaje')
    n=n+1

  elif opc == 6:
    print('Fue un placer atenderte. Regrese pronto')  
  else:
    print('Opción no válida') 