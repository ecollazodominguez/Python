import sys
import random
from PySide2.QtWidgets import (QApplication,QLabel,QPushButton, QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt

class Aplicacion (QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.saudo = ["hola", "Ola", "Hello", "Alo", "Salut", "Arigato", "Ciao"]
        boton = QPushButton ("Pulsame")
        self.etiqueta = QLabel ("Ola a todos")
        self.etiqueta.alignment()
        caixaV = QVBoxLayout ()
        caixaV.addWidget(self.etiqueta)
        caixaV.addWidget(boton)
        self.setLayout(caixaV)
        boton.clicked.connect(self.on_boton_clicked)
        self.show()
        self.resize(400,300)

    def on_boton_clicked(self):
        self.etiqueta.setText (random.choice (self.saudo))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplicacion = Aplicacion()
    #aplicacion.resize(400,300)
    #aplicacion.show()
    sys.exit(app.exec_())