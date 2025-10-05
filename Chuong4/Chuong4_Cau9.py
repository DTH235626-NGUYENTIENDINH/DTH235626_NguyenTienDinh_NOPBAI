import math

def can_bac_2_long_nhau(n):
    result = 0
    for _ in range(n):
        result = math.sqrt(2 + result)
    return result

# Nhập số lần lồng căn
so_lan = int(input("Nhập số lần lồng căn bậc 2: "))
ket_qua = can_bac_2_long_nhau(so_lan)
print(f"Kết quả sau {so_lan} lần lồng căn là: {ket_qua}")