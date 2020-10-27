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
    
    if opc == 1:
        a={}
        a['numCta']=int(len(alumnos)+1)
        a['nombre']=input('Nombre:')
        a['edad']=leerEntero('Edad:')
        a['carrera']=input('Carrera:')
        a['promedio']=leerFloat('Promedio:')
        alumnos.append(a)

        #Datos agregados en listas
    elif opc ==2:
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
        for i in alumnos:
            #print('%-20s%-5d%-10s%-5.2f'%(nombres[i],edades[i],carreras[i],promedios[i]))
            print('{:<5d}{:<20s}{:<5d}{:<10s}{:<5.2f}'.format(
            i['numCta'],i['nombre'], i['edad'], i['carrera'], i['promedio']))
    elif opc ==6:
        print('regrese pronto')
    else:
        print('opción no válida')
    input()

