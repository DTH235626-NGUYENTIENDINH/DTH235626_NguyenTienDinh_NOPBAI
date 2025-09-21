thang = int(input("Nhập tháng (1-12): "))
while True:   
    if 1 <= thang <= 12:
        if 1 <= thang <= 3:
            print("Quý 1")           
        elif 4 <= thang <= 6:
            print("Quý 2")
        elif 7 <= thang <= 9:
            print("Quý 3")
        else:
            print("Quý 4")
        break
    else:
        thang = int(input("Tháng không hợp lệ. Vui lòng nhập lại (1-12): "))
    

