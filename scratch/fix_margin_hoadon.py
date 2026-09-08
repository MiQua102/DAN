import re

with open('d:/DAN/eapp/templates/hoa_don_khach.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<div class="container py-3">', '<div class="container py-3" style="margin-top: 120px;">')

with open('d:/DAN/eapp/templates/hoa_don_khach.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed container margin in hoa_don_khach.html")
