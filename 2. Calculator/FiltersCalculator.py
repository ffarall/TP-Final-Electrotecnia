from scipy import signal

class FiltersCalculator:
    '''
    Calculates the necessary data to plot graphs for first and second order filters.
    - To create first order filters:
        myFilterCalculator('HIGH_PASS', [K, w0])
        myFilterCalculator('LOW_PASS', [K, w0])
        myFilterCalculator('ALL_PASS', [K, w0])
    - To create second order filters:
        myFilterCalculator('HIGH_PASS', [K, w0])
        myFilterCalculator('LOW_PASS', [K, w0])
        myFilterCalculator('ALL_PASS', [K, w0])
        myFilterCalculator('BAND_PASS', [K, w0])
        myFilterCalculator('NOTCH', [K, w0])
        myFilterCalculator('LOW_PASS_NOTCH', [K, w0])
        myFilterCalculator('HIGH_PASS_NOTCH', [K, w0])
    '''

    def __init__(self):
        self.sys = 0 #Set as 0 just for initialization.

    def firstOrderFilter(self, filterType: str, parameters: list):
        '''
        Detects filter type and calls corresponding method to initialize self.sys
        '''
        if filterType == 'HIGH_PASS':
            self.fstOrderHighPass(parameters[0], parameters[1])
            return True
        elif filterType == 'LOW_PASS':
            self.fstOrderLowPass(parameters[0], parameters[1])
            return True
        elif filterType == 'ALL_PASS':
            self.fstOrderAllPass(parameters[0], parameters[1])
            return True
        else:
            return False

    def secondOrderFilter(self,filterType: str, parameters: list):
        '''
        Detects filter type and calls corresponding method to initialize self.sys
        '''
        if filterType == 'HIGH_PASS':
            self.sndOrderHighPass(parameters[0], parameters[1], parameters[2])
            return True
        elif filterType == 'LOW_PASS':
            self.sndOrderLowPass(parameters[0], parameters[1], parameters[2])
            return True
        elif filterType == 'ALL_PASS':
            self.sndOrderAllPass(parameters[0], parameters[1], parameters[2])
            return True
        elif filterType == 'BAND_PASS':
            self.sndOrderBandPass(parameters[0], parameters[1], parameters[2])
            return True
        elif filterType == 'NOTCH':
            self.sndOrderNotch(parameters[0], parameters[1], parameters[2])
            return True
        elif filterType == 'LOW_PASS_NOTCH':
            self.sndOrderLowPassNotch(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4])
            return True
        elif filterType == 'HIGH_PASS_NOTCH':
            self.sndOrderHighPassNotch(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4])
            return True
        else:
            return False

    def fstOrderLowPass(self, K, wp):
        '''
        Sets self.sys as a first order low-pass filter who's transfer function is:
        H(s) = K/((s/wp)+1)
        '''
        self.sys = signal.lti([K], [1/wp, 1])

    def fstOrderHighPass(self, K, wp):
        '''
        Sets self.sys as a first order high-pass filter who's transfer function is:
        H(s) = K*s/((s/wp)+1)
        '''
        self.sys = signal.lti([K, 0], [1/wp, 1])

    def fstOrderAllPass(self, K, wp):
        '''
        Sets self.sys as a first order all-pass filter who's transfer function is:
        H(s) = K*((s/wp)-1)/((s/wp)+1)
        '''
        self.sys = signal.lti([K/wp, -K], [1/wp, 1])

    def sndOrderLowPass(self, K, wp, E):
        '''
        Sets self.sys as a second order low-pass filter who's transfer function is:
        H(s) = K/((s/wp)^2+2(E/wp)*s+1)
        '''
        self.sys = signal.lti([K], [(1/wp)**2, 2*(E/wp), 1])

    def sndOrderHighPass(self, K, wp, E):
        '''
        Sets self.sys as a second order high-pass filter who's transfer function is:
        H(s) = K*s^2/((s/wp)^2+2(E/wp)*s+1)
        '''
        self.sys = signal.lti([K, 0, 0], [(1/wp)**2, 2*(E/wp), 1])

    def sndOrderAllPass(self, K, wp, E):
        '''
        Sets self.sys as a second order all-pass filter who's transfer function is:
        H(s) = K*((s/wp)^2-2(E/wp)*s+1)/((s/wp)^2+2(E/wp)*s+1)
        '''
        self.sys = signal.lti([K*((1/wp)**2), -K*2*(E/wp), K], [(1/wp)**2, 2*(E/wp), 1])

    def sndOrderBandPass(self, K, wp, E):
        '''
        Sets self.sys as a second order band-pass filter who's transfer function is:
        H(s) = K*s/((s/wp)^2+2(E/wp)*s+1)
        '''
        self.sys = signal.lti([K, 0], [(1/wp)**2, 2*(E/wp), 1])

    def sndOrderNotch(self, K, wp, E):
        '''
        Sets self.sys as a second order notch filter who's transfer function is:
        H(s) = K*((s/wp)^2+1)/((s/wp)^2+2(E/wp)*s+1)
        '''
        self.sys = signal.lti([K*((1/wp)**2), K], [(1/wp)**2, 2*(E/wp), 1])

    def sndOrderLowPassNotch(self, K, wp, E, wz, Ez):
        '''
        Sets self.sys as a second order low-pass notch filter who's transfer function is:
        H(s) = K*((s/wz)^2+2(Ez/wz)*s+1)/((s/wp)^2+2(E/wp)*s+1)
        wz > wp WILL BE VALIDATED
        '''
        self.sys = signal.lti([K*((1/wz)**2), K*2*(Ez/wz), K], [(1/wp)**2, 2*(E/wp), 1])

    def sndOrderHighPassNotch(self, K, wp, E, wz, Ez):
        '''
        Sets self.sys as a second order low-pass notch filter who's transfer function is:
        H(s) = K*((s/wz)^2+2(Ez/wz)*s+1)/((s/wp)^2+2(E/wp)*s+1)
        wz < wp WILL BE VALIDATED
        '''
        self.sys = signal.lti([K*((1/wz)**2), K*2*(Ez/wz), K], [(1/wp)**2, 2*(E/wp), 1])

    def getBode(self, useHertz: bool, usedB: bool):
        '''
        Returns data to plot a bode graph for the current system in self.sys
        '''
        pass

    def getResponseToSine(self, f, A):
        '''
        Returns data to plot a time response to a sine of frequency f and amplitude A
        '''
        pass

    def getResponseToImpulse(self, A):
        '''
        Returns data to plot a time response to an impulse of amplitude A
        '''
        pass

    def getResponseToPulse(self, dc, A):
        '''
        Returns data to plot a time response to a pulse of amplitude A and duty cycle dc
        '''
        pass
    