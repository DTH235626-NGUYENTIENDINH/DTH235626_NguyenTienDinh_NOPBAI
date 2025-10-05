from math import sqrt

print("Nhập tọa độ điểm A (xA, yA):")
xA = float(input("xA = "))
yA = float(input("yA = "))

print("Nhập tọa độ điểm B (xB, yB):")
xB = float(input("xB = "))
yB = float(input("yB = "))

dAB = sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
print(f"Độ dài đoạn AB = {dAB}")