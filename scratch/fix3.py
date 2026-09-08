with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find("@app.route('/xuat-hoa-don-csv')")
if idx != -1:
    end_idx = content.find('filename=danh_sach_hoa_don.csv"})', idx)
    if end_idx != -1:
        end_idx += len('filename=danh_sach_hoa_don.csv"})')
        content = content[:end_idx] + '\n'
        with open('d:/DAN/eapp/admin.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Truncated successfully.')
