import re

with open('d:/DAN/eapp/templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the stray </ul></div></li> that was causing layout break
broken_html = '''                        <ul class="dropdown-menu dropdown-menu-end border-0 shadow rounded-0">
                            <li><a class="dropdown-item" href="/set-lang/vi">🇻🇳 Tiếng Việt (VND)</a></li>
                            <li><a class="dropdown-item" href="/set-lang/en">🇬🇧 English (USD)</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </li>'''

fixed_html = '''                        <ul class="dropdown-menu dropdown-menu-end border-0 shadow rounded-0">
                            <li><a class="dropdown-item" href="/set-lang/vi">🇻🇳 Tiếng Việt (VND)</a></li>
                            <li><a class="dropdown-item" href="/set-lang/en">🇬🇧 English (USD)</a></li>
                        </ul>
                    </li>'''
content = content.replace(broken_html, fixed_html)

auth_buttons_old = '''                <li class="nav-item ms-lg-3 mt-2 mt-lg-0">
                    {% if 'maND' in session %}
                        <div class="dropdown">
                            <button class="btn btn-warning fw-bold px-4 rounded-pill dropdown-toggle" type="button" data-bs-toggle="dropdown">
                                <i class="fa-solid fa-user me-1"></i> {{ _('hello') }}, {{ session['tenDangNhap'] }}
                            </button>
                            <ul class="dropdown-menu dropdown-menu-end">
                                {% if session.get('is_admin') %}
                                <li><a class="dropdown-item fw-bold text-gold" href="/quan-tri"><i class="fa-solid fa-gauge-high me-2"></i>Vào Trang Quản Trị</a></li>
                                {% else %}
                                <li><a class="dropdown-item" href="/lich-su-dat-phong"><i class="fa-solid fa-clock-rotate-left me-2"></i>{{ _('history') }}</a></li>
                                {% endif %}
                                <li><hr class="dropdown-divider"></li>
                                <li><a class="dropdown-item text-danger" href="/dang-xuat"><i class="fa-solid fa-right-from-bracket me-2"></i>{{ _('logout') }}</a></li>
                            </ul>
                        </div>
                    {% else %}
                        <a class="btn btn-outline-warning fw-bold px-3 rounded-pill me-2" href="/dang-ky"><i class="fa-solid fa-user-plus me-1"></i> {{ _('register') }}</a>
                        <a class="btn btn-warning fw-bold px-4 rounded-pill" href="/dang-nhap"><i class="fa-solid fa-user me-1"></i> {{ _('login') }}</a>
                    {% endif %}
                </li>'''

auth_buttons_new = '''                    {% if 'maND' in session %}
                    <li class="nav-item dropdown ms-lg-3 mt-2 mt-lg-0">
                        <a class="btn btn-gold dropdown-toggle" href="#" data-bs-toggle="dropdown">
                            <i class="fa-solid fa-user me-1"></i> Xin chào, {{ session['tenDangNhap'] }}
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end border-0 shadow rounded-0">
                            {% if session.get('is_admin') %}
                            <li><a class="dropdown-item fw-bold text-gold" href="/quan-tri">VÀO TRANG QUẢN TRỊ</a></li>
                            {% else %}
                            <li><a class="dropdown-item" href="/lich-su-dat-phong">{{ _('history')|upper }}</a></li>
                            {% endif %}
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item text-danger" href="/dang-xuat">{{ _('logout')|upper }}</a></li>
                        </ul>
                    </li>
                    {% else %}
                    <li class="nav-item ms-lg-3 mt-2 mt-lg-0">
                        <a class="btn btn-outline-light me-2 rounded-0 px-4" href="/dang-ky" style="font-size: 0.85rem; letter-spacing: 1px;">{{ _('register')|upper }}</a>
                        <a class="btn btn-gold px-4" href="/dang-nhap">{{ _('login')|upper }}</a>
                    </li>
                    {% endif %}'''
content = content.replace(auth_buttons_old, auth_buttons_new)

with open('d:/DAN/eapp/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed layout in base.html")
