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
        self.textoGananciaMax = "0"
        self.textoGananciaBanda = "0"
        self.textoFrec = "0"
        self.textoXsi = "0"
        self.textoXsiz = "0"
        self.textoWz = "0"

        #######Menu principal#######
        self.primerOrden.clicked.connect(self.abrirPrimerOrdenMenu)
        self.segundoOrden.clicked.connect(self.abrirSegundoOrdenMenu)
        self.returnButton.clicked.connect(self.abrirMainMenu)

        #######Menu de primer orden#######
        self.pasaAltosPrimerOrden.setEnabled(False)
        self.pasaBajosPrimerOrden.setEnabled(False)
        self.pasaTodoPrimerOrden.setEnabled(False)
        self.frecPrimerOrden.textChanged.connect(self.guardarTextoFrecOrden1)
        self.gananciaMaxPrimerOrden.textChanged.connect(self.guardartextoGananciaMaxOrden1)
        self.gananciaBandaPrimerOrden.textChanged.connect(self.guardarTextoGananciaBandaOrden1)

        #######Menu de segundo orden######
        self.pasaAltosSegundoOrden.setEnabled(False)
        self.pasaBajosSegundoOrden.setEnabled(False)
        self.pasaTodoSegundoOrden.setEnabled(False)
        self.pasaBanda.setEnabled(False)
        self.notch.setEnabled(False)
        self.lowPassNotch.setEnabled(False)
        self.highPassNotch.setEnabled(False)
        self.frecSegundoOrden.textChanged.connect(self.guardarTextoFrecOrden2)
        self.gananciaMaxSegundoOrden.textChanged.connect(self.guardartextoGananciaMaxOrden2)
        self.gananciaBandaSegundoOrden.textChanged.connect(self.guardarTextoGananciaBandaOrden2)
        self.xsi.textChanged.connect(self.guardarTextoXsi)
        self.omegaz.textChanged.connect(self.guardarTextoOmegaz)
        self.xsiz.textChanged.connect(self.guardarTextoXsiz)

        #######Menu de graficos#######
        self.entrada.currentTextChanged.connect(self.entradaUsuario)
        self.graficarSalida.clicked.connect(self.mostrarGraficoSalida)
        self.graficarBode.clicked.connect(self.mostrarGraficoBode)
    
###Estos metodos guardan el texto ingresado por el usuario en sus respectivas variables###
    def guardarTextoFrecOrden1 (self,text):
        self.textoFrec = text
        self.activarBotones1()

    def guardartextoGananciaMaxOrden1(self,text):
        self.textoGananciaMax = text
        self.activarBotones1()
    
    def guardarTextoGananciaBandaOrden1(self,text):
        self.textoGananciaBanda = text
        self.activarBotones1()

    def guardarTextoFrecOrden2(self,text):
        self.textoFrec = text
        self.activarBotones2()

    def guardartextoGananciaMaxOrden2(self,text):
        self.textoGananciaMax = text
        self.activarBotones2()

    def guardarTextoGananciaBandaOrden2(self,text):
        self.textoGananciaBanda = text 
        self.activarBotones2()
    
    def guardarTextoXsi(self,text):
        self.textoXsi = text
        self.activarBotones2()

    def guardarTextoOmegaz(self,text):
        self.textoWz = text
        self.activarBotones2()

    def guardarTextoXsiz(self,text):
        self.textoXsiz = text
        self.activarBotones2()

