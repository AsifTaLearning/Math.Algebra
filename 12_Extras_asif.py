import matplotlib.pyplot as plt
import numpy as np
from sympy.solvers import solve
from sympy import symbols

def g(x):

    x = x/100

    return x


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

# population of 40,000 produces 13 tons of garbage

x1 = 0
y1 = 0
x2 = 40
y2 = 13

m = (y2-y1)/(x2 -x1) # Slope
b = y1 - m*x1 # y-intercept equation

xmin = 0
xmax = 100
ymin = 0
ymax = 50

y3 = m*xmin + b
y4 = m*xmax + b

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

ax.set_title("Garbage By Population Graph")
ax.set_xlabel(" population(thousands)")
ax.set_ylabel(" garbage(tons)")
ax.grid(True)

ax.set_xticks(np.arange(xmin,xmax,20))
ax.set_yticks(np.arange(ymin,ymax,10))

plt.plot([xmin,xmax],[y3,y4],'r',label='Garbage in population')
ax.legend()

plt.show()

# A garden with area 5,000 feetsqure  requires 50 yard of dirt
# 50 = f(5000)

x = 5000

ans = g(x)

print("answer is ans "+str(ans))

# Another problem
# h(t) = -16*t^2 + 96*t

t = symbols('t')

eq = -16*t**2 + 96*t

ans = solve(eq,t)

for s in ans:
    
    print('answer is '+str(s))


# C(x) = 10x + 500
# C(?) = 1500

x = symbols('x')

eq = 10*x + 500 - 1500
x = solve(eq,x)

print("answer is "+str(x[0]))







