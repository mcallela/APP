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
from PyQt5 import QtGui
from  PyQt5.QtWidgets  import* 
from PyQt5 import uic, QtWidgets
from  PyQt5.uic  import  loadUi

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import (QMainWindow, QApplication, QDialog, 
                            QLineEdit, QPushButton,QLabel)

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

import  numpy   as  np 
import  random
import square_rc

#qtCreatorFile = "DINAMITA.ui" # Nombre del archivo aquí.

#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class miApp(QMainWindow):
    def __init__(self, parent=None):
        super(miApp,self).__init__(parent)
        uic.loadUi("DINAMITA.ui",self)

        self.setWindowTitle("DINAMITA - ")
        self.setWindowIcon(QIcon("square.png"))

        #self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialodHint)
        #self.setFixedSize(500,500)
        self.lbLogoMain.setPixmap(QtGui.QPixmap("spaceapps.png"))
        self.lbHome.setPixmap(QtGui.QPixmap("homeicon.png"))
        self.lbMenu.setPixmap(QtGui.QPixmap("menuicon.png"))
        self.lbFondo.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.v_operacion=vOperacion()
        self.initUI()


    def initUI(self):       
        self.pushButton_generar.clicked.connect(self.on_click)
    
    def on_click(self):
        self.v_operacion.exec_()




class vOperacion(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("OPERACION.ui",self)

        self.pushButton_evaluar.clicked.connect(self.on_click2)
        #self.label_res.setText("Valido")
    
    def initUI(self):
        self.pushButton_evaluar.clicked.connect(self.on_click2)
        
    
    def on_click2(self):
        elemento1=self.lineEdit1.text()
        elemento2=self.lineEdit2.text()
        self.label_res.setText(elemento1 + elemento2)


        #self.v_operacion.exec_()


if __name__ == '__main__':
    import sys
    app= QApplication(sys.argv)
    GUI = miApp()
    GUI.show()
    sys.exit(app.exec_())
