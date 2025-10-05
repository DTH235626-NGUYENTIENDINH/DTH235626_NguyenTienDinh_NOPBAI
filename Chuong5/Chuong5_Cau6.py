import re

def NegativeNumberInStrings(s):
    nums = re.findall(r'-\d+', s)  # tìm tất cả chuỗi có dạng: dấu '-' theo sau là số
    nums = [int(n) for n in nums]  # chuyển sang số nguyên
    print("Các số nguyên âm trong chuỗi là:", *nums)

# --- Kiểm tra ---
NegativeNumberInStrings("abc-5xyz-12k9l--p")