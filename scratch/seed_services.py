import sys
sys.path.insert(0, 'd:/DAN')
from eapp import app, db
from eapp.models import DichVu

services_data = [
    {"maDV": "DV_NUOC_LAVIE", "tenDV": "Nước khoáng Lavie", "donViTinh": "Chai", "donGia": 15000, "moTa": "Nước khoáng thiên nhiên 500ml"},
    {"maDV": "DV_NUOC_COCA", "tenDV": "Nước ngọt Coca Cola", "donViTinh": "Lon", "donGia": 20000, "moTa": "Lon 320ml ướp lạnh"},
    {"maDV": "DV_BIA_HEINEKEN", "tenDV": "Bia Heineken", "donViTinh": "Lon", "donGia": 35000, "moTa": "Lon 330ml ướp lạnh"},
    {"maDV": "DV_BIA_TIGER", "tenDV": "Bia Tiger", "donViTinh": "Lon", "donGia": 30000, "moTa": "Lon 330ml ướp lạnh"},
    {"maDV": "DV_MI_OMACHI", "tenDV": "Mì ly Omachi", "donViTinh": "Ly", "donGia": 25000, "moTa": "Mì tôm ly ăn liền"},
    {"maDV": "DV_GIAT_UI", "tenDV": "Dịch vụ Giặt ủi", "donViTinh": "Kg", "donGia": 30000, "moTa": "Giặt ủi sấy khô giao trong ngày"},
    {"maDV": "DV_BUFFET", "tenDV": "Ăn sáng Buffet", "donViTinh": "Vé", "donGia": 150000, "moTa": "Vé ăn sáng tại nhà hàng tầng trệt"},
    {"maDV": "DV_XE_SANBAY", "tenDV": "Xe đưa đón sân bay", "donViTinh": "Lượt", "donGia": 350000, "moTa": "Xe 4 chỗ đưa đón sân bay 1 chiều"},
    {"maDV": "DV_MASSAGE", "tenDV": "Massage Body 60p", "donViTinh": "Vé", "donGia": 450000, "moTa": "Vé massage thư giãn 60 phút tại Spa"},
    {"maDV": "DV_RUOU_VANG", "tenDV": "Rượu vang đỏ Đà Lạt", "donViTinh": "Chai", "donGia": 350000, "moTa": "Chai 750ml cao cấp"},
    {"maDV": "DV_THUE_XE", "tenDV": "Thuê xe máy", "donViTinh": "Ngày", "donGia": 150000, "moTa": "Cho thuê xe tay ga Honda Airblade/Vision"},
    {"maDV": "DV_SNACK", "tenDV": "Snack khoai tây Lay's", "donViTinh": "Gói", "donGia": 25000, "moTa": "Snack gói lớn"}
]

with app.app_context():
    for item in services_data:
        # Check if already exists
        exist = DichVu.query.filter_by(maDV=item["maDV"]).first()
        if not exist:
            dv = DichVu(
                maDV=item["maDV"],
                tenDV=item["tenDV"],
                donViTinh=item["donViTinh"],
                donGia=item["donGia"],
                moTa=item["moTa"],
                trangThai=True
            )
            db.session.add(dv)
    
    db.session.commit()
    print("Seeded services successfully!")
