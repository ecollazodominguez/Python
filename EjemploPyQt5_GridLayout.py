import sys
from PyQt5.QtWidgets import QWidget,QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication


class Aplicacion(QWidget):
    def __init__(self):
            super().__init__()

            lblTitulo = QLabel("Título")
            lblAutor = QLabel("Autor")
            lblResumo = QLabel("Resumo")

            edtTitulo = QLineEdit()
            edtAutor = QLineEdit()
            txtResumo = QTextEdit()

            grid = QGridLayout()
            grid.setSpacing(10)

            #Objeto, fila,columna

            grid.addWidget(lblTitulo,0,0)
            grid.addWidget(edtTitulo,0,1)
            grid.addWidget(lblAutor,1,0)
            grid.addWidget(edtAutor,1,1)
            grid.addWidget(lblResumo,2,0)
            grid.addWidget(txtResumo,2,1)

            self.setLayout(grid)

            #Nos permite dar las coordenadas donde aparezca y un tamaño inicial

            self.setGeometry(300,300,350,300)
            self.setWindowTitle("Exemplo gridLayout")
            self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exemplo = Aplicacion()
    sys.exit(app.exec())

