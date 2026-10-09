from flask import jsonify, render_template, request, redirect, url_for, session, flash
from eapp import app, db
import eapp.dao as dao
from eapp.models import KhuyenMai, DatPhong, ChiTietDatPhong, KhachHang, NguoiDung, LoaiPhong, Phong, HoaDon, DichVu, SuDung_DichVu, ThanhToan, Review, TienNghi, LoaiPhongTienNghi
from datetime import datetime
from werkzeug.security import generate_password_hash
import uuid
from eapp.translations import get_text

@app.context_processor
def inject_globals():
    lang = session.get('lang', 'vi')
    
    is_admin = False
    if 'maND' in session:
        is_admin = dao.kiem_tra_quyen_admin(session.get('maND'))
    
    def _(key):
        return get_text(lang, key)
        
    def format_currency(amount):
        if amount is None:
            return ""
        if lang == 'en':
            # convert VND to USD (approx 25000)
            usd = amount / 25000
            return f"${usd:,.2f}"
        else:
            return f"{amount:,.0f} ₫"
            
    return dict(_=_, format_currency=format_currency, current_lang=lang, is_admin=is_admin)


@app.route('/dich-vu')
def dich_vu():
    from eapp.models import DichVu
    danh_sach_dv = DichVu.query.filter_by(trangThai=True).all()
    return render_template('dich_vu.html', danh_sach_dv=danh_sach_dv)


@app.route('/set-lang/<lang>')
def set_lang(lang):
    if lang in ['vi', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('trang_chu'))

@app.route('/')
def trang_chu():
    # Lấy các tham số lọc từ request.args (GET method)
    tu_khoa = request.args.get('tuKhoa', '')
    suc_chua = request.args.get('sucChua', '')
    gia_max = request.args.get('giaMax', '')
    ngay_nhan = request.args.get('ngayNhan', '')
    ngay_tra = request.args.get('ngayTra', '')

    # Truy vấn cơ bản
    query = LoaiPhong.query

    if tu_khoa:
        query = query.filter(LoaiPhong.tenLoaiPhong.ilike(f"%{tu_khoa}%"))
    if suc_chua:
        query = query.filter(LoaiPhong.sucChua >= int(suc_chua))
    if gia_max:
        query = query.filter(LoaiPhong.giaCoBan <= float(gia_max))

    # Xử lý lọc theo ngày nhận và ngày trả
    if ngay_nhan and ngay_tra:
        try:
            check_in_date = datetime.strptime(ngay_nhan, '%Y-%m-%d')
            check_out_date = datetime.strptime(ngay_tra, '%Y-%m-%d')

            if check_in_date < check_out_date:
                # Tìm các mã phòng (maPhong) ĐÃ BỊ ĐẶT trong khoảng thời gian này
                overlapping_bookings = db.session.query(ChiTietDatPhong.maPhong)\
                    .join(DatPhong, ChiTietDatPhong.maDatPhong == DatPhong.maDatPhong)\
                    .filter(
                        DatPhong.trangThai != 'Đã hủy',
                        DatPhong.ngayNhanDuKien < check_out_date,
                        DatPhong.ngayTraDuKien > check_in_date
                    ).subquery()

                # Lọc ra các loại phòng CÓ ÍT NHẤT 1 PHÒNG KHÔNG NẰM TRONG danh sách ĐÃ BỊ ĐẶT
                query = query.filter(LoaiPhong.phongs.any(~Phong.maPhong.in_(overlapping_bookings)))
            else:
                flash("Ngày trả phòng phải lớn hơn ngày nhận phòng!", "warning")
        except ValueError:
            pass # Bỏ qua nếu định dạng ngày không hợp lệ

    danh_sach_loai = query.all()
    # Calculate average rating per room type
    avg_ratings = {}
    for loai in danh_sach_loai:
        avg = db.session.query(db.func.avg(Review.rating))\
            .join(DatPhong, Review.maDatPhong == DatPhong.maDatPhong)\
            .join(ChiTietDatPhong, ChiTietDatPhong.maDatPhong == DatPhong.maDatPhong)\
            .join(Phong, ChiTietDatPhong.maPhong == Phong.maPhong)\
            .filter(Phong.maLoaiPhong == loai.maLoaiPhong)\
            .scalar()
        avg_ratings[loai.maLoaiPhong] = avg

    # Load amenities per room type from DB
    tien_nghi_map = {}
    for loai in danh_sach_loai:
        items = db.session.query(TienNghi)\
            .join(LoaiPhongTienNghi, TienNghi.maTienNghi == LoaiPhongTienNghi.maTienNghi)\
            .filter(LoaiPhongTienNghi.maLoaiPhong == loai.maLoaiPhong)\
            .all()
        tien_nghi_map[loai.maLoaiPhong] = items

    # Load top recent positive reviews
    top_reviews = Review.query.filter(Review.rating >= 4).order_by(Review.ngay.desc()).limit(3).all()

    return render_template('trang_chu.html',
                           danh_sach_loai=danh_sach_loai,
                           avg_ratings=avg_ratings,
                           tien_nghi_map=tien_nghi_map,
                           tu_khoa=tu_khoa,
                           suc_chua=suc_chua,
                           gia_max=gia_max,
                           ngay_nhan=ngay_nhan,
                           ngay_tra=ngay_tra,
                           top_reviews=top_reviews)


