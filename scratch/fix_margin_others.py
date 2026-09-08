import glob
import re

files_to_fix = [
    'd:/DAN/eapp/templates/goi_dich_vu_khach.html',
    'd:/DAN/eapp/templates/hoa_don_khach.html',
    'd:/DAN/eapp/templates/thanh_toan.html',
    'd:/DAN/eapp/templates/thanh_toan_online.html',
    'd:/DAN/eapp/templates/xem_hoa_don.html'
]

for t in files_to_fix:
    try:
        with open(t, 'r', encoding='utf-8') as f:
            content = f.read()

        if '<div class="container">' in content:
            content = content.replace('<div class="container">', '<div class="container" style="margin-top: 120px;">')
        elif '<div class="container my-5">' in content:
            content = content.replace('<div class="container my-5">', '<div class="container my-5" style="margin-top: 120px !important;">')
        elif '<div class="container mt-5">' in content:
            content = content.replace('<div class="container mt-5">', '<div class="container mt-5" style="margin-top: 120px !important;">')
            
        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)
    except FileNotFoundError:
        pass

print("Fixed container margins for all other pages")
