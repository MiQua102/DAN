import re

with open('d:/DAN/eapp/templates/dich_vu.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('{{ dv.tenDV }}', '{{ _(dv.tenDV) }}')
content = content.replace("{{ dv.moTa if dv.moTa else _('premium_service_desc') }}", "{{ _(dv.moTa) if dv.moTa else _('premium_service_desc') }}")
content = content.replace("{{ _('per_unit') }} {{ dv.donViTinh }}", "{{ _('per_unit') }} {{ _(dv.donViTinh) }}")

with open('d:/DAN/eapp/templates/dich_vu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied dynamic DB translations to dich_vu.html")