@app.route('/chi-tiet-phong/<ma_loai>')
def chi_tiet_phong(ma_loai):
    loai = db.session.get(LoaiPhong, ma_loai)
    if not loai:
        flash("Không tìm thấy loại phòng!", "danger")
        return redirect(url_for('trang_chu'))

    # Amenities
    tien_nghis = db.session.query(TienNghi)\
        .join(LoaiPhongTienNghi, TienNghi.maTienNghi == LoaiPhongTienNghi.maTienNghi)\
        .filter(LoaiPhongTienNghi.maLoaiPhong == ma_loai)\
        .all()

    # Available rooms count
    so_phong_trong = Phong.query.filter_by(maLoaiPhong=ma_loai, trangThai='Trong').count()
    tong_phong = Phong.query.filter_by(maLoaiPhong=ma_loai).count()

    # Average rating
    avg_rating = db.session.query(db.func.avg(Review.rating))\
        .join(DatPhong, Review.maDatPhong == DatPhong.maDatPhong)\
        .join(ChiTietDatPhong, ChiTietDatPhong.maDatPhong == DatPhong.maDatPhong)\
        .join(Phong, ChiTietDatPhong.maPhong == Phong.maPhong)\
        .filter(Phong.maLoaiPhong == ma_loai)\
        .scalar()

    review_count = db.session.query(db.func.count(Review.maReview))\
        .join(DatPhong, Review.maDatPhong == DatPhong.maDatPhong)\
        .join(ChiTietDatPhong, ChiTietDatPhong.maDatPhong == DatPhong.maDatPhong)\
        .join(Phong, ChiTietDatPhong.maPhong == Phong.maPhong)\
        .filter(Phong.maLoaiPhong == ma_loai)\
        .scalar() or 0

    # Latest reviews (top 5)
    reviews = db.session.query(Review)\
        .join(DatPhong, Review.maDatPhong == DatPhong.maDatPhong)\
        .join(ChiTietDatPhong, ChiTietDatPhong.maDatPhong == DatPhong.maDatPhong)\
        .join(Phong, ChiTietDatPhong.maPhong == Phong.maPhong)\
        .filter(Phong.maLoaiPhong == ma_loai)\
        .order_by(Review.ngay.desc())\
        .limit(5)\
        .all()

    return render_template('chi_tiet_phong.html',
                           loai=loai,
                           tien_nghis=tien_nghis,
                           so_phong_trong=so_phong_trong,
                           tong_phong=tong_phong,
                           avg_rating=avg_rating,
                           review_count=review_count,
                           reviews=reviews)

