from flask import render_template, session, redirect, url_for, flash, request
from eapp import app, db
import eapp.dao as dao
import uuid
import datetime
from eapp.models import LoaiPhong, Phong, DichVu, KhachHang, NguoiDung, DatPhong, ChiTietDatPhong, HoaDon, SuDung_DichVu, ThanhToan, KhuyenMai, NhanVien


@app.route('/quan-tri')
def quan_tri():
    # Kiểm tra quyền đăng nhập
    if 'maND' not in session:
        return redirect(url_for('dang_nhap'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    if not nhan_vien:
        flash("Bạn không có quyền truy cập trang quản trị!", "danger")
        return redirect(url_for('trang_chu'))

    # 1. Đếm số lượng phòng theo từng trạng thái
    so_phong_trong = Phong.query.filter_by(trangThai='Trống').count()
    so_phong_thue = Phong.query.filter_by(trangThai='Đang thuê').count()
    so_phong_don = Phong.query.filter_by(trangThai='Cần dọn').count()

    # 2. Tính tổng doanh thu hóa đơn trong ngày hôm nay
    hom_nay = datetime.datetime.now().date()
    tat_ca_hoa_don = HoaDon.query.all()

    doanh_thu_nay = 0
    doanh_thu_thang = [0] * 12

    for hd in tat_ca_hoa_don:
        if hd.ngayLap:
            if hd.ngayLap.date() == hom_nay:
                doanh_thu_nay += (hd.tongTien or 0)
            if hd.ngayLap.year == hom_nay.year:
                thang_idx = hd.ngayLap.month - 1
                doanh_thu_thang[thang_idx] += (hd.tongTien or 0)

    import json
    return render_template('quan_tri.html',
                           nhan_vien=nhan_vien,
                           so_phong_trong=so_phong_trong,
                           so_phong_thue=so_phong_thue,
                           so_phong_don=so_phong_don,
                           doanh_thu_nay=doanh_thu_nay,
                           doanh_thu_thang_json=json.dumps(doanh_thu_thang))


@app.route('/quan-ly-phong')
def quan_ly_phong():
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!")
        return redirect(url_for('dang_nhap'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    # Lấy danh sách loại phòng từ CSDL
    danh_sach_loai = dao.lay_danh_sach_loai_phong()

    return render_template('quan_ly_phong.html', nhan_vien=nhan_vien, danh_sach_loai=danh_sach_loai)


@app.route('/quan-ly-dat-phong')
def quan_ly_dat_phong():
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!", "danger")
        return redirect(url_for('dang_nhap'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))

    tu_khoa = request.args.get('tuKhoa')

    # Kết hợp bảng DatPhong và KhachHang để lấy được họ tên khách
    query = db.session.query(DatPhong, KhachHang).join(KhachHang, DatPhong.maKH == KhachHang.maKH)
    
    if tu_khoa:
        query = query.filter(
            (DatPhong.maDatPhong.ilike(f"%{tu_khoa}%")) |
            (KhachHang.hoTen.ilike(f"%{tu_khoa}%")) |
            (KhachHang.sdt.ilike(f"%{tu_khoa}%"))
        )

    danh_sach_dp = query.order_by(DatPhong.ngayNhanDuKien.desc()).all()

    return render_template('quan_ly_dat_phong.html', nhan_vien=nhan_vien, danh_sach_dp=danh_sach_dp, tu_khoa=tu_khoa)


@app.route('/quan-ly-dat-phong/cap-nhat/<ma_dp>', methods=['POST'])
def cap_nhat_trang_thai_dp(ma_dp):
    try:
        trang_thai_moi = request.form.get('trangThai')
        dp = db.session.get(DatPhong, ma_dp)

        if dp:
            dp.trangThai = trang_thai_moi

            # Xử lý thông minh: Nếu khách trả phòng hoặc hủy đơn, trả lại phòng trống
            if trang_thai_moi in ['Đã trả phòng', 'Đã hủy']:
                chi_tiet = ChiTietDatPhong.query.filter_by(maDatPhong=ma_dp).first()
                if chi_tiet and chi_tiet.maPhong:
                    phong = db.session.get(Phong, chi_tiet.maPhong)
                    if phong:
                        phong.trangThai = 'Trống'

            db.session.commit()
            flash(f"Đã cập nhật trạng thái đơn {ma_dp} thành: {trang_thai_moi}", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Lỗi cập nhật: {str(e)}", "danger")

    return redirect(url_for('quan_ly_dat_phong'))


@app.route('/quan-ly-phong/them', methods=['POST'])
def them_loai_phong():
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))

    ma_loai = request.form.get('maLoai')
    ten_loai = request.form.get('tenLoai')
    suc_chua = request.form.get('sucChua')
    dien_tich = request.form.get('dienTich')
    gia_co_ban = request.form.get('giaCoBan')

    try:
        # Tạo đối tượng loại phòng mới
        loai_moi = LoaiPhong(
            maLoaiPhong=ma_loai,
            tenLoaiPhong=ten_loai,
            sucChua=int(suc_chua),
            dienTich=float(dien_tich) if dien_tich else None,
            giaCoBan=float(gia_co_ban)
        )
        db.session.add(loai_moi)
        db.session.commit()
        flash("Thêm loại phòng thành công!")
    except Exception as e:
        db.session.rollback()
        flash("Có lỗi xảy ra hoặc Mã loại phòng đã tồn tại!")

    return redirect(url_for('quan_ly_phong'))


@app.route('/quan-ly-phong/xoa/<ma_loai>')
def xoa_loai_phong(ma_loai):
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))

    try:
        # Tìm loại phòng theo mã (dùng chuẩn mới của SQLAlchemy)
        loai_can_xoa = db.session.get(LoaiPhong, ma_loai)
        if loai_can_xoa:
            db.session.delete(loai_can_xoa)
            db.session.commit()
            flash("Đã xóa loại phòng thành công!")
    except Exception as e:
        db.session.rollback()
        flash("Không thể xóa! Loại phòng này có thể đang dính tới dữ liệu phòng khác.")

    return redirect(url_for('quan_ly_phong'))


@app.route('/quan-ly-phong/sua/<ma_loai>', methods=['GET', 'POST'])
def sua_loai_phong(ma_loai):
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))

    # Lấy thông tin nhân viên để hiển thị trên sidebar
    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))

    # Tìm loại phòng theo mã
    loai_can_sua = db.session.get(LoaiPhong, ma_loai)
    if not loai_can_sua:
        flash("Không tìm thấy loại phòng!")
        return redirect(url_for('quan_ly_phong'))

    if request.method == 'POST':
        try:
            loai_can_sua.tenLoaiPhong = request.form.get('tenLoai')
            loai_can_sua.sucChua = int(request.form.get('sucChua'))
            loai_can_sua.dienTich = float(request.form.get('dienTich')) if request.form.get('dienTich') else None
            loai_can_sua.giaCoBan = float(request.form.get('giaCoBan'))

            db.session.commit()
            flash("Cập nhật thông tin loại phòng thành công!")
            return redirect(url_for('quan_ly_phong'))
        except Exception as e:
            db.session.rollback()
            flash("Lưu thất bại! Vui lòng kiểm tra lại dữ liệu nhập.")

    return render_template('sua_loai_phong.html', loai=loai_can_sua, nhan_vien=nhan_vien)


