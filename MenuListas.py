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
numCta=[]
nombres=[]
edades=[]
carreras=[]
promedios=[]
while opc != 6:
    os.system('cls')
    print(menu)
    opc = int(input('Dame una opción:'))
    
    if opc == 1:
        numCta.append(int(len(numCta)+1))
        nombres.append(input('Nombre:'))
        edades.append(int(input('Edad:')))
        carreras.append(input('Carrera:'))
        promedios.append(float(input('Promedio:')))
        #Datos agregados en listas
    elif opc ==2:
       nC=int(input('Id a dar de baja:'))
       existe = False
       for i in range(0,len(numCta)):
            if numCta[i]==nC:
                existe=True
                break
        
       if existe:
            numCta.pop(i)
            nombres.pop(i)
            edades.pop(i)
            carreras.pop(i)
            promedios.pop(i)
       else:
            print(nC,'No existe')
    elif opc ==3:
        nC=int(input('Id a Consultar:'))
        existe=False
        for i in range(0,len(numCta)):
            if numCta[i]==nC:
                existe=True
                break
        
        if existe:
             print('{:<5d}{:<20s}{:<5d}{:<10s}{:<5.2f}'.format(
            numCta[i],nombres[i],edades[i],carreras[i],promedios[i]))
        else:
            print(nC,'No existe')

    elif opc ==4:
        nC=int(input('Id a Actualizar:'))
        existe=False
        for i in range(0,len(numCta)):
            if numCta[i]==nC:
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
                   nombres[i]=input('dame el nuevo nombre:')
                elif opc2 ==2:
                    edades[i]=int(input('dame la nueva edad:'))
                elif opc2==3:
                    carreras[i]=input('dame la nueva carrera:')
                elif opc2==4:
                    promedios[i]=float(input('dame el nuevo promedio:'))
                else:
                    print('regresando...')
               

        else:
            print(nC,'No existe')



    elif opc ==5:
        for i in range(0,len(nombres)):
            #print('%-20s%-5d%-10s%-5.2f'%(nombres[i],edades[i],carreras[i],promedios[i]))
            print('{:<5d}{:<20s}{:<5d}{:<10s}{:<5.2f}'.format(
            numCta[i],nombres[i],edades[i],carreras[i],promedios[i]))
    elif opc ==6:
        print('regrese pronto')
    else:
        print('opción no válida')
    input()

