import re

with open('d:/DAN/eapp/templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_head = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Luxury Hotel & Resort{% endblock %}</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <!-- Bootstrap & FontAwesome -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <!-- AOS Animation -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>
        :root {
            --gold: #D4AF37;
            --gold-dark: #b5952f;
            --dark-charcoal: #1a1a1a;
            --pearl: #F8F5F0;
        }
        
        body { 
            font-family: 'Jost', sans-serif;
            background-color: var(--pearl); 
            color: #333;
            padding-top: 0 !important; /* Navbar will be overlay */
        }
        
        h1, h2, h3, h4, h5, h6, .font-serif {
            font-family: 'Playfair Display', serif;
        }

        /* Navbar Styling */
        .navbar-custom {
            background-color: transparent;
            transition: all 0.4s ease;
            padding: 20px 0;
        }
        .navbar-custom.scrolled {
            background-color: rgba(26, 26, 26, 0.95);
            backdrop-filter: blur(10px);
            padding: 10px 0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        .navbar-custom .nav-link {
            color: white !important;
            text-transform: uppercase;
            font-size: 0.9rem;
            letter-spacing: 1px;
            margin: 0 10px;
            position: relative;
        }
        .navbar-custom .nav-link::after {
            content: '';
            position: absolute;
            width: 0; height: 1px;
            bottom: 0; left: 50%;
            background-color: var(--gold);
            transition: all 0.3s ease;
        }
        .navbar-custom .nav-link:hover::after {
            width: 100%; left: 0;
        }
        
        /* Buttons */
        .btn-gold {
            background-color: var(--gold);
            color: #fff;
            border: 1px solid var(--gold);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 0.85rem;
            border-radius: 0;
            padding: 10px 25px;
            transition: all 0.3s;
        }
        .btn-gold:hover {
            background-color: transparent;
            color: var(--gold);
        }
        
        /* Utility Colors */
        .text-gold { color: var(--gold) !important; }
        .bg-dark-charcoal { background-color: var(--dark-charcoal) !important; }
        
        /* Footer */
        footer {
            background-color: var(--dark-charcoal);
            color: rgba(255,255,255,0.7);
        }
        footer a { color: rgba(255,255,255,0.7); text-decoration: none; transition: 0.3s; }
        footer a:hover { color: var(--gold); }
        .footer-logo { font-size: 2rem; border-top: 1px solid var(--gold); border-bottom: 1px solid var(--gold); padding: 5px 0; color: var(--gold); }
        
        {% block extra_css %}{% endblock %}
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav id="mainNav" class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
        <div class="container">
            <a class="navbar-brand font-serif fw-bold fs-3 text-gold" href="/">
                LUXURY
            </a>
            <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <i class="fa-solid fa-bars text-white fs-4"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mx-auto align-items-center">
                    <li class="nav-item"><a class="nav-link" href="/">{{ _('home') }}</a></li>
                    <li class="nav-item"><a class="nav-link" href="/#phong">{{ _('rooms') }}</a></li>
                    <li class="nav-item"><a class="nav-link" href="#dichvu">DỊCH VỤ</a></li>
                    <li class="nav-item"><a class="nav-link" href="#lienhe">LIÊN HỆ</a></li>
                </ul>
                <ul class="navbar-nav align-items-center">
                    <li class="nav-item dropdown me-3">
                        <a class="nav-link dropdown-toggle text-white" href="#" data-bs-toggle="dropdown">
                            <i class="fa-solid fa-globe"></i> {{ current_lang|upper }}
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end border-0 shadow rounded-0">
                            <li><a class="dropdown-item" href="/set-lang/vi">🇻🇳 Tiếng Việt (VND)</a></li>
                            <li><a class="dropdown-item" href="/set-lang/en">🇬🇧 English (USD)</a></li>
                        </ul>
                    </li>'''

# Find the start and replace up to login logic
content = re.sub(r'<!DOCTYPE html>.*?<li><a class="dropdown-item" href="/set-lang/en">.*?</a></li>', new_head, content, flags=re.DOTALL)

# Add AOS and Navbar JS to the bottom
js_scripts = '''
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        // Init Animation
        AOS.init({ duration: 800, once: true });
        
        // Navbar Scroll Effect
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                document.getElementById('mainNav').classList.add('scrolled');
            } else {
                document.getElementById('mainNav').classList.remove('scrolled');
            }
        });
    </script>
</body>
</html>'''
content = re.sub(r'<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>.*?</body>', js_scripts, content, flags=re.DOTALL)

with open('d:/DAN/eapp/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated base.html with luxury UI")
