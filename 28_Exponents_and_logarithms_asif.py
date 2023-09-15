import math
import matplotlib.pyplot as plt
import numpy as np

# base 10 , the common log

print(math.log(10000,10))

    # python weirdness (expect 3 in this problem but )

print(math.log(1000,10))

    # so need to round it

print(round(math.log(1000,10),4))

# base 2 , or any other base

print(math.log(16,2))

# Natural log
# e = 2.718281828

print(math.log(2.718281828))

x = math.e**3

print(math.log(x))

# A = Pe^rt
# 2P = Pe^rt
# 2 = e^rt
# ln(2) = rt
# ln(2)/r = t 

r =.02
t =round(math.log(2)/r)

print("it will double in "+str(t)+" years")

# Graphing

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points = 10*(xmax-xmin)
x = np.linspace(xmin,xmax,points)
x2 = np.linspace(.01,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

y1 = math.e**x
plt.plot(x,y1,'r')

y2 = np.log(x2)
plt.plot(x2,y2,'violet')

y3 = x
plt.plot(x,y3,'g')

plt.show()

# Scientific notation

print(3.2*10**5)

# Exponent -2 works fine

print(4.5*10**-2)

# Exponent -3 get weird

print(4.5*10**-3)

# Exponent -4 requires round() to display decimal notation

a = round(4.5*10**-4,5)

print(a)

# Exponent -5 forces the sceintific notation

a = round(4.5*10**-5,6)

print(a)

# convert to scientific notation

a = .0005

exp = math.floor(math.log(a,10))
n = round(a/(10**exp),2)

if n>=10:
    exp = exp + 1
    n = a/(10**exp)

print("a = "+str(n)+" 10** "+str(exp))