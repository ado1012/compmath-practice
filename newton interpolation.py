import numpy as np
import math

#no 1
print("Number 1")

p = np.array([44 * math.pi/180 , 46 * math.pi/180])
q = np.ones(len(p))

for i in range(len(p)):
    q[i] = math.tan(p[i])



def newton_interpolation(p,q,p1):
    b0 = q[0]
    b1 = (q[1] - q[0])/(p[1] - p[0])

    order_1 = b0
    order_2 = b0 + b1 * (p1-p[0])

    return order_2

print("Second order Newton's interpolation method , tan 45 estimated: ", newton_interpolation(p,q,45*math.pi/180))



def lagrange_interpolation(p,q,p1):

    b0 = q[0]* ((p1-p[1]) / (p[0]-p[1]))
    b1 = q[0]* ((p1-p[0]) / (p[1]-p[0]))

    return b0+b1

print("Second order lagrange interpolation method , tan 45 estimated: ", lagrange_interpolation(p,q,45*math.pi/180))
exact = 1
newton = round(abs(((exact - newton_interpolation(p,q,45*math.pi/180))/exact) * 100),3)
larange = round(abs(((exact - lagrange_interpolation(p,q,45*math.pi/180))/exact) * 100),3)

print("Relative errors :")
print("Newton : ", newton)
print("Lagrange : ", larange)
print("Hence, Newton interpolation method is the best estimation")
