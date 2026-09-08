import re

with open('d:/DAN/eapp/translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add to vi dict
vi_old = "'ready_to_experience_desc': 'Để sử dụng các dịch vụ này, quý khách vui lòng đặt phòng trước. Các tiện ích có thể được gọi trực tiếp lên phòng sau khi nhận phòng.'"
vi_new = vi_old + """,
        'Bia Heineken': 'Bia Heineken',
        'Bia Tiger': 'Bia Tiger',
        'Ăn sáng Buffet': 'Ăn sáng Buffet',
        'Dịch vụ Giặt ủi': 'Dịch vụ Giặt ủi',
        'Massage Body 60p': 'Massage Body 60p',
        'Mì ly Omachi': 'Mì ly Omachi',
        'Nước ngọt Coca Cola': 'Nước ngọt Coca Cola',
        'Nước khoáng Lavie': 'Nước khoáng Lavie',
        'Rượu vang đỏ Đà Lạt': 'Rượu vang đỏ Đà Lạt',
        "Snack khoai tây Lay's": "Snack khoai tây Lay's",
        'Thuê xe máy': 'Thuê xe máy',
        'Xe đưa đón sân bay': 'Xe đưa đón sân bay',
        'Nước Sting': 'Nước Sting',
        'Lon 330ml ướp lạnh': 'Lon 330ml ướp lạnh',
        'Vé ăn sáng tại nhà hàng tầng trệt': 'Vé ăn sáng tại nhà hàng tầng trệt',
        'Giặt ủi sấy khô giao trong ngày': 'Giặt ủi sấy khô giao trong ngày',
        'Vé massage thư giãn 60 phút tại Spa': 'Vé massage thư giãn 60 phút tại Spa',
        'Mì tôm ly ăn liền': 'Mì tôm ly ăn liền',
        'Lon 320ml ướp lạnh': 'Lon 320ml ướp lạnh',
        'Nước khoáng thiên nhiên 500ml': 'Nước khoáng thiên nhiên 500ml',
        'Chai 750ml cao cấp': 'Chai 750ml cao cấp',
        'Snack gói lớn': 'Snack gói lớn',
        'Cho thuê xe tay ga Honda Airblade/Vision': 'Cho thuê xe tay ga Honda Airblade/Vision',
        'Xe 4 chỗ đưa đón sân bay 1 chiều': 'Xe 4 chỗ đưa đón sân bay 1 chiều',
        'Lon': 'Lon',
        'Vé': 'Vé',
        'Kg': 'Kg',
        'Ly': 'Ly',
        'Chai': 'Chai',
        'Gói': 'Gói',
        'Ngày': 'Ngày',
        'Lượt': 'Lượt'"""

if vi_old in content:
    content = content.replace(vi_old, vi_new)

# Add to en dict
en_old = "'ready_to_experience_desc': 'To use these services, please book a room first. Amenities can be ordered directly to your room after check-in.'"
en_new = en_old + """,
        'Bia Heineken': 'Heineken Beer',
        'Bia Tiger': 'Tiger Beer',
        'Ăn sáng Buffet': 'Buffet Breakfast',
        'Dịch vụ Giặt ủi': 'Laundry Service',
        'Massage Body 60p': 'Body Massage 60m',
        'Mì ly Omachi': 'Omachi Cup Noodles',
        'Nước ngọt Coca Cola': 'Coca Cola',
        'Nước khoáng Lavie': 'Lavie Mineral Water',
        'Rượu vang đỏ Đà Lạt': 'Dalat Red Wine',
        "Snack khoai tây Lay's": "Lay's Potato Chips",
        'Thuê xe máy': 'Motorbike Rental',
        'Xe đưa đón sân bay': 'Airport Transfer',
        'Nước Sting': 'Sting Energy Drink',
        'Lon 330ml ướp lạnh': 'Cold 330ml can',
        'Vé ăn sáng tại nhà hàng tầng trệt': 'Breakfast ticket at ground floor restaurant',
        'Giặt ủi sấy khô giao trong ngày': 'Same-day wash and dry laundry',
        'Vé massage thư giãn 60 phút tại Spa': '60-minute relaxation massage ticket at Spa',
        'Mì tôm ly ăn liền': 'Instant cup noodles',
        'Lon 320ml ướp lạnh': 'Cold 320ml can',
        'Nước khoáng thiên nhiên 500ml': '500ml natural mineral water',
        'Chai 750ml cao cấp': 'Premium 750ml bottle',
        'Snack gói lớn': 'Large snack bag',
        'Cho thuê xe tay ga Honda Airblade/Vision': 'Honda Airblade/Vision scooter rental',
        'Xe 4 chỗ đưa đón sân bay 1 chiều': '4-seater car for 1-way airport transfer',
        'Lon': 'Can',
        'Vé': 'Ticket',
        'Kg': 'Kg',
        'Ly': 'Cup',
        'Chai': 'Bottle',
        'Gói': 'Bag',
        'Ngày': 'Day',
        'Lượt': 'Trip'"""

if en_old in content:
    content = content.replace(en_old, en_new)

with open('d:/DAN/eapp/translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated translations with DB values")
