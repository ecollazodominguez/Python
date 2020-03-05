# importamos la libreria
import sqlite3 as dbapi

print(dbapi.apilevel)
print(dbapi.threadsafety)
print(dbapi.paramstyle)


# creamos bd, sqlite es monousuario y se guarda en fichero local (no hace falta, servidor, puerto, usuario)
try:
    bd = dbapi.connect("BD_Proba.dat")
    # Para trabajar con la BD creamos un objeto llamado cursor que se crea a través del método connection
    cursor = bd.cursor()

    # Mediante execute() creamos nuestra tabla
    """cursor.execute("create table users
    (dni text,
    name text,
    adress text)")"""

    # Insertamos datos en la tabla
    cursor.execute("""insert into users
                    VALUES ('3333-A',
                            'Pepe',
                            'Garcia Barbon')""")
    cursor.execute("""insert into users 
                    VALUES ('3331-B',
                            'Fran',
                            'Toledo')""")

    # Hacemos select * e iteramos para monstrar los resultados
    cursor.execute("""SELECT * FROM users""")
    # Nos recoge el resultado, el primero
    print(cursor.fetchall())
    # Este otro, le decimos el número de resultados que nos puede imprimir como máximo si los hay
    print(cursor.fetchmany(2))
    # Otra forma, sería iterando
    for resultado in cursor.fetchall():
        print("Usuario; ", resultado[1])
        print("Dni ", resultado[0])
        print("Direccion ", resultado[2])

    bd.commit()

except dbapi.OperationalError as erroOperation:
    print("""Erro (operationalError)""" + str(erroOperation))
except dbapi.DatabaseError as erroDatabase:
    print("Erro (DatabaseError) " + str(erroDatabase))
finally:
    # Siempre cerramos todos los objetos creados
    cursor.close()
    bd.close()
