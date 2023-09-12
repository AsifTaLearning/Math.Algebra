      #! %matplotlib inline 
from datetime import datetime
from meteostat import Point, Daily

from ipywidgets import interactive # For interactive graph

import matplotlib.pyplot as plt
import numpy as np

# Shading and graphing inequality

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points = 10*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

y1 = x+6
plt.plot(x,y1)
plt.fill_between(x,y1,ymax,facecolor = 'red')

y2 = x+3
plt.plot(x,y2)
plt.fill_between(x,y2,y1, facecolor = 'yellow')

y3 = x-1
plt.plot(x,y3)
plt.fill_between(x,y3,y2,facecolor = 'green')

y4 = x-4
plt.plot(x,y4,'-')
plt.fill_between(x,y4,y3,facecolor = 'blue')

plt.show()

# Interactive graph

def f(m , b, zoom):

    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)


    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'black')
    plt.plot([0,0],[ymin,ymax],'black')
    plt.title('y = mx + b')

    plt.plot(x, m*x+b)

    plt.show()

interactive_plot = interactive(f, m=(-9,9),b=(-9,9),zoom=(1,100))

interactive_plot

# Meteostat

start = datetime(2022,1,1)
end = datetime(2022,7,31)

philly = Point(39.97,-75.13,25)

data = Daily(philly, start, end)
data = data.fetch()

data.plot(y=['tavg','tmin','tmax'])
plt.show()