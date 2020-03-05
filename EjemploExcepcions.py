def division (a,b):
    return a/b

try:
    division(3,0)
except ZeroDivisionError:
    print ("Divisón entre cero")
except ValueError:
    print("o valor non é un número")

try:
    division(3, 0)
except  ZeroDivisionError as Erro1:
    print("Error na chamada a funcion division: ", Erro1)
else:
    print("Division correcta")
finally:
    print("Funcion: division")


class MeuErro(Exception):
    def __init__(self, mensaxe):
        self.mensaxe = mensaxe

    def __str__(self):
        return "Error " + self.mensaxe + "" + Exception.__str__(self)


valor = 90

try:
    if valor > 10:
        raise MeuErro("Exceppcion")
except MeuErro as erro:
    print(erro)


