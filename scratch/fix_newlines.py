import re

with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

bad = "    tien_giam_gia = getattr(dp, 'tienGiamGia', 0) or 0\\n    tong_tien = tien_phong + tien_dich_vu - tien_giam_gia\\n    if tong_tien < 0: tong_tien = 0\\n\n"
good = """    tien_giam_gia = getattr(dp, 'tienGiamGia', 0) or 0
    tong_tien = tien_phong + tien_dich_vu - tien_giam_gia
    if tong_tien < 0:
        tong_tien = 0
"""

content = content.replace(bad, good)

# also check if I did it for giamGia=tien_giam_gia,\n
bad2 = "            giamGia=tien_giam_gia,\\n\n"
good2 = "            giamGia=tien_giam_gia,\n"
content = content.replace(bad2, good2)

with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed literal newlines in admin.py")
