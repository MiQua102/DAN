import re

with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Define tien_giam_gia and fix tong_tien
old_calc = '''    for sd in danh_sach_su_dung:
        tien_dich_vu += (sd.thanhTien or 0)
    tong_tien = tien_phong + tien_dich_vu'''

new_calc = '''    for sd in danh_sach_su_dung:
        tien_dich_vu += (sd.thanhTien or 0)
    
    tien_giam_gia = getattr(dp, 'tienGiamGia', 0) or 0
    tong_tien = tien_phong + tien_dich_vu - tien_giam_gia
    if tong_tien < 0:
        tong_tien = 0'''

content = content.replace(old_calc, new_calc)

# 2. Update POST block to use tien_giam_gia
old_post = '''        # 1. Lưu vào bảng Hóa Đơn (Khớp 100% với models.py)
        hd_moi = HoaDon(
            maHD=ma_hd,
            ngayLap=ngay_tra_thuc_te,
            tienPhong=tien_phong,
            tienDV=tien_dich_vu,
            phuThu=0,  # Mặc định 0
            giamGia=0,  # Mặc định 0
            tongTien=tong_tien,
            trangThai='Đã thanh toán',
            maDatPhong=ma_dp
        )'''

new_post = '''        # 1. Lưu vào bảng Hóa Đơn (Khớp 100% với models.py)
        hd_moi = HoaDon(
            maHD=ma_hd,
            ngayLap=ngay_tra_thuc_te,
            tienPhong=tien_phong,
            tienDV=tien_dich_vu,
            phuThu=0,  # Mặc định 0
            giamGia=tien_giam_gia,
            tongTien=tong_tien,
            trangThai='Đã thanh toán',
            maDatPhong=ma_dp
        )'''

content = content.replace(old_post, new_post)

with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed tien_giam_gia NameError in admin.py")
