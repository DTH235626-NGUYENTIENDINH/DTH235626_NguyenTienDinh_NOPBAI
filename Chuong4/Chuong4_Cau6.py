from random import randrange

# Sinh thử 10 giá trị để minh họa
print("Ví dụ 10 giá trị sinh ra từ randrange(0, 100):")
for _ in range(10):
    print(randrange(0, 100), end=' ')

print("\nCác giá trị có thể xuất hiện là các số nguyên từ 0 đến 99.")
print("Các giá trị sau KHÔNG thể xuất hiện: 4.5, -1, 100")
print("Các giá trị sau CÓ thể xuất hiện: 0, 34, 99")