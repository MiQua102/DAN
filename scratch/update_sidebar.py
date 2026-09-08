import glob

templates = glob.glob('d:/DAN/eapp/templates/*.html')
insert_html = '''
        {% if is_admin %}
        <a href="/quan-ly-nhan-su"><i class="fa-solid fa-user-tie me-2"></i> Quản Lý Nhân Sự</a>
        {% endif %}
'''

for t in templates:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<a href="quan-ly-hoa-don"' in content or '<a href="/quan-ly-hoa-don"' in content:
        if 'Quản Lý Nhân Sự' not in content:
            # We want to replace it by appending the new link after the Hoa Don line
            import re
            content = re.sub(
                r'(<a href="/?quan-ly-hoa-don".*?</a>)',
                r'\1' + insert_html,
                content
            )
            with open(t, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {t}')
