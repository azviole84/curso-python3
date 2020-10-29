import os

#import Leer deves poner Leer.leerEntero / Leer.leerFloat
from Leer import leerEntero,leerFloat
def buscar(alumno, nC):
    existe=False
    indice=-1
    for a in alumnos:
            indice+=1
            if a['numCta']==nC:
                existe=True
                break
    return existe,indice
def buscarArchivo(alumno, nC):
    existe=False
    indice=-1
    for a in alumnos:
            a=d.indice+=1
            if a['numCta']==nC:
                existe=True
                break
    return existe,indice
           






menu="""
    MENU (CRUD)
    1. Altas (C)
    2. Bajas (D)
    3. Consultas (R)
    4. Actualizar (U)
    5. Reportes (R)
    6. Salir
    """

opc = None
alumnos=[]
while opc != 6:
    os.system('cls')

    print(menu)   
    opc= leerEntero('Dame una opcion:')

    n=[]
    if opc == 1:
        a={}
        try:
            f=open('alumnos.txt','r')
            n=f.readlines()
            f.close()
                       
        except IOError as e:
            print('error al abrir el archivo',e.errno)


        try:
            f=open('alumnos.txt','a')
            nCta=int(len(n)+1)
            nombre=input('Nombre:')
            edad=leerEntero('Edad:')
            carrera=input('Carrera:')
            promedio=leerFloat('Promedio:')
            f.write('{},{},{},{},{}\n'.format(nCta,nombre,edad,carrera,promedio))
            f.close()
        except IOError as e:
            print('error al abrir el archivo',e.errno)
        

        #Datos agregados en listas
    elif opc ==2:
        try:
            f=open('alumnos.txt','r')
            n=f.readlines()
            exite=True
            f.close()
                       
        except IOError as e:
            print('error al abrir el archivo',e.errno)
            existe=False
        if existe:
            nC=leerEntero('id a dar a baja: ')
        else:
            pass

       nC=leerEntero('Id a dar de baja:')

       r=buscar(alumnos,nC)
          
       if existe:
           alumnos.pop(indice)
       else:
            print(nC,'No existe')
    elif opc ==3:
        nC=leerEntero('Id a Consultar:')
        existe, indice=buscar(alumnos,nC)
        
        if existe:
             print('{:<5d}{:<20s}{:<5d}{:<10s}{:<5.2f}'.format(
            alumnos[indice]['numCta'],alumnos[indice]['nombre'], alumnos[indice]['edad'], alumnos[indice]['carrera'], alumnos[indice]['promedio']))
        else:
            print(nC,'No existe')

    elif opc ==4:
        nC=leerEntero('Id a Actualizar:')
        existe, indice=buscar(alumnos,nC)
        for i in alumnos:
            if i['numCta']==nC:
                existe=True
                break
        
        if existe:
            menu2="""
            MENU Actualizar
            1. nombre
            2. edad
            3. carrera
            4. promedio
            5. regresar a menu principal
            """
            opc2 =None
            while opc2 !=5:
                datos=None
                os.system('cls')
                print(menu2)
                opc2 = leerEntero('Dame una opción:')
                
                if opc2 == 1:
                   alumnos[indice]['nombre']=input('dame el nuevo nombre:')
                elif opc2 ==2:
                    alumnos[indice]['edades']=leerEntero('dame la nueva edad:')
                elif opc2==3:
                    alumnos[indice]['carreras']=input('dame la nueva carrera:')
                elif opc2==4:
                    alumnos[indice]['promedios']=leerFloat('dame el nuevo promedio:')
                else:
                    print('regresando...')
               

        else:
            print(nC,'No existe')



    elif opc ==5:
        datos=None
        try:
            f=open('alumnos.txt','r')
            datos=f.readlines()
            for i in datos: 
                a=i.split(',')#separar mi cadena 
                #print(a)
                print('{:<5s}{:<20s}{:<5s}{:<10s}{:<5.2s}'.format(
                    a[0],a[1], a[2], a[3], a[4][:-1]))
            
        except IOError as e:
            print('error al abrir el archivo',e.errno)

        """
        if existe:
            for i in datos:
                #print(i[:-1])
                print(i,end="")
                """
      
    elif opc ==6:
        print('regrese pronto')
    else:
        print('opción no válida')
    input()

