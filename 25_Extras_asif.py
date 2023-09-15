import matplotlib.pyplot as plt

# Supply and demand graph

old_demand_x = 1
new_demand_x = 12
old_price_y = 14
new_price_y = 3
old_supply_x = 11
new_supply_x = 1

xmin = 0
xmax = 15
ymin = 0
ymax = 15

fig ,ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')

plt.xlabel("Quantity")
plt.ylabel('price')
plt.title("Green = supply , Red = Demand")

plt.plot([old_demand_x,new_demand_x],[old_price_y,new_price_y],'r')

plt.plot([old_supply_x,new_supply_x],[old_price_y,new_price_y],'g')

plt.show()

# Calculate the price if elasticity of demand
# elasticity = (percent change in demand) / (percent change in price)

old_demand = 5
new_demand = 6
old_price = 11
new_price = 10

price_change = (new_price - old_price) / old_price # percent change in price

demand_change = (new_demand/old_demand) / old_demand # percent change in demand

e_number = demand_change / price_change

print(e_number)

if e_number > 1:

    print("Demand is elastic")

elif e_number == 1:

    print("demand is unitary or proportional")

elif e_number < 1 :

    print('Demand is inelastic')

else:

    print("?")

# Calculate the price if elasticity of supply
# elasticity = (percent change in supply) / (percent change in price)

old_price = 4
new_price = 7
old_supply = 10
new_supply = 11

price_change = (new_price - old_price) / old_price # percent change in price

supply_change = (new_supply/old_supply) / old_supply # percent change in supply

e_number = supply_change / price_change

print(e_number)

if e_number > 1:

    print("Supply is elastic")

elif e_number == 1:

    print("Supply is unitary or proportional")

elif e_number < 1 :

    print('Supply is inelastic')

else:

    print("?")