@app.route('/dang-nhap', methods=['GET', 'POST'])
def dang_nhap():
    if request.method == 'POST':
        ten_dang_nhap = request.form.get('tenDangNhap')
        mat_khau = request.form.get('matKhau')

        user = dao.xac_thuc_nguoi_dung(ten_dang_nhap, mat_khau)
        if user:
            session['maND'] = user.maND
            session['tenDangNhap'] = user.tenDangNhap

            # Kiểm tra xem có phải nhân viên không để đẩy vào trang admin
            if dao.kiem_tra_nhan_vien(user.maND):
                session['is_admin'] = True  # Đánh dấu đây là Admin/Nhân viên
                return redirect(url_for('quan_tri'))

            session['is_admin'] = False  # Đánh dấu đây là Khách hàng thường
            return redirect(url_for('trang_chu'))
        else:
            flash("Tên đăng nhập hoặc mật khẩu không đúng!", "danger")
    try:
        return render_template('dang_nhap.html')
    except:
        return "Giao diện Đăng nhập đang được xây dựng..."

@app.route('/dang-ky', methods=['GET', 'POST'])
def dang_ky():
    if request.method == 'POST':
        ten_dang_nhap = request.form.get('tenDangNhap')
        email = request.form.get('email')
        mat_khau = request.form.get('matKhau')
        ho_ten = request.form.get('hoTen')
        sdt = request.form.get('sdt')
        cccd = request.form.get('cccd')

        try:
            ma_nd = "ND_" + str(uuid.uuid4())[:8]

            mat_khau_bam = generate_password_hash(mat_khau)

            # 1. Tạo tài khoản người dùng
            nd_moi = NguoiDung(
                maND=ma_nd,
                tenDangNhap=ten_dang_nhap,
                email=email,
                matKhau=mat_khau_bam,
                maVaiTro=None  # Đặt bằng None để tránh lỗi khóa ngoại bảng vaitro
            )
            db.session.add(nd_moi)
            db.session.flush()

            # 2. Tạo thông tin khách hàng liên kết 1-1 với người dùng
            kh_moi = KhachHang(
                maKH=ma_nd,
                hoTen=ho_ten,
                sdt=sdt,
                cccd=cccd
            )
            db.session.add(kh_moi)
            db.session.commit()

            flash("Đăng ký tài khoản thành công! Vui lòng đăng nhập.", "success")
            return redirect(url_for('dang_nhap'))  # Hoặc chuyển hướng đến trang đăng nhập của ní
        except Exception as e:
            db.session.rollback()
            flash(f"Lỗi đăng ký: {str(e)}")

    return render_template('dang_ky.html')


@app.route('/dang-xuat')
def dang_xuat():
    session.clear()
    return redirect(url_for('trang_chu'))


