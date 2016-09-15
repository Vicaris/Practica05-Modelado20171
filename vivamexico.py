import sys, os, time
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import datetime


class Window(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.setWindowTitle('¡Viva México!')
        self.setGeometry(300, 300, 250, 150)
        script_dir = sys.path[0]
        img_path = os.path.join(script_dir, 'mexico_icon.png')
        self.setWindowIcon(QtGui.QIcon(img_path))

        #Label patriótico
        l1 = QLabel()
        l1.setText("Vicente Guerrero \n Miguel Hidalgo y Costilla \n José María Morelos")
        l1.setAlignment(Qt.AlignCenter)

        #Botón de la patria
        self.button = QtGui.QPushButton('Apriétame', self)
        self.button.setToolTip('Presiona si eres un patriotazo')
        cuantofalta = self.button.clicked.connect(self.cuantoFalta)

        vbox1 = QtGui.QVBoxLayout(self)
        vbox1.addWidget(l1)
        vbox1.addWidget(self.button)
        
       
        self.setLayout(vbox1)

    #Cuanto falta para el gran día
    def cuantoFalta(self):
        hoy = time.strftime('%d %m %Y')
        dia, mes, anio = hoy.split()
        cf = ''
        d = int(dia)
        m = int(mes)
        a = int(anio)
        if d <= 15 and m <= 9:
        	x = datetime(a,9,16)
        	y = datetime(a,m,d)
        	cf = str((x-y).days)
        else:
        	x = datetime(a+1,9,16)
        	y = datetime(a,m,d)
        	cf = str((x-y).days)
        self.button.setText(cf)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())