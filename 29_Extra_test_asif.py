    #! %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq ,latex
from IPython.display import display, Math
from ipywidgets import interactive
import math




# Graphing Inequalities

xmin = -10
xmax = 10
ymin = - 10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.title("y > 2x")

y1 = 2*x
plt.plot(x, y1)

plt.fill_between(x, y1, ymax)

plt.show()

# Graphing inequalities - Part 2

xmin = -10
xmax = 10
ymin = - 10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

y1 = 2*x

plt.plot(x, y1,'r--')

plt.fill_between(x, y1, ymin)
plt.show()

# Making Art with Graphs

xmin = -10
xmax = 10
ymin = - 10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

y1 = x+6
plt.plot(x, y1)
plt.fill_between(x, y1, 10, facecolor='blue') # change this line

y2 = x+3
plt.plot(x, y2)
plt.fill_between(x, y2, y1, facecolor='green') # change this line

y3 = x-1
plt.plot(x, y3)
plt.fill_between(x, y3, y2, facecolor='yellow') # change this line

y4 = x-4
plt.plot(x, y4)
plt.fill_between(x, y4, y3, facecolor='red') # change this line

plt.show()

# Monomials

x = symbols('x')
eq1 = Eq(-2*x**3 , -16)
display(eq1)

# Polynomials

x,y = symbols('x y')

a = int(input("Enter coefficient A: "))
b = int(input("Enter coefficient B: "))

c = int(input("Enter coefficient C: "))
d = int(input("Enter coefficient D: "))

y = a*x**3 + b*x**2 + c*x + d

print("Here is your equation:")
display(Math("y = " + latex(y)))

# Interactive Polynomial Graph

def f(a, b, c):
    plt.axis([-10,10,-10,10]) # window size
    plt.plot([-10,10],[0,0],'k') # blue x axis
    plt.plot([0,0],[-10,10], 'k') # blue y axis
    x = np.linspace(-10, 10, 200)
    plt.plot(x, a*x**2+b*x+c) # Change this line
    plt.show()

interactive_plot = interactive(f, a=(-9, 9), b=(-9, 9), c=(-9,9))
display(interactive_plot)

# Exponential Functions

xmin = -10
xmax = 10
ymin = -100
ymax = 100

def f(a, b):
    plt.axis([xmin,xmax,ymin,ymax]) # window size
    plt.plot([xmin,xmax],[0,0],'k') # x axis
    plt.plot([0,0],[ymin,ymax], 'k') # y axis
    x = np.linspace(xmin, xmax, 1000)
    plt.plot(x, a*b**x)
    plt.show()

interactive_plot = interactive(f, a=(-9, -1), b=(1, 9))
display(interactive_plot)

# Percent Increase

p = float(input("Starting amount = "))
r = float(input("Enter the percentage rate, converted to a decimal: "))
t = float(input("How many years will this investment grow? "))

a = p*(1+r)**t

print("The annuity is ", a)


# Percent Decrease

p = float(input("Starting amount = "))
r = float(input("Enter the percentage rate, converted to a decimal: "))
t = float(input("How many years will this decrease continue? "))

a = p*(1-r)**t

print("The final amount is ", a)

# Compound Interest

p = float(input("Starting amount: "))
r = float(input("Percentage rate, converted to a decimal: "))
t = float(input("Number of years this investment will grow: "))
n = int(input("Number of times compounded per year: "))

annuity = p*(1+(r/n))**(n*t)

print("The annuity is ", annuity)


# Continuous Growth

p = float(input("Principle: "))
r = float(input("Rate: "))
t = int(input("Time: "))
n = int(input("N: "))

a_annual = p*(1+r)**t
a_n_times = p*(1+r/n)**(n*t)
a_continuous = p*math.e**(r*t) # use math.e in this formula

print("Compounded annually, anuity = ", a_annual)
print("Compounded ", n, "times per year, anuity = ", a_n_times)
print("Compounded continuously, anuity = ", a_continuous)

# Investments

p = float(input("Starting amount: "))
r = float(input("Annual percentage rate: "))
t = int(input("Number of years: "))
monthly = float(input("Monthly contribution: "))

annuity = p

for a in range(12*t):
    annuity = annuity + monthly
    # Change the next line to calculate the interest
    interest = annuity * r / 12 
    annuity = annuity + interest

print("Annuity = ", annuity)


# Mortgage Payments

p = float(input("Amount borrowed: "))
r = float(input("Annual percentage rate: "))
t = float(input("Number of years: "))

mult = 1+r/12
exp = 12*t
top = r/12*mult**exp
bot = (mult**exp)-1
pmt = top/bot

print("Monthly payment = $", pmt)


# Exponents and Logarithms

base = float(input("base: "))
result = float(input("result: "))

exp = math.log(result,base)

print("exponent = ", exp)


# Natural Logs

r = float(input("Enter the annual rate as a decimal: \n"))
t = math.log(2)/r
print("Your money will double in ", t, " years")


# Common Logs

n = input('Enter a number with several digits or several decimal places: ')
n = float(n)

exp = math.log(n, 10)

if n==1000:
    exp = 3

print("exponent = ", exp)


# Scientific Notation

a = 156000000000
b = 0.000000000413

a1 = 1.56
a2 = 11
b1 = 4.13
b2 = -10

print(a, " = ", a1, "* 10^", a2)

print(b, " = ", b1, "* 10^", b2)


# Logs and Scientific Notation

a = .00000000000234
b = 12300000000000

x1 = math.floor(math.log(a,10))
n1 = round(a*10**(-x1),2)
print("a = ", n1, "* 10^", x1)

x2 = math.floor(math.log(b,10))
n2 = round(b*10**(-x2),2)
print("b = ", n2, "* 10^", x2)



# Scientific Notation Conversion

a = float(input('Enter a number to convert to scientific notation: '))

n = round(a*10**(-x1),2) 
x = math.floor(math.log(a,10))
print(a, " = ", n, "* 10^", x)

# Graphing Exponents and Logs

xmin = -10
xmax = 10
ymin = -10
ymax = 10
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'k') # x axis
plt.plot([0,0],[ymin,ymax], 'k') # y axis

x1 = np.linspace(xmin, xmax, 1000)

plt.plot(x1, 2**x1, 'b')  # Change this line

plt.plot(x1, x1, 'r')

x2 = np.linspace(.001, xmax, 500)

plt.plot(x2, np.log2(x2), 'g')  # Change this line

plt.show()


# Log Application - pH Scale

decimal = float(input("Enter the hydrogen concentration as a decimal number: "))

h = math.ceil(-math.log(decimal,10))

print("pH = ", h)

# Functions for the Project

def mort_pay():
    
    p = float(input("Amount borrowed: "))
    r = float(input("Annual percentage rate: "))
    t = float(input("Number of years: "))
    mult = 1+r/12
    exp = 12*t
    top = r/12*mult**exp
    bot = (mult**exp)-1
    pmt = top/bot

    answer = "Monthly payment = $", pmt

def mort_tpay_prt(p,r,t):

    numerator = (r/12)*(1+(r/12))**(12*t)
    denominator = (1+(r/12))**(12*t) - 1

    payment = p* numerator/denominator
    
    answer = "payment = "+str(payment) 

    return answer

def to_sci_notation():

    a = float(input('Enter a number to convert to scientific notation: '))

    n = round(a*10**(-x1),2) 
    x = math.floor(math.log(a,10))
    answer = a, " = ", n, "* 10^", x

    return answer


print(mort_pay())

print(mort_tpay_prt(24000000,.05,30))

print(to_sci_notation)
