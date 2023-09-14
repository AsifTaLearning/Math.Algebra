   #! %matplotlib inline
from ipywidgets import interactive
from sympy import symbols , linsolve
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from IPython import display
import math

# Cartesian Coordinates

fig, ax = plt.subplots()
plt.show()

# Cartesian Coordinates (Part 2)

fig, ax = plt.subplots()

plt.axis([-20,20,-20,20])

plt.show()

# Graph Dimensions

xmin = -10
xmax = 20
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.show()

# Displaying Axis Lines

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'g') # green x axis
plt.plot([0,0],[ymin,ymax], 'g') # green y axis

plt.show()

# Plotting a Point

import matplotlib.pyplot as plt

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.plot([-5],[1], 'ro')

plt.show()

# Plotting Several Points

x = [4,1]
y = [2,1]

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax],'b') # blue y axis

plt.plot(x, y, 'ro') # red points
plt.show()

# Plotting Points and Lines

linex = [2,4]
liney = [1,5]
pointx = [1,6]
pointy = [6,3]

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.plot(linex,liney,'r')
plt.plot(pointx,pointy,'gs')

plt.show()

# Making a Scatterplot Game

score = 0

xmin = -8
xmax = 8
ymin = -8
ymax = 8

fig, ax = plt.subplots()

for i in range(3):
    xpoint = random.randint(xmin, xmax)
    ypoint = random.randint(ymin, ymax)
    x = [xpoint]
    y = [ypoint]
    plt.axis([xmin,xmax,ymin,ymax]) # window size
    plt.plot([xmin,xmax],[0,0],'b') # blue x axis
    plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
    plt.plot(x, y, 'ro')
    print(" ")
    plt.grid() # displays grid lines on graph
    plt.show()
    guess = input("Enter the coordinates of the red point point: \n")
    guess_array = guess.split(",")
    xguess = int(guess_array[0])
    yguess = int(guess_array[1])
    if xguess == xpoint and yguess == ypoint:
        score = score + 1

print("Your score: ", score) # notice this is not in the loop

# Graphing Linear Equations

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

x = np.linspace(-9,9,36)

plt.plot(x, -x + 3)



plt.show()

# Creating Interactive Graphs

def f(m, b):
    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10
    plt.axis([xmin,xmax,ymin,ymax]) # window size
    plt.plot([xmin,xmax],[0,0],'black') # black x axis
    plt.plot([0,0],[ymin,ymax], 'black') # black y axis
    plt.title('y = mx + b')
    x = np.linspace(-10, 10, 1000)
    plt.plot(x, m*x+b)
    plt.show()

interactive_plot = interactive(f, m=(-9, 9), b=(-9, 9))
interactive_plot

# Graphing Systems

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin)

x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

y1 = 2*x
plt.plot(x, y1)

y2 = -x - 3
plt.plot(x, y2)

plt.show()

# Systems of Equations - Algebra

x,y = symbols('x y')

print(linsolve([2*x + y - 15, 3*x - y], (x, y)))


# Solutions as Coordinates

x,y = symbols('x y')

first = x + y
second = x - y

solution = linsolve([first, second], (x, y))
x_solution = solution.args[0][0]
y_solution = solution.args[0][1]

print("x = ", x_solution)
print("y = ", y_solution)
print(" ")
print("Solution: (",x_solution,",",y_solution,")")

# Systems from User Input

x,y = symbols('x y')

first = input("Enter the first equation: 0 = ")
second = input("Enter the second equation: 0 = ")
solution = linsolve([first, second], (x, y))
x_solution = solution.args[0][0]
y_solution = solution.args[0][1]

print("x = ", x_solution)
print("y = ", y_solution)

# Solve and graph a system

print("First equation: y = mx + b")
mb_1 = input("Enter m and b, separated by a comma: ")
mb_in1 = mb_1.split(",")
m1 = float(mb_in1[0])
b1 = float(mb_in1[1])

print("Second equation: y = mx + b")
mb_2 = input("Enter m and b, separated by a comma: ")
mb_in2 = mb_2.split(",")
m2 = float(mb_in2[0])
b2 = float(mb_in2[1])

