import re

with open('d:/DAN/eapp/templates/xem_hoa_don.html', 'r', encoding='utf-8') as f:
    content = f.read()

bad_snippet = '''{% if is_admin %}
            <a href="/quan-ly-khuyen-mai"><i class="fa-solid fa-ticket me-2"></i> Khuyến Mãi (Voucher)</a>
            <a href="/quan-ly-nhan-su"><i class="fa-solid fa-user-tie me-2"></i> Quản Lý Nhân Sự</a>
            {% endif %}'''

# Might have different indentation
content = re.sub(r'\{%\s*if is_admin\s*%\}\s*<a href="/quan-ly-khuyen-mai".*?</a>\s*<a href="/quan-ly-nhan-su".*?</a>\s*\{%\s*endif\s*%\}', '', content, flags=re.DOTALL)

with open('d:/DAN/eapp/templates/xem_hoa_don.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed stray admin links from xem_hoa_don.html")
