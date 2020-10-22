"""
#una tupla se pone en parentesis
t=(1,2,3,4) 
#t.append(5)no se puede
#t[1]=40 no se puede
print(t[1:4])
print(t[-1])

for i in t:
    print(i)
"""
"""
l=list(t)
l.append(5)
print(1)
t2=tuple(1)
l.pop(2)
l.remove(2)#nombre
del l[2]#borrar variables
print(type(l))
print(type(t))
print(type(t2))
"""
"""
Progra = {'Juan','Pedro','Maria','Diana'}
Calculo = {'jesus','Psantiago','pedro','Maria'}
Progra.add('Eduardo')
Progra.remove('Juan')#borrar
#del Progra #eliminar para ciempre de la RAM
#Progra.clear()

#C2=Progra & Calculo #union
#C2=Progra - Calculo
C2=Progra | Calculo
print(C2)


print('Maria' in Progra)
print(Calculo)
print(Calculo)
"""
#Diccionarios (JSON)
#key, value
alumnos1={'nombre':'Juan',
         'edad':20,
         'carrera':'ICO',
         'promedio':9.5
         }#tiene un nombre y un valor

alumnos2={'nombre':'Ana',
         'edad':15,
         'carrera':'ICO',
         'promedio':8.5
         }#tiene un nombre y un valor

alumnos = [alumnos1,alumnos2]

for a in alumnos:
     print('{:<10s}{:<5d}{:<10s}{:<5.2f}'.format(a['nombre'],a['edad'],a['promedio']))


"""
print(len(alumnos))
alumnos['promedio']=8.0
alumnos['nombre']='Maria'
print (alumnos['nombre'])
print (alumnos['promedio'])
print (alumnos.get('promedio'))
print(alumnos)

for v in alumnos.values():#k.v
    #print(alumnos[d])
    #print(k)
    print(v)

#print(alumnos.values())#lista de los valores
#print(alumnos.keys())#keys
#print(alumnos.items())#lista de tuples es nombre y valor