###Estos metodos activan y desactivan los botones para seleccionar un filtro solo si los datos requeridos fueron ingresados###
    def activarBotones1(self):
        if self.textoFrec != "0" and self.textoFrec != "" and ((self.textoGananciaMax != "0" and self.textoGananciaMax != "") or (self.textoGananciaBanda != "0" and self.textoGananciaBanda != "")):
            if self.textoGananciaMax != "0" and self.textoGananciaMax != "":
                self.gananciaBandaPrimerOrden.setEnabled(False)
                self.pasaAltosPrimerOrden.setEnabled(True)
                self.pasaBajosPrimerOrden.setEnabled(True)
                self.pasaTodoPrimerOrden.setEnabled(True)
                self.pasaAltosPrimerOrden.clicked.connect(self.abrirGraficosMenu)
                self.pasaAltosPrimerOrden.clicked.connect(self.setHighPass)
                self.pasaBajosPrimerOrden.clicked.connect(self.abrirGraficosMenu)
                self.pasaBajosPrimerOrden.clicked.connect(self.setLowPass)
                self.pasaTodoPrimerOrden.clicked.connect(self.abrirGraficosMenu)
                self.pasaTodoPrimerOrden.clicked.connect(self.setPassAll)
            else:
                self.gananciaBandaPrimerOrden.setEnabled(True)
                if self.textoGananciaBanda != "0" and self.textoGananciaBanda != "":
                    self.gananciaMaxPrimerOrden.setEnabled(False)
                    self.pasaAltosPrimerOrden.setEnabled(True)
                    self.pasaBajosPrimerOrden.setEnabled(True)
                    self.pasaTodoPrimerOrden.setEnabled(True)
                    self.pasaAltosPrimerOrden.clicked.connect(self.abrirGraficosMenu)
                    self.pasaAltosPrimerOrden.clicked.connect(self.setHighPass)
                    self.pasaBajosPrimerOrden.clicked.connect(self.abrirGraficosMenu)
                    self.pasaBajosPrimerOrden.clicked.connect(self.setLowPass)
                    self.pasaTodoPrimerOrden.clicked.connect(self.abrirGraficosMenu)
                    self.pasaTodoPrimerOrden.clicked.connect(self.setPassAll)
                else:
                    self.gananciaMaxPrimerOrden.setEnabled(True)
        else:
            self.gananciaBandaPrimerOrden.setEnabled(True)
            self.gananciaMaxPrimerOrden.setEnabled(True)
            self.pasaAltosPrimerOrden.setEnabled(False)
            self.pasaBajosPrimerOrden.setEnabled(False)
            self.pasaTodoPrimerOrden.setEnabled(False)

    def activarBotones2(self):
        if self.textoFrec != "0" and self.textoXsi != "0" and self.textoXsi != "" and self.textoFrec != "" and ((self.textoGananciaMax != "0" and self.textoGananciaMax != "") or (self.textoGananciaBanda != "0" and self.textoGananciaBanda != "")) :
            if self.textoGananciaBanda != "0" and self.textoGananciaBanda != "":
                self.gananciaMaxSegundoOrden.setEnabled(False)
                self.pasaAltosSegundoOrden.setEnabled(True)
                self.pasaBajosSegundoOrden.setEnabled(True)
                self.pasaTodoSegundoOrden.setEnabled(True)
                self.pasaBanda.setEnabled(True)
                self.notch.setEnabled(True)    
                self.pasaAltosSegundoOrden.clicked.connect(self.abrirGraficosMenu)
                self.pasaAltosSegundoOrden.clicked.connect(self.setHighPass)
                self.pasaBajosSegundoOrden.clicked.connect(self.abrirGraficosMenu)
                self.pasaBajosSegundoOrden.clicked.connect(self.setLowPass)
                self.pasaTodoSegundoOrden.clicked.connect(self.abrirGraficosMenu)
                self.pasaTodoSegundoOrden.clicked.connect(self.setPassAll)
                self.pasaBanda.clicked.connect(self.abrirGraficosMenu)
                self.pasaBanda.clicked.connect(self.setBandPass)
                self.notch.clicked.connect(self.abrirGraficosMenu)
                self.notch.clicked.connect(self.setNotch)
            else:
                self.gananciaMaxSegundoOrden.setEnabled(True)
                if self.textoGananciaMax != "0" and self.textoGananciaMax != "":
                    self.gananciaBandaSegundoOrden.setEnabled(False)
                    self.pasaAltosSegundoOrden.setEnabled(True)
                    self.pasaBajosSegundoOrden.setEnabled(True)
                    self.pasaTodoSegundoOrden.setEnabled(True)
                    self.pasaBanda.setEnabled(True)
                    self.notch.setEnabled(True)    
                    self.pasaAltosSegundoOrden.clicked.connect(self.abrirGraficosMenu)
                    self.pasaAltosSegundoOrden.clicked.connect(self.setHighPass)
                    self.pasaBajosSegundoOrden.clicked.connect(self.abrirGraficosMenu)
                    self.pasaBajosSegundoOrden.clicked.connect(self.setLowPass)
                    self.pasaTodoSegundoOrden.clicked.connect(self.abrirGraficosMenu)
                    self.pasaTodoSegundoOrden.clicked.connect(self.setPassAll)
                    self.pasaBanda.clicked.connect(self.abrirGraficosMenu)
                    self.pasaBanda.clicked.connect(self.setBandPass)
                    self.notch.clicked.connect(self.abrirGraficosMenu)
                    self.notch.clicked.connect(self.setNotch)
                else:
                    self.gananciaBandaSegundoOrden.setEnabled(True)
            
            if self.textoXsiz != "0" and self.textoWz != "0" and self.textoXsiz != "" and self.textoWz != "":
                self.highPassNotch.setEnabled(True)
                self.lowPassNotch.setEnabled(True)    
                self.highPassNotch.clicked.connect(self.abrirGraficosMenu)
                self.highPassNotch.clicked.connect(self.setHighPassNotch)
                self.lowPassNotch.clicked.connect(self.abrirGraficosMenu)   
                self.lowPassNotch.clicked.connect(self.setLowPassNotch)
            else:
                self.highPassNotch.setEnabled(False)
                self.lowPassNotch.setEnabled(False)  
        else:
            self.gananciaBandaSegundoOrden.setEnabled(True)
            self.gananciaMaxSegundoOrden.setEnabled(True)
            self.pasaAltosSegundoOrden.setEnabled(False)
            self.pasaBajosSegundoOrden.setEnabled(False)
            self.pasaTodoSegundoOrden.setEnabled(False)
            self.pasaBanda.setEnabled(False)
            self.notch.setEnabled(False)
            self.highPassNotch.setEnabled(False)
            self.lowPassNotch.setEnabled(False)  

