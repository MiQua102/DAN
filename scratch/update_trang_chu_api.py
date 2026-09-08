import re

with open('d:/DAN/eapp/index.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_logic = '''    return render_template('trang_chu.html',
                           danh_sach_loai=danh_sach_loai,
                           avg_ratings=avg_ratings,
                           tien_nghi_map=tien_nghi_map,
                           tu_khoa=tu_khoa,
                           suc_chua=suc_chua,
                           gia_max=gia_max,
                           ngay_nhan=ngay_nhan,
                           ngay_tra=ngay_tra)'''

new_logic = '''    # Load top recent positive reviews
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
                           top_reviews=top_reviews)'''

if "top_reviews=top_reviews" not in content:
    content = content.replace(old_logic, new_logic)
    with open('d:/DAN/eapp/index.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.py with top_reviews")
else:
    print("Already exists")
