from sympy import *

# Another solving equation
# a*x^2 + b*x + c

var('a b c x')

eq = a*x**2 + b*x + c
eq1 = Eq(eq,0)

ans = solve(eq1,x)

for s in ans:

    print("solution = "+str(s))