@app.route('/danh-sach-phong')
def danh_sach_phong():
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!")
        return redirect(url_for('dang_nhap'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    danh_sach = dao.lay_danh_sach_phong()
    # Lấy thêm loại phòng để đổ vào thanh chọn (Dropdown) lúc thêm phòng mới
    danh_sach_loai = dao.lay_danh_sach_loai_phong()

    return render_template('danh_sach_phong.html', nhan_vien=nhan_vien, danh_sach_phong=danh_sach,
                           danh_sach_loai=danh_sach_loai)


@app.route('/danh-sach-phong/them', methods=['POST'])
def them_phong():
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))

    ma_phong = request.form.get('maPhong')
    so_phong = request.form.get('soPhong')
    tang = request.form.get('tang')
    trang_thai = request.form.get('trangThai')
    ma_loai = request.form.get('maLoaiPhong')
    ghi_chu = request.form.get('ghiChu')

    try:
        phong_moi = Phong(
            maPhong=ma_phong,
            soPhong=so_phong,
            tang=int(tang) if tang else 1,
            trangThai=trang_thai,
            ghiChu=ghi_chu,
            maLoaiPhong=ma_loai
        )
        db.session.add(phong_moi)
        db.session.commit()
        flash("Thêm phòng thực tế thành công!")
    except Exception as e:
        db.session.rollback()
        # In thẳng lỗi gốc ra Terminal và lên màn hình web để mình xem
        print("====== LỖI THÊM PHÒNG ======")
        print(str(e))
        flash(f"Lỗi hệ thống: {str(e)}")

    return redirect(url_for('danh_sach_phong'))


