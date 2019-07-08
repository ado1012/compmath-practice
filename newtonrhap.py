def func(x):
    return x*x*x + 7*x*x - 36

def derifunc(x):
    return 3*x*x + 14*x

def newtonrhap(x):
    h = func(x)/derifunc(x)
    while abs(h) >= 0.01:
        h = func(x)/derifunc(x)
        x = x - h
    print(x)

x= -3
newtonrhap(x)
