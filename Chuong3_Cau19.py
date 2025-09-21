import math
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
s = 0
for i in range(n + 1):
    mu = 2*i+1
    s += x**mu/math.factorial(mu)
print("S({0},{1}) = {2}" .format(x,n,s))

