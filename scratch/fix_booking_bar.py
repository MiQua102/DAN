import re

with open('d:/DAN/eapp/templates/trang_chu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the CSS for booking-bar
old_css = '''    /* Floating Booking Bar */
    .booking-bar {
        position: absolute;
        bottom: -40px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;'''

new_css = '''    /* Floating Booking Bar */
    .booking-bar {
        position: absolute;
        bottom: -40px;
        left: 0;
        right: 0;
        margin: 0 auto;
        width: 80%;'''

content = content.replace(old_css, new_css)

with open('d:/DAN/eapp/templates/trang_chu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed booking-bar CSS")
