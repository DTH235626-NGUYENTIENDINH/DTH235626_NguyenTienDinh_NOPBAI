import datetime

def NgayKeTiep(ngay, thang, nam):
    try:
        date = datetime.date(nam, thang, ngay)
        next_day = date + datetime.timedelta(days=1)
        return next_day.day, next_day.month, next_day.year
    except ValueError:
        return "Ngay khong hop le"
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False  
def isYearValid(year):
    return year > 0
def isMonthValid(month):
    return 1 <= month <= 12
def isDayValid(day, month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        if isLeapYear(year):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    return False 
#main
""""
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
d,m,y = NgayKeTiep(ngay,thang,nam)
print(f"Ngày kế tiếp là: {d}/{m}/{y}")
"""
#test
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
while True:
    if not isYearValid(nam):
        print("Năm không hợp lệ. Vui lòng nhập lại.")
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        continue
    if not isMonthValid(thang):
        print("Tháng không hợp lệ. Vui lòng nhập lại.")
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        continue
    if not isDayValid(ngay, thang, nam):
        print("Ngày không hợp lệ. Vui lòng nhập lại.")
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        continue
    break
d,m,y = NgayKeTiep(ngay,thang,nam)
print(f"Ngày kế tiếp là: {d}/{m}/{y}")

