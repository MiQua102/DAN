from eapp import db
from datetime import datetime

class VaiTro(db.Model):
    __tablename__ = 'vaitro'
    maVaiTro = db.Column(db.String(20), primary_key=True)
    tenVaiTro = db.Column(db.String(50), nullable=False)
    moTa = db.Column(db.String(255))
    nguoiDungs = db.relationship('NguoiDung', backref='vaitro', lazy=True)

class NguoiDung(db.Model):
    __tablename__ = 'nguoidung'
    maND = db.Column(db.String(20), primary_key=True)
    tenDangNhap = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    matKhau = db.Column(db.String(255), nullable=False)
    trangThai = db.Column(db.Boolean, default=True)
    ngayTao = db.Column(db.DateTime, default=datetime.utcnow)
    maVaiTro = db.Column(db.String(20), db.ForeignKey('vaitro.maVaiTro'))

# Bảng con 1-1 của NguoiDung (Theo đúng ghi chú highlight vàng)
class KhachHang(db.Model):
    __tablename__ = 'khachhang'
    maKH = db.Column(db.String(20), db.ForeignKey('nguoidung.maND'), primary_key=True)
    hoTen = db.Column(db.String(100), nullable=False)
    sdt = db.Column(db.String(15))
    cccd = db.Column(db.String(20), unique=True)
    ngaySinh = db.Column(db.Date)
    gioiTinh = db.Column(db.String(10))
    diaChi = db.Column(db.String(255))
    datPhongs = db.relationship('DatPhong', backref='khachhang', lazy=True)

# Bảng con 1-1 của NguoiDung (Theo đúng ghi chú highlight vàng)
class NhanVien(db.Model):
    __tablename__ = 'nhanvien'
    maNV = db.Column(db.String(20), db.ForeignKey('nguoidung.maND'), primary_key=True)
    hoTen = db.Column(db.String(100), nullable=False)
    sdt = db.Column(db.String(15))
    cccd = db.Column(db.String(20), unique=True)
    ngaySinh = db.Column(db.Date)
    gioiTinh = db.Column(db.String(10))
    diaChi = db.Column(db.String(255))
    chucVu = db.Column(db.String(50))
    ngayVaoLam = db.Column(db.Date)
    trangThai = db.Column(db.Boolean, default=True)

class LoaiPhong(db.Model):
    __tablename__ = 'loaiphong'
    maLoaiPhong = db.Column(db.String(20), primary_key=True)
    tenLoaiPhong = db.Column(db.String(100), nullable=False)
    moTa = db.Column(db.Text)
    sucChua = db.Column(db.Integer, nullable=False)
    giaCoBan = db.Column(db.Float, nullable=False)
    dienTich = db.Column(db.Float)
    phongs = db.relationship('Phong', backref='loaiphong', lazy=True)

class Phong(db.Model):
    __tablename__ = 'phong'
    maPhong = db.Column(db.String(20), primary_key=True)
    soPhong = db.Column(db.String(20), unique=True, nullable=False)
    tang = db.Column(db.Integer)
    trangThai = db.Column(db.String(50))
    ghiChu = db.Column(db.String(255))
    maLoaiPhong = db.Column(db.String(20), db.ForeignKey('loaiphong.maLoaiPhong'))

class TienNghi(db.Model):
    __tablename__ = 'tiennghi'
    maTienNghi = db.Column(db.String(20), primary_key=True)
    tenTienNghi = db.Column(db.String(100), nullable=False)
    moTa = db.Column(db.String(255))
    trangThai = db.Column(db.Boolean, default=True)

class LoaiPhongTienNghi(db.Model):
    __tablename__ = 'loaiphongtiennghi'
    maLoaiPhong = db.Column(db.String(20), db.ForeignKey('loaiphong.maLoaiPhong'), primary_key=True)
    maTienNghi = db.Column(db.String(20), db.ForeignKey('tiennghi.maTienNghi'), primary_key=True)
    soLuong = db.Column(db.Integer)

class KhuyenMai(db.Model):
    __tablename__ = 'khuyenmai'
    maKM = db.Column(db.String(20), primary_key=True)
    phanTramGiam = db.Column(db.Float, nullable=False) # e.g. 10 for 10%
    soLuong = db.Column(db.Integer, default=100)
    trangThai = db.Column(db.Boolean, default=True)

