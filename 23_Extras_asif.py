     #! %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interactive

# Sliders and zoom
# y = a

def f(zoom,a):


    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)


    fig ,ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')

    y1 = a
    y2 = a
    
    plt.plot([xmin,xmax,],[y1,y2],'r')
    

    plt.show()

interactive_plot = interactive(f,zoom =(1,100),a=(-9,9))
interactive_plot


# Sliders and zoom
# y = mx + b

def fu(zoom,b,m):

    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)


    fig ,ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')

    y1 = m*x + b

    plt.plot(x,y1,'r')

    plt.show()

interactive_plot = interactive(fu,zoom =(1,100),b=(-9,9),m=(-9,9))
interactive_plot

#  Sliders and zoom
# y = ax**2 + bx + c

def fu(zoom,a,b,c):

    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)


    fig ,ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')

    y1 = a*x**2 + b*x + c

    plt.plot(x,y1,'r')

    plt.show()

interactive_plot = interactive(fu,zoom =(1,100),a=(-9,9),b=(-9,9),c = (-9,9))
interactive_plot

# Sliders and zoom
# y = abs(x)

def fu(zoom,a,b,c):

    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)


    fig ,ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')

    y1 = a * abs(x-b) + c

    plt.plot(x,y1,'r')

    plt.show()

interactive_plot = interactive(fu,zoom =(1,100),a=(-9,9),b=(-9,9),c = (-9,9))
interactive_plot

# Sliders and zoom
# y = sqrt(x)

def fu(zoom,a,b,c):

    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)


    fig ,ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')

    y1 = a * np.sqrt(x-b) + c

    plt.plot(x,y1,'r')

    plt.show()

interactive_plot = interactive(fu,zoom =(1,100),a=(-9,9),b=(-9,9),c = (-9,9))
interactive_plot

# Sliders and zoom
# y = x**3 + .......

def fu(zoom,a,b,c,d):

    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)


    fig ,ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')

    y1 = a*x**3 + b*x**2 + c*x + d

    plt.plot(x,y1,'r')

    plt.show()

interactive_plot = interactive(fu,zoom =(1,100),a=(-9,9),b=(-9,9),c = (-9,9),d =(-9,9))
interactive_plot

# Sliders and zoom
# y = x**4 + .......

def fu(zoom,a,b,c,d,e):

    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)


    fig ,ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')

    y1 = a * x**4 + b*x**3 + c*x**2 + d*x + e

    plt.plot(x,y1,'r')

    plt.show()

interactive_plot = interactive(fu,zoom =(1,100),a=(-9,9),b=(-9,9),c = (-9,9),d = (-9,9),e = (-9,9))
interactive_plot

# Sliders and zoom
# y = np.floor(x)

def fu(zoom,a,b,c):

    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)


    fig ,ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')

    y1 = a * np.floor(x-b) + c

    plt.plot(x,y1,'ro')

    plt.show()

interactive_plot = interactive(fu,zoom =(1,100),a=(-9,9),b=(-9,9),c = (-9,9))
interactive_plot

# Sliders and zoom
# y = a*b**(cx-d) + c

def fu(zoom,a,b,c,d,e):

    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)


    fig ,ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')

    y1 = a*b**(c*x-d) + c

    plt.plot(x,y1,'r')

    plt.show()

interactive_plot = interactive(fu,zoom =(1,100),a=(-9,9),b=(-9,9),c = (-9,9),d = (-9,9),e = (-9,9))
interactive_plot