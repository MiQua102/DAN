def dinh_dang_tien(so_tien):
    if not so_tien:
        return "0 ₫"
    return "{:,.0f} ₫".format(so_tien)