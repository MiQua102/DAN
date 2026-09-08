import re

with open('d:/DAN/eapp/templates/quan_ly_nhan_su.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('{% else %}{{ nv.gioiTinh }}{% endif %}', '{% else %}{{ nv.gioiTinh or \'\' }}{% endif %}')

with open('d:/DAN/eapp/templates/quan_ly_nhan_su.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed None display in HTML")
