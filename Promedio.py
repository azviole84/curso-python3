#lea n calificaciones y calcule en promedio
#ademas imprimir la calif. mas alta
#8,9,8,8,9,7,7, promedio:8.0, calif:9

i=1
n = int(input('cuantos alumnos son:'))
s=0
m=0
while i<=n:
 c = int(input('dame la calificacion:'))
 if c > m:
   m=c
 s=s+c
 i+=1
 
prom = s/n
#print('el promedios es:{0}'.format(prom))
#print('el promedios es:%.2f'%prom)
print('el promedios es:%.2f\nY la calif mayor es:%d'%(prom,m))
print(type(c))#de que tipo de dato es la variable c
print(type(prom))#de que tipo de dato es la variable prom