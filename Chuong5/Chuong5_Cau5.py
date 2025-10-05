# Nhập chuỗi từ bàn phím
chuoi = input("Nhập vào một chuỗi: ")

# Khởi tạo biến đếm
hoa = thuong = so = dacbiet = khoangtrang = nguyenam = phuam = 0

# Tập hợp nguyên âm tiếng Anh
nguyen_am = "aeiouAEIOU"

for ch in chuoi:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1
    elif ch.isspace():
        khoangtrang += 1
    else:
        dacbiet += 1

    # Đếm nguyên âm và phụ âm
    if ch.isalpha():  # chỉ xét ký tự là chữ cái
        if ch in nguyen_am:
            nguyenam += 1
        else:
            phuam += 1

# Xuất kết quả
print("Số chữ IN HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ số:", so)
print("Số ký tự đặc biệt:", dacbiet)
print("Số khoảng trắng:", khoangtrang)
print("Số nguyên âm:", nguyenam)
print("Số phụ âm:", phuam)
