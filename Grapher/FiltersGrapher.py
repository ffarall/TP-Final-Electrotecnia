import matplotlib.pyplot as plt
import sys
sys.path.insert(0, 'C:/Users/facun/OneDrive/Desktop/ITBA/C4 - Electrotecnia/TP Final')
from Calculator.FiltersCalculator import FiltersCalculator

class FiltersGrapher:
    '''
    Plots one of the given options, following the steps listed:
    Initialize the grapher with the type of filter and order you desire, or select them with myFiltersGrapher.setType('TYPE') and myFiltersGrapher.setOrder(n).
    - First order filter:
        Can be HIGH_PASS, LOW_PASS or ALL_PASS.
    - Second order filter:
        Can be HIGH_PASS, LOW_PASS, ALL_PASS, BAND_PASS, NOTCH, LOW_PASS_NOTCH, HIGH_PASS_NOTCH.
    - Plot like this:
        myFiltersGrapher.plotResponseToSine([f, A, G, wp, E, wz, Ez])
        myFiltersGrapher.plotResponseToHeaviside([A, G, wp, E, wz, Ez])
        myFiltersGrapher.plotResponseToImpulse([A, G, wp, E, wz, Ez])
        myFiltersGrapher.plotResponseToPulse([A, dc, G, wp, E, wz, Ez])
        myFiltersGrapher.plotResponseToPulseTrain([A, dc, G, wp, E, wz, Ez])
        myFiltersGrapher.plotBode([G, wp, E, wz, Ez])
        E is necessary for all second order filters.
        wz and Ez are only needed when type is LOW_PASS_NOTCH or HIGH_PASS_NOTCH.
    '''

    def __init__(self, filterType='HIGH_PASS', order=1, usingHertz=True, usingdB=True):
        self.filterType = filterType
        self.filterOrder = order
        self.usingHertz = usingHertz
        self.usingdB = usingdB
        self.calculator = FiltersCalculator()


    def setType(self, filterType):
        self.filterType = filterType


    def setOrder(self, order):
        self.filterOrder = order


    def setFrequencyUnit(self, usingHertz: bool):
        self.usingHertz = usingHertz


    def setGainUnit(self, usingdB: bool):
        self.usingdB = usingdB


    def plotResponseToSine(self, args: list):
        t = 0
        y = 0
        if self.filterOrder == 1:
            self.calculator.firstOrderFilter(self.filterType, args[2:])
            t, y, output = self.calculator.getResponseToSine(args[0], args[1])

        elif self.filterOrder == 2:
            self.calculator.secondOrderFilter(self.filterType, args[2:])
            t, y, output = self.calculator.getResponseToSine(args[0], args[1])

        plt.figure()
        plt.plot(t, y)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Respuesta a senoidal')
        plt.show()

    def plotResponseToImpulse(self, args: list):
        t = 0
        y = 0
        if self.filterOrder == 1:
            self.calculator.firstOrderFilter(self.filterType, args[1:])
            t, y = self.calculator.getResponseToImpulse(args[0])

        elif self.filterOrder == 2:
            self.calculator.secondOrderFilter(self.filterType, args[1:])
            t, y = self.calculator.getResponseToImpulse(args[0])
            
        plt.figure()
        plt.plot(t, y)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Respuesta al impulso')
        plt.show()


    def plotResponseToPulse(self, args: list):
        t = 0
        y = 0
        if self.filterOrder == 1:
            self.calculator.firstOrderFilter(self.filterType, args[2:])
            t, y = self.calculator.getResponseToPulse(args[0], args[1])

        elif self.filterOrder == 2:
            self.calculator.secondOrderFilter(self.filterType, args[2:])
            t, y = self.calculator.getResponseToPulse(args[0], args[1])
            
        plt.figure()
        plt.plot(t, y)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Respuesta al pulso')
        plt.show()


    def plotResponseToHeaviside(self, args: list):
        t = 0
        y = 0
        if self.filterOrder == 1:
            self.calculator.firstOrderFilter(self.filterType, args[1:])
            t, y, output= self.calculator.getResponseToHeaviside(args[0])

        elif self.filterOrder == 2:
            self.calculator.secondOrderFilter(self.filterType, args[1:])
            t, y, output = self.calculator.getResponseToHeaviside(args[0])
            
        plt.figure()
        plt.plot(t, y)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Respuesta al escalón')
        plt.show()


    def plotResponseToPulseTrain(self, args: list):
        t = 0
        y = 0
        if self.filterOrder == 1:
            self.calculator.firstOrderFilter(self.filterType, args[2:])
            t, y, output = self.calculator.getResponseToPulseTrain(args[0], args[1])

        elif self.filterOrder == 2:
            self.calculator.secondOrderFilter(self.filterType, args[2:])
            t, y, output = self.calculator.getResponseToPulseTrain(args[0], args[1])
            
        plt.figure()
        plt.plot(t, y)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Respuesta al tren de pulsos')
        plt.show()


    def plotBode(self, args: list):
        w = 0
        g = 0
        phase = 0
        if self.filterOrder == 1:
            self.calculator.firstOrderFilter(self.filterType, args)
            w, g, phase = self.calculator.getBode(self.usingHertz, self.usingdB)

        elif self.filterOrder == 2:
            self.calculator.secondOrderFilter(self.filterType, args)
            w, g, phase = self.calculator.getBode(self.usingHertz, self.usingdB)

        plt.figure()
        plt.semilogx(w, g)
        if self.usingHertz:
            plt.xlabel('Frecuencia (Hz)')
        else:
            plt.xlabel('Frecuencia (rad/s)')
        if self.usingdB:
            plt.ylabel('Ganancia (dB)')
        else:
            plt.ylabel('Ganancia (respuesta/entrada)')
        plt.show()


if __name__ == '__main__':
    grapher = FiltersGrapher()
    testTypes = ['HIGH_PASS', 'LOW_PASS', 'ALL_PASS']
    for test in testTypes:
        grapher.setType(test)
        grapher.plotBode([20, 1, 1, 1, 1])
        grapher.plotResponseToHeaviside([1, 10, 1, 1, 1, 1])
        grapher.plotResponseToPulseTrain([1, 0.5, 10, 1, 1, 1, 1])
        grapher.plotResponseToSine([50, 1, 10, 1, 1, 1, 1])

    testTypes = ['HIGH_PASS', 'LOW_PASS', 'ALL_PASS', 'BAND_PASS', 'NOTCH', 'LOW_PASS_NOTCH', 'HIGH_PASS_NOTCH']
    grapher.setOrder(2)
    for test in testTypes:
        grapher.setType(test)
        grapher.plotBode([20, 1, 3, 5, 2])
        grapher.plotResponseToHeaviside([1, 10, 1, 3, 5, 2])
        grapher.plotResponseToPulseTrain([1, 0.5, 10, 1, 3, 5, 2])
        grapher.plotResponseToSine([50, 1, 10, 1, 3, 5, 2])