@app.route('/dat-phong/<ma_loai_phong>', methods=['GET', 'POST'])
def dat_phong_client(ma_loai_phong):
    # 1. BẮT BUỘC PHẢI ĐĂNG NHẬP MỚI ĐƯỢC ĐẶT PHÒNG
    if 'maND' not in session:
        flash("Vui lòng đăng nhập để tiến hành đặt phòng!", "warning")
        return redirect(url_for('dang_nhap'))

    loai_phong = db.session.get(LoaiPhong, ma_loai_phong)
    if not loai_phong:
        flash("Không tìm thấy loại phòng!", "danger")
        return redirect(url_for('trang_chu'))

    # Lấy thông tin khách hàng đang đăng nhập từ session
    ma_nd = session.get('maND')
    khach_hang = db.session.get(KhachHang, ma_nd)
    danh_sach_tat_ca_loai = LoaiPhong.query.all()

    if request.method == 'POST':
        try:
            ngay_nhan = request.form.get('ngayNhan')
            ngay_tra = request.form.get('ngayTra')
            so_luong_khach = int(request.form.get('soLuongKhach', 1))

            ma_dp = "DP_" + str(uuid.uuid4())[:8]
            ma_ct = "CT_" + str(uuid.uuid4())[:8]

            check_in_date = datetime.strptime(ngay_nhan, '%Y-%m-%d')
            check_out_date = datetime.strptime(ngay_tra, '%Y-%m-%d')

            if check_in_date >= check_out_date:
                flash("Ngày trả phòng phải lớn hơn ngày nhận phòng!", "danger")
                return redirect(request.url)

            # 4. Tìm một phòng thuộc loại này mà không bị trùng lịch đặt
            overlapping_bookings = db.session.query(ChiTietDatPhong.maPhong)\
                .join(DatPhong, ChiTietDatPhong.maDatPhong == DatPhong.maDatPhong)\
                .filter(
                    DatPhong.trangThai != 'Đã hủy',
                    DatPhong.ngayNhanDuKien < check_out_date,
                    DatPhong.ngayTraDuKien > check_in_date
                ).subquery()

            phong_trong = Phong.query.filter(
                Phong.maLoaiPhong == ma_loai_phong,
                ~Phong.maPhong.in_(overlapping_bookings)
            ).first()

            if not phong_trong:
                flash("Xin lỗi, loại phòng này đã hết phòng trống trong khoảng thời gian bạn chọn!", "danger")
                return redirect(request.url)

            ma_phong_chon = phong_trong.maPhong

            # 5. Tạo Đơn Đặt Phòng (Dùng trực tiếp mã khách đang đăng nhập)
            dat_phong_moi = DatPhong(
                maDatPhong=ma_dp,
                ngayNhanDuKien=datetime.strptime(ngay_nhan, '%Y-%m-%d'),
                ngayTraDuKien=datetime.strptime(ngay_tra, '%Y-%m-%d'),
                soLuongKhach=so_luong_khach,
                trangThai='Chờ nhận phòng',
                maKH=ma_nd,
                maNV=None  # Khách tự đặt nên nhân viên trống
            )
            db.session.add(dat_phong_moi)

            # 6. Tạo Chi Tiết Đặt Phòng
            chi_tiet = ChiTietDatPhong(
                maChiTiet=ma_ct,
                soNguoi=so_luong_khach,
                donGiaPhong=loai_phong.giaCoBan,
                maDatPhong=ma_dp,
                maPhong=ma_phong_chon
            )
            db.session.add(chi_tiet)

            # Nếu tìm thấy phòng trống thì đổi trạng thái phòng thành 'Đang thuê' (hoặc 'Đã đặt' tùy logic của ní)
            if phong_trong:
                phong_trong.trangThai = 'Đang thuê'

            db.session.commit()

            # SEND AUTO EMAIL WITH QR CODE
            try:
                from eapp.email_service import send_booking_email
                email_to = request.form.get('email', session.get('tenDangNhap'))
                ho_ten = request.form.get('hoTen', 'Khách hàng')
                so_ngay = (check_out_date - check_in_date).days
                if so_ngay == 0:
                    so_ngay = 1
                tong_tien = so_ngay * loai_phong.giaCoBan
                send_booking_email(
                    email_to=email_to, 
                    ho_ten=ho_ten, 
                    ma_dp=ma_dp, 
                    checkin=check_in_date, 
                    checkout=check_out_date, 
                    so_ngay=so_ngay, 
                    phong=phong_trong.soPhong, 
                    tong_tien=tong_tien
                )
            except Exception as email_e:
                print(f"Lỗi gửi email: {email_e}")

            flash("Đặt phòng thành công! Email xác nhận chứa Mã QR đã được gửi. Xin cảm ơn quý khách", "success")
            return redirect(url_for('lich_su_dat_phong'))

        except Exception as e:
            db.session.rollback()
            print(f"Lỗi đặt phòng: {str(e)}")
            flash(f"Có lỗi xảy ra khi đặt phòng: {str(e)}", "danger")

    ngay_nhan_get = request.args.get('ngayNhan', '')
    ngay_tra_get = request.args.get('ngayTra', '')
    return render_template('form_dat_phong.html', loai_phong=loai_phong, khach_hang=khach_hang, danh_sach_tat_ca_loai=danh_sach_tat_ca_loai, ngay_nhan=ngay_nhan_get, ngay_tra=ngay_tra_get)

