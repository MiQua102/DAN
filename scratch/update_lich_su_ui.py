import re

with open('d:/DAN/eapp/templates/lich_su_dat_phong.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_logic = '''                            {% if don.trangThai in ('Đã thanh toán', 'Đã trả phòng', 'Đã cọc (Online)') %}
                                <a href="/review/{{ don.maDatPhong }}" class="btn btn-sm btn-outline-warning fw-bold w-100">
                                    <i class="fa-solid fa-star me-1"></i> Đánh Giá
                                </a>
                            {% elif don.trangThai != 'Đang thuê' and don.trangThai != 'Chờ nhận phòng' and don.trangThai != 'Đã cọc (Online)' and don.trangThai != 'Đã thanh toán' %}
                                <span class="text-muted">-</span>
                            {% endif %}'''

new_logic = '''                            {% if don.trangThai in ('Đã thanh toán', 'Đã trả phòng') %}
                                <a href="/review/{{ don.maDatPhong }}" class="btn btn-sm btn-outline-warning fw-bold w-100 mb-1">
                                    <i class="fa-solid fa-star me-1"></i> Đánh Giá
                                </a>
                            {% endif %}
                            
                            {% if don.trangThai in ['Chờ nhận phòng', 'Đã cọc (Online)'] %}
                                {% set hours_left = (don.ngayNhanDuKien - now).total_seconds() / 3600 %}
                                {% if hours_left >= 24 %}
                                    <a href="/huy-phong/{{ don.maDatPhong }}" class="btn btn-sm btn-outline-danger fw-bold w-100" onclick="return confirm('Bạn có chắc chắn muốn hủy đơn đặt phòng này? (Sẽ được hoàn tiền cọc nếu có)')">
                                        <i class="fa-solid fa-xmark me-1"></i> Hủy Phòng
                                    </a>
                                {% else %}
                                    <button class="btn btn-sm btn-outline-secondary fw-bold w-100" title="Đã quá hạn hủy phòng miễn phí (trước 24h)" onclick="alert('Đã quá thời hạn hủy phòng (phải hủy trước giờ check-in ít nhất 24h). Xin vui lòng liên hệ Lễ tân.'); return false;">
                                        <i class="fa-solid fa-xmark me-1"></i> Không thể hủy
                                    </button>
                                {% endif %}
                            {% elif don.trangThai == 'Đã hủy' %}
                                <span class="text-muted"><i class="fa-solid fa-ban"></i> Đã hủy</span>
                            {% endif %}'''

content = content.replace(old_logic, new_logic)

with open('d:/DAN/eapp/templates/lich_su_dat_phong.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated lich_su_dat_phong.html")