@app.route('/danh-sach-phong/xoa/<ma_phong>')
def xoa_phong(ma_phong):
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))

    try:
        phong_can_xoa = db.session.get(Phong, ma_phong)
        if phong_can_xoa:
            db.session.delete(phong_can_xoa)
            db.session.commit()
            flash("Đã xóa phòng thành công!")
    except Exception as e:
        db.session.rollback()
        flash(f"Lỗi: Không thể xóa phòng này! ({str(e)})")

    return redirect(url_for('danh_sach_phong'))


@app.route('/danh-sach-phong/sua/<ma_phong>', methods=['GET', 'POST'])
def sua_phong(ma_phong):
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    phong_can_sua = db.session.get(Phong, ma_phong)

    if not phong_can_sua:
        flash("Không tìm thấy phòng!")
        return redirect(url_for('danh_sach_phong'))

    if request.method == 'POST':
        try:
            phong_can_sua.soPhong = request.form.get('soPhong')
            phong_can_sua.tang = int(request.form.get('tang'))
            phong_can_sua.maLoaiPhong = request.form.get('maLoaiPhong')
            phong_can_sua.trangThai = request.form.get('trangThai')
            phong_can_sua.ghiChu = request.form.get('ghiChu')

            db.session.commit()
            flash("Cập nhật thông tin phòng thành công!")
            return redirect(url_for('danh_sach_phong'))
        except Exception as e:
            db.session.rollback()
            flash(f"Lỗi cập nhật: {str(e)}")

    # Lấy danh sách loại phòng để đổ vào dropdown select
    danh_sach_loai = dao.lay_danh_sach_loai_phong()
    return render_template('sua_phong.html', phong=phong_can_sua, danh_sach_loai=danh_sach_loai, nhan_vien=nhan_vien)


@app.route('/quan-ly-dich-vu')
def quan_ly_dich_vu():
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!")
        return redirect(url_for('dang_nhap'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    danh_sach_dv = dao.lay_danh_sach_dich_vu()

    return render_template('quan_ly_dich_vu.html', nhan_vien=nhan_vien, danh_sach_dv=danh_sach_dv)


@app.route('/quan-ly-dich-vu/them', methods=['POST'])
def them_dich_vu():
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))

    ma_dv = request.form.get('maDV')
    ten_dv = request.form.get('tenDV')
    gia = request.form.get('gia')
    don_vi = request.form.get('donVi')

    try:
        dv_moi = DichVu(
            maDV=ma_dv,
            tenDV=ten_dv,
            donGia=float(gia) if gia else 0,
            donViTinh=don_vi
        )
        db.session.add(dv_moi)
        db.session.commit()
        flash("Thêm dịch vụ thành công!")
    except Exception as e:
        db.session.rollback()
        print(f"Lỗi thêm dịch vụ: {str(e)}")
        flash(f"Lỗi hệ thống: {str(e)}")

    return redirect(url_for('quan_ly_dich_vu'))