@app.route('/lich-su-dat-phong')
def lich_su_dat_phong():
    # Bắt buộc phải đăng nhập mới được xem
    if 'maND' not in session:
        flash("Ní cần đăng nhập để xem lịch sử đặt phòng nhé!", "warning")
        return redirect(url_for('dang_nhap'))

    ma_kh = session.get('maND')

    # Lấy toàn bộ đơn đặt phòng của khách này, sắp xếp đơn mới nhất lên đầu
    danh_sach_don = DatPhong.query.filter_by(maKH=ma_kh).order_by(DatPhong.ngayNhanDuKien.desc()).all()

    return render_template('lich_su_dat_phong.html', danh_sach_don=danh_sach_don, now=datetime.now())

@app.route('/chi-tiet-hoa-don/<ma_dp>')
def chi_tiet_hoa_don_khach(ma_dp):
    if 'maND' not in session:
        flash("Vui lòng đăng nhập để xem hóa đơn!", "warning")
        return redirect(url_for('dang_nhap'))

    ma_kh = session.get('maND')
    dp = db.session.get(DatPhong, ma_dp)

    # Bảo mật: Kiểm tra xem đơn đặt phòng này có đúng là của khách đang đăng nhập không
    if not dp or dp.maKH != ma_kh:
        flash("Ní không có quyền xem hóa đơn này nha!", "danger")
        return redirect(url_for('lich_su_dat_phong'))

    # Lấy Hóa Đơn dựa vào mã đặt phòng
    hd = HoaDon.query.filter_by(maDatPhong=ma_dp).first()
    if not hd:
        flash("Đơn này chưa được lập hóa đơn!", "info")
        return redirect(url_for('lich_su_dat_phong'))

    # Truy xuất các thông tin liên quan để in ra Bill
    kh = db.session.get(KhachHang, ma_kh)
    chi_tiet = ChiTietDatPhong.query.filter_by(maDatPhong=ma_dp).first()
    phong = db.session.get(Phong, chi_tiet.maPhong) if chi_tiet and chi_tiet.maPhong else None

    so_ngay = (hd.ngayLap - dp.ngayNhanDuKien).days
    if so_ngay <= 0:
        so_ngay = 1

    return render_template('hoa_don_khach.html', hd=hd, dp=dp, kh=kh, phong=phong, chi_tiet=chi_tiet, so_ngay=so_ngay)


@app.route('/goi-dich-vu/<ma_dp>', methods=['GET', 'POST'])
def goi_dich_vu_khach(ma_dp):
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!", "warning")
        return redirect(url_for('dang_nhap'))

    dp = db.session.get(DatPhong, ma_dp)
    if not dp or dp.maKH != session.get('maND'):
        flash("Không có quyền truy cập!", "danger")
        return redirect(url_for('lich_su_dat_phong'))

    chi_tiet = ChiTietDatPhong.query.filter_by(maDatPhong=ma_dp).first()
    if not chi_tiet:
        flash("Đơn đặt phòng chưa có phòng nhận!", "warning")
        return redirect(url_for('lich_su_dat_phong'))

    # Lấy danh sách dịch vụ đang kinh doanh
    danh_sach_dv = DichVu.query.filter_by(trangThai=True).all()

    if request.method == 'POST':
        try:
            ma_dv = request.form.get('maDV')
            so_luong = int(request.form.get('soLuong', 1))

            dv = db.session.get(DichVu, ma_dv)
            thanh_tien = so_luong * dv.donGia
            ma_sd = "SD_" + str(uuid.uuid4())[:8]

            su_dung_moi = SuDung_DichVu(
                maSD=ma_sd,
                soLuong=so_luong,
                donGia=dv.donGia,
                thanhTien=thanh_tien,
                maChiTiet=chi_tiet.maChiTiet,
                maDV=ma_dv,
                maNV=None  # Khách tự gọi nên nhân viên bằng None hoặc để trống
            )
            db.session.add(su_dung_moi)
            db.session.commit()

            flash(f"Đã gọi thành công {so_luong} {dv.donViTinh} {dv.tenDV}!", "success")
            return redirect(url_for('goi_dich_vu_khach', ma_dp=ma_dp))
        except Exception as e:
            db.session.rollback()
            flash(f"Lỗi gọi dịch vụ: {str(e)}", "danger")

    # Lấy lịch sử dịch vụ khách đã gọi cho đơn này
    da_dung = SuDung_DichVu.query.filter_by(maChiTiet=chi_tiet.maChiTiet).all()

    return render_template('goi_dich_vu_khach.html', dp=dp, danh_sach_dv=danh_sach_dv, da_dung=da_dung)

