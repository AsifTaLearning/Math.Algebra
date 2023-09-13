      #!  %matplotlib inline
import math
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interactive


# Solve quadratic equation
# y = ax**2 + bx + c

a = 1
b = 5
c = 6

print("y = "+str(a)+"x**2 + "+str(b)+"x + "+str(c))

vx = -b/(2*a) # vertex
vy = a*(vx**2) + b*vx + c
print("vertex: ("+str(vx)+","+str(vy)+")")

d = b**2 - 4*a*c # roots

if d>=0:
    root_1 = (-b + math.sqrt(d))/(2*a)
    root_2 = (-b - math.sqrt(d))/(2*a)
    print("roots: x = "+str(root_1)+" and x = "+str(root_2))
else:
    print("no real roots")

# Graph a quadratic function

a = 1
b = 5
c = 6

print("y = "+str(a)+"x**2 + "+str(b)+"x + "+str(c))

vx = -b/(2*a) # vertex
vy = a*(vx**2) + b*vx + c
print("vertex: ("+str(vx)+","+str(vy)+")")

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points = 10*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig ,ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0])
plt.plot([0,0],[ymin,ymax])

y1 = a*(x**2) + b*x + c
plt.plot(x,y1)

plt.plot([vx],[vy],'ro') # vertex

d = b**2 - 4*a*c # roots
if d>=0: 
    root_1 = (-b + math.sqrt(d))/(2*a)
    root_2 = (-b - math.sqrt(d))/(2*a)
    plt.plot([root_1,root_2],[0,0],'go')
    print("roots: x = "+str(root_1)+" and x = "+str(root_2))
else:
    print("no real roots")

plt.show()

# Sliders to show how a,b, and c affect the graph

def f():

    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)

    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0])
    plt.plot([0,0],[ymin,ymax])

    y1 = a*(x**2) + b*x + c
    plt.plot(x,y1)

    plt.plot([vx],[vy],'ro') # vertex

    d = b**2 - 4*a*c # roots
    if d>=0: 
        root_1 = (-b + math.sqrt(d))/(2*a)
        root_2 = (-b - math.sqrt(d))/(2*a)
        plt.plot([root_1,root_2],[0,0],'go')
        print("roots: x = "+str(root_1)+" and x = "+str(root_2))
    else:
        print("no real roots")

    sa = str(a) # Conver into string
    sb = str(b)
    sc = str(c)

    h1 = "y = "+ sa +"x**2 + "+sb+"x + "+sc
    h2 = ""

    for w in h1:

        h2 = h2 + w    

    plt.title(h2)
    plt.show()

interactive_plot = interactive(f, a=(1,2) , b=(-9,9) ,c=(-9,9))
interactive_plot

