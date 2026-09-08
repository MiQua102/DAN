from eapp.models import LoaiPhong, NguoiDung, KhachHang, NhanVien, Phong, DichVu
from werkzeug.security import check_password_hash
from eapp import db

def lay_danh_sach_loai_phong():
    return LoaiPhong.query.all()

def lay_danh_sach_phong():
    return Phong.query.all()

def lay_danh_sach_dich_vu():
    return DichVu.query.all()

def lay_danh_sach_khach_hang():
    return KhachHang.query.all()

def xac_thuc_nguoi_dung(ten_dang_nhap, mat_khau):
    user = NguoiDung.query.filter_by(tenDangNhap=ten_dang_nhap).first()
    if user and check_password_hash(user.matKhau, mat_khau):
        return user
    return None

def kiem_tra_nhan_vien(ma_nd):
    return NhanVien.query.filter_by(maNV=ma_nd).first()

def kiem_tra_quyen_admin(ma_nd):
    nd = NguoiDung.query.filter_by(maND=ma_nd).first()
    if nd and nd.maVaiTro == 'ADMIN':
        return True
    return False

def lay_danh_sach_nhan_vien():
    return db.session.query(NhanVien, NguoiDung).join(NguoiDung, NhanVien.maNV == NguoiDung.maND).all()