from scipy import signal
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
        self.G = 0
        self.wp = 0
        self.E = 0
        self.wz = 0
        self.Ez = 0


    def firstOrderFilter(self, filterType: str, parameters: list):
        '''
        Detects filter type and calls corresponding method to initialise self.sys
        '''
        self.G = parameters[0]
        self.wp = parameters[1]*2*numpy.pi

        if filterType == 'HIGH_PASS':
            self.fstOrderHighPass(self.G, self.wp)
            return True
        elif filterType == 'LOW_PASS':
            self.fstOrderLowPass(self.G, self.wp)
            return True
        elif filterType == 'ALL_PASS':
            self.fstOrderAllPass(self.G, self.wp)
            return True
        else:
            return False


    def secondOrderFilter(self,filterType: str, parameters: list):
        '''
        Detects filter type and calls corresponding method to initialise self.sys
        '''
        self.G = parameters[0]
        self.wp = parameters[1]*2*numpy.pi
        self.E = parameters[2]
        self.wz = parameters[3]*2*numpy.pi
        self.Ez = parameters[4]

        if filterType == 'HIGH_PASS':
            self.sndOrderHighPass(self.G, self.wp, self.E)
            return True
        elif filterType == 'LOW_PASS':
            self.sndOrderLowPass(self.G, self.wp, self.E)
            return True
        elif filterType == 'ALL_PASS':
            self.sndOrderAllPass(self.G, self.wp, self.E)
            return True
        elif filterType == 'BAND_PASS':
            self.sndOrderBandPass(self.G, self.wp, self.E)
            return True
        elif filterType == 'NOTCH':
            self.sndOrderNotch(self.G, self.wp, self.E)
            return True
        elif filterType == 'LOW_PASS_NOTCH':
            self.sndOrderLowPassNotch(self.G, self.wp, self.E, self.wz, self.Ez)
            return True
        elif filterType == 'HIGH_PASS_NOTCH':
            self.sndOrderHighPassNotch(self.G, self.wp, self.E, self.wz, self.Ez)
            return True
        else:
            return False


    def fstOrderLowPass(self, G, wp):
        '''
        Sets self.sys as a first order low-pass filter who's transfer function is:
        H(s) = K/((s/wp)+1)
        '''
        K = G
        self.sys = signal.lti([K], [1/wp, 1])


    def fstOrderHighPass(self, G, wp):
        '''
        Sets self.sys as a first order high-pass filter who's transfer function is:
        H(s) = K*s/((s/wp)+1)
        '''
        K = G / wp
        self.sys = signal.lti([K, 0], [1/wp, 1])


    def fstOrderAllPass(self, G, wp):
        '''
        Sets self.sys as a first order all-pass filter who's transfer function is:
        H(s) = K*((s/wp)-1)/((s/wp)+1)
        '''
        K = G
        self.sys = signal.lti([K/wp, -K], [1/wp, 1])


    def sndOrderLowPass(self, G, wp, E):
        '''
        Sets self.sys as a second order low-pass filter who's transfer function is:
        H(s) = K/((s/wp)^2+2(E/wp)*s+1)
        '''
        K = G
        self.sys = signal.lti([K], [(1/wp)**2, 2*(E/wp), 1])


    def sndOrderHighPass(self, G, wp, E):
        '''
        Sets self.sys as a second order high-pass filter who's transfer function is:
        H(s) = K*s^2/((s/wp)^2+2(E/wp)*s+1)
        '''
        K = G / (wp**2)
        self.sys = signal.lti([K, 0, 0], [(1/wp)**2, 2*(E/wp), 1])


    def sndOrderAllPass(self, G, wp, E):
        '''
        Sets self.sys as a second order all-pass filter who's transfer function is:
        H(s) = K*((s/wp)^2-2(E/wp)*s+1)/((s/wp)^2+2(E/wp)*s+1)
        '''
        K = G
        self.sys = signal.lti([K*((1/wp)**2), -K*2*(E/wp), K], [(1/wp)**2, 2*(E/wp), 1])


    def sndOrderBandPass(self, G, w0, E):
        '''
        Sets self.sys as a second order band-pass filter who's transfer function is:
        H(s) = K*s/((s/wp)^2+2(E/wp)*s+1)
        '''
        K = 2*E*G/w0
        self.sys = signal.lti([K, 0], [(1/w0)**2, 2*(E/w0), 1])


    def sndOrderNotch(self, G, wp, E):
        '''
        Sets self.sys as a second order notch filter who's transfer function is:
        H(s) = K*((s/wp)^2+1)/((s/wp)^2+2(E/wp)*s+1)
        '''
        K = G
        self.sys = signal.lti([K*((1/wp)**2), K], [(1/wp)**2, 2*(E/wp), 1])


    def sndOrderLowPassNotch(self, G, wp, E, wz, Ez):
        '''
        Sets self.sys as a second order low-pass notch filter who's transfer function is:
        H(s) = K*((s/wz)^2+2(Ez/wz)*s+1)/((s/wp)^2+2(E/wp)*s+1)
        wz > wp WILL BE VALIDATED
        '''
        K = G
        self.sys = signal.lti([K*((1/wz)**2), K*2*(Ez/wz), K], [(1/wp)**2, 2*(E/wp), 1])


    def sndOrderHighPassNotch(self, G, wp, E, wz, Ez):
        '''
        Sets self.sys as a second order low-pass notch filter who's transfer function is:
        H(s) = K*((s/wz)^2+2(Ez/wz)*s+1)/((s/wp)^2+2(E/wp)*s+1)
        wz < wp WILL BE VALIDATED
        '''
        K = G * (wz / wp)**2
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
        t = numpy.linspace(0, 10*(1/f), 5000)
        x = A*numpy.sin(2 * numpy.pi * f * t)

        return self.sys.output(x, t)

    
    def getResponseToHeaviside(self, A):
        '''
        Returns data to plot a time response to a heaviside function of amplitude A as a 
        3-tuple with T (1D ndarray with the time values for the output), yout (1D ndarray 
        with the system's response) and xout (ndarray the time evolution of the state vector)
        '''
        t = numpy.linspace(0, 5*(1/self.wp), 5000)
        x = A * (numpy.sign(t) + 1)

        return self.sys.output(x, t)


    def getResponseToPulseTrain(self, A, dc):
        '''
        Returns data to plot a time response to a pulse train of amplitude A as a 
        3-tuple with T (1D ndarray with the time values for the output), yout (1D ndarray 
        with the system's response) and xout (ndarray the time evolution of the state vector)
        '''
        t = numpy.linspace(0, 10*(1/f), 5000)
        x=signal.square(2 * numpy.pi * f * t, dc)

        return self.sys.output(x, t)


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
    