import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QSizePolicy


class Aplicacion(QWidget):
    def __init__(self):
            super().__init__()

            btn1 = QPushButton("Boton 1")
            btn2 = QPushButton("Boton 2")
            btn3 = QPushButton("Boton 3")
            btn4 = QPushButton("Boton 4")
            btn5 = QPushButton("Boton 5")
            btn6 = QPushButton("Boton 6")

            grid = QGridLayout()

            #expandir
            btn1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            btn2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            btn3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            btn4.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)
            btn5.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)
            btn6.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)

            #espacio
            grid.setSpacing(3)

            #Objeto, fila,columna
            grid.addWidget(btn1,0,0)
            grid.addWidget(btn2,0,1,1,2)
            grid.addWidget(btn3,1,0,2,1)
            grid.addWidget(btn4,1,1,1,2)
            grid.addWidget(btn5,2,1)
            grid.addWidget(btn6,2,2)



            self.setLayout(grid)

            #Nos permite dar las coordenadas donde aparezca y un tamaño inicial
            self.setWindowTitle("Ejercicio gridLayout")
            self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exemplo = Aplicacion()
    sys.exit(app.exec())