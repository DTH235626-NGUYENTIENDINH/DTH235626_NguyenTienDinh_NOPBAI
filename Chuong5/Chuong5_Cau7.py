def ToiUuChuoiDanhTu(chuoi):
    # Bước 1: Xóa khoảng trắng đầu và cuối, tách các từ
    tu = chuoi.strip().split()

    # Bước 2: Viết hoa chữ cái đầu mỗi từ, các chữ sau viết thường
    tu_da_dinh_dang = [t.capitalize() for t in tu]

    # Bước 3: Ghép lại thành chuỗi với mỗi từ cách nhau 1 khoảng trắng
    chuoi_toi_uu = " ".join(tu_da_dinh_dang)

    return chuoi_toi_uu


# --- Kiểm tra ---
chuoi = "  TRần   duY   thAnH  "
print("Chuỗi gốc:  ", chuoi)
print("Chuỗi tối ưu:", ToiUuChuoiDanhTu(chuoi))