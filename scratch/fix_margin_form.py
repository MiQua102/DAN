import re

with open('d:/DAN/eapp/templates/form_dat_phong.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<div class="container mb-5">', '<div class="container mb-5" style="margin-top: 120px;">')

with open('d:/DAN/eapp/templates/form_dat_phong.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed container margin in form_dat_phong")
