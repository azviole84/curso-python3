#gusrdar en el disco duro
#Binarios (objetos) imagenes, audios
#texto informacion
#abrir un archivo es r,a,w,x read, apen final texto, whrite escribir en un archvo y x es crear 
"""
f=open('alumnos.txt','w')

for i in range(5):
    f.write('cadena '+str(i)+'\n')# acia abajo 7/n

f.close()

"""#si no existe el archivo
datos=None
try:
    f=open('alumnos.txt','r')
    datos=f.readlines()
    print(datos)
    f.close()
except IOError as e:
    print('error al abrir el archivo',e.errno)
if datos!=None:
    pass
else:
    for i in datos:
    #print(i[:-1])
        print(i,end="")

"""
f=open('alumnos.txt','r')
#abra el archivo
#datos =f.read(5)#(5)leer los primero 5 caracteres
#datos=f.readline(4)#(4)renglones
datos=f.readlines()#lista
for i in datos:
    #print(i[:-1])
    print(i,end="")

print(datos)

f.close()
"""
