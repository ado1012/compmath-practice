from tkinter import *
import sympy

def calculate():
    global numbers
    num1 = float(x0.get())
    num2 = float(h.get())
    result.set(num2)
    eq = str(equation.get())
    num3 = str(eval(eq))
    print(num3)

# equation function
def equationFunc(x):
    eq = str (equation.get())
    num3 = str(eval(eq))
    return num3

# derivtion function
def derivedFunc(X):
    a = str(equation.get())
    x = sympy.Symbol('x')
    number = str(eval(a))
    return sympy.diff(number).subs({x:X})

# bisection method
def bisection(a, b, h):
    fc = 1.0
    while( b-a >= h):
        fa = float(equationFunc(a))
        fb = float(equationFunc(b))
        xm = float((a+b)/2)
        fcprev = float(fc)
        fc = float(equationFunc(xm))
        if (fc == 0.0):
            result.set(xm)
        h1 = ((fc - fcprev) /fc) * 100.0
        if (fa * fc) < 0:
            b = xm
        elif (fa * fc) > 0:
            a = xm
        elif (fa * fc) == 0:
            result.set(xm)
    result.set(xm)

# newton method
def newton(x0):
    h1 = (float(equationFunc(x0)) / derivedFunc(x0))
    while abs (h1) >= 0.01:
        h1 = (float(equationFunc(x0)) / derivedFunc(x0))
        x0 = x0 - h1
    result.set(x0)

# UI for bisection
def UIbisect():
    global x0_input, result_output, x0, result, equation, numbers, h
    screen1 = Toplevel(screen)
    screen1.title()
    screen1.geometry("500x400")
    numbers = ""
    equation = StringVar()
    result = StringVar()
    h = StringVar()
    a = StringVar()
    b = StringVar()
    Label(screen1, text = "Enter the equation: ").pack()
    Entry(screen1, textvariable = equation).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Enter the variable a (xl):").pack()
    x0_input = Entry(screen1, textvariable=a).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Enter the variable b (xu):").pack()
    Entry(screen1, textvariable=b).pack()
    Label(screen1, text= "").pack()
    Label(screen1, text="Enter the variable h:").pack()
    Entry(screen1, textvariable=h).pack()
    Label(screen1, text="").pack()
    # calculate button
    Button(screen1, text = "Calculate", height = "1", width = "15", command = lambda:bisection(float(a.get()), float(b.get()), float(h.get()))).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Result: ").pack()
    Entry(screen1, textvariable=result).pack()



# UI for newton rhapson
def UInewton():
    global equation, numbers, result
    screen1 = Toplevel(screen)
    screen1.title()
    screen1.geometry("500x400")
    numbers = ""
    equation = StringVar()
    x0 = StringVar()
    result = StringVar()
    Label(screen1, text="Enter the equation: ").pack()
    Entry(screen1, textvariable=equation).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="x0:").pack()
    Entry(screen1, textvariable=x0).pack()
    Label(screen1, text="").pack()
    # calculate button
    Button(screen1, text="Calculate", height="1", width="15", command=lambda: newton(float(x0.get()))).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Result: ").pack()
    Entry(screen1, textvariable=result).pack()

# main function
def main():
    global screen
    screen = Tk()
    screen.geometry("600x400")
    screen.title("Root Finding Calculator")
    Label(text = "Root Finding Calculator", bg = "white", width = "600", height = "3", font = ("Helvetica, 16")).pack()
    Label(text = "").pack()
    Button(text = "Newton Raphson Method", height = "4", width = "40", command = UInewton).pack()
    Label(text= "").pack()
    Button(text = "Bisection Method", height = "4", width = "40", command = UIbisect).pack()
    screen.mainloop()

main()
