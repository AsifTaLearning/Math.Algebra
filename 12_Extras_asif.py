import matplotlib.pyplot as plt
import numpy as np
from sympy.solvers import solve
from sympy import symbols

# in 2010 population was 55,000 & in 2012 population is 76,000

x1 = 0
y1 = 55
x2 = 2
y2 = 76

m = (y2-y1)/(x2 -x1) # Slope
b = y1 - m*x1 # y-intercept equation

xmin = 0
xmax = 10
ymin = 0
ymax = 150

y3 = m*xmin + b
y4 = m*xmax + b

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

ax.set_title("Population Graph")
ax.set_xlabel("time")
ax.set_ylabel("population")
ax.grid(True)

ax.set_xticks(np.arange(xmin,xmax,2))
ax.set_yticks(np.arange(ymin,ymax,10))

plt.plot([xmin,xmax],[y3,y4],'r',label='population in yr')
ax.legend()

plt.show()


# 50 poeple dropped steadly each year since 2004 until 2010 , in 2004 875 peoples


x1 = 0
y1 = 875
x2 = 1
y2 = 825

m = (y2-y1)/(x2 -x1) # Slope
b = y1 - m*x1 # y-intercept equation

xmin = 0
xmax = 18
ymin = 0
ymax = 900

y3 = m*xmin + b
y4 = m*xmax + b

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

ax.set_title("Common Cold Effect Graph")
ax.set_xlabel("time")
ax.set_ylabel("cases")
ax.grid(True)

ax.set_xticks(np.arange(xmin,xmax,2))
ax.set_yticks(np.arange(ymin,ymax,100))

plt.plot([xmin,xmax],[y3,y4],'r',label='cases in yr')
ax.legend()

plt.show()

              # when cases zero ?

x = symbols('x')
eq = 875 -50*x
eq1 = solve(eq,x)

print("cases zero at "+str(eq1[0]))


# Another problem 

x1 = 5
y1 = 10
x2 = 25
y2 = 4

m = (y2-y1)/(x2 -x1) # Slope
b = y1 - m*x1 # y-intercept equation

xmin = 0
xmax = 50
ymin = 0
ymax = 15

y3 = m*xmin + b
y4 = m*xmax + b

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

ax.set_title("Profit Graph")
ax.set_xlabel("time")
ax.set_ylabel("profit")
ax.grid(True)

ax.set_xticks(np.arange(xmin,xmax,5))
ax.set_yticks(np.arange(ymin,ymax,2))

plt.plot([xmin,xmax],[y3,y4],'r',label='Profit')
ax.legend()

plt.show()

# in 2004 school population is 1,700 & in 2012 grown to 2,500

x1 = 0
y1 = 1700
x2 = 8
y2 = 2500

m = (y2-y1)/(x2 -x1) # Slope
b = y1 - m*x1 # y-intercept equation

xmin = 0
xmax = 10
ymin = 0
ymax = 3000

y3 = m*xmin + b
y4 = m*xmax + b

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

ax.set_title("School Population Graph")
ax.set_xlabel("time")
ax.set_ylabel("population")
ax.grid(True)

ax.set_xticks(np.arange(xmin,xmax,2))
ax.set_yticks(np.arange(ymin,ymax,500))

plt.plot([xmin,xmax],[y3,y4],'r',label='school population in yr')
ax.legend()

plt.show()