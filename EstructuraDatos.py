#listas = areglos
#inidimencionales, bidimensionales, tridi, multi

x=[10,5,20,8] 
nombres = [1,4.56,True,[1,2,3],'aldo', 'ana','angel','maria', 'violeta']

m = [[1,2,3],[4,5,6],[7,8,9]]
#print(m)
#print(m[1])
print(m[1][1])#5 es el 1 dentro del [ ] y 1 del 2 []

print(nombres[3])
#print(nombres[-1])#va del final al inicio violeta

print(x)
#print(type(x))
print(x[0])

print(len(nombres))#cuantos elementos hay

print(nombres[1:5])#llega del 1 al 4
print(nombres[0:5])#igual [:5]
print(nombres[0:])#se va hasta el final
print(nombres[0:8:2])#es los mismo print(nombres[::2])
print(nombres[::])#todos
print(nombres[::-1])#la lista alreves
print(nombres[-1:-5:-1])#de atras hacia enfrente del -1 al -4
print(nombres[3][1])#2 es el 2 dentro de []

#nombres =  []#borre mi lista y solo tiene juan

nombres.append('Juan')#pone un elemento al final de la lista
nombres.extend([1,2,3])#agregar una lista mas a la lista
nombres.pop(3)#borrar elemento de la lista
print(nombres)
nombres [2] = 'tempura1'#los sobrescribe

#listas(mutables, tindices un orden)

noms = ('juan', 'Maria')#entre parentesis
#noms.append('luis')#no existe porque no puedes cambiar valor
#noms[0]='luis'#no se puede porque no se puede cambiar
print(noms)
#tuplas(inmutables cuando se crean no se pueden modificar )
#conjuntos(no indices)
#diccionario(no indices)