@app.route('/quan-ly-dich-vu/xoa/<ma_dv>')
def xoa_dich_vu(ma_dv):
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))

    try:
        dv_can_xoa = db.session.get(DichVu, ma_dv)
        if dv_can_xoa:
            db.session.delete(dv_can_xoa)
            db.session.commit()
            flash("Đã xóa dịch vụ thành công!")
    except Exception as e:
        db.session.rollback()
        flash("Không thể xóa dịch vụ này vì đang được sử dụng!")

    return redirect(url_for('quan_ly_dich_vu'))


@app.route('/quan-ly-dich-vu/sua/<ma_dv>', methods=['GET', 'POST'])
def sua_dich_vu(ma_dv):
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    dv_can_sua = db.session.get(DichVu, ma_dv)

    if not dv_can_sua:
        flash("Không tìm thấy dịch vụ!")
        return redirect(url_for('quan_ly_dich_vu'))

    if request.method == 'POST':
        try:
            dv_can_sua.tenDV = request.form.get('tenDV')
            dv_can_sua.gia = float(request.form.get('gia')) if request.form.get('gia') else 0
            dv_can_sua.donViTinh = request.form.get('donVi')

            db.session.commit()
            flash("Cập nhật dịch vụ thành công!")
            return redirect(url_for('quan_ly_dich_vu'))
        except Exception as e:
            db.session.rollback()
            flash(f"Lỗi cập nhật: {str(e)}")

    return render_template('sua_dich_vu.html', dv=dv_can_sua, nhan_vien=nhan_vien)


@app.route('/quan-ly-khach-hang')
def quan_ly_khach_hang():
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!")
        return redirect(url_for('dang_nhap'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    danh_sach_kh = dao.lay_danh_sach_khach_hang()

    return render_template('quan_ly_khach_hang.html', nhan_vien=nhan_vien, danh_sach_kh=danh_sach_kh)


@app.route('/quan-ly-khach-hang/xoa/<ma_kh>')
def xoa_khach_hang(ma_kh):
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))

    try:
        kh_can_xoa = db.session.get(KhachHang, ma_kh)
        if kh_can_xoa:
            db.session.delete(kh_can_xoa)
            # Xóa luôn tài khoản người dùng tương ứng nếu muốn
            nd_can_xoa = db.session.get(NguoiDung, ma_kh)
            if nd_can_xoa:
                db.session.delete(nd_can_xoa)
            db.session.commit()
            flash("Đã xóa khách hàng thành công!")
    except Exception as e:
        db.session.rollback()
        flash(f"Không thể xóa khách hàng này: {str(e)}")

    return redirect(url_for('quan_ly_khach_hang'))


