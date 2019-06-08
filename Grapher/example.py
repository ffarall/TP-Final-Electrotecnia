from scipy import signal
import matplotlib.pyplot as plt
import numpy

sys = signal.lti([1], [1, 1])
w, mag, phase = sys.bode()

#w = w/(2*numpy.pi)

plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.show()