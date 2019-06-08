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
        myFiltersGrapher.plotResponseToImpulse([A, G, wp, E, wz, Ez])
        myFiltersGrapher.plotResponseTopPulse([A, dc, G, wp, E, wz, Ez])
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
        if self.filterOrder == 1:
            self.calculator.firstOrderFilter(self.filterType, args[2:])
            t, y, out = self.calculator.getResponseToSine(args[0], args[1])
            plt.figure()
            plt.plot(t, y)
            plt.show()

        elif self.filterOrder == 2:
            self.calculator.secondOrderFilter(self.filterType, args[2:])
            t, y = self.calculator.getResponseToSine(args[0], args[1])
            plt.figure()
            plt.plot(t, y)
            plt.show()


    def plotResponseToImpulse(self, args: list):
        if self.filterOrder == 1:
            self.calculator.firstOrderFilter(self.filterType, args[1:])
            t, y = self.calculator.getResponseToImpulse(args[0])
            plt.figure()
            plt.plot(t, y)
            plt.show()

        elif self.filterOrder == 2:
            self.calculator.secondOrderFilter(self.filterType, args[1:])
            t, y = self.calculator.getResponseToImpulse(args[0])
            plt.figure()
            plt.plot(t, y)
            plt.show()


    def plotResponseTopPulse(self, args: list):
        if self.filterOrder == 1:
            self.calculator.firstOrderFilter(self.filterType, args[2:])
            t, y = self.calculator.getResponseToPulse(args[0], args[1])
            plt.figure()
            plt.plot(t, y)
            plt.show()

        elif self.filterOrder == 2:
            self.calculator.secondOrderFilter(self.filterType, args[2:])
            t, y = self.calculator.getResponseToPulse(args[0], args[1])
            plt.figure()
            plt.plot(t, y)
            plt.show()


    def plotBode(self, args: list):
        if self.filterOrder == 1:
            self.calculator.firstOrderFilter(self.filterType, args)
            w, g, phase = self.calculator.getBode(self.usingHertz, self.usingdB)
            plt.figure()
            plt.plot(w, g)
            plt.show()

        elif self.filterOrder == 2:
            self.calculator.secondOrderFilter(self.filterType, args)
            t, y = self.calculator.getBode(self.usingHertz, self.usingdB)
            plt.figure()
            plt.plot(t, y)
            plt.show()


if __name__ == '__main__':
    grapher = FiltersGrapher()
    grapher.plotBode([10, 1, 1, 1, 1])
    grapher.plotResponseToImpulse([1, 10, 1, 1, 1, 1])
    grapher.plotResponseTopPulse([1, 0.5, 10, 1, 1, 1, 1])
    grapher.plotResponseToSine([50, 1, 10, 1, 1, 1, 1])