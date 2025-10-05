import os

def LayTenFile(duongdan):
    return os.path.basename(duongdan)  # lấy phần cuối cùng của đường dẫn

def LayTenBaiHat(duongdan):
    ten_file = os.path.basename(duongdan)
    ten_baihat, _ = os.path.splitext(ten_file)  # tách tên và phần mở rộng
    return ten_baihat

# --- Kiểm tra ---
duongdan = r"d:\music\muabui.mp3"

print("Tên file:", LayTenFile(duongdan))
print("Tên bài hát:", LayTenBaiHat(duongdan))