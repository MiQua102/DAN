import re

with open('d:/DAN/eapp/templates/dich_vu.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Tiện Ích Đặc Quyền', '{{ _(\'exclusive_amenities\') }}')
content = content.replace('Exclusive Services', '{{ _(\'exclusive_services_sub\') }}')
content = content.replace('Tận Hưởng Sự Khác Biệt', '{{ _(\'enjoy_difference\') }}')
content = content.replace('Khám phá các dịch vụ thượng lưu được thiết kế riêng biệt để mang lại cho bạn những trải nghiệm nghỉ dưỡng hoàn hảo và đáng nhớ nhất.', '{{ _(\'enjoy_difference_desc\') }}')
content = content.replace('Dịch vụ cao cấp chuẩn 5 sao.', '{{ _(\'premium_service_desc\') }}')
content = content.replace('Theo {{ dv.donViTinh }}', '{{ _(\'per_unit\') }} {{ dv.donViTinh }}')
content = content.replace('Hệ thống hiện tại chưa có dịch vụ nào.', '{{ _(\'no_services\') }}')
content = content.replace('Bạn đã sẵn sàng trải nghiệm?', '{{ _(\'ready_to_experience\') }}')
content = content.replace('Để sử dụng các dịch vụ này, quý khách vui lòng đặt phòng trước. Các tiện ích có thể được gọi trực tiếp lên phòng sau khi nhận phòng.', '{{ _(\'ready_to_experience_desc\') }}')
content = content.replace('ĐẶT PHÒNG NGAY', '{{ _(\'book_room\')|upper }}')

with open('d:/DAN/eapp/templates/dich_vu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied translations to dich_vu.html")
