# Posative and negative exponents

print(10**1)
print(10**2)
print(10**3)

print(10**0)

print(10**-1)
print(10**-2)
print(10**-3)

# length of variables

num = input("enter a number ")

len_num = len(num)

print('length of number is '+str(len_num))

# Some additions with decimals.like(.003)

num = input("enter a number")

ans = float(num) + 4

print("final is "+str(ans))

# conversion (fraction , percent)

deci = input("enter a decimal for convert ")

exponent = int(len(deci))-1
n = float(deci)
numerator = n * 10**exponent
denominator = 10**exponent
percent = n * 100

print("decimal ="+str(n))
print("fraction = "+str(numerator)+"/"+str(denominator))
print("percent = "+str(percent)+"%")


