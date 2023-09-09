from sympy import *

print("\nWelcome to ASIF'S calculatoR \n       .....................\n1.  1/2 = x/16\n2.  custom solve equation\n3.  x^3 - 2*x^2 - 5*x + 6 \n4.  a*x^2 + b*x + c\n5.  conversion (fraction , percent)\n6.  a*x^2 + b*x + c\n")

selection = int(input("Choose a number  \n"))

# Proportion
# 1/2 = x/16
# put a zero in unknown number

if selection == 1:

    n1 = 1 
    d1 = 2

    n2 = 0
    d2 = 16

    # cross multiplication

    if n2 == 0:
        n2=(n1*d2)/d1
        print("n2 is "+str(n2))


    if d2 == 0:
        d2=(d1*n2)/n1
        print("d2 is "+str(d2))

# .............................................................


# Taking input and solve equation

elif selection == 2:

    x = symbols("x")
    eq = input("Enter equation(=0) \n")
    ans = solve(eq,x)

    for s in ans:

        print("x = "+str(s))


#...............................................................

# Factor
# x^3 - 2*x^2 - 5*x + 6

elif selection == 3:

    var('x')
    eq = x**3 - 2*x**2 - 5*x + 6
    ans = factor(eq)

    print("x = "+str(ans))

#..............................................................

# solve for variables
# a*x^2 + b*x + c

elif selection == 4:

    var('a b c x')

    eq = a*x**2 + b*x + c
    eq1 = Eq(eq,0)

    ans = solve(eq1,x)

    for s in ans:

        print("solution = "+str(s))


#...............................................................

# conversion (fraction , percent)

elif selection == 5:

    deci = input("enter a decimal for convert ")

    exponent = int(len(deci))-1
    n = float(deci)
    numerator = n * 10**exponent
    denominator = 10**exponent
    percent = n * 100

    print("decimal ="+str(n))
    print("fraction = "+str(numerator)+"/"+str(denominator))
    print("percent = "+str(percent)+"%")

#................................................................

# Another solving equation
# a*x^2 + b*x + c

elif selection == 6:

    var('a b c x')

    eq = a*x**2 + b*x + c
    eq1 = Eq(eq,0)

    ans = solve(eq1,x)

    for s in ans:

        print("solution = "+str(s))


else :

    print("This number is not existed")
