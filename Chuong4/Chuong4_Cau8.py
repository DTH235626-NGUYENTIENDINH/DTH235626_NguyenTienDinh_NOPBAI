from math import log

print("Nhập x (x > 0):")
x = float(input())
print("Nhập a (a > 0, a ≠ 1):")
a = float(input())

if x > 0 and a > 0 and a != 1:
    loga_x = log(x) / log(a)
    print(f"log_a({x}) = {loga_x}")
else:
    print("Giá trị x và a không hợp lệ (x > 0, a > 0, a ≠ 1).")