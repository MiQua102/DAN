import re

with open('d:/DAN/eapp/templates/trang_chu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The broken block starts with {% block title %}Trang Chủ - Luxury Hotel
# and ends with the first {% endblock %} at line 37.
broken_title_pattern = r'\{\%\s*block title\s*\%\}Trang Chủ - Luxury Hotel.*?\{\%\s*endblock\s*\%\}'
fixed_title = '{% block title %}Trang Chủ - Luxury Hotel{% endblock %}'

content = re.sub(broken_title_pattern, fixed_title, content, flags=re.DOTALL)

with open('d:/DAN/eapp/templates/trang_chu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed title block bug in trang_chu.html")
