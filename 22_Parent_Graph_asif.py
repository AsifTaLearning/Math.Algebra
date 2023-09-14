import matplotlib.pyplot as plt
import numpy as np
import math

# Graph with no slope and no x value

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot([xmin,xmax],[5,5],'r')

plt.show()

# Linear graph
# y = x

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

y = x

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot(x,y,'r')

plt.show()

# Quadratic graph
# y = x^2

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

y = x**2

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot(x,y,'r')

plt.show()

# Cubic graph
# y = x^3

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

y = x**3

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot(x,y,'r')

plt.show()

# Quartic graph
# y = x^4

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

y = x**4

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot(x,y,'r')

plt.show()

# Quintic graph
# y = x^5

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

y = x**5

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot(x,y,'r')

plt.show()

# Absolute value graph
# y = |x|
xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

y = abs(x)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot(x,y,'r')

plt.show()

# Square root graph
# y = sqrt(x) 

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

y = np.sqrt(x)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot(x,y,'r')

plt.show()

# Square root with rational exponent
# y = x^(1/2)

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

y = x**(1/2)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot(x,y,'r')

plt.show()

# Cube root of x
# y = x^(1/3)

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

y = np.cbrt(x)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot(x,y,'r')

plt.show()

# Floor function
# y = ⌊x⌋

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

for x in range(points):

    plt.plot([0.25*x - 10],[math.floor(0.25*x)-10],'ro')

plt.show()

# Exponential function
# y = 2^x

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points= 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

y = 2**x

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.plot(x,y,'r')

plt.show()