@app.route('/quan-ly-hoa-don')
def quan_ly_hoa_don():
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!", "danger")
        return redirect(url_for('dang_nhap'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    tu_khoa = request.args.get('tuKhoa')

    query = HoaDon.query
    if tu_khoa:
        query = query.filter_by(
            (HoaDon.maHD.ilike(f"%{tu_khoa}%")) |
            (HoaDon.maDatPhong.ilike(f"%{tu_khoa}%"))
        )

    danh_sach_hd = query.all()

    # Lấy danh sách các đơn đặt phòng "Đang thuê" hoặc "Đã trả phòng" để chuẩn bị thanh toán
    danh_sach_cho_thanh_toan = db.session.query(DatPhong, KhachHang) \
        .join(KhachHang, DatPhong.maKH == KhachHang.maKH) \
        .filter(DatPhong.trangThai.in_(['Đang thuê', 'Đã trả phòng'])) \
        .order_by(DatPhong.ngayNhanDuKien.desc()).all()

    return render_template('quan_ly_hoa_don.html', nhan_vien=nhan_vien, danh_sach_dp=danh_sach_cho_thanh_toan, danh_sach_hd=danh_sach_hd, tu_khoa=tu_khoa)


@app.route('/thanh-toan/<ma_dp>', methods=['GET', 'POST'])
def thanh_toan(ma_dp):
    # Kiểm tra đăng nhập
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!", "danger")
        return redirect(url_for('dang_nhap'))

    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))

    # Lấy thông tin đơn đặt phòng và khách hàng
    dp = db.session.get(DatPhong, ma_dp)
    kh = db.session.get(KhachHang, dp.maKH)

    # Lấy thông tin chi tiết và phòng
    chi_tiet = ChiTietDatPhong.query.filter_by(maDatPhong=ma_dp).first()
    phong = db.session.get(Phong, chi_tiet.maPhong) if chi_tiet and chi_tiet.maPhong else None

    # Tính số ngày ở thực tế (Từ ngày nhận đến hôm nay)
    ngay_nhan = dp.ngayNhanDuKien
    ngay_tra_thuc_te = datetime.datetime.now()
    so_ngay = (ngay_tra_thuc_te - ngay_nhan).days

    # Nếu khách ở chưa tới 24h thì vẫn tính là 1 ngày
    if so_ngay <= 0:
        so_ngay = 1

    tien_phong = so_ngay * (chi_tiet.donGiaPhong if chi_tiet else 0)


    tien_dich_vu = 0
    if chi_tiet:
        danh_sach_su_dung = SuDung_DichVu.query.filter_by(maChiTiet = chi_tiet.maChiTiet).all()
        for sd in danh_sach_su_dung:
            tien_dich_vu += (sd.thanhTien or 0)
    tien_giam_gia = getattr(dp, 'tienGiamGia', 0) or 0
    tong_tien = tien_phong + tien_dich_vu - tien_giam_gia
    if tong_tien < 0:
        tong_tien = 0
    # Calculate already paid deposit (if any)
    tien_da_coc = 0
    cac_khoan_tt = ThanhToan.query.filter_by(trangThai='Thành công').all()
    # Find payments that relate to this booking (since we don't have direct relation in DB for deposit, 
    # we can check if it's related by looking at DatPhong state or we might just query it).
    # Wait, the MoMo deposit doesn't link DatPhong directly in ThanhToan schema (ThanhToan has maHD, but deposit doesn't have HD yet).
    # But wait, earlier we created ThanhToan with maGD as orderId or transId. It doesn't have a direct link to DatPhong except via some custom field if we didn't add it.
    
    # Actually, we can check if dp.trangThai is 'Đã cọc (Online)'. If so, they paid 50% of the originally booked price.
    if dp.trangThai == 'Đã cọc (Online)':
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
            giamGia=tien_giam_gia,
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
                           chi_tiet=chi_tiet, so_ngay=so_ngay, tien_phong=tien_phong, tien_giam_gia=tien_giam_gia,
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
        yield '﻿'
        header = ['Mã HĐ', 'Ngày Lập', 'Tiền Phòng', 'Tiền Dịch Vụ', 'Phụ Thu', 'Tổng Tiền', 'Mã Đặt Phòng', 'Nhân Viên Lập']
        yield ','.join(header) + '\n'
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
            yield ','.join(safe_row) + '\n'

    return Response(generate(), mimetype='text/csv', headers={"Content-Disposition": "attachment; filename=danh_sach_hoa_don.csv"})

from werkzeug.security import generate_password_hash

@app.route('/quan-ly-nhan-su')
def quan_ly_nhan_su():
    if 'maND' not in session:
        return redirect(url_for('dang_nhap'))
    
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Chỉ Admin mới có quyền truy cập trang quản lý nhân sự!", "danger")
        return redirect(url_for('quan_tri'))
        
    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    danh_sach_nhan_vien = dao.lay_danh_sach_nhan_vien()
    
    return render_template('quan_ly_nhan_su.html', nhan_vien=nhan_vien, danh_sach_nhan_vien=danh_sach_nhan_vien)

