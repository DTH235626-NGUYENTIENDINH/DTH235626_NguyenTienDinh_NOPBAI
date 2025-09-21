import datetime

def NgayKeTiep(ngay, thang, nam):
    try:
        date = datetime.date(nam, thang, ngay)
        next_day = date + datetime.timedelta(days=1)
        return next_day.day, next_day.month, next_day.year
    except ValueError:
        return "Ngay khong hop le"
    
#main
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
d,m,y = NgayKeTiep(ngay,thang,nam)
print(f"Ngày kế tiếp là: {d}/{m}/{y}")


