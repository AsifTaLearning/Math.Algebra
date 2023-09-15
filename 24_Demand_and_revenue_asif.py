import matplotlib.pyplot as plt
import numpy as np

# Selling t shirts example

price = 5
demand = 50 - 2*price 
revenue = price*demand # Equations
total_cost = 4*demand
profit = revenue - total_cost

print("price = "+str(price))
print("demand = "+str(demand))
print("revenue = "+str(revenue))
print("total cost = "+str(total_cost))
print("profit = "+str(profit))


price_1 = 2
demand_1 = 46
price_2 = 10
demand_2 = 30

m = (demand_2 - demand_1)/(price_2 - price_1)
b = demand_1 - m*price_1

xmin = 0
xmax = 50
ymin = 0
ymax = 320

points = 10*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig,ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.xlabel("price")
plt.title("Financial algebra")

demand = m*x+b

        #plt.ylabel("Demand")
        #plt.plot(x,demand)

revenue = x*demand

plt.ylabel("Revenue")
plt.plot(x,revenue)

plt.show()
