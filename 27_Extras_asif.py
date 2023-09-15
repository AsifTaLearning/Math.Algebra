  #! %matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np

# Payment function without rounding

def payment(p,r,t):
    numerator = (r/12)*(1+(r/12))**(12*t)
    denominator = (1+(r/12))**(12*t) - 1

    payment = p* numerator/denominator

    return payment

p = 240000
r = .055
t = 30

payment1 = payment(p,r,t)

print("payment = "+str(payment1))

# Similar function with rounding to compare payments for slight changes in principle

def pmt(p):
    r = .06
    t =30

    numerator = (r/12)*(1+(r/12))**(12*t)
    denominator = (1+(r/12))**(12*t) - 1

    pay = round(p* numerator/denominator, 2)

    print("principle: "+str(p)+" payment: "+str(pay))

show_slider = interactive(pmt ,p = (1,300000))
show_slider

# Same problem with graph

xmin = 0
xmax = 300000
ymin = 0
ymax = 4000

points = 10*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.grid()
ax.set_xlabel('amount borrowed')
ax.set_ylabel('monthly payment')

y1 = payment(x, .06 ,30)
plt.plot(x,y1)

plt.show()

# Slope formula

r = .06
t = 30

x1 = 50000
y1 = payment(x1,r,t)
x2 = 300000
y2 = payment(x2,r,t)

slope = (y2-y1)/(x2-x1)

print("Slope = "+str(slope))