
import matplotlib.pyplot as plt
import numpy as np

#numpy array loop

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'blue')

y = 2*x + 1

plt.plot(x,y,'k') # k is black

plt.show()

# Custamization (labels , grid lines ,trick marks)

xmin = -10
xmax = 10
ymin = -10
ymax = 10

points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])

ax.set_title("Graph") # Heading
ax.set_xlabel("x values")
ax.set_ylabel("y values")

ax.grid(True) # Grid lines

ax.set_xticks(np.arange(xmin,xmax,2)) # ticks (gap between numbers)
ax.set_yticks(np.arange(ymin,ymax,2))

plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'blue')

y = 2*x + 1

plt.plot(x,y,'k', label = 'y = 2*x + 1')
plt.plot([4],[6],'ro', label = '(4,6)')
plt.plot(x,3*x, label = 'steeper line')
plt.legend() # For show labels

plt.show()

