#adivina un numero a la compu.
#que numero estoy pensando

import random

num=random.randint(1,20)

i=1
while i<=3:
  n=int(input('adivina el numero que pense:'))
  if n==num:
    print('adivinaste')
    #i=3
    break
  elif n<num:
    print('el numero es Mayor')
  else:
    print('el numero es menor')
  i+=1

if i!=3:
   print('el numero que pense fue:',num)

#if i ==3:
  #pass
#else:
  #print('el numero que pense fue:'num)
#print(num)
