from scipy import signal
from sympy.solvers import solve
from sympy import Symbol
import numpy

class FiltersCalculator:
    '''
    Calculates the necessary data to plot graphs for first and second order filters (G is the gain).
    - To create first order filters:
        myFilterCalculator.firstOrderFilter('HIGH_PASS', [G, wp])
        myFilterCalculator.firstOrderFilter('LOW_PASS', [G, wp])
        myFilterCalculator.firstOrderFilter('ALL_PASS', [G, wp])
    - To create second order filters:
        myFilterCalculator.secondOrderFilter('HIGH_PASS', [G, wp, E])
        myFilterCalculator.secondOrderFilter('LOW_PASS', [G, wp, E])
        myFilterCalculator.secondOrderFilter('ALL_PASS', [G, wp, E])
        myFilterCalculator.secondOrderFilter('BAND_PASS', [G, w0, E])
        myFilterCalculator.secondOrderFilter('NOTCH', [G, wp, E])
        myFilterCalculator.secondOrderFilter('LOW_PASS_NOTCH', [G, wp, E, wz, Ez])
        myFilterCalculator.secondOrderFilter('HIGH_PASS_NOTCH', [G, wp, E, wz, Ez])
    - To get the data for the response to:
        Sine of frequency f and amplitude A: 
            t, y, xout = myFilterCalculator.getResponseToSine(f, A)
        Impulse of amplitude A: 
            t, y = myFilterCalculator.getResponseToImpulse(A)
        Pulse of amplitude A and duty cycle dc: 
            t, y = myFilterCalculator.getResponseToPulse(A, dc)
    - To get the data for the bode graph:
        w, g, phase = myFilterCalculator.getBode(usingHertz, usingdB)
    '''

    def __init__(self):
        self.sys = 0 #Set as 0 just for initialisation.
        self.maxG = 0
        self.bandG = 0
        self.wp = 0
        self.E = 0
        self.wz = 0
        self.Ez = 0


    def firstOrderFilter(self, filterType: str, parameters: list):
        '''
        Detects filter type and calls corresponding method to initialise self.sys
        '''
        self.maxG = parameters[0]
        self.bandG = parameters[1]
        self.wp = parameters[2]*2*numpy.pi

        if filterType == 'HIGH_PASS':
            self.fstOrderHighPass(self.maxG, self.bandG, self.wp)
            return True
        elif filterType == 'LOW_PASS':
            self.fstOrderLowPass(self.maxG, self.bandG, self.wp)
            return True
        elif filterType == 'ALL_PASS':
            self.fstOrderAllPass(self.maxG, self.bandG, self.wp)
            return True
        else:
            return False


    def secondOrderFilter(self,filterType: str, parameters: list):
        '''
        Detects filter type and calls corresponding method to initialise self.sys
        '''
        self.maxG = parameters[0]
        self.bandG = parameters[1]
        self.wp = parameters[2]*2*numpy.pi
        self.E = parameters[3]
        self.wz = parameters[4]*2*numpy.pi
        self.Ez = parameters[5]

        if filterType == 'HIGH_PASS':
            self.sndOrderHighPass(self.maxG, self.bandG, self.wp, self.E)
            return True
        elif filterType == 'LOW_PASS':
            self.sndOrderLowPass(self.maxG, self.bandG, self.wp, self.E)
            return True
        elif filterType == 'ALL_PASS':
            self.sndOrderAllPass(self.maxG, self.bandG, self.wp, self.E)
            return True
        elif filterType == 'BAND_PASS':
            self.sndOrderBandPass(self.maxG, self.bandG, self.wp, self.E)
            return True
        elif filterType == 'NOTCH':
            self.sndOrderNotch(self.maxG, self.bandG, self.wp, self.E)
            return True
        elif filterType == 'LOW_PASS_NOTCH':
            if self.wz > self.wp:
                self.sndOrderLowPassNotch(self.maxG, self.bandG, self.wp, self.E, self.wz, self.Ez)
                return True
            else:
                return False
        elif filterType == 'HIGH_PASS_NOTCH':
            if self.wz < self.wp:
                self.sndOrderHighPassNotch(self.maxG, self.bandG, self.wp, self.E, self.wz, self.Ez)
                return True
            else:
                return False
        else:
            return False


    def fstOrderLowPass(self, maxG, bandG, wp):
        '''
        Sets self.sys as a first order low-pass filter who's transfer function is:
        H(s) = K/((s/wp)+1)
        '''

        if maxG != 0 and maxG != '':
            K = maxG
        else:
            K = bandG

        self.sys = signal.lti([K], [1/wp, 1])


    def fstOrderHighPass(self, maxG, bandG, wp):
        '''
        Sets self.sys as a first order high-pass filter who's transfer function is:
        H(s) = K*s/((s/wp)+1)
        '''

        if maxG != 0 and maxG != '':
            K = maxG / wp
        else:
            K = bandG / wp

        self.sys = signal.lti([K, 0], [1/wp, 1])


    def fstOrderAllPass(self, maxG, bandG, wp):
        '''
        Sets self.sys as a first order all-pass filter who's transfer function is:
        H(s) = K*((s/wp)-1)/((s/wp)+1)
        '''

        if maxG != 0 and maxG != '':
            K = maxG
        else:
            K = bandG

        self.sys = signal.lti([K/wp, -K], [1/wp, 1])


    def sndOrderLowPass(self, maxG, bandG, wp, E):
        '''
        Sets self.sys as a second order low-pass filter who's transfer function is:
        H(s) = K/((s/wp)^2+2(E/wp)*s+1)
        '''
        Q = 1 / (2*E)
        rootOfB = (wp**2 * numpy.sqrt(1 - 1 / (4 * Q**2))) / Q
        if maxG != 0 and maxG != '':
            if numpy.isnan(rootOfB):
                K = maxG
            else:
                a0 = Symbol('a0', positive=True)
                K = float(solve( a0 * wp**2 / rootOfB - maxG , a0)[0])
        else:
            K = bandG

        self.sys = signal.lti([K], [(1/wp)**2, 2*(E/wp), 1])


    def sndOrderHighPass(self, maxG, bandG, wp, E):
        '''
        Sets self.sys as a second order high-pass filter who's transfer function is:
        H(s) = K*s^2/((s/wp)^2+2(E/wp)*s+1)
        '''
        Q = 1 / (2*E)
        rootOfB = (numpy.sqrt(1 - 1 / (4 * Q**2))) / Q
        if maxG != 0 and maxG != '':
            if numpy.isnan(rootOfB):
                K = maxG / (wp**2)
            else:
                a0 = Symbol('a0', positive=True)
                K = float(solve( a0 * wp**2 / rootOfB - maxG , a0)[0])
        else:
            K = bandG / (wp**2)
            
        self.sys = signal.lti([K, 0, 0], [(1/wp)**2, 2*(E/wp), 1])


    def sndOrderAllPass(self, maxG, bandG, wp, E):
        '''
        Sets self.sys as a second order all-pass filter who's transfer function is:
        H(s) = K*((s/wp)^2-2(E/wp)*s+1)/((s/wp)^2+2(E/wp)*s+1)
        '''
        if maxG != 0 and maxG != '':
            K = maxG
        else:
            K = bandG

        self.sys = signal.lti([K*((1/wp)**2), -K*2*(E/wp), K], [(1/wp)**2, 2*(E/wp), 1])


    def sndOrderBandPass(self, maxG, bandG, w0, E):
        '''
        Sets self.sys as a second order band-pass filter who's transfer function is:
        H(s) = K*s/((s/wp)^2+2(E/wp)*s+1)
        '''
        Q = 1 / (2*E)
        rootOfB = w0 / Q
        if maxG != 0 and maxG != '':
            if numpy.isnan(rootOfB):
                K = 2*E*maxG/w0
            else:
                a0 = Symbol('a0', positive=True)
                K = float(solve( a0 * w0**2 / rootOfB - maxG , a0)[0])
        else:
            K = 2*E*bandG/w0

        self.sys = signal.lti([K, 0], [(1/w0)**2, 2*(E/w0), 1])


    def sndOrderNotch(self, maxG, bandG, wp, E):
        '''
        Sets self.sys as a second order notch filter who's transfer function is:
        H(s) = K*((s/wp)^2+1)/((s/wp)^2+2(E/wp)*s+1)
        '''
        if maxG != 0 and maxG != '':
            K = maxG
        else:
            K = bandG

        self.sys = signal.lti([K*((1/wp)**2), 0, K], [(1/wp)**2, 2*(E/wp), 1])


    def sndOrderLowPassNotch(self, maxG, bandG, wp, E, wz, Ez):
        '''
        Sets self.sys as a second order low-pass notch filter who's transfer function is:
        H(s) = K*((s/wz)^2+2(Ez/wz)*s+1)/((s/wp)^2+2(E/wp)*s+1)
        wz > wp WILL BE VALIDATED
        '''
        Q = 1 / (2*E)
        badassSquareRoot = numpy.sqrt( ((1 - (wz / wp)**2)**2 + (1 / (Q**2)) * (wz / wp)**2) / (1 - (1 / (4 * Q**2))))
        if maxG != 0 and maxG != '':
            if numpy.isnan(badassSquareRoot):
                K = maxG
            else:
                a0 = Symbol('a0', positive=True)
                K = float(solve( a0 * wp**2 * Q * badassSquareRoot - maxG , a0)[0])
        else:
            K = bandG

        self.sys = signal.lti([K*((1/wz)**2), K*2*(Ez/wz), K], [(1/wp)**2, 2*(E/wp), 1])


    def sndOrderHighPassNotch(self, maxG, bandG, wp, E, wz, Ez):
        '''
        Sets self.sys as a second order low-pass notch filter who's transfer function is:
        H(s) = K*((s/wz)^2+2(Ez/wz)*s+1)/((s/wp)^2+2(E/wp)*s+1)
        wz < wp WILL BE VALIDATED
        '''
        Q = 1 / (2*E)
        badassSquareRoot = numpy.sqrt( ((1 - (wz / wp)**2)**2 + (1 / (Q**2)) * (wz / wp)**2) / (1 - (1 / (4 * Q**2))))
        if maxG != 0 and maxG != '':
            if numpy.isnan(badassSquareRoot):
                K = maxG * (wz / wp)**2
            else:
                a0 = Symbol('a0', positive=True)
                K = float(solve( a0 * wp**2 * Q * badassSquareRoot - maxG , a0)[0])
        else:
            K = bandG * (wz / wp)**2

        self.sys = signal.lti([K*((1/wz)**2), K*2*(Ez/wz), K], [(1/wp)**2, 2*(E/wp), 1])


    def getBode(self, usingHertz: bool, usingdB: bool):
        '''
        Returns data to plot a bode graph for the current system in self.sys as a 
        3-tuple containing arrays of frequencies [rad/s], magnitude [dB] and phase [deg]
        '''
        w, g, phase = self.sys.bode()
        if usingHertz:
            w = w/(2*numpy.pi)
        if not usingdB:
            g = numpy.e**(g/20)

        return w, g, phase


    def getResponseToSine(self, f, A):
        '''
        Returns data to plot a time response to a sine of frequency f and amplitude A as a 
        3-tuple with T (1D ndarray with the time values for the output), yout (1D ndarray 
        with the system's response) and xout (ndarray the time evolution of the state vector)
        '''
        t = numpy.linspace(0, 10*(1/f), 13000)
        x = A*numpy.sin(2 * numpy.pi * f * t)

        return x, self.sys.output(x, t)

    
    def getResponseToHeaviside(self, A):
        '''
        Returns data to plot a time response to a heaviside function of amplitude A as a 
        3-tuple with T (1D ndarray with the time values for the output), yout (1D ndarray 
        with the system's response) and xout (ndarray the time evolution of the state vector)
        '''
        t = numpy.linspace(-(1/self.wp), 5*(1/self.wp), 5000)
        x = A * (numpy.sign(t) + 1)

        return x, self.sys.output(x, t)


    def getResponseToPulseTrain(self, f, A, dc):
        '''
         Returns data to plot a time response to a pulse train of amplitude A, frequency f and
        duty cycle dc, as a 3-tuple with T (1D ndarray with the time values for the output),
        yout (1D ndarray with the system's response) and xout (ndarray the time evolution of
        the state vector)
        '''
        t = numpy.linspace(-(1/f), 10*(1/f), 5000)
        x=signal.square(2 * numpy.pi * f * t, dc)

        return x, self.sys.output(x, t)


    def getResponseToImpulse(self, A):
        '''
        Returns data to plot a time response to an impulse of amplitude A as a
        2-tuple with T (a 1-D array of time points) and yout (a 1-D array containing 
        the response of the system to the impulse (except for singularities at zero))
        '''
        return self.sys.impulse()


    def getResponseToPulse(self, A, dc):
        '''
        Returns data to plot a time response to a pulse of amplitude A and duty cycle dc as a
        2-tuple with T (1D ndarray with the time values for the output) and yout (1 ndarray 
        with the system's response to the step)
        '''
        return self.sys.step()
    