@app.route('/quan-ly-nhan-su/them', methods=['POST'])
def them_nhan_su():
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền thực hiện chức năng này!", "danger")
        return redirect(url_for('quan_tri'))
        
    tenDangNhap = request.form.get('tenDangNhap')
    matKhau = request.form.get('matKhau')
    email = request.form.get('email')
    hoTen = request.form.get('hoTen')
    chucVu = request.form.get('chucVu')
    maVaiTro = request.form.get('maVaiTro', 'STAFF')
    
    try:
        # Check if username exists
        if NguoiDung.query.filter_by(tenDangNhap=tenDangNhap).first():
            flash("Tên đăng nhập đã tồn tại!", "danger")
            return redirect(url_for('quan_ly_nhan_su'))
            
        ma_nd = "NV" + str(uuid.uuid4())[:6]
        mk_hash = generate_password_hash(matKhau)
        
        nd_moi = NguoiDung(
            maND=ma_nd,
            tenDangNhap=tenDangNhap,
            email=email,
            matKhau=mk_hash,
            maVaiTro=maVaiTro
        )
        
        nv_moi = NhanVien(
            maNV=ma_nd,
            hoTen=hoTen,
            chucVu=chucVu
        )
        
        db.session.add(nd_moi)
        db.session.add(nv_moi)
        db.session.commit()
        
        flash("Tạo tài khoản nhân viên thành công!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Lỗi: {str(e)}", "danger")
        
    return redirect(url_for('quan_ly_nhan_su'))

@app.route('/quan-ly-nhan-su/xoa/<ma_nv>')
def xoa_nhan_su(ma_nv):
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền thực hiện chức năng này!", "danger")
        return redirect(url_for('quan_tri'))
        
    try:
        nv_can_xoa = db.session.get(NhanVien, ma_nv)
        nd_can_xoa = db.session.get(NguoiDung, ma_nv)
        
        if nd_can_xoa and nd_can_xoa.tenDangNhap == 'admin':
            flash("Không thể xóa tài khoản admin gốc!", "danger")
            return redirect(url_for('quan_ly_nhan_su'))
            
        if nv_can_xoa:
            db.session.delete(nv_can_xoa)
        if nd_can_xoa:
            db.session.delete(nd_can_xoa)
            
        db.session.commit()
        flash("Xóa nhân viên thành công!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Lỗi không thể xóa: {str(e)}", "danger")
        
    return redirect(url_for('quan_ly_nhan_su'))

@app.route('/quan-ly-khuyen-mai')
def quan_ly_khuyen_mai():
    if 'maND' not in session:
        return redirect(url_for('dang_nhap'))
        
    nhan_vien = dao.kiem_tra_nhan_vien(session.get('maND'))
    danh_sach_km = KhuyenMai.query.all()
    
    return render_template('quan_ly_khuyen_mai.html', nhan_vien=nhan_vien, danh_sach_km=danh_sach_km)

@app.route('/quan-ly-khuyen-mai/them', methods=['POST'])
def them_khuyen_mai():
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền thực hiện chức năng này!", "danger")
        return redirect(url_for('quan_ly_khuyen_mai'))
        
    ma_km = request.form.get('maKM').strip().upper()
    phan_tram = float(request.form.get('phanTramGiam'))
    so_luong = int(request.form.get('soLuong'))
    
    try:
        km_moi = KhuyenMai(
            maKM=ma_km,
            phanTramGiam=phan_tram,
            soLuong=so_luong,
            trangThai=True
        )
        db.session.add(km_moi)
        db.session.commit()
        flash("Thêm mã khuyến mãi thành công!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Lỗi thêm mã (Có thể mã đã tồn tại): {str(e)}", "danger")
        
    return redirect(url_for('quan_ly_khuyen_mai'))

@app.route('/quan-ly-khuyen-mai/doi-trang-thai/<ma_km>')
def doi_trang_thai_km(ma_km):
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền!", "danger")
        return redirect(url_for('quan_ly_khuyen_mai'))
        
    km = db.session.get(KhuyenMai, ma_km)
    if km:
        km.trangThai = not km.trangThai
        db.session.commit()
        flash("Đã đổi trạng thái mã khuyến mãi!", "success")
    return redirect(url_for('quan_ly_khuyen_mai'))

@app.route('/quan-ly-khuyen-mai/xoa/<ma_km>')
def xoa_khuyen_mai(ma_km):
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền!", "danger")
        return redirect(url_for('quan_ly_khuyen_mai'))
        
    km = db.session.get(KhuyenMai, ma_km)
    if km:
        db.session.delete(km)
        db.session.commit()
        flash("Xóa mã thành công!", "success")
    return redirect(url_for('quan_ly_khuyen_mai'))
