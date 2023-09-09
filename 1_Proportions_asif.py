# 1/2 = x/16

# put a zero in unknown number
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
