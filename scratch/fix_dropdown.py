import re

with open('d:/DAN/eapp/templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the CSS for nav-link::after so it doesn't break dropdown-toggle
old_css = '''.navbar-custom .nav-link::after {
            content: '';
            position: absolute;
            width: 0; height: 1px;
            bottom: 0; left: 50%;
            background-color: var(--gold);
            transition: all 0.3s ease;
        }
        .navbar-custom .nav-link:hover::after {
            width: 100%; left: 0;
        }'''

new_css = '''.navbar-custom .nav-link:not(.dropdown-toggle)::after {
            content: '';
            position: absolute;
            width: 0; height: 1px;
            bottom: 0; left: 50%;
            background-color: var(--gold);
            transition: all 0.3s ease;
        }
        .navbar-custom .nav-link:not(.dropdown-toggle):hover::after {
            width: 100%; left: 0;
        }'''

content = content.replace(old_css, new_css)

with open('d:/DAN/eapp/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed dropdown arrow bug")