###Estos metodos  corren el indice de la pestaña en la que estoy···
    def abrirMainMenu(self):
        self.mainMenu.setCurrentIndex(0)
        self.textoGananciaMax = "0"
        self.textoGananciaBanda = "0"
        self.textoFrec = "0"
        self.textoXsi = "0"
        self.textoXsiz = "0"
        self.textoWz = "0"
        self.frecPrimerOrden.clear()
        self.gananciaMaxPrimerOrden.clear()
        self.frecSegundoOrden.clear()
        self.gananciaMaxSegundoOrden.clear()
        self.gananciaBandaPrimerOrden.clear()
        self.gananciaBandaSegundoOrden.clear()
        self.xsi.clear()
        self.xsiz.clear()
        self.omegaz.clear()

    def abrirPrimerOrdenMenu(self):
        self.mainMenu.setCurrentIndex(1)
        self.miGraficador.setOrder(1)

    def abrirSegundoOrdenMenu(self):
        self.mainMenu.setCurrentIndex(2)
        self.miGraficador.setOrder(2)

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

###Estos metodos se comunican con mi graficador para generar los graficos al presionar la tecla graficar###
    def mostrarGraficoSalida(self):
        if self.entrada.currentIndex() == 0: ##estoy en senoidal
            self.miGraficador.plotResponseToSine([float(self.frecEntradaSen.text()), float(self.ampEntradaSen.text()), float(self.textoGananciaMax),float(self.textoGananciaBanda), float(self.textoFrec), float(self.textoXsi), float(self.textoWz), float(self.textoXsiz)])
        elif self.entrada.currentIndex() == 1: ##estoy en escalon
            self.miGraficador.plotResponseToHeaviside([float(self.ampEntradaEscalon.text()), float(self.textoGananciaMax),float(self.textoGananciaBanda),float(self.textoFrec), float(self.textoXsi), float(self.textoWz), float(self.textoXsiz)])
        elif self.entrada.currentIndex() == 2: ##estoy en pulso
            self.miGraficador.plotResponseToPulseTrain([float(self.frecEntradaPulso.text()),float(self.ampEntradaPulso.text()), float(self.dutyCycle.text()), float(self.textoGananciaMax),float(self.textoGananciaBanda),float(self.textoFrec), float(self.textoXsi), float(self.textoWz), float(self.textoXsiz)])
        self.ampEntradaEscalon.clear()
        self.frecEntradaSen.clear()
        self.ampEntradaSen.clear()
        self.dutyCycle.clear()
        self.ampEntradaPulso.clear()
   
    def mostrarGraficoBode(self):
        if self.eje_x.currentText() == "Hz":
           hertz = True
        else:
            hertz = False
        if self.eje_y.currentText() == "dBs":
            db = True
        else:
            db = False
        self.miGraficador.setGainUnit(db)
        self.miGraficador.setFrequencyUnit(hertz)
        self.miGraficador.plotBode([float(self.textoGananciaMax), float(self.textoGananciaBanda), float(self.textoFrec), float(self.textoXsi), float(self.textoWz), float(self.textoXsiz)])

    def setHighPass(self):
        self.miGraficador.setType("HIGH_PASS")

    def setLowPass(self):
        self.miGraficador.setType("LOW_PASS")

    def setPassAll(self):
        self.miGraficador.setType("PASS_ALL")

    def setBandPass(self):
        self.miGraficador.setType("BAND_PASS")

    def setNotch(self):
        self.miGraficador.setType("NOTCH")

    def setHighPassNotch(self):
        self.miGraficador.setType("HIGH_PASS_NOTCH")

    def setLowPassNotch(self):
        self.miGraficador.setType("LOW_PASS_NOTCH")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = ElectroGUI()
    qt_app.show()
    sys.exit(app.exec_())
    