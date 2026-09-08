import re

with open('d:/DAN/eapp/templates/thanh_toan.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'\{%\s*if is_admin\s*%\}\s*<a href="/quan-ly-khuyen-mai".*?</a>\s*<a href="/quan-ly-nhan-su".*?</a>\s*\{%\s*endif\s*%\}', '', content, flags=re.DOTALL)

with open('d:/DAN/eapp/templates/thanh_toan.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed stray admin links from thanh_toan.html")
