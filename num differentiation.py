import matplotlib.pyplot as plt
import numpy as np


def derivatve(f,x,method = "second forwards 1", h=0.025):
    if method == "central 1": # central 1st derivative
        return (f(x + h) - f(x - h))/(2*h)

    elif method == "central 2": # central 2nd derivative
        return (f(x + h) - 2*f(x) + f(x - h))/(h*h)

    elif method == "forwards 1": # forward 1st derivative
        return (f(x + h) - f(x))/h

    elif method == "forwards 2": # forwards 2nd derivative
        return (f(x + 2*h) - 2*f(x + h) + f(x))/(h*h)

    elif method == "second forwards 1": # second forwards difference 1st derivative
        return (-3*f(x) + 4*f(x + h) - f(x + 2*h))/(2*h)

    elif method == "second forwards 2": # second forwards difference 2nd derivative
        return (2*f(x) - 5*f(x + h) + 4*f(x + 2*h) - f(x + 3*h))/(h*h)

    elif method == "backwards 1": # backward 1st derivative
        return (f(x) - f(x - h))/h

    elif method == "backwards 2": # backward 2nd derivative
        return (f(x) - 2*f(x - h) + f(x - h))/(h*h)

    elif method == "second backwards 1": #second backward difference 1st derivative
        return (f(x - 2*h) - 4*f(x - h) + 3*f(x))/(2*h)

    elif method == "second backwards 2": # second forwards difference 2nd derivative
        return (-f(x - 3*h) + 4*f(x - 2*h) - 5*f(x - h) + 2*f(x))/(h*h)

    else:
        print("error")

x = 1
dydx = derivatve(np.exp, -x)
print(dydx)
dYdx = np.exp(-x)
print(dYdx)

# plt.figure(figsize=(12,5))
# plt.plot(x,dydx,'r.',label='Central Difference')
# plt.plot(x,dYdx,'b',label='True Value')
#
# plt.title("Central Difference Derivative of e^-x")
# plt.legend(loc='best')
# plt.show()
