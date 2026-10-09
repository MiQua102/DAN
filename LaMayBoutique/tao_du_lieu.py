from eapp import app, db
from eapp.models import NguoiDung, NhanVien, VaiTro, LoaiPhong
from werkzeug.security import generate_password_hash


def tao_du_lieu_mau():
    with app.app_context():
        # 1. Tạo vai trò (Role)
        vt_admin = db.session.get(VaiTro,'ADMIN')
        if not vt_admin:
            vt_admin = VaiTro(maVaiTro='ADMIN', tenVaiTro='Quản trị viên', moTa='Full quyền')
            db.session.add(vt_admin)
            
        vt_staff = db.session.get(VaiTro, 'STAFF')
        if not vt_staff:
            vt_staff = VaiTro(maVaiTro='STAFF', tenVaiTro='Nhân viên lễ tân', moTa='Quyền xem và tạo đơn')
            db.session.add(vt_staff)

        # 2. Tạo tài khoản Lễ tân / Admin để đăng nhập
        if not NguoiDung.query.filter_by(tenDangNhap='admin').first():
            # Mã hóa mật khẩu '123456' để bảo mật
            mk_hash = generate_password_hash('123456')

            # Tạo NguoiDung trước (Bảng cha)
            user_admin = NguoiDung(maND='NV001', tenDangNhap='admin', email='admin@luxuryhotel.com', matKhau=mk_hash,
                                   maVaiTro='ADMIN')

            # Tạo NhanVien sau (Bảng con - map 1-1 qua maNV)
            nv_admin = NhanVien(maNV='NV001', hoTen='Nguyễn Văn Lễ Tân', sdt='0987654321', cccd='079123456789',
                                chucVu='Quản lý')

            db.session.add(user_admin)
            db.session.add(nv_admin)

        # 3. Tạo danh sách Loại Phòng
        if LoaiPhong.query.count() == 0:
            lp1 = LoaiPhong(maLoaiPhong='LP01', tenLoaiPhong='Phòng Standard', sucChua=2, giaCoBan=500000,
                            dienTich=25.0)
            lp2 = LoaiPhong(maLoaiPhong='LP02', tenLoaiPhong='Phòng Deluxe', sucChua=3, giaCoBan=1200000, dienTich=40.0)
            lp3 = LoaiPhong(maLoaiPhong='LP03', tenLoaiPhong='Phòng Suite VIP', sucChua=4, giaCoBan=2500000,
                            dienTich=60.0)

            db.session.add_all([lp1, lp2, lp3])

        # Lưu tất cả xuống Database
        db.session.commit()
        print("Đã bơm dữ liệu mẫu thành công! Tài khoản: admin | Mật khẩu: 123456")


if __name__ == '__main__':
    tao_du_lieu_mau()