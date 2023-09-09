

def calc(in_string):

    if "/" in in_string :

        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])

        ans = n/d

        return ans

    else:
        ans = in_string

        return ans

def random_eq():

    import random

    a = random.randint(1,11)
    b = random.randint(2,24)

    print(str(a)+"x="+str(b))

    ans = b/a

    x = float(input("x = "))

    if x == ans:
        print("correct")

    else:
        print("not correct")

def random_eq2():

    import random

    a = random.randint(1,11)
    b = random.randint(2,24)

    print("x+"+str(a)+"="+str(b))

    ans = b-a

    x = float(input("x = "))

    if x == ans:
        print("correct")

    else:
        print("not correct")




from sympy import *

# 2*x + 1

x = symbols("x")
eq = 2*x + 1
ans = solve(eq,x)

print("x = "+str(ans))

# 2*x^2 - 4

x = symbols("x")
eq = 2*x**2 - 4
ans = solve(eq,x)

print("x = "+str(ans[0]))

# Taking input

x = symbols("x")
eq = input("Enter equation \n")
ans = solve(eq,x)

print("x = "+str(ans[0]))

# Another method for printing
# 2*x^2 - 4

x = symbols("x")
eq = 2*x**2 - 4
ans = solve(eq,x)

for s in ans:

    print("x = "+str(s))

# Multiple solutions
# (x+1)*(x+2)*(x-3) 

for s in ans:

    x = symbols("x")
    eq = (x+1)*(x+2)*(x-3)
    ans = solve(eq,x)

    print("x = "+str(s))

# Another type of variable
# 2*x + 10

var('x')
eq = 2*x + 10
eq1 =   Eq(eq,0)
ans = solve(eq1,x)

print("x = "+str(ans[0]))

# Same problem but y = x
# 2*x + 10

var('x y')
eq = 2*x + 10
eq1 =   Eq(eq,y)
ans = solve(eq1,x)

print("x = "+str(ans[0]))

# 2*x + 10 - y

var('x y')
eq = 2*x + 10 - y
eq1 =   Eq(eq,0)
ans = solve(eq1,x)

print("x = "+str(ans[0]))

# 2*x - y

var('x y')
eq = 2*x - y
eq1 =   Eq(eq,0)
ans = solve(eq1,x)

print("x = "+str(ans[0]))

# Factor 
# (2*x) + (10*y) + 6

var('x y')
eq = 2*x + 10*y + 6
ans = factor(eq)

print("x = "+str(ans))

# x^2 - 2

var('x')
eq = x**2 - 4
ans = factor(eq)

print("x = "+str(ans))

# x^3 - 2*x^2 - 5*x + 6

var('x')
eq = x**3 - 2*x**2 - 5*x + 6
ans = factor(eq)

print("x = "+str(ans))

# Number to float conversion

fnum = float(input("fraction = "))

print("float is "+str(fnum))


# Another problem

in_input = input("Division ")

ans = calc(in_input)

print("Answer is "+str(ans))


# Random equation
# a*x = b

random_eq()

# x+a = b

random_eq2()








