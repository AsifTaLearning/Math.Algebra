
import math
import sympy
from sympy import symbols

# Addition

a=1
b=2

print(a+b)

# Substraction

c = 7
d = 3

print(c-d)

# Multiplication

e = 2
f = 4

print(e*f)

# Division

g = 8
h = 4

print(g/h)

# Cast input

strA = input('Enter a positive integer: ')
intA = int(strA)

strB = input('Enter another positive integer: ')
intB = int(strB)

print(intA+intB)

# Input and cast on the same line

intA = int(input('Enter an integer: '))
intB = int(input('Enter an integer: '))

print(intA+intB)

# Float numbers

a = float(input('Enter a number: '))

b = float(input('Enter a number: '))

print(a/b)

# Order of Operations

actual_answer = (1+4*2-14/2)**3

your_answer = 8

print('Actual answer is ', actual_answer)
print('Your answer is ', your_answer)

# Remainder and Modulus

a = 14
b = 6

print(a % b)

# Modulus and Factors

number = int(input('Enter an integer: '))
test_factor = int(input('Enter an integer to see if it’s a factor: '))

if number % test_factor == 0:
    print('true')
else:
    print('false')

# Finding Factors

number = int(input('Enter an integer: '))

for test_factor in range(1, number+1):
    if number % test_factor == 0:
        print(test_factor)

# Prime Numbers

number = int(input("Enter a positive integer: "))

prime_or_comp = "prime"

for test_number in range(2,number):

    if number % test_number == 0:

        prime_or_comp = "composite"

print(prime_or_comp)

# Reciprocals

n = float(input('Enter a number: '))

print(1/n)

# Splitting input

nums = input('Enter two numbers, separated by a comma: ')
sp = nums.split(",")

a = float(sp[0])
b = float(sp[1])

print(a,b)

# Square Numbers

n = float(input('Enter a number to square: '))

print(n**2)

# Square Root Function

n = float(input('Enter a number to find the square root: '))

print(math.sqrt(n))

# Floor Function

n = float(input('Enter a number with decimal places: '))

print(math.floor(n))

# Finding Square Factors

n = int(input('Enter an integer to find the greatest square factor: '))

max_factor = 1
upper_limit = math.floor(math.sqrt(n)) + 1

for maybe_factor in range(1,upper_limit):
    if n % (maybe_factor**2) == 0:
        max_factor = maybe_factor

print(max_factor**2)

# Dividing out Factors

n = int(input('Enter an integer to factor: '))
upper_limit = math.floor(math.sqrt(n)) + 1
square_root = 1
max_factor = 1
other_factor = 1

for maybe_factor in range(1, upper_limit):
    
    if n % (maybe_factor**2) == 0:

        max_factor = maybe_factor**2

other_factor = n/max_factor

print("", n, " = ", max_factor, " * ", other_factor)

# Factoring Square Roots

n = int(input('Without the radical, enter a square root to factor: '))

upper_limit = math.floor(math.sqrt(n)) + 1
max_factor = 1
other_factor = 1
square_root = 1

for maybe_factor in range(1, upper_limit):
    if n % (maybe_factor**2) == 0:
        max_factor = maybe_factor**2

other_factor = n/max_factor

square_root = int(math.sqrt(max_factor))
other_factor = int(other_factor)
output = square_root*sympy.sqrt(other_factor)

# Rounding

a = 14588132
b = 0.006538298336


print(round(a,-6))
print(round(b,3))

# Fractions, Decimals, Percents

digits = input("Enter a decimal number to convert: ")
exponent = int(len(digits))-1
n = float(digits)

numerator = n * 10**exponent
denominator = 10**exponent
percent = n*100

print("The decimal is ", n)
print("The fraction is ", numerator, "/", denominator)
print("The percent is ", percent, " %")

# Defining a Function

def fun():
    print("This is in the function")

print("This is outside the function")

fun()

print("Back outside the function")

# Function with Input

def greeting(name):
    print("Hello ", name)

nombre = input("What is your name? \n")

greeting(nombre)

# Function with Two Inputs

def add(a,b,c):
  
  sum = a+b+c
  print("The sum is ", sum)

first = float(input("Enter a number: \n"))
second= float(input("Enter another number: \n"))
third = 3

add(first,second,third)

# Function with Return Value

def multiplied(number):

    return number*3

a = float(input("Enter a number: \n"))

print("Your number multiplied = ", multiplied(a))

# Solving for x

import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

eq = input('Enter an equation to solve for x: 0 = ')

print(len(solve(eq,x)))
print("x = ", solve(eq,x)[0])

# Create a Menu

print("1.....\n 2............\n")

d = int(input("enter a number"))

if d == 1:
  
  print("option one selected")

if d == 2:
  
  print("option 2 selected")

else:
  
  print("some error")