@app.route('/thanh-toan-online/<ma_dp>', methods=['GET', 'POST'])
def thanh_toan_online(ma_dp):
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!", "warning")
        return redirect(url_for('dang_nhap'))
        
    dp = db.session.get(DatPhong, ma_dp)
    if not dp or dp.maKH != session.get('maND'):
        flash("Không tìm thấy đơn đặt phòng!", "danger")
        return redirect(url_for('lich_su_dat_phong'))
        
    chi_tiet = ChiTietDatPhong.query.filter_by(maDatPhong=ma_dp).first()
    phong = db.session.get(Phong, chi_tiet.maPhong) if chi_tiet and chi_tiet.maPhong else None
    
    # Calculate 50% deposit based on total stay
    so_ngay = (dp.ngayTraDuKien - dp.ngayNhanDuKien).days
    if so_ngay <= 0:
        so_ngay = 1
    tong_tien = (chi_tiet.donGiaPhong if chi_tiet else 0) * so_ngay
    # Apply discount to total if any
    tien_giam_gia = dp.tienGiamGia or 0
    tong_tien_sau_giam = tong_tien - tien_giam_gia
    if tong_tien_sau_giam < 0: 
        tong_tien_sau_giam = 0
    tien_coc = tong_tien_sau_giam * 0.5

    if request.method == 'POST':
        phuong_thuc = request.form.get('phuongThuc', 'MoMo')

        if phuong_thuc == 'MoMo':
            # Integrate MoMo
            from eapp.momo_api import create_momo_payment
            order_info = f"Thanh toan coc dat phong {ma_dp}"
            # Use request.url_root to get the base url dynamically
            base_url = request.url_root.rstrip('/')
            return_url = f"{base_url}/momo-return"
            notify_url = f"{base_url}/momo-ipn"
            
            momo_res = create_momo_payment(ma_dp, tien_coc, order_info, return_url, notify_url)
            
            if momo_res and 'payUrl' in momo_res:
                return redirect(momo_res['payUrl'])
            else:
                flash("Có lỗi khi tạo giao dịch MoMo. Vui lòng thử lại.", "danger")
                return redirect(url_for('lich_su_dat_phong'))

        else:
            # Fake other methods (like VNPay)
            dp.trangThai = 'Đã cọc (Online)'
            
            ma_tt = "TT_" + str(uuid.uuid4())[:8]
            thanh_toan = ThanhToan(
                maTT=ma_tt,
                soTien=tien_coc,
                hinhThuc=phuong_thuc,
                maGD="VN_" + str(uuid.uuid4())[:8],
                trangThai='Thành công'
            )
            db.session.add(thanh_toan)
            db.session.commit()
            
            flash("Thanh toán trực tuyến thành công! Cảm ơn quý khách.", "success")
            return redirect(url_for('lich_su_dat_phong'))
        
    return render_template('thanh_toan_online.html', dp=dp, chi_tiet=chi_tiet, tien_coc=tien_coc, tong_tien=tong_tien, so_ngay=so_ngay)

