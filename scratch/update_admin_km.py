import re

with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_routes = '''
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
'''

if 'def quan_ly_khuyen_mai(' not in content:
    # Add KhuyenMai to the import
    content = content.replace('from eapp.models import LoaiPhong, Phong, DichVu, KhachHang, DatPhong, HoaDon, ThanhToan, ChiTietDatPhong, SuDung_DichVu, NhanVien, NguoiDung', 
                              'from eapp.models import LoaiPhong, Phong, DichVu, KhachHang, DatPhong, HoaDon, ThanhToan, ChiTietDatPhong, SuDung_DichVu, NhanVien, NguoiDung, KhuyenMai')
    content += new_routes
    
    with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated admin.py with KhuyenMai routes")