class DatPhong(db.Model):
    __tablename__ = 'datphong'
    maDatPhong = db.Column(db.String(20), primary_key=True)
    ngayDat = db.Column(db.DateTime, default=datetime.utcnow)
    ngayNhanDuKien = db.Column(db.DateTime)
    ngayTraDuKien = db.Column(db.DateTime)
    ngayNhanThucTe = db.Column(db.DateTime)
    ngayTraThucTe = db.Column(db.DateTime)
    soLuongKhach = db.Column(db.Integer)
    trangThai = db.Column(db.String(50))
    ghiChu = db.Column(db.String(255))
    tienGiamGia = db.Column(db.Float, default=0)
    maKH = db.Column(db.String(20), db.ForeignKey('khachhang.maKH'))
    maNV = db.Column(db.String(20), db.ForeignKey('nhanvien.maNV'))
    chiTiets = db.relationship('ChiTietDatPhong', backref='datphong', lazy=True)

class ChiTietDatPhong(db.Model):
    __tablename__ = 'chitietdatphong'
    maChiTiet = db.Column(db.String(20), primary_key=True)
    soNguoi = db.Column(db.Integer)
    donGiaPhong = db.Column(db.Float)
    maDatPhong = db.Column(db.String(20), db.ForeignKey('datphong.maDatPhong'))
    maPhong = db.Column(db.String(20), db.ForeignKey('phong.maPhong'))

class DichVu(db.Model):
    __tablename__ = 'dichvu'
    maDV = db.Column(db.String(20), primary_key=True)
    tenDV = db.Column(db.String(100), nullable=False)
    donViTinh = db.Column(db.String(50))
    donGia = db.Column(db.Float)
    moTa = db.Column(db.String(255))
    trangThai = db.Column(db.Boolean, default=True)

class SuDung_DichVu(db.Model):
    __tablename__ = 'sudung_dichvu'
    maSD = db.Column(db.String(20), primary_key=True)
    thoiGianSuDung = db.Column(db.DateTime, default=datetime.utcnow)
    soLuong = db.Column(db.Integer)
    donGia = db.Column(db.Float)
    thanhTien = db.Column(db.Float)
    maChiTiet = db.Column(db.String(20), db.ForeignKey('chitietdatphong.maChiTiet'))
    maDV = db.Column(db.String(20), db.ForeignKey('dichvu.maDV'))
    maNV = db.Column(db.String(20), db.ForeignKey('nhanvien.maNV'))

    dichvu = db.relationship('DichVu', backref='sudung_dichv', lazy=True)

class HoaDon(db.Model):
    __tablename__ = 'hoadon'
    maHD = db.Column(db.String(20), primary_key=True)
    ngayLap = db.Column(db.DateTime, default=datetime.utcnow)
    tienPhong = db.Column(db.Float, default=0)
    tienDV = db.Column(db.Float, default=0)
    phuThu = db.Column(db.Float, default=0)
    giamGia = db.Column(db.Float, default=0)
    tongTien = db.Column(db.Float)
    trangThai = db.Column(db.String(50))
    maDatPhong = db.Column(db.String(20), db.ForeignKey('datphong.maDatPhong'))

class ThanhToan(db.Model):
    __tablename__ = 'thanhtoan'
    maTT = db.Column(db.String(20), primary_key=True)
    soTien = db.Column(db.Float)
    hinhThuc = db.Column(db.String(50))
    thoiGianThanhToan = db.Column(db.DateTime, default=datetime.utcnow)
    maGD = db.Column(db.String(50))
    trangThai = db.Column(db.String(50))
    maHD = db.Column(db.String(20), db.ForeignKey('hoadon.maHD'))

class Review(db.Model):
    __tablename__ = 'review'
    maReview = db.Column(db.String(20), primary_key=True)
    maDatPhong = db.Column(db.String(20), db.ForeignKey('datphong.maDatPhong'), nullable=False)
    maKH = db.Column(db.String(20), db.ForeignKey('khachhang.maKH'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1‑5
    comment = db.Column(db.Text)
    ngay = db.Column(db.DateTime, default=datetime.utcnow)

    # convenient relationships
    datphong = db.relationship('DatPhong', backref='reviews')
    khachhang = db.relationship('KhachHang', backref='reviews')