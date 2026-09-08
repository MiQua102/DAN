import re

target_files = ['d:/DAN/eapp/templates/quan_ly_nhan_su.html', 'd:/DAN/eapp/templates/quan_ly_khuyen_mai.html']

correct_style = '''    <style>
        body { background-color: #f4f6f9; }
        .sidebar { min-height: 100vh; background-color: #4A3B32; color: white; }
        .sidebar a { color: #e0d8d3; text-decoration: none; padding: 15px 20px; display: block; transition: 0.3s; }
        .sidebar a:hover, .sidebar a.active { background-color: #5C4A3E; color: white; border-left: 4px solid #D4AF37; }
        .bg-brown { background-color: #4A3B32 !important; color: white !important; }
        .text-gold { color: #D4AF37 !important; }
        .btn-warning { background-color: #D4AF37 !important; border-color: #D4AF37 !important; color: white !important; }
        .btn-warning:hover { background-color: #B5952F !important; border-color: #B5952F !important; color: white !important; }
    </style>'''

for t in target_files:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace <style> block
    content = re.sub(
        r'<style>.*?</style>',
        correct_style,
        content,
        flags=re.DOTALL
    )

    # Replace body structure if not already d-flex
    if '<div class="d-flex">' not in content:
        content = content.replace('<body>', '<body>\n    <div class="d-flex">')
        content = content.replace('<!-- Sidebar -->', '<!-- Sidebar -->')
        # Remove position fixed from sidebar if any
        content = content.replace('<div class="sidebar" style="width: 250px;">', '<div class="sidebar" style="width: 250px; min-height: 100vh;">')
        content = content.replace('padding-top: 20px;', '')
        
        # Replace main-content with flex-grow-1 and remove old main-content
        content = content.replace('<div class="main-content">', '<div class="flex-grow-1">')
        
        # Add closing div for d-flex before script or body
        content = content.replace('    <script src=', '    </div>\n    <script src=')

    # Fix specific colors
    content = content.replace('bg-primary text-white', 'bg-brown text-white')
    content = content.replace('bg-success text-white', 'bg-brown text-white')
    
    with open(t, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated styles for HR and Promo templates")
