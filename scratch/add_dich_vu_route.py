import re

# 1. Update base.html nav link
with open('d:/DAN/eapp/templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('href="#dichvu">{{ _(\'services\')|upper }}</a>', 'href="/dich-vu">{{ _(\'services\')|upper }}</a>')

with open('d:/DAN/eapp/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Add route to index.py
with open('d:/DAN/eapp/index.py', 'r', encoding='utf-8') as f:
    index_content = f.read()

route_code = """
@app.route('/dich-vu')
def dich_vu():
    from eapp.models import DichVu
    danh_sach_dv = DichVu.query.filter_by(trangThai=True).all()
    return render_template('dich_vu.html', danh_sach_dv=danh_sach_dv)

"""

if "def dich_vu():" not in index_content:
    # Insert before the last error handler or just before @app.route('/set-lang')
    index_content = index_content.replace("@app.route('/set-lang/<lang>')", route_code + "\n@app.route('/set-lang/<lang>')")
    with open('d:/DAN/eapp/index.py', 'w', encoding='utf-8') as f:
        f.write(index_content)

print("Updated base.html and index.py")
