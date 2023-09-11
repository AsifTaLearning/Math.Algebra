# Slope intercept equation = y = m*x + b and display graph
# y and x are points 
# M is slope 
# b is intercept

from sympy.solvers import solve
from sympy import symbols
import matplotlib.pyplot as plt

x1 = 1
y1 = 7

x2 = 2
y2 = 10

m = (y2 - y1) / (x2 - x1) 

b = symbols('b')  


eq =  m*x1 + b - y1 # y = M*x + b  , eq = 0
b = solve(eq,b)

b = int(b[0])

print("b = "+str(b))

print("y = "+str(m)+"x + "+str(b)) # full equation 

xmin = -10
xmax = 10
ymin = -10
ymax = 10

y3 = m*xmin + b
y4 = m*xmax + b

print(y3,y4)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()
