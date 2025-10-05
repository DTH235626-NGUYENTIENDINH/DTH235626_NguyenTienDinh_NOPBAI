def DocSo(n):
    donvi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if n < 10:
        return donvi[n]
    elif n < 100:
        if n % 10 == 0:
            return donvi[n // 10] + " mươi"
        elif n // 10 == 1:
            return "mười " + donvi[n % 10]
        elif n % 10 == 1:
            return donvi[n // 10] + " mươi mốt"
        elif n % 10 == 5:
            return donvi[n // 10] + " mươi lăm"
        else:
            return donvi[n // 10] + " mươi " + donvi[n % 10]
#main
n = int(input("Nhập số nguyên dương n (0 < n < 100): "))
print(DocSo(n))

