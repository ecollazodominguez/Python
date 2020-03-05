import sys
from PySide2.QtUiTools import  QUiLoader
from PySide2.QtWidgets import  QApplication
from PySide2.QtCore import  QFile

if __name__ == "__main__":
    app = QApplication(sys.argv)

    interface = QFile ("interfazPrueba.ui")
    interface.open(QFile.ReadOnly)

    cargador = QUiLoader()
    fiestra = cargador.load(interface)
    interface.close()
    fiestra.show()
    sys.exit (app.exec_())