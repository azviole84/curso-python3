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
        pass
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
        pass
    elif opc ==5:
        for i in range(0,len(nombres)):
            #print('%-20s%-5d%-10s%-5.2f'%(nombres[i],edades[i],carreras[i],promedios[i]))
            print('{:<5d}{:<20s}{:<5d}{:<10s}{:<5.2f}'.format(
            numCta[i],nombres[i],edades[i],carreras[i],promedios[i]))
    elif opc ==6:
        pass 
    else:
        print('opción no válida')
    input()

