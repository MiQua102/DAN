import re

with open('d:/DAN/eapp/templates/dich_vu.html', 'r', encoding='utf-8') as f:
    content = f.read()

bad_string = "{{ dv.moTa if dv.moTa else '{{ _(\\'premium_service_desc\\') }}' }}"
good_string = "{{ dv.moTa if dv.moTa else _('premium_service_desc') }}"

content = content.replace(bad_string, good_string)

with open('d:/DAN/eapp/templates/dich_vu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Jinja syntax error")
