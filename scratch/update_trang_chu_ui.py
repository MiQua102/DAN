import re

with open('d:/DAN/eapp/templates/trang_chu.html', 'r', encoding='utf-8') as f:
    content = f.read()

testimonials_html = '''
<!-- Testimonials Section -->
{% if top_reviews %}
<section class="py-5 bg-light mt-5">
    <div class="container">
        <div class="text-center mb-5">
            <h2 class="fw-bold"><i class="fa-solid fa-heart text-danger me-2"></i>Khách hàng nói gì về chúng tôi</h2>
            <p class="text-muted">Hơn 10,000+ lượt đánh giá 5 sao từ khách lưu trú thực tế</p>
        </div>
        <div class="row g-4">
            {% for review in top_reviews %}
            <div class="col-md-4">
                <div class="card h-100 border-0 shadow-sm rounded-4 p-4 text-center">
                    <div class="mb-3">
                        {% for i in range(1, 6) %}
                            {% if i <= review.rating %}
                                <i class="fa-solid fa-star text-warning"></i>
                            {% else %}
                                <i class="fa-regular fa-star text-muted"></i>
                            {% endif %}
                        {% endfor %}
                    </div>
                    <p class="fst-italic text-secondary mb-4">"{{ review.comment }}"</p>
                    <div class="mt-auto">
                        <h6 class="fw-bold mb-1">{{ review.khachhang.hoTen if review.khachhang else 'Khách ẩn danh' }}</h6>
                        <small class="text-muted">{{ review.ngay.strftime('%d/%m/%Y') }}</small>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
{% endif %}

{% endblock %}
'''

if "<!-- Testimonials Section -->" not in content:
    content = content.replace('{% endblock %}', testimonials_html)
    with open('d:/DAN/eapp/templates/trang_chu.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added testimonials to trang_chu.html")
else:
    print("Testimonials already exists")
