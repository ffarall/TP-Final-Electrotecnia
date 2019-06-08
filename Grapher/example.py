from scipy import signal
import matplotlib.pyplot as plt
import numpy

'''sys = signal.lti([1], [1, 1])
w, mag, phase = sys.bode()

#w = w/(2*numpy.pi)

plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.show()'''

N = 100 # sample count
P = 10  # period
t = numpy.linspace(0, 1, 500, endpoint=False)
x = 1 * signal.square(2 * numpy.pi * 5 * t)

plt.plot(t, x)
plt.show()

Fs = 700
sample = 70
t = numpy.linspace(0, 1, 500, endpoint=False)
x = 1 * 0.5 * (numpy.sign(t) + 1)

plt.plot(t, x)
plt.show()