@app.route('/momo-return')
def momo_return():
    # Verify transaction signature here in real app
    # For now, if MoMo returns resultCode=0, it's success
    resultCode = request.args.get('resultCode')
    orderId = request.args.get('orderId')
    amount = request.args.get('amount')
    transId = request.args.get('transId')

    if resultCode == '0':
        dp = db.session.get(DatPhong, orderId)
        if dp:
            dp.trangThai = 'Đã cọc (Online)'
            
            ma_tt = "TT_" + str(uuid.uuid4())[:8]
            thanh_toan = ThanhToan(
                maTT=ma_tt,
                soTien=float(amount) if amount else 0,
                hinhThuc='MoMo',
                maGD=transId,
                trangThai='Thành công'
            )
            db.session.add(thanh_toan)
            db.session.commit()
            
            flash(f"Thanh toán MoMo thành công! Đơn đặt phòng {orderId} đã được cọc.", "success")
        else:
            flash("Thanh toán thành công nhưng không tìm thấy đơn phòng.", "warning")
    else:
        flash("Thanh toán MoMo bị hủy hoặc thất bại.", "danger")
        
    return redirect(url_for('lich_su_dat_phong'))


# ===== REVIEW & ĐÁNH GIÁ =====

@app.route('/review/<ma_dp>', methods=['GET', 'POST'])
def viet_review(ma_dp):
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!", "warning")
        return redirect(url_for('dang_nhap'))

    dp = db.session.get(DatPhong, ma_dp)
    if not dp or dp.maKH != session.get('maND'):
        flash("Không tìm thấy đơn đặt phòng!", "danger")
        return redirect(url_for('lich_su_dat_phong'))

    # Only allow review for completed bookings
    if dp.trangThai not in ('Đã thanh toán', 'Đã trả phòng', 'Đã cọc (Online)'):
        flash("Bạn chỉ có thể đánh giá sau khi đã thanh toán hoặc trả phòng!", "warning")
        return redirect(url_for('lich_su_dat_phong'))

    # Check if already reviewed
    existing = Review.query.filter_by(maDatPhong=ma_dp, maKH=session['maND']).first()
    if existing:
        flash("Bạn đã đánh giá đơn này rồi!", "info")
        return redirect(url_for('xem_review', ma_dp=ma_dp))

    # Get room info for display
    chi_tiet = ChiTietDatPhong.query.filter_by(maDatPhong=ma_dp).first()
    phong = db.session.get(Phong, chi_tiet.maPhong) if chi_tiet and chi_tiet.maPhong else None
    loai_phong = db.session.get(LoaiPhong, phong.maLoaiPhong) if phong else None

    if request.method == 'POST':
        rating = int(request.form.get('rating', 5))
        comment = request.form.get('comment', '').strip()

        if rating < 1 or rating > 5:
            flash("Đánh giá phải từ 1 đến 5 sao!", "danger")
        else:
            ma_review = "RV_" + str(uuid.uuid4())[:8]
            review = Review(
                maReview=ma_review,
                maDatPhong=ma_dp,
                maKH=session['maND'],
                rating=rating,
                comment=comment
            )
            db.session.add(review)
            db.session.commit()
            flash("Cảm ơn bạn đã đánh giá!", "success")
            return redirect(url_for('xem_review', ma_dp=ma_dp))

    return render_template('review_form.html', dp=dp, loai_phong=loai_phong, phong=phong)


@app.route('/review-xem/<ma_dp>')
def xem_review(ma_dp):
    dp = db.session.get(DatPhong, ma_dp)
    if not dp:
        flash("Không tìm thấy đơn đặt phòng!", "danger")
        return redirect(url_for('trang_chu'))

    reviews = Review.query.filter_by(maDatPhong=ma_dp).order_by(Review.ngay.desc()).all()
    avg = db.session.query(db.func.avg(Review.rating)).filter_by(maDatPhong=ma_dp).scalar()
    return render_template('review_list.html', reviews=reviews, avg=avg, dp=dp)


