import re

with open('d:/DAN/eapp/translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# For Vietnamese dict
vi_old = "'guest_testimonials': 'Guest Testimonials'\n    },"
vi_new = """'guest_testimonials': 'Guest Testimonials',
        'exclusive_amenities': 'Tiện Ích Đặc Quyền',
        'exclusive_services_sub': 'Exclusive Services',
        'enjoy_difference': 'Tận Hưởng Sự Khác Biệt',
        'enjoy_difference_desc': 'Khám phá các dịch vụ thượng lưu được thiết kế riêng biệt để mang lại cho bạn những trải nghiệm nghỉ dưỡng hoàn hảo và đáng nhớ nhất.',
        'premium_service_desc': 'Dịch vụ cao cấp chuẩn 5 sao.',
        'per_unit': 'Theo',
        'no_services': 'Hệ thống hiện tại chưa có dịch vụ nào.',
        'ready_to_experience': 'Bạn đã sẵn sàng trải nghiệm?',
        'ready_to_experience_desc': 'Để sử dụng các dịch vụ này, quý khách vui lòng đặt phòng trước. Các tiện ích có thể được gọi trực tiếp lên phòng sau khi nhận phòng.'
    },"""

if vi_old in content:
    content = content.replace(vi_old, vi_new)

# For English dict
en_old = "'guest_testimonials': 'Guest Testimonials'\n    }\n}"
en_new = """'guest_testimonials': 'Guest Testimonials',
        'exclusive_amenities': 'Exclusive Amenities',
        'exclusive_services_sub': 'Tiện Ích Đặc Quyền',
        'enjoy_difference': 'Enjoy The Difference',
        'enjoy_difference_desc': 'Discover exclusive premium services tailored to provide you with the most perfect and memorable resort experiences.',
        'premium_service_desc': 'Premium 5-star standard service.',
        'per_unit': 'Per',
        'no_services': 'There are currently no services in the system.',
        'ready_to_experience': 'Ready to experience?',
        'ready_to_experience_desc': 'To use these services, please book a room first. Amenities can be ordered directly to your room after check-in.'
    }\n}"""

if en_old in content:
    content = content.replace(en_old, en_new)

with open('d:/DAN/eapp/translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated translations")
