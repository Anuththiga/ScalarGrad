# -*- coding: utf-8 -*-

# Commented out IPython magic to ensure Python compatibility.
import math
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# scalar value function
def f(x):
  return 3*x**2 - 4*x + 5

xs = np.arange(-5, 5, 0.25)
ys = f(xs)
plt.plot(xs, ys)

# find the derivative of a simple function
h = 0.000001
x = 2/3
(f(x + h) - f(x))/h