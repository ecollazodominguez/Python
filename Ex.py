tupla = [1,2,3,4]

#Ejercicio 7.6.1

def comprobaOrde (tupla):
    anterior = tupla[0]
    ordeada = True
    for elemento in tupla:
        if elemento < anterior:
            print("a serie non esta ordeada de menor a maior")
            ordeada = False
            break
        anterior = elemento
    if ordeada:
        print ("a serie esta ordeada de menor a maior")

#comprobaOrde(tupla)

#Ejercicio 7.6.2

ficha1 = [3,4]
ficha2 = [5,4]

def comprobaDomino (ficha1, ficha2):
    primero = False
    segundo = False
    if ficha1 [0] == ficha2 [0] or ficha1 [0] == ficha2 [1]:
        primero = True
    elif ficha1 [1] == ficha2 [0] or ficha1 [1] == ficha2 [1]:
        segundo = True
    if primero or segundo:
        print("las fichas encajan entre ellas")
    else:
        print("Las fichas no encajan entre ellas")

#comprobaDomino(ficha1, ficha2)

#Ejercicio 7.6.3

nombres = ["Angel", "Antonio", "Paco", "Maria", "Paula"]

def sacarNombres (nombres):
    for elemento in nombres:
        print(elemento, " Estimado")

#sacarNombres(nombres)

def sacarXNombres (nombre):
    for elemento in nombres[1:3]:
        print(elemento, " Estimado")

sacarXNombres(nombres)


# Ejercicio 7.6.7

def listaNomes (lista):
    #listaCadeas = []
    listaCadeas = list()
    for tupla in lista:
        cadea = tupla[1] + " " + tupla[2] + ". " + tupla[0]
        listaCadeas.append (cadea)

    return listaCadeas
print (listaNomes([("Diz", "Ana", "R"), ("Perez", "Luis", "N")]))

"""Ejercicio 9.5.1. Escribir una función que reciba una lista de tuplas, y que devuelva un
diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una
lista con los segundos."""


def Hazdiccio (lista):
    dic = dict()
    for tupla in lista:
        cadea = {tupla[0] : [tupla[1]]}
        dic.update(cadea)
    return dic


print (Hazdiccio(([('O','L'),(1,2)])))

def Hazdiccio2 (lista):
    dic = dict()
    for tupla in lista:
        if tupla[0] in dic:
            dic [tupla[0]].append(tupla[1])
        else:
            dic [tupla[0]] = [tupla[1]]
    return dic


print (Hazdiccio2(([('Ola','Lala'),(1,2),('Ola','Aba')])))

"""Ejercicio 9.5.2. Diccionarios usados para contar.
1. Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de
apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que
hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
2. Escribir una función que cuente la cantidad de apariciones de cada carácter en una
cadena de texto, y los devuelva en un diccionario.
3. Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los
dos dados. Nota: utilizar el módulo random para obtener tiradas aleatorias."""


#1
def apariciones(str):
    dic = dict()
    lis = str.split()
    for elemento in lis:
        dic [elemento] = lis.count(elemento)
    return dic

print (apariciones("que lindo día que hace hoy"))

#2

def aparicionescaras(str):
    dic = dict()
    for elemento in str:
        dic [elemento] = str.count(elemento)
    return dic

print (aparicionescaras("aa bb c d ee"))

#3

