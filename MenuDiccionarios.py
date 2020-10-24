import os
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
    opc = int(input('Dame una opción:'))
    
    if opc == 1:
        a={}
        a['numCta']=int(len(alumnos)+1)
        a['nombre']=input('Nombre:')
        a['edad']=int(input('Edad:'))
        a['carrera']=input('Carrera:')
        a['promedio']=float(input('Promedio:'))
        alumnos.append(a)

        #Datos agregados en listas
    elif opc ==2:
       nC=int(input('Id a dar de baja:'))
       existe=False
       indice=-1
       for i in alumnos:
            indice+=1
            if a['numCta']==nC:
                existe=True
                break
           
        
       if existe:
            alumnos.pop(indice)
       else:
            print(nC,'No existe')
    elif opc ==3:
        nC=int(input('Id a Consultar:'))
        existe=False
        for i in alumnos:
            if i['numCta']==nC:
                existe=True
                break
        
        if existe:
             print('{:<5d}{:<20s}{:<5d}{:<10s}{:<5.2f}'.format(
            i['numCta'],i['nombre'], i['edad'], i['carrera'], i['promedio']))
        else:
            print(nC,'No existe')

    elif opc ==4:
        nC=int(input('Id a Actualizar:'))
        existe=False
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
                opc2 = int(input('Dame una opción:'))
                
                if opc2 == 1:
                   i['nombre']=input('dame el nuevo nombre:')
                elif opc2 ==2:
                    i['edades']=int(input('dame la nueva edad:'))
                elif opc2==3:
                    i['carreras']=input('dame la nueva carrera:')
                elif opc2==4:
                    i['promedios']=float(input('dame el nuevo promedio:'))
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

