import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('d:/DAN/eapp/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()
idx1 = content.find('    # XỬ LÝ KHI BẤM NÚT')
print(content[idx1:idx1+2000])
