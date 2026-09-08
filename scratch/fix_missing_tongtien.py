import re

with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("            giamGia=tien_giam_gia,\n                trangThai='Đã thanh toán',", 
"""            giamGia=tien_giam_gia,
            tongTien=tong_tien,
            trangThai='Đã thanh toán',""")

with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed missing tongTien in admin.py")
