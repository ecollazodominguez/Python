from PyQt5.QtWidgets import  QApplication, QTableWidget, QTableWidgetItem
import sys

datos = {'Col1': [1,2,3,4],
         'Col2': [1,3,5,7],
         'Col3': [1,2,4,6]}

class ExemploTaboa(QTableWidget):
    def __init__(self,datos,*args):
        QTableWidget.__init__(self,*args)
        self.datos = datos
        self.asignarDatos()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def asignarDatos(self):
        cabeceirasHor = []
        # Hacemos un for que enumera el contenido, siendo n el numero y clave el contenido
        # cogemos los keys, siendo los "Cols" y lo guardamos en cabeceriasHor
        for n,clave in enumerate (self.datos.keys()):
            cabeceirasHor.append(clave)
            # Otro for enumerando, m el numero y numero el contenido
            # cogemos el contenido haciendo al diccionario con el valor clave que tiene los "Cols"
            # Guardamos los numeros en string y los añadimos indicando m y n como fila y columna.
            for m, numero in enumerate (self.datos[clave]):
                print (numero)
                novoElemento = QTableWidgetItem(str(numero))
                self.setItem(m,n,novoElemento)
        #Ponemos cabecera con los "Cols"
        self.setHorizontalHeaderLabels(cabeceirasHor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    taboa = ExemploTaboa(datos,4,3)
    taboa.show()
    sys.exit(app.exec())
