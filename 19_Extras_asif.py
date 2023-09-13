from sympy.plotting import plot
from sympy.solvers import solve
from sympy import var , nonlinsolve , Eq ,symbols
 

# Full time employed canadians worked 39.5 hours per week . typical adult sleep everyday 8 hours.left over for personal activities 

print(24*7 - 39.5 - 8*7)

# Housing ,first half of 2009 year were down 46.7633% from 2008, when 1500 new homes were started . how many housing starts there in 2009?

print(1500*(1.00 - 0.46733))

# if $ 9.99 is changed to $ 10.49 what is the percent change?

print(0.50 / 9.99 * 100)

# 19.99 lowered by 10 %  is what dollar amount

print(19.99 * (1.00 - 0.10))

# what amount when increased by 40 % is $ 3,500 ?
# x * (1 + rate) = new amount

amount = 3500 / 1.40

print(amount)

# Good tickets is 20 $ and lowest tickets is 10 $ ,at the last game 5,332 fans wre attendence and total revenue was 71,750 $
# 20*x + 10*y = 71,750
# x + y = 5332


var('x y')

first = 20*x + 10*y - 71750
second = x + y - 5332
        

solution = nonlinsolve([first,second],(x,y))

for a in range(len(solution.args)) :

    xsolution = solution.args[a][0]
    ysolution = solution.args[a][1]
    print('('+str(xsolution)+","+str(ysolution)+')')

y_first = Eq(first,0)
y1 = solve(y_first,y)

y_second = Eq(second,0)
y2 = solve(y_second,y)

print("y = "+str(y1[0]))
print("y = "+str(y2[0]))

x = symbols('x')
xmin  = -10
xmax = 10

plot(y1[0],y2[0], (x,xmin,xmax))

# pretzel 50% , cheerios 30 % , peanuts 20 % ,she wants 2 kg container of her mix . if pretzel cost $ 9.99/kg , cheerios $ 6.99/kg , peanuts $ 4.95 / kg 
# what is the average cost per 100 g rounded to four decimals?

pretzel = .5 * 2  # % and kg
cherios = .3 * 2
peanuts = .2 * 2

cost = pretzel * 9.99 + cherios * 6.99 + peanuts * 4.95

print("total cost = "+str(cost))

print("for 100 g = "+str(cost/20)) # 2kg / 100g = 20g
