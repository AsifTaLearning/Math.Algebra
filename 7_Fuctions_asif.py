
def f(x):

    y = 4*x + 3

    return y

# y = 4*x + 3

x = 5
y = 4*x + 3

print("x ="+str(x)+" , y = "+str(y))

for x in range(11):

    y = 4*x + 3

    print("x ="+str(x)+" , y ="+str(y))

# y = 4*x + 3 another way

for x in range(11):
    
    print("x = "+str(x)+" , y = "+str(f(x)))

#