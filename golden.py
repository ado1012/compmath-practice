from math import sqrt

r = (sqrt(5)-1)/2


def golden(f,a,c,b, absolutePrecision):
    if abs(a -b) < absolutePrecision:
        return(a +b)/2
    d = r*(a - b)
    if f(d) < f(c):
        return golden(f,c,d,b, absolutePrecision)
    else:
        return golden(f,d,c,a,absolutePrecision)

f = lambda x: x**2
