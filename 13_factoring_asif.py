import math
import sympy
from sympy import symbols


# Reminder

print("reminder = "+str(5 % 3))

# Find all factors

num = 12

for test_factors in range(1,num+1):

    if num % test_factors == 0 :

        print( test_factors)

# Reduce factors to lowest term

numerator = 12
denominator = 24
factor = 1

for test_factor in range(1,denominator+1):

    if numerator % test_factor == 0 and denominator % test_factor == 0:

        factor = test_factor

n = int(numerator / factor)
d = int(denominator / factor)

print("original = "+str(numerator)+"/"+str(denominator))
print("reduced = "+str(n)+"/"+str(d))

# Decimal number convert to lowest fraction 

num = input("enter  decimal number ")

exponent = int(len(num))-1

dnum = float(num)

numerator = dnum * 10**exponent
denominator = 10**exponent

print("factor = "+str(numerator)+"/"+str(denominator))

factor = 1

for test_factor in range(1,denominator+1):

    if numerator % test_factor == 0 and denominator % test_factor == 0:

        factor = test_factor

n = int(numerator / factor)
d = int(denominator / factor)

print("reduced = "+str(n)+"/"+str(d))

# square root

sqr = math.sqrt(25)

print("square root = "+str(sqr))


# factoring square roots

n = 12

limit = math.floor(math.sqrt(25)) +1

for maybe_factor in range(1,limit):

    if n % (maybe_factor**2) == 0:

        max_factor = maybe_factor


print("n = "+str(n))
print("square rooted factor = "+str(max_factor))
print("square factor = "+str(maybe_factor**2))
print("integer = "+str(n / (max_factor**2)))

 
# same problem with sympy

n = 12

limit = math.floor(math.sqrt(n)) +1
max_factor = 1
other_factor = 1
square_root = 1

for maybe_factor in range(1,limit):
    if n % (maybe_factor**2) == 0:

        max_factor = maybe_factor**2

other_factor = n/max_factor

square_root = math.sqrt(max_factor)
other_factor = int(other_factor)
output = square_root * sympy.sqrt(other_factor)

print(output)




