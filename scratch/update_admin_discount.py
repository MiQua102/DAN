import re

with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace tien_da_coc calculation and giamGia logic
old_logic = '''    if dp.trangThai == 'Đã cọc (Online)':
        so_ngay_du_kien = (dp.ngayTraDuKien - dp.ngayNhanDuKien).days
        if so_ngay_du_kien <= 0:
            so_ngay_du_kien = 1
        tien_da_coc = (chi_tiet.donGiaPhong if chi_tiet else 0) * so_ngay_du_kien * 0.5
        
    con_lai = tong_tien - tien_da_coc
    if con_lai < 0:
        con_lai = 0

    # XỬ LÝ KHI BẤM NÚT "XÁC NHẬN THANH TOÁN" TRONG GIAO DIỆN
    if request.method == 'POST':
        try:
            ma_hd = "HD_" + str(uuid.uuid4())[:8]

            # 1. Lưu vào bảng Hóa Đơn (Khớp 100% với models.py)
            hd_moi = HoaDon(
                maHD=ma_hd,
                ngayLap=ngay_tra_thuc_te,
                tienPhong=tien_phong,
                tienDV=tien_dich_vu,
                phuThu=0,  # Mặc định 0
                giamGia=0,  # Mặc định 0
                tongTien=tong_tien,'''

new_logic = '''    tien_giam_gia = dp.tienGiamGia or 0
    tong_tien = tien_phong + tien_dich_vu - tien_giam_gia
    if tong_tien < 0:
        tong_tien = 0

    if dp.trangThai == 'Đã cọc (Online)':
        so_ngay_du_kien = (dp.ngayTraDuKien - dp.ngayNhanDuKien).days
        if so_ngay_du_kien <= 0:
            so_ngay_du_kien = 1
        tong_du_kien = (chi_tiet.donGiaPhong if chi_tiet else 0) * so_ngay_du_kien - tien_giam_gia
        if tong_du_kien < 0:
            tong_du_kien = 0
        tien_da_coc = tong_du_kien * 0.5
        
    con_lai = tong_tien - tien_da_coc
    if con_lai < 0:
        con_lai = 0

    # XỬ LÝ KHI BẤM NÚT "XÁC NHẬN THANH TOÁN" TRONG GIAO DIỆN
    if request.method == 'POST':
        try:
            ma_hd = "HD_" + str(uuid.uuid4())[:8]

            # 1. Lưu vào bảng Hóa Đơn (Khớp 100% với models.py)
            hd_moi = HoaDon(
                maHD=ma_hd,
                ngayLap=ngay_tra_thuc_te,
                tienPhong=tien_phong,
                tienDV=tien_dich_vu,
                phuThu=0,  # Mặc định 0
                giamGia=tien_giam_gia,  # Lấy từ DatPhong
                tongTien=tong_tien,'''

if "giamGia=tien_giam_gia," not in content:
    content = content.replace(old_logic, new_logic)
    with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated admin.py with discount logic")
else:
    print("Already updated.")
