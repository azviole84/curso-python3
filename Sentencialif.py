#condicional if
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

#print('Terminó')
