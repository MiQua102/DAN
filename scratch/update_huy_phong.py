import re

with open('d:/DAN/eapp/index.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Pass `now` to `lich_su_dat_phong`
old_render = "return render_template('lich_su_dat_phong.html', danh_sach_don=danh_sach_don)"
new_render = "return render_template('lich_su_dat_phong.html', danh_sach_don=danh_sach_don, now=datetime.now())"
content = content.replace(old_render, new_render)

# Add /huy-phong/<ma_dp> route
new_route = '''
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
'''

if "def huy_phong(ma_dp):" not in content:
    content += new_route
    with open('d:/DAN/eapp/index.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added huy_phong route and now param")
else:
    print("Already exists")
