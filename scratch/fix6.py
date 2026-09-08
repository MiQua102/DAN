with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = lines[:464]

rest_logic = '''
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
                tongTien=tong_tien,
                trangThai='Đã thanh toán',
                maDatPhong=ma_dp
            )
            db.session.add(hd_moi)

            # 2. Tạo bản ghi Thanh Toán
            phuong_thuc = request.form.get('phuongThuc', 'Tiền mặt')
            ma_tt = "TT_" + str(uuid.uuid4())[:8]
            thanh_toan = ThanhToan(
                maTT=ma_tt,
                soTien=tong_tien,
                hinhThuc=phuong_thuc,
                maGD=ma_hd,  # Trực tiếp tại quầy dùng mã HĐ làm mã GD
                trangThai='Thành công',
                maHD=ma_hd
            )
            db.session.add(thanh_toan)

            # 3. Đổi trạng thái Đơn Đặt Phòng
            dp.trangThai = 'Đã trả phòng'

            # 4. Trả phòng trống về trạng thái "Cần dọn"
            if phong:
                phong.trangThai = 'Cần dọn'

            db.session.commit()
            flash(f"Thanh toán thành công! Mã HĐ: {ma_hd}", "success")
            return redirect(url_for('xem_hoa_don', ma_hd=ma_hd))

        except Exception as e:
            db.session.rollback()
            flash(f"Lỗi khi lập hóa đơn: {str(e)}", "danger")

    # Nếu là GET thì hiển thị giao diện Bill
    return render_template('thanh_toan.html', nhan_vien=nhan_vien, dp=dp, kh=kh, phong=phong,
                           chi_tiet=chi_tiet, so_ngay=so_ngay, tien_phong=tien_phong,
                           tong_tien=tong_tien, ngay_tra_thuc_te=ngay_tra_thuc_te,
                           tien_da_coc=tien_da_coc, con_lai=con_lai)


@app.route('/xem-hoa-don/<ma_hd>')
def xem_hoa_don(ma_hd):
    if 'maND' not in session:
        return redirect(url_for('dang_nhap'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))

    # Lấy thông tin từ database
    hd = db.session.get(HoaDon, ma_hd)
    if not hd:
        flash("Không tìm thấy hóa đơn!", "danger")
        return redirect(url_for('quan_ly_hoa_don'))

    dp = db.session.get(DatPhong, hd.maDatPhong)
    kh = db.session.get(KhachHang, dp.maKH)
    chi_tiet = ChiTietDatPhong.query.filter_by(maDatPhong=dp.maDatPhong).first()
    phong = db.session.get(Phong, chi_tiet.maPhong) if chi_tiet else None

    # Tính lại số ngày để hiển thị
    so_ngay = (hd.ngayLap - dp.ngayNhanDuKien).days
    if so_ngay <= 0:
        so_ngay = 1

    return render_template('xem_hoa_don.html', nhan_vien=nhan_vien, hd=hd, dp=dp,
                           kh=kh, phong=phong, chi_tiet=chi_tiet, so_ngay=so_ngay)


import csv
from flask import Response

@app.route('/xuat-hoa-don-csv')
def xuat_hoa_don_csv():
    if 'maND' not in session:
        return redirect(url_for('dang_nhap'))
        
    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    if not nhan_vien:
        return redirect(url_for('dang_nhap'))

    tat_ca_hoa_don = HoaDon.query.order_by(HoaDon.ngayLap.desc()).all()

    def generate():
        # Header (Use BOM for Excel UTF-8)
        yield '\ufeff'
        header = ['Mã HĐ', 'Ngày Lập', 'Tiền Phòng', 'Tiền Dịch Vụ', 'Phụ Thu', 'Tổng Tiền', 'Mã Đặt Phòng', 'Nhân Viên Lập']
        yield ','.join(header) + '\\n'
        for hd in tat_ca_hoa_don:
            row = [
                hd.maHD,
                hd.ngayLap.strftime('%Y-%m-%d %H:%M:%S') if hd.ngayLap else '',
                str(hd.tienPhong),
                str(hd.tienDV),
                str(hd.phuThu),
                str(hd.tongTien),
                hd.maDatPhong,
                hd.maNV
            ]
            safe_row = [f'"{str(item)}"' if ',' in str(item) else str(item) for item in row]
            yield ','.join(safe_row) + '\\n'

    return Response(generate(), mimetype='text/csv', headers={"Content-Disposition": "attachment; filename=danh_sach_hoa_don.csv"})
'''

with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
    f.write(rest_logic)
print('Fixed completely!')
