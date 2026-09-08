import re

with open('d:/DAN/eapp/templates/quan_ly_nhan_su.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract from <thead to </tbody>
start_idx = content.find('<thead')
end_idx = content.find('</tbody>') + len('</tbody>')

old_table = content[start_idx:end_idx]

new_table = '''<thead class="table-dark text-nowrap">
                            <tr>
                                <th>Nhân Viên</th>
                                <th>Liên Hệ</th>
                                <th>Tài Khoản & Công Việc</th>
                                <th class="text-center">Thao Tác</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for nv, nd in danh_sach_nhan_vien %}
                            <tr>
                                <td>
                                    <div class="fw-bold text-dark fs-6">{{ nv.hoTen }} <span class="badge bg-secondary ms-1" style="font-size: 0.7rem;">{{ nv.maNV }}</span></div>
                                    <div class="small text-muted mt-1">
                                        {% if nv.gioiTinh == 'Nam' %}<i class="fa-solid fa-mars text-primary"></i> Nam{% elif nv.gioiTinh == 'Nữ' %}<i class="fa-solid fa-venus text-danger"></i> Nữ{% else %}{{ nv.gioiTinh or 'Chưa rõ' }}{% endif %}
                                        <span class="mx-1">&bull;</span> <i class="fa-regular fa-calendar text-muted"></i> {{ nv.ngaySinh.strftime('%d/%m/%Y') if nv.ngaySinh else '---' }}
                                    </div>
                                </td>
                                <td>
                                    <div class="small text-dark mb-1"><i class="fa-solid fa-phone me-2 text-muted"></i>{{ nv.sdt or '---' }}</div>
                                    <div class="small text-dark mb-1"><i class="fa-solid fa-id-card me-2 text-muted"></i>{{ nv.cccd or '---' }}</div>
                                    <div class="small text-dark text-truncate" style="max-width: 250px;" title="{{ nv.diaChi or '' }}"><i class="fa-solid fa-location-dot me-2 text-muted"></i>{{ nv.diaChi or '---' }}</div>
                                </td>
                                <td>
                                    <div class="small text-dark mb-1"><i class="fa-solid fa-user-shield me-2 text-muted"></i><span class="fw-bold">{{ nd.tenDangNhap }}</span></div>
                                    <div class="small text-dark mb-2"><i class="fa-solid fa-briefcase me-2 text-muted"></i>{{ nv.chucVu or '---' }} (Vào làm: {{ nv.ngayVaoLam.strftime('%d/%m/%Y') if nv.ngayVaoLam else '---' }})</div>
                                    <div>
                                        {% if nd.maVaiTro == 'ADMIN' %}
                                            <span class="badge bg-danger text-uppercase" style="letter-spacing: 1px;">Quản Trị Viên</span>
                                        {% else %}
                                            <span class="badge bg-secondary text-uppercase" style="letter-spacing: 1px;">Nhân Viên</span>
                                        {% endif %}
                                    </div>
                                </td>
                                <td class="text-center align-middle">
                                    {% if nd.tenDangNhap != 'admin' %}
                                    <a href="/quan-ly-nhan-su/xoa/{{ nv.maNV }}" class="btn btn-sm rounded-0 btn-outline-danger" onclick="return confirm('Khóa và xóa tài khoản này?')">
                                        <i class="fa-solid fa-trash"></i> Xóa
                                    </a>
                                    {% else %}
                                    <span class="badge border border-secondary text-secondary">Tài khoản gốc</span>
                                    {% endif %}
                                </td>
                            </tr>
                            {% else %}
                            <tr>
                                <td colspan="4" class="text-center py-5 text-muted">
                                    <i class="fa-solid fa-folder-open fs-1 mb-3 opacity-25"></i>
                                    <br>Chưa có nhân viên nào.
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>'''

content = content.replace(old_table, new_table)

with open('d:/DAN/eapp/templates/quan_ly_nhan_su.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated table layout")
