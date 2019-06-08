import PyQt5 as pyqt
import sys
import FirstWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class ElectroGUI(FirstWindow.Ui_MainWindow, QtWidgets.QMainWindow):
    '''
    Class dedicated to interact with the user using PyQT.
    '''

    def __init__(self):
        super(ElectroGUI,self).__init__()
        self.setupUi(self)

        ######Variables######
        self.textoFrecOrden1 = ""    
        self.textoGananciaOrden1 = ""
        self.textoFrecOrden2 = ""
        self.textoXsi = ""
        self.textoGananciaOrden2 = ""
        self.textoXsiz = ""
        self.textoWz = ""

        #######Menu principal#######
        self.primerOrden.clicked.connect(self.abrirPrimerOrdenMenu)
        self.segundoOrden.clicked.connect(self.abrirSegundoOrdenMenu)
        self.returnButton.clicked.connect(self.abrirMainMenu)

        #######Menu de primer orden#######
        self.pasaAltosPrimerOrden.setEnabled(False)
        self.pasaBajosPrimerOrden.setEnabled(False)
        self.pasaTodoPrimerOrden.setEnabled(False)
        self.frecPrimerOrden.textChanged.connect(self.guardarTextoFrecOrden1)
        self.gananciaPrimerOrden.textChanged.connect(self.guardarTextoGananciaOrden1)

        #######Menu de segundo orden######
        self.pasaAltosSegundoOrden.setEnabled(False)
        self.pasaBajosSegundoOrden.setEnabled(False)
        self.pasaTodoSegundoOrden.setEnabled(False)
        self.pasaBanda.setEnabled(False)
        self.notch.setEnabled(False)
        self.lowPassNotch.setEnabled(False)
        self.highPassNotch.setEnabled(False)
        self.frecSegundoOrden.textChanged.connect(self.guardarTextoFrecOrden2)
        self.gananciaSegundoOrden.textChanged.connect(self.guardarTextoGananciaOrden2)
        self.xsi.textChanged.connect(self.guardarTextoXsi)
        self.omegaz.textChanged.connect(self.guardarTextoOmegaz)
        self.xsiz.textChanged.connect(self.guardarTextoXsiz)

        #######Menu de graficos#######
        self.entrada.currentTextChanged.connect(self.entradaUsuario)
    
###Estos metodos guardan el texto ingresado por el usuario en sus respectivas variables###
    def guardarTextoFrecOrden1 (self,text):
        self.textoFrecOrden1 = text
        self.activarBotones1()

    def guardarTextoGananciaOrden1(self,text):
        self.textoGananciaOrden1 = text
        self.activarBotones1()
    
    def guardarTextoFrecOrden2(self,text):
        self.textoFrecOrden2 = text
        self.activarBotones2()

    def guardarTextoGananciaOrden2(self,text):
        self.textoGananciaOrden2 = text
        self.activarBotones2()
        
    def guardarTextoXsi(self,text):
        self.textoXsi = text
        self.activarBotones2()

    def guardarTextoOmegaz(self,text):
        self.textoOmegaz = text
        self.activarBotones2()

    def guardarTextoXsiz(self,text):
        self.textoXsiz = text
        self.activarBotones2()

###Estos metodos activan y desactivan los botones para seleccionar un filtro solo si los datos requeridos fueron ingresados###
    def activarBotones1(self):
        if self.textoFrecOrden1 != "" and self.textoGananciaOrden1 != "":
            self.pasaAltosPrimerOrden.setEnabled(True)
            self.pasaBajosPrimerOrden.setEnabled(True)
            self.pasaTodoPrimerOrden.setEnabled(True)
            self.pasaAltosPrimerOrden.clicked.connect(self.abrirGraficosMenu)
            self.pasaBajosPrimerOrden.clicked.connect(self.abrirGraficosMenu)
            self.pasaTodoPrimerOrden.clicked.connect(self.abrirGraficosMenu)
        else:
            self.pasaAltosPrimerOrden.setEnabled(False)
            self.pasaBajosPrimerOrden.setEnabled(False)
            self.pasaTodoPrimerOrden.setEnabled(False)

    def activarBotones2(self):
        if self.textoFrecOrden2 != "" and self.textoGananciaOrden2 != "" and self.textoXsi != "":
            self.pasaAltosSegundoOrden.setEnabled(True)
            self.pasaBajosSegundoOrden.setEnabled(True)
            self.pasaTodoSegundoOrden.setEnabled(True)
            self.pasaBanda.setEnabled(True)
            self.notch.setEnabled(True)    
            self.pasaAltosSegundoOrden.clicked.connect(self.abrirGraficosMenu)
            self.pasaBajosSegundoOrden.clicked.connect(self.abrirGraficosMenu)
            self.pasaTodoSegundoOrden.clicked.connect(self.abrirGraficosMenu)
            self.pasaBanda.clicked.connect(self.abrirGraficosMenu)
            self.notch.clicked.connect(self.abrirGraficosMenu)
            
            if self.textoXsiz != "" and self.textoOmegaz != "":
                self.highPassNotch.setEnabled(True)
                self.lowPassNotch.setEnabled(True)    
                self.highPassNotch.clicked.connect(self.abrirGraficosMenu)
                self.lowPassNotch.clicked.connect(self.abrirGraficosMenu)   
            else:
                self.highPassNotch.setEnabled(False)
                self.lowPassNotch.setEnabled(False)  
        else:
            self.pasaAltosSegundoOrden.setEnabled(False)
            self.pasaBajosSegundoOrden.setEnabled(False)
            self.pasaTodoSegundoOrden.setEnabled(False)
            self.pasaBanda.setEnabled(False)
            self.notch.setEnabled(False)

###Estos metodos  corren el indice de la pestaña en la que estoy···
    def abrirMainMenu(self):
        self.mainMenu.setCurrentIndex(0)

    def abrirPrimerOrdenMenu(self):
        self.mainMenu.setCurrentIndex(1)

    def abrirSegundoOrdenMenu(self):
        self.mainMenu.setCurrentIndex(2)

    def abrirGraficosMenu(self):
        self.mainMenu.setCurrentIndex(3)

###Este metodo es para graficar la salida a cierta entrada, cambia los datos pedidos segun la entrada que se le requiera###
    def entradaUsuario(self, text):
        if text == "Senoide":
            self.dependeDeEntrada.setCurrentIndex(0)
        elif text == "Escalon unitario":
            self.dependeDeEntrada.setCurrentIndex(1)
        elif text == "Pulso periódico":
            self.dependeDeEntrada.setCurrentIndex(2)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = ElectroGUI()
    qt_app.show()
    sys.exit(app.exec_())
    