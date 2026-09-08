import re

with open('d:/DAN/eapp/templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hardcoded base.html texts
content = content.replace('href="#dichvu">DỊCH VỤ</a>', 'href="#dichvu">{{ _(\'services\')|upper }}</a>')
content = content.replace('href="#lienhe">LIÊN HỆ</a>', 'href="#lienhe">{{ _(\'contact\')|upper }}</a>')
content = content.replace('Xin chào, {{ session[\'tenDangNhap\'] }}', '{{ _(\'hello\') }}, {{ session[\'tenDangNhap\'] }}')
content = content.replace('VÀO TRANG QUẢN TRỊ', '{{ _(\'admin_page\') }}')
content = content.replace('{{ _(\'history\')|upper }}', '{{ _(\'history\')|upper }}') # Already correct but just to verify

with open('d:/DAN/eapp/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('d:/DAN/eapp/templates/trang_chu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hardcoded trang_chu.html texts
content = content.replace('<p>Welcome to</p>', '<p>{{ _(\'welcome_to\') }}</p>')
content = content.replace('Ngày nhận (Check-in)', '{{ _(\'checkin\') }}')
content = content.replace('Ngày trả (Check-out)', '{{ _(\'checkout\') }}')
content = content.replace('Khách (Guests)', '{{ _(\'guests\') }}')
content = content.replace('>Tất cả<', '>{{ _(\'all\') }}<')
content = content.replace('>1 Người<', '>1 {{ _(\'person\') }}<')
content = content.replace('>2 Người<', '>2 {{ _(\'person\') }}<')
content = content.replace('>Gia đình (4+)<', '>{{ _(\'family\') }}<')
content = content.replace('KIỂM TRA PHÒNG', '{{ _(\'check_room\') }}')
content = content.replace('TÌM PHÒNG NHANH', '{{ _(\'quick_search\') }}')
content = content.replace('KIỂM TRA NGAY', '{{ _(\'check_room_now\') }}')
content = content.replace('Khám Phá Hạng Phòng', '{{ _(\'explore_rooms\') }}')
content = content.replace('Discover Our Rooms', '{{ _(\'discover_rooms\') }}')
content = content.replace('Tối đa', '{{ _(\'max\') }}')
content = content.replace(' Khách &nbsp;', ' {{ _(\'guest\') }} &nbsp;')
content = content.replace('Khách Hàng Nói Về Chúng Tôi', '{{ _(\'testimonials\') }}')
content = content.replace('Guest Testimonials', '{{ _(\'guest_testimonials\') }}')

with open('d:/DAN/eapp/templates/trang_chu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied translations")
