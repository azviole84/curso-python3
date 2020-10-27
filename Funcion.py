#separar probrama por pequeños programas

#mandar a llamar nombre y parentesis
#mensaje()

def mensaje():
    print('Mensaje')#resive
def funcionRegresa():
    return 'Cadena de regreso'#regresa

def f2(x):
    print('el valor de x es:',x )#no resive y no regresa

def cuadrado(x):
    y=x*x
    return y #resive y gresar

def alumno1():
    nom = 'juan'
    edad = 20
    calif = 9.5
    return nom,edad,calif

def alumno(**kwargs):
    print(kwargs)
    print(kwargs['nom'])
    print(kwargs['edad'])
    print(kwargs['calif'])
    #diccionario ya que tiene llaves
    #nom = 'juan'
    #edad = 20
    #calif = 9.5
    #return nom,edad,calif

def suma(n1,n2,n3,n4,n5=0):#n1=0,n2=0,n3=0,n4=0,n5=0 todos los pone en 0 y si queremos uno es n1,n2=0,n3=0,n4=0,n5=0
    return n1+n2+n3+n4+n5
    """
def suma2(*args):#argumento que queramos
    print (args)
    s=0
    for i in args:
        s+=i
    return s
    """
def suma2(x,*args):#argumento que queramos variable x
    print (args)
    print(x)
    s=0
    for i in args:
        s+=i
    return s
def combinacion(n,**args,**kwargs)
    print(n)
    print(args)
    print(kwargs)
combinacion(10,20,30,x=10,y=10)    
alumno(nom='juan', edad=20,calif=9.5)
#print('la suma es: ',suma2(5,7,6,9,7,3,4,6,7,8))


"""
x,y,z = alumno()#tupla
dato = alumno()
print(alumno())
print(x)
print(y)
print(z)
print(dato)
print(dato[0])
"""


print('estoy en el programa principal')
mensaje()

cad = funcionRegresa()
print(cad)
print(funcionRegresa())

f2(20)

r=cuadrado(2)
print(r)