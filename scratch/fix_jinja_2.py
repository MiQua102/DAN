import re

with open('d:/DAN/eapp/templates/dich_vu.html', 'r', encoding='utf-8') as f:
    content = f.read()

bad = "'{{ _(\\'premium_service_desc\\') }}'"
good = "_('premium_service_desc')"

content = content.replace(bad, good)

with open('d:/DAN/eapp/templates/dich_vu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Jinja syntax")
