import re

with open('d:/DAN/eapp/templates/quan_ly_nhan_su.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_thead = '''                        <thead class="table-dark">
                            <tr>
                                <th>Mã NV</th>
                                <th>Tên Đăng Nhập</th>
                                <th>Họ Tên</th>
                                <th>Chức Vụ</th>
                                <th>Phân Quyền</th>
                                <th class="text-center">Thao Tác</th>
                            </tr>
                        </thead>'''

new_thead = '''                        <thead class="table-dark text-nowrap">
                            <tr>
                                <th>Mã NV</th>
                                <th>Tên Đăng Nhập</th>
                                <th>Họ Tên</th>
                                <th>Giới Tính</th>
                                <th>Ngày Sinh</th>
                                <th>SĐT</th>
                                <th>CCCD</th>
                                <th>Địa Chỉ</th>
                                <th>Ngày Vào Làm</th>
                                <th>Chức Vụ</th>
                                <th>Phân Quyền</th>
                                <th class="text-center">Thao Tác</th>
                            </tr>
                        </thead>'''

content = content.replace(old_thead, new_thead)

old_tbody = '''                        <tbody>
                            {% for nv, nd in danh_sach_nhan_vien %}
                            <tr>
                                <td class="fw-bold">{{ nv.maNV }}</td>
                                <td>{{ nd.tenDangNhap }}</td>
                                <td>{{ nv.hoTen }}</td>
                                <td>{{ nv.chucVu }}</td>
                                <td>
                                    {% if nd.maVaiTro == 'ADMIN' %}
                                        <span class="badge bg-danger">Quản Trị Viên</span>
                                    {% else %}
                                        <span class="badge bg-primary">Nhân Viên (Lễ Tân)</span>
                                    {% endif %}
                                </td>
                                <td class="text-center">'''

new_tbody = '''                        <tbody>
                            {% for nv, nd in danh_sach_nhan_vien %}
                            <tr>
                                <td class="fw-bold">{{ nv.maNV }}</td>
                                <td>{{ nd.tenDangNhap }}</td>
                                <td class="fw-bold text-dark">{{ nv.hoTen }}</td>
                                <td>
                                    {% if nv.gioiTinh == 'Nam' %}<i class="fa-solid fa-mars text-primary me-1"></i>Nam
                                    {% elif nv.gioiTinh == 'Nữ' %}<i class="fa-solid fa-venus text-danger me-1"></i>Nữ
                                    {% else %}{{ nv.gioiTinh }}{% endif %}
                                </td>
                                <td>{{ nv.ngaySinh.strftime('%d/%m/%Y') if nv.ngaySinh else '' }}</td>
                                <td>{{ nv.sdt or '' }}</td>
                                <td>{{ nv.cccd or '' }}</td>
                                <td style="max-width: 200px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="{{ nv.diaChi }}">{{ nv.diaChi or '' }}</td>
                                <td>{{ nv.ngayVaoLam.strftime('%d/%m/%Y') if nv.ngayVaoLam else '' }}</td>
                                <td>{{ nv.chucVu or '' }}</td>
                                <td>
                                    {% if nd.maVaiTro == 'ADMIN' %}
                                        <span class="badge bg-danger">Quản Trị Viên</span>
                                    {% else %}
                                        <span class="badge bg-secondary">Nhân Viên</span>
                                    {% endif %}
                                </td>
                                <td class="text-center text-nowrap">'''

content = content.replace(old_tbody, new_tbody)

# Make sure table is wrapped in table-responsive
if 'class="table-responsive"' not in content:
    content = content.replace('<table class="table', '<div class="table-responsive">\n<table class="table')
    content = content.replace('</table>\n                    </div>\n                </div>', '</table>\n</div>\n                    </div>\n                </div>')

with open('d:/DAN/eapp/templates/quan_ly_nhan_su.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated quan_ly_nhan_su.html with full personal info")
