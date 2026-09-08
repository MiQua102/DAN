import re

with open('d:/DAN/eapp/templates/dich_vu.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('{% block extra_css %}\n<style>', '{% block extra_css %}')
content = content.replace('</style>\n{% endblock %}', '{% endblock %}')

# Also fix the image links that are broken, maybe they just need a refresh, but let's use reliable images
# Or just let them be, the main issue is the CSS ignoring
with open('d:/DAN/eapp/templates/dich_vu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed CSS nesting bug in dich_vu.html")
