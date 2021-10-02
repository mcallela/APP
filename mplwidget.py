# ------------------------------------------------- ----- 
# --------------------- mplwidget.py -------------------- 
# ------------------------------------------------- --------------- ---- 
desde  PyQt5.QtWidgets  import *

de  matplotlib.backends.backend_qt5agg  importar  FigureCanvas

de  matplotlib.figure  figura de importación 

    
clase  MplWidget ( QWidget ):
    
    def  __init__ ( self ,  parent  =  None ):

        QWidget . __init__ ( yo ,  padre )
        
        yo . lienzo  =  FigureCanvas ( Figura ())
        
        vertical_layout  =  QVBoxLayout () 
        vertical_layout . addWidget ( auto . lienzo )
        
        yo . lienzo . ejes  =  self . lienzo . figura . add_subplot ( 111 ) 
        self . setLayout ( vertical_layout )
