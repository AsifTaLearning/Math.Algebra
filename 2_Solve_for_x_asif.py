from sympy import symbols
from sympy.solvers import solve

# using sympy

# x-2

x = symbols("x")

eq = x-2
ans = solve(eq,x)

print("x is "+str(ans))

# 2x-4

x = symbols("x")

eq = 2*x - 4
ans = solve(eq,x)

print("x is "+str(ans))

# x^2 - 4

eq = x**2 - 4
ans = solve(eq,x)

print("x is "+str(ans))

#.............................................................................

# not using sympy

# x+3=5

num1 = 3
num2 = 5

x = num2-num1

print("x is "+str(x))


# x-2=10

num1 = 2
num2 = 10

x = num2+num1

print("x is "+str(x))

# 3x=12

num1 = 3
num2 = 12

x = num2/num1

print("x is "+str(x))

# x/4=2

num1 = 4
num2 = 2

x = num2*num1

print("x is "+str(x))

#extra x+7.2=11.1

num1 = 7.2
num2 = 11.1

x = num2 - num1

print("x is "+str(x))


# 4x+6=22

num1 = 4
num2 = 6
num3 = 22

x = (num3 - num2)/num1

print("x is "+str(x))
