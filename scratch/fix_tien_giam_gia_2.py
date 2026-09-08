import re

with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1
content = content.replace("    tong_tien = tien_phong + tien_dich_vu\n\n    # Calculate already",
"""    tien_giam_gia = getattr(dp, 'tienGiamGia', 0) or 0
    tong_tien = tien_phong + tien_dich_vu - tien_giam_gia
    if tong_tien < 0:
        tong_tien = 0

    # Calculate already""")

# Fix 2
old_post = """        hd_moi = HoaDon(
            maHD=ma_hd,
            ngayLap=ngay_tra_thuc_te,
            tienPhong=tien_phong,
            tienDV=tien_dich_vu,
            phuThu=0,  # Mặc định 0
            giamGia=0,  # Mặc định 0
            tongTien=tong_tien,
            trangThai='Đã thanh toán',
            maDatPhong=ma_dp
        )"""

new_post = """        hd_moi = HoaDon(
            maHD=ma_hd,
            ngayLap=ngay_tra_thuc_te,
            tienPhong=tien_phong,
            tienDV=tien_dich_vu,
            phuThu=0,  # Mặc định 0
            giamGia=tien_giam_gia,
            tongTien=tong_tien,
            trangThai='Đã thanh toán',
            maDatPhong=ma_dp
        )"""

content = content.replace(old_post, new_post)

with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed admin.py")
