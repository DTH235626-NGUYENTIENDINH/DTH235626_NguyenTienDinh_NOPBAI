def PhepToan(x, y, toantu):
    if toantu == '+':
        return x + y
    elif toantu == '-':
        return x - y
    elif toantu == '*':
        return x * y
    elif toantu == '/':
        if y != 0:
            return x / y
        else:
            return "Lỗi: Chia cho 0"
    else:
        return "Lỗi: Toán tử không hợp lệ"
#main
a = float(input("Nhập a: "))
dau = input("Nhập phép toán (+, -, *, /): ")
b = float(input("Nhập b: "))

kq = PhepToan(a, b, dau)
print(f"{a} {dau} {b} = {kq}")