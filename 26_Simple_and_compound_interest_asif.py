import math

# Simple interest
# interest = principle * rate * time

p = 1000
r = .05
t = 3

interest = p*r*t

print("interest = "+str(interest))

#  New amount = principle + interest

p = 1000
r = .05
t = 3

interest = p*r*t
a = p + interest

print("new amount = "+str(a))

# The algebra for for any perecent increase
# New amount = p + p*r
# new amount = p * (1+r)

p = 1000
r = .05

a = p * (1+r)

print("New amount = "+str(a))

# Original amount = p
# New amount = p(1+r)
# compounded again = p(1+r)(1+r)
# and again = p(1+r)(1+r)(1+r) = p(1+r)^3

p = 1000
r = .05
t = 3

annuity = p * (1+r)**t

print("Annuity "+str(annuity))

# when the compounding n times per year
# A = p(1+r/n)**nt

p = 1000
r = .05
t = 3
n = 12

annuity = p * (1+(r/n))**(n*t)

print("Annuity "+str(annuity))

# The irrational number e

print(math.e)

# Countinous growth : annuity = pe^rt   (when large n)

p = 1000
r = .05
t = 3
n = 52

n_times = p * (1+(r/n))**(n*t)

continous = p*math.e**(r*t)

print(str(n_times)+" or "+str(continous))

# mortgage formula  (when large amount of money)
# monthly payment = p * ((r/12)*(1+(r/12))**(12*t)) / ((1+(r/12))**(12*t) - 1)

p = 240000.00
r = .055
t = 30

numerator = (r/12)*(1+(r/12))**(12*t)
denominator = (1+(r/12))**(12*t) - 1

payment = round(p* numerator/denominator, 2)

print("monthly payment = "+str(payment))

# Amortization (mortgage payment schedule)

p = 240000
r = .055
t = 30

numerator = (r/12)*(1+(r/12))**(12*t)
denominator = (1+(r/12))**(12*t) - 1

payment = round(p* numerator/denominator, 2)

print("payment = "+str(payment))

balance = p

print("month \t balance \t interest")

for a in range(12*t):
    interest = round(balance*r/12 , 2)
    if a % 24 == 0 or a == 359:
        print(str(a) +" \t "+str(balance)+" \t "+str(interest))
    balance = round(balance + interest - payment,2)

# Retirement account estimation

p = 1000
r = .08
t = 38

monthly = 350
annuity = p

for a in range(12*t):

    annuity = (annuity + monthly)*(1+(r/12))

print("annuity = "+str(round(annuity,2)))
print("Annual income from interest = "+str(round(annuity*r,2)))
