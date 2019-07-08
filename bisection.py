# The function is x^3 - x^2 - 10x -8 = 0
def func(x):
    return x*x*x + 7*x*x - 36

# Prints root of func(x)
# with error of EPSILON
def bisection(a,b):
    c = a
    while ((b-a) >= -3):

        # Find middle point
        c = (a+b)/2

        # Check if middle point is root
        if (func(c) == 0.0):
             break

        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c
    print("The value of root is : ","%.4f"%c)

# Driver code
# Initial values assumed
a = -4
b = -2
bisection(a, b)
