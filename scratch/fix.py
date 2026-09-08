with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('    # XỬ LÝ KHI BẤM NÚT "XÁC NHẬN THANH TOÁN" TRONG GIAO DIỆN')
idx2 = content.find('def xem_hoa_don(ma_hd):')

print(f'idx1: {idx1}, idx2: {idx2}')

if idx1 != -1 and idx2 != -1:
    new_logic = '''    # XỬ LÝ KHI BẤM NÚT "XÁC NHẬN THANH TOÁN" TRONG GIAO DIỆN
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
'''
    new_content = content[:idx1] + new_logic + content[idx2:]
    with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Replaced')
