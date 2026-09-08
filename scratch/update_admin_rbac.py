import re

with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add route for /quan-ly-nhan-su
new_routes = '''
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
'''

# Append new routes if they don't exist
if 'def quan_ly_nhan_su(' not in content:
    content += new_routes

# Add protection logic to sensitive routes
sensitive_routes = [
    r'(def them_loai_phong\(\):)',
    r'(def xoa_loai_phong\(ma_loai\):)',
    r'(def sua_loai_phong\(ma_loai\):)',
    r'(def them_phong\(\):)',
    r'(def xoa_phong\(ma_phong\):)',
    r'(def sua_phong\(ma_phong\):)',
    r'(def them_dich_vu\(\):)',
    r'(def xoa_dich_vu\(ma_dv\):)',
    r'(def sua_dich_vu\(ma_dv\):)',
    r'(def xoa_khach_hang\(ma_kh\):)'
]

protection_code = '''
    if not dao.kiem_tra_quyen_admin(session.get('maND')):
        flash("Bạn không có quyền quản trị để thực hiện chức năng này!", "danger")
        return redirect(request.referrer or url_for('quan_tri'))
'''

for pattern in sensitive_routes:
    # Check if protection already added by looking for a unique string
    content = re.sub(
        pattern,
        r'\1' + protection_code,
        content
    )

with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated admin.py")
