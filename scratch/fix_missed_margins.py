import re

files_to_fix = [
    ('d:/DAN/eapp/templates/goi_dich_vu_khach.html', '<div class="container py-3">', '<div class="container py-3" style="margin-top: 120px;">'),
    ('d:/DAN/eapp/templates/thanh_toan.html', '<div class="container py-5">', '<div class="container py-5" style="margin-top: 120px;">'),
    ('d:/DAN/eapp/templates/thanh_toan_online.html', '<div class="container py-5 mt-5">', '<div class="container py-5 mt-5" style="margin-top: 120px !important;">'),
    ('d:/DAN/eapp/templates/xem_hoa_don.html', '<div class="container py-5">', '<div class="container py-5" style="margin-top: 120px;">')
]

for t, bad, good in files_to_fix:
    try:
        with open(t, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace(bad, good)
            
        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)
    except FileNotFoundError:
        pass

print("Fixed container margins for missed pages")
