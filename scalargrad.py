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

h = 0.000001
x = 2/3
(f(x + h) - f(x))/h

# find the derivatives for more complex function
a = 2.0
b = -3.0
c = 10.0
d = a*b + c
d

# find the derivatives with multiple inputs
h = 0.0001

#inputs
a = 2.0
b = -3.0
c = 10.0

d1 = a*b + c
a += h
d2 = a*b + c

print('d1', d1)
print('d2', d2)
print('slope', (d2 - d1)/h)

# core value object
class Value:
  def __init__(self, data, _children=(), _op=''):
    self.data = data
    self._prev = set(_children)
    self._op = _op

  def __repr__(self):
    return f"Value(data={self.data})"

  def __add__(self, other):
    out = Value(self.data + other.data, (self, other), '+')
    return out

  def __mul__(self, other):
    out = Value(self.data * other.data, (self, other), '*')
    return out


a = Value(3.0)
b = Value(-5.0)
c = Value(10.0)

d1 = a*b + c
# it will call like this (a.__mul__(b)).__add__(c)
# d1._prev
# d1._op

from graphviz import Digraph

def trace(root):
  nodes, edges = set(), set()

  def build(v):
    if v not in nodes:
      nodes.add(v)
      for child in v._prev:
        edges.add(child, v)
        build(child)
  build(root)
  return nodes, edges

def draw_dot(root):
  dot = Digraph(format='svg', graph_attr={'randir', 'LR'})
