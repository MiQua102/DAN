import re

with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "tien_giam_gia = getattr(dp" in line and "\\n" in line:
        new_lines.append("    tien_giam_gia = getattr(dp, 'tienGiamGia', 0) or 0\n")
        new_lines.append("    tong_tien = tien_phong + tien_dich_vu - tien_giam_gia\n")
        new_lines.append("    if tong_tien < 0:\n")
        new_lines.append("        tong_tien = 0\n")
    elif "giamGia=tien_giam_gia" in line and "\\n" in line:
        new_lines.append("            giamGia=tien_giam_gia,\n")
    else:
        new_lines.append(line)

with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed")
