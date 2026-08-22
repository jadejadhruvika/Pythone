from pylab import *
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y = np.sin(x)

figure()
plot(x, y, color='blue', linewidth=2)
title("Sine Curve")
xlabel("x")
ylabel("sin(x)")
grid(True)

axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)

show()
