from sympy.plotting import plot

from sympy import *


# Two equation solve 
# 0 = 2*x + y - 1
# 0 = x - 2*y + 7


x , y = symbols('x y')

first = 2*x + y - 1
second = x - 2*y + 7

solution = linsolve([first,second],(x,y))

print(solution)

# Nicer looking output (same problem)

x,y = symbols('x y')

first = 2*x + y - 1
second = x - 2*y + 7

solution = linsolve([first,second],(x,y))

x_solution = solution.args[0][0]
y_solution = solution.args[0][1]

print("x = "+str(x_solution)+" , y = "+str(y_solution))

# sympy plotting

var("x y")

first = 2*x + y - 1
second = x - 2*y + 7

solution = linsolve([first,second],(x,y))

x_solution = solution.args[0][0]
y_solution = solution.args[0][1]

print('('+str(x_solution)+","+str(y_solution)+')')

y_first = Eq(first,0)
y1 = solve(y_first,y)

y_second = Eq(second,0)
y2 = solve(y_second,y)

print("y = "+str(y1[0]))
print("y = "+str(y2[0]))

x = symbols('x')

plot(y1[0],y2[0], (x,-10,10))