x,y = symbols('x y')
first = m1*x + b1 - y
second = m2*x + b2 - y
solution = linsolve([first, second], (x, y))
x_solution = round(float(solution.args[0][0]),3)
y_solution = round(float(solution.args[0][1]),3)

xmin = int(x_solution) - 20
xmax = int(x_solution) + 20
ymin = int(y_solution) - 20
ymax = int(y_solution) + 20
points = 2*(xmax-xmin)

graph_x = np.linspace(xmin,xmax,points)

y1 = m1*graph_x + b1
y2 = m2*graph_x + b2

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.plot(graph_x, y1)

plt.plot(graph_x, y2)

plt.plot([x_solution],[y_solution],'ro')

plt.show()
print(" ")
print("Solution: (", x_solution, ",", y_solution, ")")

# Quadratic Functions

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

y = x**2

plt.plot(x,y)
plt.show()

# Quadratic Function ABC's

def f(a,b,c):
    plt.axis([-10,10,-10,10]) # window size
    plt.plot([-10,10],[0,0],'k') # blue x axis
    plt.plot([0,0],[-10,10], 'k') # blue y axis
    x = np.linspace(-10, 10, 1000)

    plt.plot(x, a*x**2 + b*x + c)
    plt.show()

interactive_plot = interactive(f, a=(-9, 9), b=(-9,9),c=(-9,9))
interactive_plot

# Quadratic Functions - Vertex

print("y = ax\u00b2 + bx + c")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

vx =  -b/(2*a)
vy = a*vx**2 + b*vx + c

print(" (", vx, " , ", vy, ")")
print(" ")

xmin = int(vx)-10
xmax = int(vx)+10
ymin = int(vy)-10
ymax = int(vy)+10
points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.plot([vx],[vy],'ro') # vertex

x = np.linspace(vx-10,vx+10,100)
y = a*x**2 + b*x + c
plt.plot(x,y)

plt.show()

# Projectile Motion

a = -4.9
b = float(input("Initial velocity = "))
c = float(input("Initial height = "))

vx = -b/(2*a)
vy = a*vx**2 + b*vx + c

xmin = -1
xmax = int(2*vx * 20)
ymin = -1
ymax = int(vy + 10)

points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)
y = a*x**2 + b*x + c

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.plot(x,y) # plot the line for the equation
plt.plot([vx],[vy],'ro') # plot the vertex point

print(" (", vx, ",", vy, ")")
print(" ")
plt.show()

# Quadratic Functions - C

x = np.linspace(-4,4,16)
fig, ax = plt.subplots()
cvalue = "c = "

for c in range(10):
    y = -x**2+c
    plt.plot(x,y)
    cvalue = "c = ", c
    ax.set_title(cvalue)
    display.display(plt.gcf())
    time.sleep(0.5)
    display.clear_output(wait=True)

# The Quadratic Formula

print("0 = ax\u00b2 + bx + c")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
x1 = 0
x2 = 0

if b**2-4*a*c < 0:
    print("No real roots")
else:
    # Write your code here, changing x1 and x2
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    print("The roots are ", x1, " and ", x2)

# Table of Values

ax = plt.subplot()
ax.set_axis_off()
title = "y = 3x + 2" # Change this title
cols = ('x', 'y')
rows = []
for a in range(1,10):
    rows.append([a, 3*a+2]) # Change only the function in this line

ax.set_title(title)
plt.table(cellText=rows, colLabels=cols, cellLoc='center', loc='upper left')
plt.show()

# Projectile Game

loc = random.randint(1,100)
print("a toy rocket has to land "+str(loc)+"meters away")
a = -4.9
b = float(input("Initial velocity in m/s = "))
c = 1

vx = -b/(2*a)
vy = a*vx**2 + b*vx + c

xmin = -1
xmax = int(2*vx * 20)
ymin = -1
ymax = int(vy + 10)

points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)
y = a*x**2 + b*x + c

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.plot([loc,loc],[0,ymax]) # plot the line for the equation
plt.plot([x],[y],'ro') # plot the vertex point

root2 = round((-b - math.sqrt(b**2 - 4*a*c))/(2*a),2)
if root2 >= loc:
    print("Distance: "+str(root2)+"success! ")

else:
    print("missed it by that much")

print(" ")
plt.show()



