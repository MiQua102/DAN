import re

with open('d:/DAN/eapp/templates/form_dat_phong.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add styles
css_block = '''{% block extra_css %}
<style>
    .booking-card {
        background: #fff;
        border: none;
        box-shadow: 0 15px 40px rgba(0,0,0,0.08);
        border-radius: 0;
    }
    .booking-header {
        background: var(--dark-charcoal);
        color: var(--gold);
        padding: 30px;
        text-align: center;
        border-bottom: 2px solid var(--gold);
    }
    .form-control, .form-select {
        border-radius: 0;
        border: 1px solid #ddd;
        padding: 12px 15px;
        font-family: 'Jost', sans-serif;
    }
    .form-control:focus, .form-select:focus {
        border-color: var(--gold);
        box-shadow: none;
    }
    .form-label {
        font-weight: 600;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #555;
    }
    .section-divider {
        display: flex;
        align-items: center;
        text-align: center;
        margin: 40px 0 20px;
        color: var(--gold);
    }
    .section-divider::before, .section-divider::after {
        content: '';
        flex: 1;
        border-bottom: 1px solid #eee;
    }
    .section-divider span {
        padding: 0 15px;
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-style: italic;
    }
</style>
{% endblock %}'''

content = re.sub(r'\{\%\s*block extra_css\s*\%\}.*?\{\%\s*endblock\s*\%\}', css_block, content, flags=re.DOTALL)

# Tweak layout
content = content.replace('class="card shadow-sm border-0"', 'class="booking-card"')
content = content.replace('class="card-header bg-brown text-white py-3"', 'class="booking-header"')
content = content.replace('<h4 class="mb-0 fw-bold"><i class="fa-solid fa-file-invoice me-2"></i>Form Đặt Phòng Trực Tuyến</h4>', '<h2 class="mb-0 font-serif">Reservation</h2><p class="mb-0 text-white" style="letter-spacing: 2px; font-size:0.8rem; text-transform:uppercase;">Secure Your Stay</p>')

content = content.replace('<h5 class="fw-bold text-secondary mb-3"><i class="fa-solid fa-user me-2"></i>Thông Tin Khách Hàng</h5>', '<div class="section-divider"><span>Guest Details</span></div>')
content = content.replace('<h5 class="fw-bold text-secondary mb-3"><i class="fa-solid fa-clock me-2"></i>Thời Gian Lưu Trú</h5>', '<div class="section-divider"><span>Stay Information</span></div>')

content = content.replace('bg-white border border-warning border-2 rounded-3 shadow-sm', 'bg-light border-0 p-4 rounded-0')
content = content.replace('fw-bold text-gold mb-2', 'form-label')

with open('d:/DAN/eapp/templates/form_dat_phong.html', 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Updated form_dat_phong.html UI")
