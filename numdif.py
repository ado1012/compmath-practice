def equation(x):
    return x**4 - 3*(x**3) + 6*(x**2) - 10*x - 9

def derived1(x,h):
    return (equation(x+h) - equation(x-h)) / (2*h)

def derived2(x,h):
    return (equation(x+h) - 2*equation(x) + equation(x-h)) / (h**2)

def forward(x,h):
    return ((equation(x+h) - equation(x))/h)

def backward(x,h):
    return ((equation(x) - equation(x-h))/h)

def central(x,h):
    return ((equation(x+h) - equation(x-h))/ (2*h))

print("------------------------------------------------------")
print("h\t f'exact\t f'approximation\t f'relative error\t f''exact\t f''approximation\t f''relative error")
print("0.5\t", -10, "\t ", derived1(0,0.5), "\t\t\t\t ", ((-10-(derived1(0,0.5)))/-10) * 100, "\t\t\t\t 12\t\t\t", derived2(0,0.5), "\t\t\t\t", ((12-(derived2(0,0.5)))/12) * 100)
print("0.25 ", -10, "\t ", derived1(0,0.25), "\t\t\t\t ", ((-10-(derived1(0,0.25)))/-10) * 100, "\t\t\t 12\t\t\t", derived2(0,0.25), "\t\t\t\t", ((12-(derived2(0,0.25)))/12) * 100)
print("0.125", -10, "\t ", derived1(0,0.125), "\t\t\t ", ((-10-(derived1(0,0.125)))/-10) * 100, "\t\t\t 12\t\t\t", derived2(0,0.125), "\t\t\t\t", ((12-(derived2(0,0.125)))/12) * 100)
print("------------------------------------------------------")
print("h\t f'exact\tf'backward\t  f'forward\t  f'cental")
print("0.5\t", -10, "\t ", backward(0,0.5), "\t\t ", forward(0,0.5), "\t", central(0,0.5))
print("0.25", -10, "\t ", backward(0,0.25), "\t ", forward(0,0.25), "\t", central(0,0.25))
print("0.125", -10, "\t ", backward(0,0.125), "\t ", forward(0,0.125), "\t", central(0,0.125))
