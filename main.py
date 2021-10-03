# ------------------------------------------------- ----- 
# ---------------------- main.py ---------------- --- - 
# --------------------------------------------- - ------- 
from  PyQt5.QtWidgets  import* 
from  PyQt5.uic  import  loadUi

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

import  numpy   as  np 
import  random
     
class  MatplotlibWidget ( QMainWindow ):
    
    def __init__ ( self):
        
        QMainWindow . __init__ ( self )

        loadUi ( "DINAMITAGUI.ui" , self )

        self.setWindowTitle ( "Ejemplo de GUI de PyQt5 y Matplotlib" )

        self.pushButton_generar.clicked.connect(self.update_graph)
        self.addToolBar (NavigationToolbar(self.MplWidget.canvas,self))


    def update_graph ( self ):
        cantidad =int(self.lineEdit.text())
        cantidad2 =int(self.lineEdit_2.text())

        #fs  =  500 
        #f  =  random . randint ( 1 ,  100 ) 
        fs=cantidad +1
        f= cantidad2
        ts  =  1 / fs 
        length_of_signal  =  100
        t  =  np . linspace ( 0 , 10 , length_of_signal )
        
        cosinus_signal  =  np . cos ( 2 * np . pi * fs * t ) 
        sinus_signal  =  np . sin ( 2 * np . pi * f * t )

        self. MplWidget . canvas. axes . clear () 
        self . MplWidget . canvas . axes . plot ( t ,  cosinus_signal ) 
        self . MplWidget . canvas . axes . plot ( t ,  sinus_signal ) 
        self . MplWidget . canvas . axes . legend(( 'Dato1' ,  'Dato2' ),loc = 'upper right' ) 
        self . MplWidget . canvas . axes . set_title ( ' Dato ' ) 
        self . MplWidget . canvas . draw()
        

app =  QApplication([]) 
windows  =  MatplotlibWidget() 
windows . show() 
app . exec_()