@app.route('/loai-phong/<ma_loai>/review')
def review_loai_phong(ma_loai):
    loai = db.session.get(LoaiPhong, ma_loai)
    if not loai:
        flash("Không tìm thấy loại phòng!", "danger")
        return redirect(url_for('trang_chu'))

    # Get all reviews for rooms of this type
    reviews = db.session.query(Review)\
        .join(DatPhong, Review.maDatPhong == DatPhong.maDatPhong)\
        .join(ChiTietDatPhong, ChiTietDatPhong.maDatPhong == DatPhong.maDatPhong)\
        .join(Phong, ChiTietDatPhong.maPhong == Phong.maPhong)\
        .filter(Phong.maLoaiPhong == ma_loai)\
        .order_by(Review.ngay.desc())\
        .all()

    avg = db.session.query(db.func.avg(Review.rating))\
        .join(DatPhong, Review.maDatPhong == DatPhong.maDatPhong)\
        .join(ChiTietDatPhong, ChiTietDatPhong.maDatPhong == DatPhong.maDatPhong)\
        .join(Phong, ChiTietDatPhong.maPhong == Phong.maPhong)\
        .filter(Phong.maLoaiPhong == ma_loai)\
        .scalar()

    return render_template('review_list.html', reviews=reviews, avg=avg, loai=loai)

@app.route('/api/check-voucher', methods=['POST'])
def check_voucher():
    data = request.json
    ma_km = data.get('ma_km', '').strip().upper()
    km = db.session.get(KhuyenMai, ma_km)
    
    if not km:
        return jsonify({'success': False, 'message': 'Mã giảm giá không tồn tại!'})
        
    if not km.trangThai:
        return jsonify({'success': False, 'message': 'Mã giảm giá đã hết hạn hoặc bị khóa!'})
        
    if km.soLuong <= 0:
        return jsonify({'success': False, 'message': 'Mã giảm giá đã hết lượt sử dụng!'})
        
    return jsonify({
        'success': True,
        'phanTramGiam': km.phanTramGiam,
        'message': f'Áp dụng mã giảm giá thành công! Giảm {km.phanTramGiam}%'
    })

@app.route('/huy-phong/<ma_dp>')
def huy_phong(ma_dp):
    if 'maND' not in session:
        flash("Vui lòng đăng nhập!", "danger")
        return redirect(url_for('dang_nhap'))
        
    dp = db.session.get(DatPhong, ma_dp)
    if not dp or dp.maKH != session.get('maND'):
        flash("Không tìm thấy đơn đặt phòng!", "danger")
        return redirect(url_for('lich_su_dat_phong'))
        
    if dp.trangThai not in ['Chờ nhận phòng', 'Đã cọc (Online)']:
        flash("Đơn này không thể hủy!", "danger")
        return redirect(url_for('lich_su_dat_phong'))
        
    # Check 24 hours rule
    hours_left = (dp.ngayNhanDuKien - datetime.now()).total_seconds() / 3600
    if hours_left < 24:
        flash("Bạn chỉ có thể hủy phòng trước ngày nhận ít nhất 24 giờ!", "danger")
        return redirect(url_for('lich_su_dat_phong'))
        
    try:
        # Change status
        dp.trangThai = 'Đã hủy'
        
        # Free up the room
        chi_tiet = ChiTietDatPhong.query.filter_by(maDatPhong=dp.maDatPhong).first()
        if chi_tiet and chi_tiet.maPhong:
            phong = db.session.get(Phong, chi_tiet.maPhong)
            if phong:
                # Trả lại trạng thái phòng trống cho hệ thống
                phong.trangThai = 'Trống'
                
        db.session.commit()
        flash("Đã hủy phòng thành công! Hẹn gặp lại bạn lần sau.", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Có lỗi xảy ra: {str(e)}", "danger")
        
    return redirect(url_for('lich_su_dat_phong'))
