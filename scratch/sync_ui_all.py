import re
import glob

# 1. Update pages that extend base.html
client_pages = [
    'd:/DAN/eapp/templates/chi_tiet_phong.html',
    'd:/DAN/eapp/templates/lich_su_dat_phong.html',
    'd:/DAN/eapp/templates/review_form.html',
    'd:/DAN/eapp/templates/review_list.html',
    'd:/DAN/eapp/templates/xem_hoa_don.html'
]

for t in client_pages:
    try:
        with open(t, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add top margin to container if missing
        if '<div class="container">' in content and 'style="margin-top:' not in content:
            content = content.replace('<div class="container">', '<div class="container" style="margin-top: 120px;">')
        elif '<div class="container my-5">' in content:
            content = content.replace('<div class="container my-5">', '<div class="container my-5" style="margin-top: 120px !important;">')
        elif '<div class="container py-5 mt-5">' in content:
            content = content.replace('<div class="container py-5 mt-5">', '<div class="container py-5" style="margin-top: 80px;">')
        
        # Replace colors
        content = content.replace('bg-primary', 'bg-dark-charcoal')
        content = content.replace('btn-primary', 'btn-gold')
        content = content.replace('text-primary', 'text-gold')
        content = content.replace('btn-outline-primary', 'btn-outline-dark')
        content = content.replace('bg-warning', 'bg-gold')
        
        # specific for chi_tiet_phong
        if 'hero-room' in content:
            content = content.replace('height: 420px;', 'height: 60vh;')
            content = content.replace('h1 { color: #fff;', 'h1 { color: #fff; font-family: "Playfair Display", serif;')

        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)
    except FileNotFoundError:
        pass

# 2. Update standalone Auth pages (dang_nhap, dang_ky)
auth_pages = ['d:/DAN/eapp/templates/dang_nhap.html', 'd:/DAN/eapp/templates/dang_ky.html']
for t in auth_pages:
    try:
        with open(t, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add fonts
        if 'Playfair Display' not in content:
            font_link = '<link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">'
            content = content.replace('</title>', '</title>\n    ' + font_link)
        
        # Update css
        content = content.replace('font-family: sans-serif;', 'font-family: "Jost", sans-serif;')
        content = content.replace('background: #212529;', 'background: #1a1a1a;') # bg-dark to dark-charcoal
        content = content.replace('color: #ffc107;', 'color: #D4AF37; font-family: "Playfair Display", serif; letter-spacing: 2px;') # warning to gold
        content = content.replace('btn-warning', 'btn-dark') # Change buttons if needed or let them be gold
        
        # Change card style
        content = content.replace('box-shadow: 0 15px 35px rgba(0,0,0,0.2);', 'box-shadow: 0 20px 50px rgba(0,0,0,0.3); border-top: 4px solid #D4AF37; border-radius: 0;')
        
        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)
    except FileNotFoundError:
        pass

print("Sync completed!")
