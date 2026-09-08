import re

with open('d:/DAN/eapp/index.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_logic = '''        so_luong_khach = int(request.form.get('soLuongKhach', 1))

        ma_dp = "DP_" + str(uuid.uuid4())[:8]'''

new_logic = '''        so_luong_khach = int(request.form.get('soLuongKhach', 1))
        voucher_code = request.form.get('voucherCode', '').strip().upper()

        ma_dp = "DP_" + str(uuid.uuid4())[:8]'''

if "voucher_code =" not in content:
    content = content.replace(old_logic, new_logic)

old_logic_dp = '''        # 5. Tạo Đơn Đặt Phòng (Dùng trực tiếp mã khách đang đăng nhập)
        dat_phong_moi = DatPhong(
            maDatPhong=ma_dp,
            ngayNhanDuKien=datetime.strptime(ngay_nhan, '%Y-%m-%d'),
            ngayTraDuKien=datetime.strptime(ngay_tra, '%Y-%m-%d'),
            soLuongKhach=so_luong_khach,
            trangThai='Chờ nhận phòng',
            maKH=ma_nd,
            maNV=None  # Khách tự đặt nên nhân viên trống
        )'''

new_logic_dp = '''        # Validate Voucher
        tien_giam_gia = 0
        if voucher_code:
            km = db.session.get(KhuyenMai, voucher_code)
            if km and km.trangThai and km.soLuong > 0:
                # Calculate total expected cost to find discount amount
                so_ngay = (check_out_date - check_in_date).days
                if so_ngay <= 0: so_ngay = 1
                tong_tam = loai_phong.giaCoBan * so_ngay
                tien_giam_gia = tong_tam * (km.phanTramGiam / 100)
                
                # Decrease voucher count
                km.soLuong -= 1
                
        # 5. Tạo Đơn Đặt Phòng (Dùng trực tiếp mã khách đang đăng nhập)
        dat_phong_moi = DatPhong(
            maDatPhong=ma_dp,
            ngayNhanDuKien=check_in_date,
            ngayTraDuKien=check_out_date,
            soLuongKhach=so_luong_khach,
            trangThai='Chờ nhận phòng',
            maKH=ma_nd,
            maNV=None,  # Khách tự đặt nên nhân viên trống
            tienGiamGia=tien_giam_gia
        )'''

if "tien_giam_gia =" not in content:
    content = content.replace(old_logic_dp, new_logic_dp)
    
with open('d:/DAN/eapp/index.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.py logic")
