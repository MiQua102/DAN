import glob
import re

templates = glob.glob('d:/DAN/eapp/templates/*.html')
insert_html = '''
            {% if is_admin %}
            <a href="/quan-ly-khuyen-mai"><i class="fa-solid fa-ticket me-2"></i> Khuyến Mãi (Voucher)</a>
            <a href="/quan-ly-nhan-su">
'''

for t in templates:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<a href="/quan-ly-nhan-su"' in content and '<a href="/quan-ly-khuyen-mai"' not in content:
        content = re.sub(
            r'\{\%\s*if\s*is_admin\s*\%\}\s*<a href="/quan-ly-nhan-su"',
            r'{% if is_admin %}\n            <a href="/quan-ly-khuyen-mai"><i class="fa-solid fa-ticket me-2"></i> Khuyến Mãi (Voucher)</a>\n            <a href="/quan-ly-nhan-su"',
            content
        )
        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated sidebar in {t}')
