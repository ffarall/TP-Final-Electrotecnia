import PyQt5 as pyqt
import sys
sys.path.insert(0, 'C:/Users/gonzalo/Desktop/ITBA/ELECTROTECNIA/tp final/TP-Final-Electrotecnia')
import FirstWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Grapher.FiltersGrapher import FiltersGrapher


class ElectroGUI(FirstWindow.Ui_MainWindow, QtWidgets.QMainWindow):
    '''
    Class dedicated to interact with the user using PyQT.
    '''

    def __init__(self):
        super(ElectroGUI,self).__init__()
        self.setupUi(self)
        self.miGraficador = FiltersGrapher()
        ######Variables######    
        self.textoGanancia = "0"
        self.textoFrec = "0"
        self.textoXsi = "0"
        self.textoXsiz = "0"
        self.textoWz = "0"

        #######Menu principal#######
        self.primerOrden.clicked.connect(self.abrirPrimerOrdenMenu)
        self.miGraficador.setOrder(1)
        self.segundoOrden.clicked.connect(self.abrirSegundoOrdenMenu)
        self.miGraficador.setOrder(2)
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
        self.graficarSalida.clicked.connect(self.mostrarGraficoSalida)
        ##self.graficarBode.clicked.connect(self.mostrarGraficoBode)
    
###Estos metodos guardan el texto ingresado por el usuario en sus respectivas variables###
    def guardarTextoFrecOrden1 (self,text):
        self.textoFrec = text
        self.activarBotones1()

    def guardarTextoGananciaOrden1(self,text):
        self.textoGanancia = text
        self.activarBotones1()
    
    def guardarTextoFrecOrden2(self,text):
        self.textoFrec = text
        self.activarBotones2()

    def guardarTextoGananciaOrden2(self,text):
        self.textoGanancia = text
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
        if self.textoFrec != "0" and self.textoGanancia != "0":
            self.pasaAltosPrimerOrden.setEnabled(True)
            self.pasaBajosPrimerOrden.setEnabled(True)
            self.pasaTodoPrimerOrden.setEnabled(True)
            self.pasaAltosPrimerOrden.clicked.connect(self.abrirGraficosMenu)
            self.miGraficador.setType("HIGH_PASS")
            self.pasaBajosPrimerOrden.clicked.connect(self.abrirGraficosMenu)
            self.miGraficador.setType("LOW_PASS")
            self.pasaTodoPrimerOrden.clicked.connect(self.abrirGraficosMenu)
            self.miGraficador.setType("ALL_PASS")
        else:
            self.pasaAltosPrimerOrden.setEnabled(False)
            self.pasaBajosPrimerOrden.setEnabled(False)
            self.pasaTodoPrimerOrden.setEnabled(False)

    def activarBotones2(self):
        if self.textoFrec != "0" and self.textoGanancia != "0" and self.textoXsi != "0":
            self.pasaAltosSegundoOrden.setEnabled(True)
            self.pasaBajosSegundoOrden.setEnabled(True)
            self.pasaTodoSegundoOrden.setEnabled(True)
            self.pasaBanda.setEnabled(True)
            self.notch.setEnabled(True)    
            self.pasaAltosSegundoOrden.clicked.connect(self.abrirGraficosMenu)
            self.miGraficador.setType("HIGH_PASS")
            self.pasaBajosSegundoOrden.clicked.connect(self.abrirGraficosMenu)
            self.miGraficador.setType("LOW_PASS")
            self.pasaTodoSegundoOrden.clicked.connect(self.abrirGraficosMenu)
            self.miGraficador.setType("PASS_ALL")
            self.pasaBanda.clicked.connect(self.abrirGraficosMenu)
            self.miGraficador.setType("BAND_PASS")
            self.notch.clicked.connect(self.abrirGraficosMenu)
            self.miGraficador.setType("NOTCH")
            
            if self.textoXsiz != "" and self.textoOmegaz != "":
                self.highPassNotch.setEnabled(True)
                self.lowPassNotch.setEnabled(True)    
                self.highPassNotch.clicked.connect(self.abrirGraficosMenu)
                self.miGraficador.setType("HIGH_PASS_NOTCH")
                self.lowPassNotch.clicked.connect(self.abrirGraficosMenu)   
                self.miGraficador.setType("LOW_PASS_NOTCH")
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

    def mostrarGraficoSalida(self):
        if self.entrada.currentIndex() == 0: ##estoy en senoidal
            self.miGraficador.plotResponseToSine([float(self.frecEntradaSen.text()), float(self.ampEntradaSen.text()), float(self.textoGanancia), float(self.textoFrec), float(self.textoXsi), float(self.textoWz), float(self.textoXsiz)])
        elif self.entrada.currentIndex() == 1:
            self.miGraficador.plotResponseToHeaviside([float(self.ampEntradaEscalon.text()), float(self.textoGanancia),float(self.textoFrec), float(self.textoXsi), float(self.textoWz), float(self.textoXsiz)])
        elif self.entrada.currentIndex() == 2:
            self.miGraficador.plotResponseToPulseTrain([float(self.ampEntradaPulso.text()), float(self.dutyCycle.text()), float(self.textoGanancia),float(self.textoFrec), float(self.textoXsi), float(self.textoWz), float(self.textoXsiz)])

   ## def mostrarGraficoBode(self):




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = ElectroGUI()
    qt_app.show()
    sys.exit(app.exec_())
    