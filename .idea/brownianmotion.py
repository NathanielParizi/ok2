import matplotlib.pyplot as plt
import numpy as np

import math
from matplotlib.pyplot import *
from numpy import *
from numpy.random import standard_normal

T = 2
mu = 0.1
sigma = 0.01
S0 = 20
dt = 0.01
N = round(T/dt)
t = np.linspace(0, T, N)
W = np.random.standard_normal(size = N)
W = np.cumsum(W)*np.sqrt(dt) ### standard brownian motion ###
X = (mu-0.5*sigma**2)*t + sigma*W
S = S0*np.exp(X) ### geometric brownian motion ###
plt.plot(t, S)
plt.show()