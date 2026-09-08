import re
import os

target = 'd:/DAN/eapp/templates/danh_sach_phong.html'

google_fonts = '''
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
'''

luxury_css = '''
        body { background-color: #f8f5f0; font-family: 'Jost', sans-serif; }
        h1, h2, h3, h4, h5, h6, .font-serif { font-family: 'Playfair Display', serif !important; }
        .sidebar { min-height: 100vh; background-color: #1a1a1a; color: white; border-right: 2px solid #D4AF37; }
        .sidebar a { color: #ccc; text-decoration: none; padding: 15px 20px; display: block; transition: 0.3s; font-size: 0.95rem; letter-spacing: 1px; }
        .sidebar a:hover, .sidebar a.active { background-color: #2a2a2a; color: #D4AF37; border-left: 4px solid #D4AF37; }
        .stat-card { border-radius: 0; border-top: 3px solid #D4AF37; color: #333; padding: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.05); background: #fff; }
        .bg-brown { background-color: #1a1a1a !important; color: white !important; }
        .text-gold { color: #D4AF37 !important; }
        .btn-warning { background-color: #D4AF37 !important; border-color: #D4AF37 !important; color: white !important; border-radius: 0; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; }
        .btn-warning:hover { background-color: #B5952F !important; border-color: #B5952F !important; color: white !important; }
        
        .card { border-radius: 0; border: none; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .card-header { border-radius: 0 !important; background-color: #1a1a1a !important; color: #D4AF37 !important; font-family: 'Playfair Display', serif; letter-spacing: 1px; border-bottom: 2px solid #D4AF37; }
        
        .table { font-size: 0.95rem; }
        .table thead th { background-color: #1a1a1a !important; color: #D4AF37 !important; font-family: 'Playfair Display', serif; font-weight: normal; letter-spacing: 1px; }
        
        .btn-primary, .btn-success, .btn-info { background-color: #1a1a1a !important; border-color: #1a1a1a !important; color: #D4AF37 !important; border-radius: 0; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }
        .btn-primary:hover, .btn-success:hover, .btn-info:hover { background-color: #D4AF37 !important; border-color: #D4AF37 !important; color: white !important; }
        .btn-danger { border-radius: 0; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }
'''

if os.path.exists(target):
    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'fonts.googleapis.com' not in content:
        content = content.replace('</title>', '</title>\n' + google_fonts)
    
    content = re.sub(r'<style>.*?</style>', f'<style>{luxury_css}</style>', content, flags=re.DOTALL)
    content = content.replace('<h4 class="fw-bold text-gold mb-0">', '<h4 class="font-serif fw-bold text-gold mb-0" style="letter-spacing: 3px;">')
    content = content.replace('btn-sm', 'btn-sm rounded-0')
    
    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("Fixed danh_sach_phong")
