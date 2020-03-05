import math

class Punto:
    """Clase que define un punto xeométrico
    nun plano de dúas dimensións"""

    def __init__(self, x=0, y=0):
        '''   "__"X INDICA QUE É PRIVADO'''
        self.__x = x
        self.__y = y

    def obterX(self):
        return self.__x

    def obterY(self):
        return self.__y

    def asignarX(self,x):
        self.__x = x

    def asignarY(self,y):
        self.__y = y

    x = property(obterX, asignarX)
    y = property(obterY, asignarY)


class Circulo(Punto):

    def __init__(self, x=0, y=0, r=1):
        Punto.__init__(self,x,y)
        self.r = r

    def superficie(self):
        return math.pi*self.r*self.r
class Vector ():
    def __init__(self, m):
        self.modulo = m

class Cilindro (Circulo,Vector):
    def __init__(self, x=0,y=0,r=0,m=0):
        Circulo.__init__(self,x,y,r)
        Vector.__init__(self,m)

    def volume(self):

        return self.superficie()*self.modulo


p1 = Punto()
p2 = Punto(y=5)
p3 = Punto(5)
c1 = Circulo(r=5)
print(c1.obterX())
#ci1 = Cilindro(r=2,m=10)
#print(ci1.volume())
"""PARA MOSTRAR O PRIVADO"""
p3._Punto__y = 10
""""""""

p3.asignarY(5)
print (p3.obterX())
p3.x=7
print(p3.x)