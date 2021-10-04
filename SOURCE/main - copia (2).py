# ------------------------------------------------- ----- 
# ---------------------- main.py ---------------- --- - 
# --------------------------------------------- - ------- 
# from  PyQt5.QtWidgets  import* 
# from  PyQt5.uic  import  loadUi

# from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

# import  numpy   as  np 
# import  random
     
#from _typeshed import Self
import sys
from  PyQt5.QtWidgets  import* 
from PyQt5 import uic, QtWidgets
from  PyQt5.uic  import  loadUi

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import (QMainWindow, QApplication, QDialog, 
                            QLineEdit, QPushButton,QLabel)

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

import  numpy   as  np 
import  random

#qtCreatorFile = "DINAMITA.ui" # Nombre del archivo aquí.

#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class miApp(QMainWindow):
    def __init__(self, parent=None):
        super(miApp,self).__init__(parent)
        uic.loadUi("DINAMITA.ui",self)

        self.setWindowTitle("DINAMITA - ")
        self.setWindowIcon(QIcon("square.qrc"))
        #self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialodHint)
        #self.setFixedSize(500,500)



        self.initUI()

    def initUI(self):
        self.pushButton_generar.clicked.connect(self.on_click)
    
    def on_click(self):
        print("hola")



if __name__ == '__main__':
    import sys
    app= QApplication(sys.argv)
    GUI = miApp()
    GUI.show()
    sys.exit(app.exec_())
