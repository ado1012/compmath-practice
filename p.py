import numpy as np

def equation(x,y):
    return 2*x*y + 2*x + x**2 - 2*(y**2)

def derived_x(x,y):
    return 2*y + 2 +2*x

def derived_y (x,y):
    return 2*x + 2 - 4*y

def optimization(x,y,set):
    sx = (set * derived_x(x,y))
    sy = (set * derived_y(x,y))
    iteration = 0
    while(iteration <= 10):
        x_new = (x-sx)
        y_new = (y-sy)
        print("iteration: ", iteration, "x1: ", x, "x0: ", y, "f(x): ", equation(x,y))
        x = x_new
        y = y_new
        iteration +=1

optimization(0.5,1,0.1)
