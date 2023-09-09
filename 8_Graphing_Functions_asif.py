import matplotlib.pyplot as plt

# basic graph

fig, ax = plt.subplots()
plt.show()

# Dimensions

fig, ax = plt.subplots()
plt.axis([-10,10,-10,10])
plt.show()

# Another way

xmin = 1
xmax = 10
ymin = 1
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.show()

# Display axis line

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'r') # r is red
plt.plot([[0,0],[ymin,ymax]],'b') # b is blue
plt.show()

# plot a point

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([5],[4],'ro') # o for circle # r for red
plt.show()

# plot multiple points (with table of points)

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([[0,0],[ymin,ymax]],'b')

for x in range (-2,10):
    
    y = 0.5*x + 1
    plt.plot([x],[y],'ro')
    print("x = "+str(x)+", y = "+str(y))

plt.show()



