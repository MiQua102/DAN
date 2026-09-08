import re

with open('d:/DAN/eapp/templates/form_dat_phong.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('{% block extra_css %}\n<style>', '{% block extra_css %}')
content = content.replace('</style>\n{% endblock %}', '{% endblock %}')

with open('d:/DAN/eapp/templates/form_dat_phong.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed CSS nesting in form_dat_phong.html")
