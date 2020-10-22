"""
#una tupla se pone en parentesis
t=(1,2,3,4) 
#t.append(5)no se puede
#t[1]=40 no se puede
print(t[1:4])
print(t[-1])

for i in t:
    print(i)

l=list(t)
l.append(5)
print(l)
t2=tuple(l)
l.pop()
l.remove(2)
del l[2]
print(type(t))
print(type(l))
print(type(t2))

Progra = {'Juan','Pedro','Maria','Diana'}
Calculo = {'Santiago','Jesus','Pedro','Maria'}
Progra.add('Eduardo')
Progra.remove('Juan')#borrar
#del Progra #eliminar para ciempre de la RAM
#Progra.clear()

#C2=Progra & Calculo #union
#C2=Progra - Calculo
C2=Progra | Calculo
print(C2)


print('Mary' in Progra)
print(Calculo)
print(Progra)
"""
#Diccionarios (JSON)
#key, value

alumno1={'nombre':'Juan',
         'edad':20,
         'carrera':'ICO',
         'promedio':9.5
         }
         #tiene un nombre y un valor
alumno2={'nombre':'Pedro',
         'edad':19,
         'carrera':'IMT',
         'promedio':9.2
         }
         #tiene un nombre y un valor
a3={'nombre':'Maria',
         'edad':21,
         'carrera':'IBIO',
         'promedio':9.6
         }
         #tiene un nombre y un valor
alumnos = [alumno1,alumno2,a3]

for a in alumnos:
    print('{:<10s}{:<5d}{:<10s}{:<5.2f}'.format(a['nombre'],a['edad'],a['carrera'],a['promedio']))



"""
print(len(alumnos))
alumnos['promedio']=9.5
alumnos['nombre']='Maria'
print(alumnos['nombre'])
print(alumnos['promedio'])
print(alumnos.get('promedio'))
print(alumnos)

for k,v in alumnos.items():#k.v
    #print(alumnos[d])
    #print(k)
    print(v)


for v in alumnos.values():    
    print(v)
    
print(alumnos.values())  #lista de los valores  
print(alumnos.keys())#keys
print(alumnos.items())#lista de tuples es nombre y valor
"""