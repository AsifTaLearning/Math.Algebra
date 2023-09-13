
    #! %matplotlib inline

from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols , var , factor ,nonlinsolve , Eq # nonlinsolve because non linear 
from sympy.solvers import solve

print("\nWelcome to ASIF'S calculatoR \n       .....................\n1.  1/2 = x/16\n2.  custom solve equation\n3.  x^3 - 2*x^2 - 5*x + 6 \n4.  a*x^2 + b*x + c\n5.  conversion (fraction , percent)\n6.  a*x^2 + b*x + c\n7.  Slope_intercept equation from two points\n8.  Interactive graph\n9.  Shading and graphing inequality\n10. Round(around)\n11. Sympy plotting\n12. Save graph and download")

selection = int(input("Choose a number  \n"))

# Proportion
# 1/2 = x/16
# put a zero in unknown number

if selection == 1:

    n1 = 1 
    d1 = 2

    n2 = 0
    d2 = 16

    # cross multiplication

    if n2 == 0:
        n2=(n1*d2)/d1
        print("n2 is "+str(n2))


    if d2 == 0:
        d2=(d1*n2)/n1
        print("d2 is "+str(d2))

# .............................................................


# Taking input and solve equation

elif selection == 2:

    x = symbols("x")
    eq = input("Enter equation(=0) \n")
    ans = solve(eq,x)

    for s in ans:

        print("x = "+str(s))


#...............................................................

# Factor
# x^3 - 2*x^2 - 5*x + 6

elif selection == 3:

    var('x')
    eq = x**3 - 2*x**2 - 5*x + 6
    ans = factor(eq)

    print("x = "+str(ans))

#..............................................................

# solve for variables
# a*x^2 + b*x + c

elif selection == 4:

    var('a b c x')

    eq = a*x**2 + b*x + c
    eq1 = Eq(eq,0)

    ans = solve(eq1,x)

    for s in ans:

        print("solution = "+str(s))


#...............................................................

# conversion (fraction , percent)

elif selection == 5:

    deci = input("enter a decimal for convert ")

    exponent = int(len(deci))-1
    n = float(deci)
    numerator = n * 10**exponent
    denominator = 10**exponent
    percent = n * 100

    print("decimal ="+str(n))
    print("fraction = "+str(numerator)+"/"+str(denominator))
    print("percent = "+str(percent)+"%")

#................................................................

# Another solving equation
# a*x^2 + b*x + c

elif selection == 6:

    var('a b c x')

    eq = a*x**2 + b*x + c
    eq1 = Eq(eq,0)

    ans = solve(eq1,x)

    for s in ans:

        print("solution = "+str(s))




#..................................................................

# Slope_intercept equation from two points

elif selection == 7:

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

#...............................................................

# Interactive graph

elif selection == 8:

    def fo(m , b, zoom):

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



    interactive_plot = interactive(fo, m=(-9,9),b=(-9,9),zoom=(1,100))

    interactive_plot

#................................................................

# Shading and graphing inequality

elif selection == 9:

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
    plt.fill_between(x,y1,facecolor = 'red')

    y2 = x+3
    plt.plot(x,y2)
    plt.fill_between(x,y2,y1, facecolor = 'yellow')

    y3 = x-1
    plt.plot(x,y3)
    plt.fill_between(x,y3,y2,facecolor = 'green')

    y4 = x-4
    plt.plot(x,y4,'-')
    plt.fill_between(x,y4,xmax,facecolor = 'blue')

    plt.show()

#...............................................................

# Round(around)

elif selection == 10:

    def f(zoom):
        


        xmin = -zoom
        xmax = zoom
        ymin = -zoom
        ymax = zoom 

        points = 10*xmax-xmin
        x = np.linspace(xmin,xmax,points)
        
        fig ,ax = plt.subplots()
        plt.axis([xmin,xmax,ymin,ymax])
        plt.plot([xmin,xmax],[0,0],'b')
        plt.plot([0,0],[ymin,ymax],'b')

        ax.set_xlabel("x values")
        ax.set_ylabel("y values")
        ax.set_title("Some Graph")

        ticks = int(round((xmax-xmin)/20)) # round

        ax.set_xticks(np.arange(xmin,xmax,ticks))
        ax.set_yticks(np.arange(ymin,ymax,ticks))

        ax.grid(True)

        y1 = 3*x**2 -4
        plt.plot(x,y1)
        plt.fill_between(x,y1,ymax, facecolor = 'green')

        y2 = x
        plt.plot(x,y2)
        plt.fill_between(x,y2,ymin, facecolor = 'blue')
        
        ax.grid(True)

        plt.show()

    interactive_plot = interactive(f,zoom = (1,100))

    interactive_plot

#................................................................

# Sympy plotting

elif selection == 11:
       
    from sympy.plotting import plot

    var('x y')

    first = -x**2 + y + 10
    second = 2*x**2 - 2*y - 4
        

    solution = nonlinsolve([first,second],(x,y))

    for a in range(len(solution.args)) :

        xsolution = solution.args[a][0]
        ysolution = solution.args[a][1]
        print('('+str(xsolution)+","+str(ysolution)+')')

    y_first = Eq(first,0)
    y1 = solve(y_first,y)

    y_second = Eq(second,0)
    y2 = solve(y_second,y)

    print("y = "+str(y1[0]))
    print("y = "+str(y2[0]))

    x = symbols('x')
    xmin  = -10
    xmax = 10

    plot(y1[0],y2[0], (x,xmin,xmax))

elif selection == 12:

    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10

        
    fig ,ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')

    plt.savefig("adc.png")
    plt.show()

else :

    print("This number is not existed")
