#smbd sistema manejadores de bases de datos
#SQLite, MySQL, MariaDB, SQLServer, Postgress, etc.

import sqlite3

cxn = sqlite3.connect('alumnos.db') #db es un arquivo de base de datos y se lleve a cualquier lugar
cur = cxn.cursor() #abrir la ejecucion

#CREATE TABLE Alumnos()  #una tabla una clase donde guardas muchos registros

#SELECT #reporte
#INSERT #create
#UPDATE #crear
#DELITE #borrar

#sql = 'CREATE ABLE Alumnos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(30), edad INTEGER, carrera VACHAR(20), promedio DECIMAL)'#consulta VACHAR ES UNA CADENA
#sql="""INSERT INTO Alumnos Values(NULL,'Maria', 18, 'ICO',8)"""
#id=2
#sql="""DELETE FROM Alumnos WHERE id={}""".format(id)#borrar
id=1
sql="""update Alumnos SET nombre ='Antonio' WHERE id={}""".format(id)#actualizar

cur.execute(sql)
cxn.commit()

cur.close() #cerrar el puntero
cxn.close() #cerrar la coneccion

