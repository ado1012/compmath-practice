from math import *

def lagrange_interpolation(x, y):
  '''
  Parameters
  ----------
  x : list of floats
  y : list of floats
  u : float

  Returns
  -------
  float
      an estimate at the point u
  '''
  r = range(len(y))
  a = [y[i]/product( x[i]-x[j] for j in r if j != i ) for i in r]
  return sum(a[i]*product([-x[j] for j in r if j != i]) for i in r)


def product(a):
  p = 1
  for i in a: p *= i
  return p

def main():
  x = [0.965689]
  y = [1.035530]
  estim = lagrange_interpolation(x, y)
  exact = 1
  print("estimate = ", estim, ",", "exact = ", exact)

main()
