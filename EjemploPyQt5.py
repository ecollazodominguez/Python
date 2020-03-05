from PyQt5 import QtWidgets, uic
import sys

class Fiestra ():
    def __init__(self):
        self.ui = uic.loadUi("interfazPrueba.ui")
        #self.ui.boton.clicked.connect(self.on_boton_clicked)
        self.ui.show()

    def on_boton_clicked(self):
        self.ui.etiqueta.setText("Boton pulsado")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    aplicacion = Fiestra()
    sys.exit(app.exec())