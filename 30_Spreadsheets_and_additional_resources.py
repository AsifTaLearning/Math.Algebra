import pandas as pd
import matplotlib.pyplot as plt
from meteostat import Point ,Daily
from datetime import datetime
from numpy.core.fromnumeric import mean
import numpy as np

# pandas

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/faithful.csv"

table_1 = pd.read_csv(url)
print(table_1.head(2))

col_names = table_1.columns

print("\n column names: ")

for a in range(len(col_names)):

    print(str(a)+" "+str(col_names[a]))

print("\n column names: ")

for col in col_names:

    print(col)
    
# graph

x = table_1['Index'].to_numpy()
y = table_1[' "Eruption length (mins)"'].to_numpy()

xmin = x.min()-5
xmax = x.max()+5
ymin = y.min()-5
ymax = y.max()+5

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'black')
plt.plot([0,0],[ymin,ymax],'black')

plt.plot(x,y,'ro')
plt.plot(x,y,'b')

plt.show()

# using variables for column names

x_name = col_names[0]
y_name = col_names[2]

x = table_1[x_name].to_numpy()
y = table_1[y_name].to_numpy()

xmin = x.min()-5
xmax = x.max()+5
ymin = y.min()-5
ymax = y.max()+5

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'black')
plt.plot([0,0],[ymin,ymax],'black')

plt.plot(x,y,'ro')
plt.plot(x,y,'b')

ax.set_xlabel(x_name)
ax.set_ylabel(y_name)

plt.show()

# metostat

start = datetime(2022,1,1)
end = datetime(2022,12,31)

Philly = Point(39.99,-75.15,10)
burbs = Point(40.1,-75.2)

daily_data = Daily(Philly,start,end)
my_data = daily_data.fetch()
num_data = my_data['wspd'].to_numpy()
print('city mean = '+str(mean(num_data)))

daily_data2 = Daily(burbs,start,end)
my_data2 = daily_data2.fetch()
num_data2 = my_data2['wspd'].to_numpy()
print('suburbs mean = '+str(mean(num_data2)))

x = np.linspace(1,365,365)

plt.plot(x,my_data['wspd'])
plt.plot(x,my_data2['wspd'])
plt.show()

# monthly loop

for m in range(1,11):

    start = datetime(2022,1,1)
    end = datetime(2022,12,31)

    burbs = Point(40.1,-75.2)

    daily_data = Daily(burbs,start,end)
    my_data = daily_data.fetch()
    num_data = my_data['wspd'].to_numpy()
    print("month = "+str(m)+' mean = '+str(mean(num_data)))

    my_data.plot(y = ['wspd'])

    plt.show()
