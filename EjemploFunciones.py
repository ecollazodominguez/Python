def funcion1(parametro1,parametro2):

    print(parametro1,parametro2)

funcion1(1,2)

#crea tupla maisparametros
def funcion2 (parametro1 = "ola", parametro2 = "Benvidos", *maisParamentros):

    print (parametro1, parametro2, )
    for parametro in maisParamentros:
        print (parametro)

funcion2 ("Ola", "que", "tal", "estas")

#Crea diccionario maisparametros
def funcion3 (parametro1 = 1, parametro2 = 2, **maisParamentros):

    print (parametro1, parametro2, )
    for parametro in maisParamentros.items():
        print (parametro)

funcion3 (4,5,num3=2,num4=3,num5=4)


######################################

def saudar(idioma):
        def saudo_es(saudo2):
                print("Hola",saudo2)
        def saudo_en():
                print("Hi")
        def saudo_gl():
                print("ola")
        funcion_saudo = {
                "es" : saudo_es,
                "en" : saudo_en,
                "gl" : saudo_gl
        }
        return funcion_saudo [idioma]

funcion = saudar("es")

#funcion()
funcion("que tal estas")

#funcion lambda/anónima

#suma = lambda x, y : x+y
#print(suma (5,3))

def suma (tupla):
    return tupla[0]+tupla[1]

lista = [(1,2),(3,4),(5,6)]
#funcion map coge como parametro la lista y aplicará la funcion suma
lista2 = map(suma,lista)
for elemento in lista2:
    print(elemento)

#alternativa lambda

lista2 = map(lambda lista: lista[0]+lista[1], lista)
for elemento in lista2:
    print(elemento)

#alternativa operaciones simples
lista2=[lista[0]+lista[1] for lista in lista]
print(lista2)

#for ins anidados

caracteres = ["a","b","c"]
numeros = [-1,0,1,2,3,4,5]
cadeas = [n*c for n in numeros
             for c in caracteres
             if n > 0]
print(cadeas)

#ejercicio pasar de Fahren a celsius

Fahrenheit = [50,78.8,66.2]

listaf = map (lambda grados: (grados-32)*5/9, Fahrenheit)
for elemento in listaf:
    print(elemento)

listaf = [(g-32)*5/9 for g in Fahrenheit]
print(listaf)

#funcion de rango
#n onde empeza, m onde termina, s o incremento

def meuXerador(n, m, s):
    while (n < m):
        yield n
        n +=s

x = meuXerador (2,7,2)
print (x)

for n in meuXerador (2,7,2):
    print(n)

# **es elevado a
xLista = (n**2 for n in numeros)
for n in xLista:
    print(n)