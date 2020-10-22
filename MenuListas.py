menu="""
 MENU    (CRUD)
 1 ALTAS  (C)
 2BAJAS   (D)
 3CONSULTAS (R)
 4MODIFICACIONES  (U)
 5REPORTES   (R)
 6SALIR
 
#print(menu)
"""
opc = None
nombres=[]
edades=[]
carreras=[]
promedios=[]
while opc !=6:
    print(menu)
    opc=int(input('dame una opcion'))

    if opc == 1:
        nombres.append(input('Nombre:'))
        edades.append(int(input('Edad:')))
        carreras.append(input('Carrera:'))
        promedios.append(float(input('Promedio:')))
        #datos agregados en listas
    
    elif opc ==2:
        pass
    elif opc ==3:
        pass
    elif opc ==4:
        pass
    elif opc ==4:
        pass
    elif opc ==5:
        pass
    elif opc ==5:
        for i in range(0,len(alumnos)):
           print('{:<10s}{:<5d}{:<10s}{:<5.2f}'.format(
           nombres[i],edades[i],carreras[i],pormedios[i]))
    elif opc ==6:
        pass
    else:
        print('opcion no valida')

