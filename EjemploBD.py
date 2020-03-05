import sqlite3 as dbapi

print(dbapi.apilevel)
print(dbapi.threadsafety)
print(dbapi.paramstyle)

try:
    #conectar a la base de datos
    bbdd = dbapi.connect("baseDatosProba.dat")
    cursor = bbdd.cursor()
    #comandos sql
    #cursor.execute("""create table usuarios
                #        (dni text,
               #          nome text,
                 #         direccion text)""")

   # cursor.execute("""insert into usuarios
                       # VALUES ('33333333-A',
                      #          'Pepe',
                       #         'Garcia Barbon')""")
   # cursor.execute("""insert into usuarios
                      #  VALUES ('33333334-B',
                       #         'Ana',
                       #         'Rosalía')""")

    #Lista a añadir
    lista = [('BBBB-4','Alfre','Zaragoza'),('CCCC-5','Meme','Zamora')]

    #Se añade lista
  #  for alumno in lista:
     #   cursor.execute("""insert into usuarios
       #                         VALUES (?,
       #                                 ?,
        #                              ?)""", alumno)

    #mais resumido
    #cursor.executemany("""insert into usuarios VALUES (?,?,?)""", lista)


    # añadir tabla colores a diccionario
    cursor.execute("SELECT * FROM colores")
    diccionario = dict()

    for color in cursor.fetchall():
        diccionario [color[0]] = color[1]

    print(diccionario)

    #mostrar contenido tabla usuarios
    cursor.execute("SELECT * FROM usuarios")

    #print(cursor.fetchall())


    for usuario in cursor.fetchall():
        print("Usuario: ", usuario[1])
        print("Dni: ", usuario[0])
        print("Dirección: ", usuario[2])
        print("************************")

    bbdd.commit()
except dbapi.OperationalError as erroOperacion:
    print("Erro (operationalError): " + str(erroOperacion))
except dbapi.DatabaseError as erroBaseDatos:
    print("Erro (DatabaseError ): " + str(erroBaseDatos))
finally:
    cursor.close()
    bbdd.close()

