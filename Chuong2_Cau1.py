import math
try:
    r = float(input("Nhập bán kính hình tròn: "))
    if r < 0:
        print("Bán kính không được âm.")
    else:
        chu_vi = 2 * math.pi * r
        dien_tich = math.pi * r ** 2
        print(f"Chu vi hình tròn: {chu_vi:.2f}")
        print(f"Diện tích hình tròn: {dien_tich:.2f}")
except:
    print("Vui lòng nhập một số hợp lệ.") 