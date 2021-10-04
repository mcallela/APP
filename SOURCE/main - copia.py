# ------------------------------------------------- ----- 
# ---------------------- main.py ---------------- --- - 
# --------------------------------------------- - ------- 
# from  PyQt5.QtWidgets  import* 
# from  PyQt5.uic  import  loadUi

# from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

# import  numpy   as  np 
# import  random
     
import sys
from  PyQt5.QtWidgets  import* 
from PyQt5 import uic, QtWidgets
from  PyQt5.uic  import  loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


from PyQt5.QtWidgets import QMainWindow, QApplication

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

import  numpy   as  np 
import  random

#qtCreatorFile = "DINAMITA.ui" # Nombre del archivo aquí.

#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("DINAMITA.ui",self)

        self.pushButton_generar.clicked.connect(self.on_click)
    
    def on_click(self):
        print("hola")



if __name__ == '__main__':
    app= QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())
