# BÁO CÁO ĐỒ ÁN CHUYÊN NGÀNH CNTT

**ĐỀ TÀI: XÂY DỰNG HỆ THỐNG QUẢN LÝ VÀ ĐẶT PHÒNG KHÁCH SẠN TRỰC TUYẾN**

**Trường Đại Học Mở Thành Phố Hồ Chí Minh**
**Khoa Công Nghệ Thông Tin**

---

## MỤC LỤC

[LỜI CẢM ƠN](#lời-cảm-ơn)
[DANH MỤC HÌNH ẢNH](#danh-mục-hình-ảnh)
[DANH MỤC BẢNG BIỂU](#danh-mục-bảng-biểu)
[DANH MỤC TỪ VIẾT TẮT](#danh-mục-từ-viết-tắt)

**[CHƯƠNG 1: GIỚI THIỆU](#chương-1-giới-thiệu)**
1.1 [Bối cảnh và vấn đề](#11-bối-cảnh-và-vấn-đề)
1.2 [Mục tiêu đề tài](#12-mục-tiêu-đề-tài)
1.3 [Đối tượng và phạm vi](#13-đối-tượng-và-phạm-vi)
1.4 [Phương pháp thực hiện](#14-phương-pháp-thực-hiện)
1.5 [Bố cục báo cáo](#15-bố-cục-báo-cáo)

**[CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ SỬ DỤNG](#chương-2-cơ-sở-lý-thuyết-và-công-nghệ-sử-dụng)**
2.1 [Tổng quan về hệ thống quản lý và đặt phòng khách sạn trực tuyến](#21-tổng-quan-về-hệ-thống-quản-lý-và-đặt-phòng-khách-sạn-trực-tuyến)
2.2 [Cơ sở lý thuyết về cơ sở dữ liệu](#22-cơ-sở-lý-thuyết-về-cơ-sở-dữ-liệu)
2.3 [Các mô hình sử dụng trong phân tích và thiết kế](#23-các-mô-hình-sử-dụng-trong-phân-tích-và-thiết-kế)
2.4 [Công nghệ sử dụng](#24-công-nghệ-sử-dụng)
2.5 [Vai trò của các công nghệ trong đồ án](#25-vai-trò-của-các-công-nghệ-trong-đồ-án)
2.6 [Lý do lựa chọn Flask và MySQL](#26-lý-do-lựa-chọn-flask-và-mysql)

**[CHƯƠNG 3: PHÂN TÍCH, THIẾT KẾ VÀ XÂY DỰNG HỆ THỐNG](#chương-3-phân-tích-thiết-kế-và-xây-dựng-hệ-thống)**
3.1 [Giới thiệu hệ thống](#31-giới-thiệu-hệ-thống)
3.2 [Khảo sát và phân tích yêu cầu](#32-khảo-sát-và-phân-tích-yêu-cầu)
3.3 [Kiến trúc hệ thống](#33-kiến-trúc-hệ-thống)
3.4 [Phân tích Use Case hệ thống](#34-phân-tích-use-case-hệ-thống)
3.5 [Thiết kế cơ sở dữ liệu](#35-thiết-kế-cơ-sở-dữ-liệu)
3.6 [Thiết kế giao diện](#36-thiết-kế-giao-diện)

**[CHƯƠNG 4: HIỆN THỰC VÀ KIỂM THỬ](#chương-4-hiện-thực-và-kiểm-thử)**
4.1 [Môi trường phát triển và triển khai](#41-môi-trường-phát-triển-và-triển-khai)
4.2 [Cấu trúc mã nguồn dự án](#42-cấu-trúc-mã-nguồn-dự-án)
4.3 [Chi tiết hiện thực từng module](#43-chi-tiết-hiện-thực-từng-module)
4.4 [Giao diện và chức năng cốt lõi](#44-giao-diện-và-chức-năng-cốt-lõi)
4.5 [Kiểm thử (Testing)](#45-kiểm-thử-testing)

**[CHƯƠNG 5: KẾT QUẢ, ĐÁNH GIÁ VÀ KẾT LUẬN](#chương-5-kết-quả-đánh-giá-và-kết-luận)**
5.1 [Kết quả đạt được](#51-kết-quả-đạt-được)
5.2 [Bàn luận và Đánh giá](#52-bàn-luận-và-đánh-giá)
5.3 [Hạn chế và hướng phát triển](#53-hạn-chế-và-hướng-phát-triển)

[TÀI LIỆU THAM KHẢO](#tài-liệu-tham-khảo)
[PHỤ LỤC](#phụ-lục)

---

## LỜI CẢM ƠN

Nhóm sinh viên xin gửi lời cảm ơn chân thành đến giảng viên hướng dẫn đã tận tình hỗ trợ, định hướng và cung cấp những kiến thức quý báu giúp chúng em hoàn thành đồ án này. Xin cảm ơn Khoa Công nghệ Thông tin, Trường Đại học Mở TP.HCM đã tạo môi trường học tập và nghiên cứu tốt nhất.

Chúng em cũng xin gửi lời tri ân đến gia đình, bạn bè và các thầy cô đã luôn động viên, hỗ trợ trong suốt quá trình thực hiện đồ án.

---

## DANH MỤC HÌNH ẢNH

| STT | Hình | Mô tả |
|-----|------|-------|
| 1 | Hình 2.1 | Kiến trúc tổng quan Flask Framework |
| 2 | Hình 2.2 | Luồng hoạt động ORM SQLAlchemy |
| 3 | Hình 2.3 | Quy trình thanh toán MoMo API |
| 4 | Hình 3.1 | Sơ đồ Use Case tổng quát |
| 5 | Hình 3.2 | Sơ đồ kiến trúc MVC |
| 6 | Hình 3.3 | Sơ đồ ERD Cơ sở dữ liệu |
| 7 | Hình 3.4 | Sơ đồ hoạt động Đặt phòng |
| 8 | Hình 3.5 | Sơ đồ hoạt động Thanh toán MoMo |
| 9 | Hình 4.1 | Giao diện Trang chủ |
| 10 | Hình 4.2 | Giao diện Chi tiết phòng |
| 11 | Hình 4.3 | Giao diện Đặt phòng |
| 12 | Hình 4.4 | Giao diện Thanh toán MoMo |
| 13 | Hình 4.5 | Giao diện Trang Quản trị (Dashboard) |
| 14 | Hình 4.6 | Giao diện Quản lý Đặt phòng |
| 15 | Hình 4.7 | Giao diện Lập Hóa đơn và Thanh toán |

---

## DANH MỤC BẢNG BIỂU

| STT | Bảng | Mô tả |
|-----|------|-------|
| 1 | Bảng 2.1 | Tổng hợp công nghệ sử dụng trong dự án |
| 2 | Bảng 3.1 | Yêu cầu chức năng phía Khách hàng |
| 3 | Bảng 3.2 | Yêu cầu chức năng phía Quản trị |
| 4 | Bảng 3.3 | Danh sách các bảng trong CSDL |
| 5 | Bảng 3.4 | Chi tiết bảng NguoiDung |
| 6 | Bảng 3.5 | Chi tiết bảng DatPhong |
| 7 | Bảng 4.1 | Cấu trúc thư mục mã nguồn |
| 8 | Bảng 4.2 | Danh sách các route chính |
| 9 | Bảng 4.3 | Bảng kiểm thử chức năng (Test Cases) |

---

## DANH MỤC TỪ VIẾT TẮT

| Viết tắt | Nghĩa đầy đủ |
|----------|--------------|
| **CNTT** | Công nghệ thông tin |
| **CSDL** | Cơ sở dữ liệu |
| **ERD** | Entity-Relationship Diagram (Sơ đồ thực thể - mối kết hợp) |
| **API** | Application Programming Interface (Giao diện lập trình ứng dụng) |
| **ORM** | Object-Relational Mapping (Ánh xạ đối tượng - quan hệ) |
| **MVC** | Model - View - Controller |
| **CRUD** | Create - Read - Update - Delete |
| **HMAC** | Hash-based Message Authentication Code |
| **SHA-256** | Secure Hash Algorithm 256-bit |
| **SMTP** | Simple Mail Transfer Protocol |
| **REST** | Representational State Transfer |
| **UUID** | Universally Unique Identifier |
| **QR Code** | Quick Response Code |
| **CSS** | Cascading Style Sheets |
| **HTML** | HyperText Markup Language |
| **I18N** | Internationalization (Đa ngôn ngữ) |

---

## CHƯƠNG 1: GIỚI THIỆU

### 1.1 Bối cảnh và vấn đề

Ngành công nghiệp khách sạn và du lịch đang ngày càng phát triển mạnh mẽ, đặc biệt tại Việt Nam — một trong những quốc gia có tốc độ tăng trưởng du lịch nhanh nhất khu vực Đông Nam Á. Theo Tổng cục Du lịch Việt Nam, lượng khách du lịch quốc tế và nội địa tăng đều qua các năm, kéo theo nhu cầu lưu trú và đặt phòng trực tuyến tăng cao.

Tuy nhiên, nhiều khách sạn quy mô vừa và nhỏ tại Việt Nam vẫn đang quản lý phòng, dịch vụ và khách hàng thông qua sổ sách giấy hoặc các phần mềm rời rạc, không đồng bộ. Điều này dẫn đến hàng loạt vấn đề:

- **Khó khăn trong tra cứu**: Nhân viên mất nhiều thời gian tìm kiếm thông tin phòng trống, lịch sử đặt phòng.
- **Dễ sai sót**: Đặt phòng trùng lặp (overbooking), tính sai hóa đơn, bỏ sót dịch vụ phát sinh.
- **Trải nghiệm khách hàng kém**: Khách không thể xem phòng, so sánh giá hay đặt phòng trước từ xa.
- **Thiếu công cụ thống kê**: Quản lý không nắm được doanh thu theo thời gian thực, không có biểu đồ phân tích kinh doanh.

Xuất phát từ những vấn đề thực tiễn trên, nhóm sinh viên đề xuất xây dựng **Hệ thống Quản lý và Đặt phòng Khách sạn Trực tuyến** — một giải pháp phần mềm toàn diện, tích hợp đặt phòng, thanh toán điện tử, quản lý dịch vụ và thống kê doanh thu trên một nền tảng duy nhất.

### 1.2 Mục tiêu đề tài

Đề tài nhằm xây dựng một **Hệ thống Quản lý và Đặt phòng Khách sạn Trực tuyến** hoàn chỉnh, đáp ứng các mục tiêu cụ thể sau:

1. **Xây dựng giao diện web cho khách hàng** dễ dàng tìm kiếm phòng (lọc theo ngày, sức chứa, mức giá), xem chi tiết thông tin phòng cùng tiện nghi, và đặt phòng trực tuyến.
2. **Tích hợp cổng thanh toán trực tuyến MoMo** để khách hàng có thể đặt cọc 50% giá trị đơn phòng một cách tiện lợi, bảo mật qua giao thức HMAC-SHA256.
3. **Xây dựng trang quản trị (Admin Dashboard)** dành cho nhân viên và quản lý để kiểm soát lượng phòng trống, xác nhận/hủy đơn đặt phòng, lập hóa đơn tại quầy, và theo dõi biểu đồ doanh thu theo tháng.
4. **Quản lý toàn diện dữ liệu**: Khách hàng, Nhân viên (phân quyền ADMIN/STAFF), Loại Phòng, Phòng cụ thể, Tiện nghi, Dịch vụ phát sinh, Khuyến mãi (Voucher), Hóa đơn, Thanh toán và Đánh giá (Review 1-5 sao).
5. **Gửi email xác nhận kèm mã QR Code** tự động cho khách hàng sau khi đặt phòng thành công.
6. **Hỗ trợ đa ngôn ngữ** Tiếng Việt / English (I18N) để phục vụ cả khách quốc tế.

### 1.3 Đối tượng và phạm vi

#### 1.3.1 Đối tượng sử dụng

Hệ thống phục vụ **ba nhóm đối tượng** chính, mỗi nhóm có vai trò, quyền hạn và nhu cầu sử dụng khác nhau:

**a) Khách hàng (Customer)**

| Tiêu chí | Mô tả |
|----------|-------|
| **Đối tượng cụ thể** | Khách du lịch trong nước và quốc tế, khách công tác, gia đình có nhu cầu lưu trú ngắn/dài hạn |
| **Trình độ CNTT** | Người dùng phổ thông, quen thuộc với thao tác web cơ bản (đăng ký, đăng nhập, điền form) |
| **Nhu cầu chính** | Tìm kiếm phòng phù hợp, so sánh giá, xem tiện nghi, đặt phòng nhanh chóng, thanh toán trực tuyến |
| **Quyền hạn trên hệ thống** | Đăng ký/Đăng nhập tài khoản; Tìm kiếm và lọc phòng trống; Xem chi tiết loại phòng và tiện nghi; Đặt phòng trực tuyến; Áp dụng mã khuyến mãi (Voucher); Thanh toán đặt cọc 50% qua MoMo; Xem lịch sử đặt phòng cá nhân; Hủy phòng (trước 24 giờ); Gọi dịch vụ phát sinh (minibar, spa, giặt ủi...); Xem hóa đơn của chính mình; Viết đánh giá (Review 1-5 sao); Chuyển đổi ngôn ngữ Tiếng Việt / Tiếng Anh |
| **Thiết bị truy cập** | Máy tính để bàn, laptop, tablet, điện thoại thông minh (giao diện responsive) |

**b) Nhân viên lễ tân (Staff)**

| Tiêu chí | Mô tả |
|----------|-------|
| **Đối tượng cụ thể** | Nhân viên lễ tân, nhân viên tiếp nhận đặt phòng, nhân viên chăm sóc khách hàng tại khách sạn |
| **Trình độ CNTT** | Đã được đào tạo sử dụng phần mềm nghiệp vụ, thao tác thành thạo trên máy tính |
| **Nhu cầu chính** | Theo dõi trạng thái phòng theo thời gian thực, xử lý đơn đặt phòng, lập hóa đơn thanh toán tại quầy, ghi nhận dịch vụ phát sinh |
| **Quyền hạn trên hệ thống** | Xem Dashboard tổng quan (thống kê phòng, doanh thu); Xem danh sách Loại phòng, Phòng, Dịch vụ, Khách hàng; Quản lý đơn đặt phòng (xem, tìm kiếm, cập nhật trạng thái); Lập hóa đơn và thanh toán tại quầy; Xem và xuất báo cáo hóa đơn CSV; Quản lý mã khuyến mãi (chỉ xem) |
| **Hạn chế quyền** | Không được thêm/sửa/xóa loại phòng, phòng, dịch vụ; Không quản lý nhân sự; Không xóa khách hàng |

**c) Quản trị viên (Admin)**

| Tiêu chí | Mô tả |
|----------|-------|
| **Đối tượng cụ thể** | Quản lý khách sạn, chủ khách sạn, trưởng bộ phận lễ tân |
| **Trình độ CNTT** | Thành thạo sử dụng phần mềm, có khả năng quản lý hệ thống và phân tích dữ liệu |
| **Nhu cầu chính** | Quản lý toàn bộ hoạt động kinh doanh khách sạn, theo dõi doanh thu, quản lý nhân sự, cấu hình hệ thống |
| **Quyền hạn trên hệ thống** | Toàn bộ quyền của Nhân viên lễ tân; Thêm / Sửa / Xóa loại phòng (CRUD); Thêm / Sửa / Xóa phòng cụ thể (CRUD); Thêm / Sửa / Xóa dịch vụ (CRUD); Quản lý tài khoản nhân viên (thêm/xóa, phân quyền ADMIN/STAFF); Quản lý khách hàng (xem/xóa tài khoản); Quản lý mã khuyến mãi (thêm/xóa/bật-tắt trạng thái); Xem biểu đồ doanh thu theo 12 tháng (Chart.js) |

#### 1.3.2 Phạm vi đề tài

**a) Phạm vi chức năng**

*Phía Khách hàng:*
- **Quản lý tài khoản**: Đăng ký tài khoản mới (username, email, mật khẩu, họ tên, SĐT, CCCD), đăng nhập bằng username + password (mã hóa hash), đăng xuất (xóa session).
- **Tìm kiếm và Lọc phòng**: Lọc theo từ khóa tên phòng, sức chứa tối thiểu, mức giá tối đa, khoảng ngày nhận-trả (thuật toán Overlap Detection kiểm tra trùng lịch).
- **Đặt phòng trực tuyến**: Chọn loại phòng → nhập ngày nhận/trả và số khách → hệ thống tự động tìm phòng trống → tạo đơn đặt phòng → gửi email xác nhận kèm mã QR Code.
- **Khuyến mãi và Thanh toán**: Áp dụng mã giảm giá (Voucher) khi đặt phòng; đặt cọc 50% giá trị đơn phòng qua cổng thanh toán **MoMo** (chữ ký HMAC-SHA256).
- **Quản lý đơn đặt**: Xem lịch sử đặt phòng cá nhân, hủy phòng (quy tắc: chỉ hủy trước ngày nhận tối thiểu 24 giờ).
- **Dịch vụ phát sinh**: Gọi thêm dịch vụ minibar, spa, giặt ủi, thuê xe... từ danh sách dịch vụ đang kinh doanh.
- **Hóa đơn và Đánh giá**: Xem chi tiết hóa đơn (có kiểm tra bảo mật quyền sở hữu); viết đánh giá 1-5 sao kèm bình luận sau khi trả phòng (mỗi đơn chỉ 1 lần).
- **Đa ngôn ngữ**: Chuyển đổi giao diện Tiếng Việt ↔ Tiếng Anh, tự động chuyển đổi đơn vị tiền tệ VND ↔ USD.

*Phía Quản trị (Admin/Staff):*
- **Dashboard tổng quan**: Thống kê số phòng trống / đang thuê / cần dọn, doanh thu hôm nay, biểu đồ doanh thu 12 tháng (Chart.js).
- **Quản lý danh mục**: CRUD Loại phòng, Phòng cụ thể, Dịch vụ bổ sung, Mã khuyến mãi (chỉ Admin).
- **Quản lý đặt phòng**: Tìm kiếm theo mã đơn / tên khách / SĐT; cập nhật trạng thái đơn (Chờ nhận → Đang thuê → Đã trả / Đã hủy); tự động trả phòng về trạng thái "Trống" khi trả phòng hoặc hủy.
- **Quản lý người dùng**: Xem / xóa tài khoản khách hàng; thêm / xóa nhân viên với phân quyền ADMIN hoặc STAFF; bảo vệ tài khoản admin gốc.
- **Lập Hóa đơn và Thanh toán tại quầy**: Tính tự động tiền phòng + dịch vụ − giảm giá − đã cọc → tạo `HoaDon` + `ThanhToan`.
- **Xuất báo cáo**: Tải xuống danh sách hóa đơn dạng CSV tương thích Excel (UTF-8 BOM).

*Ngoài phạm vi chức năng:*

| Module / Tính năng | Lý do loại trừ |
|-------------------|----------------|
| Quản lý kho vật tư, chấm công, bảng lương | Thuộc nghiệp vụ hậu cần / nhân sự chuyên sâu, vượt quy mô đề tài |
| Tích hợp OTA (Booking.com, Agoda) và PMS bên thứ ba | Yêu cầu Channel Manager và API license chi phí cao |
| Ứng dụng Mobile native (iOS/Android) | Chỉ tập trung vào nền tảng Web responsive |
| Real-time Notification, AI gợi ý phòng | Dự kiến phát triển ở giai đoạn tương lai |
| Nhiều cổng thanh toán (VNPay, ZaloPay, thẻ quốc tế) | Chỉ tích hợp MoMo trong phạm vi đồ án |

**b) Phạm vi kỹ thuật**

- **Back-end**: Python 3.10+ với web framework Flask 3.0.2, WSGI toolkit Werkzeug 3.0.1.
- **ORM**: SQLAlchemy 2.0.25 + Flask-SQLAlchemy 3.1.1, kết nối MySQL qua driver PyMySQL 1.1.0.
- **CSDL**: MySQL 8.0 (Host: `127.0.0.1`, Port: `3307`, Database: `hoteldb`).
- **Front-end**: HTML5 / CSS3 / JavaScript, Bootstrap 5 (responsive), Chart.js (biểu đồ doanh thu).
- **Template Engine**: Jinja2 (tích hợp Flask) — render 28 trang HTML động, kế thừa 2 layout (`base.html` cho Client, `base_admin.html` cho Admin).
- **Tích hợp bên ngoài**: MoMo Payment Gateway API v2 (môi trường test, chữ ký HMAC-SHA256); Email HTML + QR Code (thư viện `qrcode`, SMTP mock trong development).
- **Bảo mật**: Mã hóa mật khẩu scrypt/pbkdf2 (Werkzeug); phân quyền ADMIN/STAFF qua session; kiểm tra quyền sở hữu đơn đặt phòng.
- **Đa ngôn ngữ (I18N)**: Tự xây dựng module `translations.py` hỗ trợ Tiếng Việt / Tiếng Anh (80+ key dịch, format tiền tệ VND/USD).
- **Triển khai**: Máy chủ cục bộ (localhost), Flask development server, chế độ debug.

**c) Phạm vi dữ liệu**

Dữ liệu sử dụng trong đề tài là dữ liệu mẫu do người thực hiện xây dựng để phục vụ quá trình phát triển và kiểm thử hệ thống. Dữ liệu bao gồm:

- Tài khoản quản trị viên, nhân viên và khách hàng.
- Thông tin loại phòng và phòng cụ thể.
- Giá phòng, sức chứa, diện tích và tiện nghi.
- Thông tin đơn đặt phòng và chi tiết đặt phòng.
- Danh mục dịch vụ và thông tin sử dụng dịch vụ.
- Mã khuyến mãi (Voucher) và thông tin áp dụng giảm giá.
- Hóa đơn, thanh toán và dữ liệu doanh thu.
- Đánh giá (Review) của khách hàng.

Dữ liệu không được lấy trực tiếp từ Booking.com, Agoda hoặc Traveloka và không phải dữ liệu hoạt động thực tế của một khách sạn. Những thông tin cá nhân dùng để kiểm thử là dữ liệu giả lập, không sử dụng thông tin nhạy cảm của người dùng thật. Số lượng dữ liệu được xây dựng ở mức phù hợp để kiểm tra chức năng, ràng buộc toàn vẹn, xử lý đặt phòng trùng lịch và thực hiện các truy vấn thống kê cơ bản.

### 1.4 Phương pháp thực hiện

Đề tài tiếp cận theo phương pháp **phát triển phần mềm hướng đối tượng (OOP)** kết hợp mô hình kiến trúc **MVC (Model - View - Controller)**, thực hiện qua các bước:

```
Khảo sát thực tế
    → Phân tích yêu cầu (Chức năng & Phi chức năng)
        → Thiết kế CSDL (ERD) & Kiến trúc phần mềm
            → Lập trình hiện thực (Flask + SQLAlchemy + Jinja2)
                → Tích hợp API bên ngoài (MoMo Payment, Email + QR Code)
                    → Kiểm thử (Unit Test & Manual Test)
                        → Triển khai & Viết báo cáo
```

### 1.5 Bố cục báo cáo

| Chương | Nội dung |
|--------|----------|
| **Chương 1** | Giới thiệu tổng quan về đề tài, bối cảnh, mục tiêu, đối tượng, phạm vi và phương pháp thực hiện |
| **Chương 2** | Trình bày cơ sở lý thuyết, **chi tiết từng công nghệ** sử dụng trong dự án, so sánh với hệ thống hiện có |
| **Chương 3** | Phân tích yêu cầu, thiết kế CSDL (ERD), kiến trúc phần mềm, sơ đồ Use Case và Activity Diagram |
| **Chương 4** | Hiện thực hóa hệ thống, mô tả chi tiết từng module mã nguồn, giao diện, và kiểm thử |
| **Chương 5** | Kết luận về kết quả đạt được, bàn luận, chỉ ra hạn chế và hướng phát triển tương lai |

---

## CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ SỬ DỤNG

Chương này trình bày nền tảng lý thuyết và bộ công cụ kỹ thuật phục vụ cho việc phân tích, thiết kế và hiện thực hệ thống. Nội dung được chia thành ba phần chính: phần đầu giới thiệu tổng quan về nghiệp vụ quản lý và đặt phòng khách sạn trực tuyến; phần thứ hai trình bày hệ thống kiến thức nền tảng về cơ sở dữ liệu quan hệ; phần cuối liệt kê và giải thích vai trò của từng công nghệ, thư viện và dịch vụ bên ngoài đã được áp dụng vào dự án.

### 2.1 Tổng quan về hệ thống quản lý và đặt phòng khách sạn trực tuyến

Trong bối cảnh chuyển đổi số, ngành khách sạn đang dần thay thế phương thức quản lý truyền thống bằng sổ sách bằng các giải pháp phần mềm tập trung. Một hệ thống quản lý và đặt phòng khách sạn trực tuyến cho phép khách hàng chủ động tra cứu thông tin phòng, thực hiện đặt chỗ và thanh toán từ xa, trong khi phía khách sạn có thể kiểm soát tình trạng phòng, theo dõi doanh thu và xử lý nghiệp vụ lưu trú thông qua một nền tảng web duy nhất.

So với cách vận hành thủ công, việc ứng dụng hệ thống phần mềm mang lại ba lợi ích cốt lõi. Thứ nhất, dữ liệu được tập trung tại một nguồn duy nhất, giảm tình trạng thất lạc hay trùng lặp thông tin. Thứ hai, các quy trình như kiểm tra phòng trống, tạo đơn đặt phòng và lập hóa đơn được tự động hóa, rút ngắn đáng kể thời gian xử lý. Thứ ba, quản lý có thể truy xuất báo cáo doanh thu, tỉ lệ lấp đầy phòng và phản hồi của khách hàng bất cứ lúc nào, giúp đưa ra quyết định kinh doanh kịp thời.

#### 2.1.1 Khái niệm hệ thống đặt phòng khách sạn trực tuyến

Xét về bản chất, hệ thống đặt phòng khách sạn trực tuyến là một ứng dụng phần mềm hoạt động trên nền tảng web, cho phép người dùng cuối — cụ thể là khách du lịch hoặc khách công tác — thực hiện việc tìm kiếm, so sánh và giữ chỗ phòng lưu trú mà không cần đến trực tiếp quầy lễ tân. Người dùng chỉ cần truy cập vào website, cung cấp thông tin về khoảng thời gian lưu trú mong muốn (ngày đến, ngày đi) cùng số lượng khách, và hệ thống sẽ đối chiếu lịch đặt hiện có để đưa ra danh sách những phòng thực sự còn khả dụng.

Trên thị trường hiện nay, mô hình đặt phòng trực tuyến tồn tại dưới hai dạng phổ biến. Dạng thứ nhất là các sàn trung gian (OTA — Online Travel Agency) như Booking.com, Agoda hay Traveloka, nơi nhiều khách sạn đăng ký bán phòng thông qua một nền tảng chung và phải trả phí hoa hồng cho mỗi giao dịch thành công. Dạng thứ hai là hệ thống tự vận hành (Self-hosted), trong đó mỗi khách sạn tự xây dựng hoặc mua phần mềm riêng để quản lý toàn bộ quy trình đặt phòng, sở hữu toàn bộ cơ sở dữ liệu khách hàng và không bị phụ thuộc vào bất kỳ bên thứ ba nào.

Đồ án này hướng đến mô hình Self-hosted: xây dựng một hệ thống web dành riêng cho một khách sạn đơn lẻ, hoạt động độc lập trên server riêng. Ba nhóm người dùng tham gia vào hệ thống bao gồm: khách hàng (tìm phòng, đặt chỗ, cọc tiền, đánh giá), nhân viên lễ tân (xác nhận đơn, ghi nhận dịch vụ, xuất hóa đơn) và quản trị viên (cấu hình danh mục phòng — dịch vụ, quản lý nhân sự, theo dõi doanh thu). Mỗi nhóm được gán quyền hạn riêng biệt nhằm đảm bảo an toàn dữ liệu và tránh xung đột thao tác.

#### 2.1.2 Quy trình tìm kiếm và đặt phòng

Quy trình đặt phòng là luồng nghiệp vụ trung tâm mà toàn bộ thiết kế hệ thống xoay quanh. Luồng này bắt đầu từ phía khách hàng và kết thúc khi đơn đặt phòng được tạo thành công trên hệ thống.

Khi truy cập trang chủ, khách hàng sẽ thấy danh sách các loại phòng đang kinh doanh, kèm thông tin tóm tắt như tên, ảnh đại diện, mức giá mỗi đêm, sức chứa tối đa và điểm đánh giá trung bình. Phía trên danh sách, hệ thống cung cấp bộ lọc đa tiêu chí cho phép khách thu hẹp kết quả: nhập từ khóa để tìm theo tên phòng, đặt ngưỡng sức chứa tối thiểu, giới hạn mức giá tối đa, hoặc chọn khoảng ngày nhận — trả phòng. Đáng chú ý, khi khách chọn khoảng ngày, hệ thống không chỉ kiểm tra trạng thái hiện tại của phòng mà còn truy vấn toàn bộ lịch sử đặt phòng trong CSDL để phát hiện xung đột thời gian. Thuật toán kiểm tra xung đột (Overlap Detection) hoạt động theo nguyên tắc: hai khoảng thời gian [A, B] và [C, D] bị trùng khi và chỉ khi A < D và C < B. Chỉ những phòng không xuất hiện trong bất kỳ đơn đặt nào vi phạm điều kiện trên mới được đưa vào kết quả trả về cho khách.

Sau khi chọn được loại phòng ưng ý, khách hàng nhấn vào xem chi tiết để tham khảo thêm mô tả, diện tích, danh sách tiện nghi đi kèm (WiFi, TV, điều hòa, két sắt…) và các bài đánh giá gần nhất từ khách trước đó. Nếu quyết định đặt, khách chuyển sang form đặt phòng, nơi cần nhập ngày nhận, ngày trả, số lượng khách và email liên hệ. Hệ thống còn cho phép nhập mã giảm giá (voucher) — một lệnh gọi AJAX sẽ được gửi tới API kiểm tra mã ngay trên form; nếu mã hợp lệ, phần trăm giảm giá sẽ được áp dụng tức thì và tổng tiền được cập nhật. Khi nhấn xác nhận, hệ thống thực hiện bốn bước liên tiếp trong cùng một giao dịch CSDL: (1) tìm phòng trống thuộc loại đã chọn, (2) tạo bản ghi DatPhong kèm ChiTietDatPhong, (3) đánh dấu phòng vật lý sang trạng thái "Đang thuê", (4) gửi email xác nhận chứa mã QR Code để khách mang theo khi nhận phòng.

Ngoài việc thanh toán tại quầy khi nhận phòng, khách hàng có thêm lựa chọn cọc trước 50% tổng giá trị đơn thông qua ví điện tử MoMo. Hệ thống sẽ tạo yêu cầu thanh toán, ký bằng HMAC-SHA256 rồi chuyển hướng khách sang trang thanh toán của MoMo. Sau khi giao dịch hoàn tất, MoMo gọi ngược về URL callback của hệ thống; nếu mã kết quả là 0 (thành công), trạng thái đơn tự động chuyển thành "Đã cọc (Online)" và một bản ghi thanh toán được lưu lại với đầy đủ mã giao dịch.

#### 2.1.3 Quy trình nhận phòng và trả phòng

Khi khách đến khách sạn vào ngày đã hẹn, nhân viên lễ tân mở trang quản trị, nhập mã đặt phòng hoặc tên khách vào ô tìm kiếm để tra cứu đơn. Nhân viên có thể xác minh nhanh bằng cách quét mã QR trên email xác nhận mà khách xuất trình. Sau khi xác nhận danh tính, nhân viên cập nhật trạng thái đơn sang "Đã nhận phòng"; hệ thống đồng thời ghi nhận mốc thời gian nhận phòng thực tế và đảm bảo phòng tương ứng vẫn ở trạng thái "Đang thuê".

Suốt thời gian lưu trú, khách có thể yêu cầu các dịch vụ bổ sung — ví dụ: đồ uống từ minibar, liệu trình spa, dịch vụ giặt ủi hay thuê xe đưa đón sân bay. Mỗi lần phát sinh, nhân viên tạo một bản ghi sử dụng dịch vụ trong hệ thống, ghi rõ tên dịch vụ, số lượng, đơn giá tại thời điểm sử dụng và thành tiền. Tất cả bản ghi này đều được gắn với mã chi tiết đặt phòng, đảm bảo khi lập hóa đơn cuối cùng sẽ không bỏ sót bất kỳ khoản nào.

Tại thời điểm trả phòng, nhân viên khởi tạo hóa đơn thanh toán. Hệ thống tự động tổng hợp chi phí theo bốn hạng mục: tiền phòng (đơn giá nhân số đêm thực tế), tiền dịch vụ phát sinh (cộng dồn toàn bộ lần sử dụng), khoản giảm giá (nếu khách đã áp voucher) và số tiền đã cọc trực tuyến (nếu có). Phần còn lại được thanh toán tại quầy bằng tiền mặt hoặc chuyển khoản. Khi nhân viên xác nhận thanh toán, hệ thống tạo bản ghi HoaDon liên kết với bản ghi ThanhToan, chuyển trạng thái đơn thành "Đã trả phòng" và đổi trạng thái phòng vật lý sang "Cần dọn". Sau khi nhân viên buồng phòng dọn dẹp xong, phòng được đặt lại về "Trống" để đón khách tiếp theo.

Bên cạnh luồng chính, hệ thống còn xử lý nghiệp vụ hủy phòng. Khách chỉ được phép hủy khi đơn chưa chuyển sang trạng thái "Đã nhận phòng" và thời điểm hủy cách ngày nhận phòng dự kiến ít nhất 24 giờ. Ràng buộc 24 giờ giúp khách sạn có đủ thời gian mở lại phòng cho khách khác. Khi hủy thành công, phòng được giải phóng và trả về trạng thái "Trống".

#### 2.1.4 Quản lý phòng và tình trạng phòng

Dữ liệu phòng trong hệ thống được tổ chức thành hai tầng. Tầng trừu tượng là "loại phòng" — mỗi loại phòng mô tả một hạng phòng với các đặc điểm chung: tên gọi (Standard, Deluxe, Suite VIP…), đoạn mô tả, sức chứa tối đa, diện tích và mức giá cơ bản mỗi đêm. Mỗi loại phòng còn gắn liền với một tập tiện nghi (WiFi, máy lạnh, TV, minibar, bồn tắm…) thông qua bảng liên kết trung gian, tạo thành mối quan hệ nhiều-nhiều — nghĩa là một loại phòng có thể sở hữu nhiều tiện nghi, và ngược lại, một tiện nghi có thể thuộc về nhiều loại phòng khác nhau.

Tầng vật lý là "phòng cụ thể" — tức các phòng thực tế nằm trong tòa nhà, mỗi phòng được phân biệt bằng số phòng duy nhất, thuộc một tầng nhất định, gắn với một loại phòng và mang một trạng thái vận hành. Hệ thống định nghĩa bốn trạng thái cơ bản cho mỗi phòng:

- "Trống": phòng đã sẵn sàng, có thể tiếp nhận khách mới.
- "Đang thuê": phòng đang có khách lưu trú.
- "Cần dọn": phòng vừa được trả, chờ nhân viên buồng phòng dọn dẹp.
- "Bảo trì": phòng tạm ngưng khai thác do sửa chữa hoặc nâng cấp.

Điểm quan trọng là trạng thái phòng không chỉ được cập nhật thủ công mà còn được hệ thống tự động chuyển đổi tại các điểm nghiệp vụ then chốt: tạo đơn đặt phòng → chuyển "Trống" thành "Đang thuê"; nhân viên xác nhận trả phòng → chuyển "Đang thuê" thành "Cần dọn"; đơn bị hủy → trả phòng về "Trống". Cơ chế tự động này giúp Dashboard quản trị luôn phản ánh đúng số phòng khả dụng theo thời gian thực.

Về mặt phân quyền, chỉ quản trị viên (ADMIN) mới được thêm, sửa hoặc xóa loại phòng và phòng cụ thể. Trước khi xóa, hệ thống kiểm tra ràng buộc khóa ngoại: nếu một phòng đang có đơn đặt liên quan thì không cho phép xóa, tránh mất mát dữ liệu lịch sử. Nhân viên lễ tân (STAFF) chỉ có quyền xem danh sách và theo dõi tình trạng phòng, không thể thay đổi cấu hình danh mục.

#### 2.1.5 Quản lý khách hàng, dịch vụ và hóa đơn

**Quản lý khách hàng.** Thông tin của mỗi khách hàng được lưu ở hai bảng liên kết 1-1: bảng NguoiDung chứa dữ liệu tài khoản (tên đăng nhập, email, mật khẩu đã hash, trạng thái hoạt động, vai trò) và bảng KhachHang chứa dữ liệu nhân thân (họ tên, số điện thoại, số CCCD, ngày sinh, giới tính, địa chỉ). Khi khách đăng ký, hệ thống tạo đồng thời cả hai bản ghi trong cùng một giao dịch; nếu bước nào thất bại thì toàn bộ đăng ký bị hủy. Tên đăng nhập, email và CCCD đều mang ràng buộc UNIQUE, ngăn chặn trùng lặp ngay tại tầng CSDL. Quản trị viên có thể duyệt danh sách khách đã đăng ký, xóa tài khoản khi cần — thao tác xóa sẽ cascade xóa cả bản ghi NguoiDung lẫn KhachHang.

**Quản lý dịch vụ.** Ngoài dịch vụ lưu trú cốt lõi, khách sạn còn cung cấp nhiều dịch vụ phụ trợ tạo thêm doanh thu: minibar, spa, giặt ủi, xe đưa đón, dịch vụ ăn uống tại phòng… Mỗi dịch vụ trong CSDL có các trường: mã dịch vụ, tên, đơn vị tính (lần, chai, kg…), đơn giá, mô tả ngắn và cờ trạng thái (đang kinh doanh hoặc ngừng kinh doanh). Quản trị viên toàn quyền thêm, sửa, xóa dịch vụ; nhân viên chỉ có quyền ghi nhận việc khách sử dụng dịch vụ bằng cách tạo bản ghi SuDung_DichVu liên kết tới chi tiết đặt phòng. Mỗi bản ghi ghi rõ thời điểm sử dụng, số lượng, đơn giá tại thời điểm đó (để bảo toàn khi đơn giá thay đổi sau này) và thành tiền.

**Quản lý hóa đơn.** Hóa đơn là sản phẩm cuối cùng của quy trình lưu trú. Mỗi hóa đơn gắn liền với một đơn đặt phòng và tổng hợp bốn thành phần chi phí: tiền phòng (đơn giá × số đêm), tổng tiền dịch vụ phát sinh, khoản giảm giá (voucher) và phần phụ thu (nếu có). Trường `tongTien` lưu kết quả cuối cùng sau khi cộng trừ toàn bộ. Mỗi hóa đơn có thể liên kết với nhiều bản ghi thanh toán — ví dụ, một khoản cọc trực tuyến (MoMo) được lưu là một bản ghi ThanhToan, và phần còn lại thanh toán tại quầy là bản ghi ThanhToan thứ hai. Nhân viên có thể xem bill chi tiết trên giao diện web và xuất toàn bộ danh sách hóa đơn sang file CSV để phục vụ đối chiếu sổ sách hoặc gửi cho kế toán.

**Đánh giá (Review).** Sau khi trả phòng và thanh toán hoàn tất, khách hàng có thể viết đánh giá cho đơn lưu trú của mình. Mỗi đánh giá bao gồm điểm số từ 1 đến 5 sao và một đoạn bình luận tự do. Hệ thống ràng buộc mỗi đơn chỉ được đánh giá một lần duy nhất nhằm tránh spam. Điểm trung bình của từng loại phòng được tính từ tất cả đánh giá liên quan và hiển thị trên trang chủ lẫn trang chi tiết loại phòng. Ba bài đánh giá có điểm từ 4 sao trở lên được chọn ngẫu nhiên để trưng bày trong phần "Khách hàng nói gì" ở trang chủ, góp phần tạo niềm tin cho khách tiềm năng.

### 2.2 Cơ sở lý thuyết về cơ sở dữ liệu

Nền tảng lý thuyết về cơ sở dữ liệu quan hệ cung cấp bộ nguyên tắc để tổ chức, lưu trữ và truy xuất dữ liệu một cách có hệ thống. Nắm vững các khái niệm này giúp nhóm phát triển đưa ra quyết định thiết kế đúng đắn — từ việc phân chia bảng, đặt khóa, xây dựng ràng buộc cho đến tối ưu hiệu suất truy vấn và đảm bảo an toàn thông tin. Các nội dung dưới đây được trình bày kèm ví dụ minh họa cụ thể từ hệ thống quản lý khách sạn của đồ án.

#### 2.2.1 Khái niệm cơ sở dữ liệu và hệ quản trị cơ sở dữ liệu

Cơ sở dữ liệu (viết tắt CSDL) có thể hiểu đơn giản là một kho chứa thông tin được sắp xếp theo cấu trúc xác định, sao cho nhiều người dùng và ứng dụng có thể cùng truy cập, cập nhật mà vẫn duy trì được tính nhất quán. Trong mô hình quan hệ — mô hình được sử dụng rộng rãi nhất hiện nay — dữ liệu được biểu diễn dưới dạng các bảng hai chiều: mỗi hàng tương ứng một bản ghi (record), mỗi cột tương ứng một trường thông tin (field). Giữa các bảng có thể tồn tại quan hệ logic thông qua cơ chế khóa, nhờ đó dữ liệu ở nhiều bảng khác nhau được liên kết chặt chẽ mà không bị trùng lặp.

Để quản lý và thao tác trên CSDL, người ta sử dụng Hệ quản trị cơ sở dữ liệu (Database Management System — DBMS). Đây là lớp phần mềm trung gian đứng giữa ứng dụng và dữ liệu vật lý, đảm nhiệm các chức năng: tạo lược đồ bảng, kiểm tra ràng buộc, thực thi câu truy vấn SQL, quản lý giao dịch và kiểm soát truy cập. Một số DBMS quan hệ thông dụng có thể kể đến: MySQL, PostgreSQL, MariaDB, Microsoft SQL Server và Oracle Database. Mỗi hệ quản trị có ưu nhược điểm riêng về hiệu suất, khả năng mở rộng, chi phí bản quyền và hệ sinh thái công cụ hỗ trợ.

Trong đồ án này, MySQL phiên bản 8.0 được lựa chọn dựa trên ba tiêu chí: (1) hoàn toàn miễn phí với giấy phép mã nguồn mở, phù hợp với ngân sách đồ án; (2) có lượng tài liệu hướng dẫn bằng tiếng Việt phong phú, giúp nhóm tra cứu nhanh khi gặp vướng mắc; (3) tương thích tốt với hệ sinh thái Python thông qua thư viện driver PyMySQL và bộ công cụ ORM SQLAlchemy. Đặc biệt, thay vì viết trực tiếp câu lệnh SQL, đồ án sử dụng SQLAlchemy để ánh xạ mỗi bảng trong MySQL thành một lớp Python — nhờ vậy mã nguồn trở nên dễ đọc, dễ bảo trì và giảm thiểu nguy cơ lỗi SQL Injection vốn thường gặp khi ghép chuỗi SQL thủ công.

#### 2.2.2 Thực thể, thuộc tính và mối quan hệ

Mô hình thực thể — mối kết hợp (Entity-Relationship Model, viết tắt ER) là công cụ phân tích và thiết kế CSDL ở mức khái niệm. Trong mô hình này, mỗi đối tượng cần lưu trữ thông tin được gọi là thực thể (Entity), và mỗi đặc điểm mô tả thực thể đó được gọi là thuộc tính (Attribute). Lấy ví dụ từ đồ án: thực thể "Phòng" có các thuộc tính gồm mã phòng, số phòng, tầng, trạng thái và ghi chú; thực thể "Dịch vụ" có mã dịch vụ, tên, đơn vị tính, đơn giá, mô tả và trạng thái kinh doanh.

Khi chuyển từ mô hình ER sang lược đồ quan hệ trong MySQL, mỗi thực thể tương ứng với một bảng, và mỗi thuộc tính trở thành một cột trong bảng đó. Đồ án thiết kế tổng cộng 16 bảng, phản ánh 16 thực thể nghiệp vụ: VaiTro, NguoiDung, KhachHang, NhanVien, LoaiPhong, Phong, TienNghi, LoaiPhongTienNghi, KhuyenMai, DatPhong, ChiTietDatPhong, DichVu, SuDung_DichVu, HoaDon, ThanhToan và Review. Trong SQLAlchemy, mỗi bảng được khai báo dưới dạng một class kế thừa `db.Model`; các cột được định nghĩa bằng `db.Column()` với kiểu dữ liệu và ràng buộc tương ứng.

Giữa các thực thể tồn tại ba kiểu mối quan hệ:

- **Quan hệ 1-1** (một-một): mỗi bản ghi bên này chỉ đối ứng với duy nhất một bản ghi bên kia. Điển hình trong đồ án là cặp NguoiDung — KhachHang: mỗi tài khoản người dùng chỉ có một hồ sơ khách hàng, và ngược lại. Tương tự với cặp NguoiDung — NhanVien.
- **Quan hệ 1-N** (một-nhiều): một bản ghi ở bảng cha có thể liên kết với nhiều bản ghi ở bảng con. Ví dụ: một KhachHang có thể tạo nhiều DatPhong (đặt phòng nhiều lần), một LoaiPhong quản lý nhiều Phong vật lý, một HoaDon có thể gồm nhiều khoản ThanhToan.
- **Quan hệ N-N** (nhiều-nhiều): nhiều bản ghi ở cả hai bên đều có thể liên kết chéo với nhau. Đồ án có một mối N-N điển hình giữa LoaiPhong và TienNghi — một hạng phòng Deluxe có thể bao gồm WiFi, TV, minibar; đồng thời WiFi cũng có mặt trong hạng Standard, Deluxe lẫn Suite VIP. Quan hệ này được hiện thực qua bảng trung gian LoaiPhongTienNghi chứa hai khóa ngoại tham chiếu tới hai bảng gốc.

#### 2.2.3 Khóa chính và khóa ngoại

Khóa chính (Primary Key, viết tắt PK) là cột hoặc nhóm cột mà giá trị của nó nhận diện duy nhất từng hàng trong bảng. Hai quy tắc bắt buộc: giá trị khóa chính không được trùng nhau giữa các hàng, và không được phép rỗng (NULL). Trong thực tế, khóa chính thường là một số nguyên tự tăng (AUTO_INCREMENT) hoặc một chuỗi UUID. Đồ án chọn phương án chuỗi UUID kết hợp tiền tố phân loại để vừa đảm bảo tính duy nhất toàn cục vừa mang ngữ nghĩa nhận dạng — chẳng hạn "DP_a3f4c2e1" cho biết ngay đây là mã đặt phòng, "HD_b7d2e3f9" là mã hóa đơn, "SD_e9c1d5a2" là mã sử dụng dịch vụ. Cách đặt tên này cũng giúp việc gỡ lỗi và đọc log trở nên trực quan hơn so với các con số không mang ý nghĩa.

Trường hợp đặc biệt là bảng LoaiPhongTienNghi: thay vì một cột khóa chính đơn, bảng này sử dụng khóa chính ghép (Composite Primary Key) gồm cặp (maLoaiPhong, maTienNghi). Nhờ đó, CSDL tự động ngăn chặn việc gán trùng cùng một tiện nghi cho cùng một loại phòng.

Khóa ngoại (Foreign Key, viết tắt FK) là cột trong bảng con chứa giá trị tham chiếu đến khóa chính của bảng cha. Mục đích chính của khóa ngoại là duy trì tính toàn vẹn tham chiếu (Referential Integrity): hệ quản trị sẽ từ chối thêm bản ghi con nếu giá trị khóa ngoại không tồn tại ở bảng cha, và từ chối xóa bản ghi cha nếu vẫn còn bản ghi con tham chiếu đến (trừ khi cấu hình CASCADE). Trong đồ án, hàng chục khóa ngoại được thiết lập: cột `maKH` trong DatPhong trỏ về KhachHang, cột `maPhong` trong ChiTietDatPhong trỏ về Phong, cột `maDatPhong` trong HoaDon trỏ về DatPhong, cột `maHD` trong ThanhToan trỏ về HoaDon… Mạng lưới khóa ngoại này tạo ra một đồ thị liên kết chặt chẽ giữa 16 bảng, đảm bảo dữ liệu luôn tham chiếu đúng.

#### 2.2.4 Phụ thuộc hàm và chuẩn hóa cơ sở dữ liệu

Phụ thuộc hàm (Functional Dependency) là mối ràng buộc ngữ nghĩa giữa các thuộc tính trong cùng một bảng. Nói cách khác, nếu biết giá trị của thuộc tính X thì có thể xác định duy nhất giá trị của thuộc tính Y, ta viết X → Y. Lấy ví dụ cụ thể trong đồ án: bảng DatPhong có phụ thuộc hàm {maDatPhong} → {ngayDat, ngayNhanDuKien, ngayTraDuKien, soLuongKhach, trangThai, ghiChu, tienGiamGia, maKH, maNV} — nghĩa là biết mã đặt phòng thì xác định được toàn bộ thông tin còn lại của đơn đặt.

Chuẩn hóa (Normalization) là quy trình phân tách và tái cấu trúc bảng dựa trên phụ thuộc hàm, nhằm đạt hai mục tiêu: loại bỏ dư thừa dữ liệu (một thông tin chỉ lưu một nơi) và tránh các bất thường (anomaly) khi thêm, sửa, xóa.

Đồ án tuân thủ ba dạng chuẩn phổ biến:

- **Dạng chuẩn thứ nhất (1NF)**: yêu cầu mọi giá trị trong mỗi ô phải là giá trị nguyên tử — tức không chứa danh sách, tập hợp hay cấu trúc lồng nhau. Cả 16 bảng trong đồ án đều thỏa mãn: mỗi cột chỉ lưu đúng một giá trị đơn lẻ. Chẳng hạn, danh sách tiện nghi của loại phòng không được nhồi chung vào một cột text, mà được tách thành các bản ghi riêng trong bảng trung gian LoaiPhongTienNghi.
- **Dạng chuẩn thứ hai (2NF)**: trên nền 1NF, thêm điều kiện mỗi thuộc tính không thuộc khóa phải phụ thuộc vào toàn bộ khóa chính chứ không phải chỉ một phần. Điều kiện này chủ yếu liên quan đến bảng có khóa chính ghép. Trong đồ án, bảng LoaiPhongTienNghi có khóa ghép (maLoaiPhong, maTienNghi); thuộc tính `soLuong` phụ thuộc đầy đủ vào cả hai cột khóa (số lượng TV trong phòng Deluxe khác với số lượng TV trong phòng Suite). Các bảng còn lại có khóa chính đơn nên tự động đạt 2NF.
- **Dạng chuẩn thứ ba (3NF)**: trên nền 2NF, thêm yêu cầu không tồn tại phụ thuộc bắc cầu — tức thuộc tính không khóa A không được phụ thuộc vào khóa thông qua một thuộc tính không khóa B trung gian. Đồ án đã loại bỏ phụ thuộc bắc cầu bằng cách tách bảng: thông tin nhân thân khách hàng nằm riêng trong KhachHang thay vì lặp lại trong mỗi đơn DatPhong, thông tin loại phòng nằm riêng trong LoaiPhong thay vì ghi kèm trong mỗi bản ghi Phong, đơn giá dịch vụ gốc nằm trong DichVu còn đơn giá tại thời điểm sử dụng được lưu riêng trong SuDung_DichVu (tránh sai lệch khi giá thay đổi).

Tổng kết, toàn bộ 16 bảng đều đạt tối thiểu 3NF, đảm bảo mỗi mẩu thông tin chỉ xuất hiện một lần trong toàn bộ lược đồ và mọi cập nhật chỉ cần thực hiện tại một điểm duy nhất.

#### 2.2.5 Ràng buộc và toàn vẹn dữ liệu

Ràng buộc toàn vẹn (Integrity Constraint) là tập hợp các quy tắc mà CSDL luôn phải thỏa mãn, bất kể thao tác nào được thực hiện. Nếu một thao tác vi phạm ràng buộc, DBMS sẽ từ chối thực thi và trả về lỗi. Đồ án áp dụng năm loại ràng buộc chính tại tầng CSDL:

Thứ nhất, **ràng buộc khóa chính** (PRIMARY KEY) đảm bảo mỗi bảng có một hoặc một nhóm cột định danh duy nhất. Giá trị khóa chính không bao giờ trùng và không bao giờ rỗng. Tất cả 16 bảng đều được thiết lập khóa chính rõ ràng.

Thứ hai, **ràng buộc khóa ngoại** (FOREIGN KEY) ngăn cản việc tạo bản ghi "mồ côi" — tức bản ghi tham chiếu đến một đối tượng không tồn tại. Chẳng hạn, MySQL sẽ báo lỗi nếu ai đó cố tạo một đơn đặt phòng với mã khách hàng không có trong bảng KhachHang.

Thứ ba, **ràng buộc duy nhất** (UNIQUE) áp dụng lên những cột mà giá trị không được phép lặp giữa các hàng, mặc dù chúng không phải khóa chính. Trong đồ án, các cột mang ràng buộc này gồm: `tenDangNhap` và `email` trong NguoiDung (hai người không thể dùng chung username hoặc email), `cccd` trong KhachHang và NhanVien (mỗi số CCCD chỉ thuộc về một người), `soPhong` trong Phong (không tồn tại hai phòng cùng số).

Thứ tư, **ràng buộc NOT NULL** buộc một số cột luôn phải có giá trị khi thêm bản ghi, không được bỏ trống. Những cột quan trọng như tên đăng nhập, email, mật khẩu hash, tên loại phòng, sức chứa và giá cơ bản đều mang ràng buộc này.

Thứ năm, **ràng buộc giá trị mặc định** (DEFAULT) tự động gán giá trị cho cột khi người dùng không cung cấp. Ví dụ: cột `trangThai` của NguoiDung mặc định bằng TRUE (tài khoản hoạt động), cột `ngayTao` mặc định bằng thời điểm hiện tại (`datetime.now()`), cột `tienGiamGia` của DatPhong mặc định bằng 0.

Song song với ràng buộc tại tầng CSDL, hệ thống còn kiểm tra logic nghiệp vụ tại tầng ứng dụng. Các kiểm tra bao gồm: ngày trả phòng phải sau ngày nhận, phòng phải thực sự trống trước khi gán cho đơn mới, khách chỉ được xem hóa đơn thuộc về chính mình, và đơn chỉ được hủy khi cách ngày nhận tối thiểu 24 giờ. Hai tầng kiểm soát bổ trợ nhau giúp dữ liệu luôn ở trạng thái hợp lệ.

#### 2.2.6 Giao dịch và tính chất ACID

Giao dịch (Transaction) là một chuỗi thao tác CSDL được gom thành một khối logic thống nhất. Nguyên tắc cốt lõi: hoặc toàn bộ chuỗi thao tác thành công (commit), hoặc không thao tác nào được áp dụng (rollback). Giao dịch đặc biệt quan trọng trong các nghiệp vụ đòi hỏi thay đổi nhiều bảng đồng thời — nếu chỉ một bước bị lỗi mà các bước trước đó đã ghi vào CSDL, dữ liệu sẽ rơi vào trạng thái nửa vời, gây ra hàng loạt mâu thuẫn.

Bốn đặc tính mà một giao dịch hợp lệ phải đảm bảo, thường được gọi tắt là ACID:

**Tính nguyên tử (Atomicity)**: giao dịch là "tất cả hoặc không gì cả". Minh họa trong đồ án: khi tạo đơn đặt phòng, hệ thống phải liên tiếp thực hiện: chèn bản ghi DatPhong → chèn ChiTietDatPhong → cập nhật trạng thái phòng vật lý. Nếu bước cập nhật trạng thái phòng thất bại (chẳng hạn do vi phạm ràng buộc), hai bản ghi vừa chèn cũng bị hủy bỏ hoàn toàn, khách sẽ nhận thông báo lỗi thay vì bị "treo" đơn.

**Tính nhất quán (Consistency)**: sau khi giao dịch kết thúc, CSDL phải chuyển từ trạng thái hợp lệ cũ sang trạng thái hợp lệ mới, không phá vỡ bất kỳ ràng buộc nào. Ví dụ: nếu một phòng đang ở trạng thái "Trống" và được gán cho đơn đặt, sau giao dịch nó phải ở trạng thái "Đang thuê" — không thể vẫn là "Trống".

**Tính cô lập (Isolation)**: các giao dịch chạy đồng thời không nhìn thấy dữ liệu chưa commit của nhau. Tình huống thực tế: hai khách cùng lúc đặt loại phòng Deluxe trong khi chỉ còn một phòng trống duy nhất. Nhờ tính cô lập, giao dịch đến trước sẽ khóa bản ghi phòng; giao dịch đến sau sẽ phát hiện phòng đã hết và trả về thông báo "Hết phòng" thay vì tạo ra hai đơn đặt trùng.

**Tính bền vững (Durability)**: khi giao dịch đã commit thành công, dữ liệu phải được ghi lâu bền xuống ổ đĩa. Dù server bị tắt đột ngột ngay sau đó, dữ liệu vẫn không mất. MySQL InnoDB engine hỗ trợ tính bền vững thông qua cơ chế ghi nhật ký trước (Write-Ahead Logging): mọi thay đổi được ghi vào file log trước khi áp dụng vào file dữ liệu, nhờ đó có thể khôi phục toàn bộ sau sự cố.

Trong mã nguồn đồ án, giao dịch được quản lý thông qua đối tượng `db.session` của SQLAlchemy. Mỗi nhóm thao tác liên quan được thực thi trong cùng một session; lệnh `db.session.commit()` được gọi khi thành công và `db.session.rollback()` được gọi trong khối xử lý ngoại lệ (try/except) khi có bất kỳ lỗi nào xảy ra.

#### 2.2.7 Chỉ mục và tối ưu truy vấn

Chỉ mục (Index) là cấu trúc dữ liệu phụ trợ do DBMS tạo ra nhằm tăng tốc việc tìm kiếm bản ghi trong bảng. Nếu không có chỉ mục, mỗi truy vấn tìm kiếm đều phải duyệt toàn bộ bảng từ đầu đến cuối (Full Table Scan) — điều này chấp nhận được khi bảng chỉ có vài trăm bản ghi nhưng sẽ trở nên chậm đáng kể khi bảng chứa hàng chục nghìn bản ghi trở lên. Chỉ mục cho phép DBMS nhảy trực tiếp tới vùng dữ liệu liên quan, rút ngắn thời gian phản hồi từ vài giây xuống còn mili giây.

Tuy nhiên, chỉ mục cũng đi kèm chi phí: mỗi chỉ mục chiếm thêm dung lượng lưu trữ trên đĩa, và mỗi thao tác ghi (INSERT, UPDATE, DELETE) phải cập nhật cả dữ liệu lẫn chỉ mục, khiến tốc độ ghi giảm nhẹ. Do đó, nguyên tắc chung là chỉ đánh chỉ mục trên những cột thường xuyên xuất hiện trong mệnh đề WHERE, JOIN hoặc ORDER BY, và tránh đánh chỉ mục tràn lan.

Trong đồ án, MySQL tự động sinh chỉ mục cho ba nhóm cột: cột khóa chính (PRIMARY KEY), cột mang ràng buộc UNIQUE và cột khóa ngoại (FOREIGN KEY). Nhờ đó, hầu hết các truy vấn quan trọng đều được hưởng lợi mà không cần can thiệp thủ công. Cụ thể:

- Truy vấn tìm phòng trống (phức tạp nhất trong hệ thống): sử dụng subquery JOIN ba bảng Phong, ChiTietDatPhong và DatPhong, lọc theo loại phòng và phát hiện xung đột khoảng ngày. Chỉ mục trên `maLoaiPhong` (Phong), `maPhong` và `maDatPhong` (ChiTietDatPhong) giúp thu hẹp phạm vi quét.
- Truy vấn thống kê doanh thu: nhóm bảng ThanhToan theo tháng (GROUP BY tháng), tính tổng số tiền (SUM) để vẽ biểu đồ cột trên Dashboard. Chỉ mục trên cột `thoiGianThanhToan` hỗ trợ lọc theo khoảng thời gian hiệu quả.
- Truy vấn tìm đơn đặt phòng trên trang quản trị: tìm theo mã đặt, tên khách hoặc số điện thoại. Khóa chính `maDatPhong` đã có sẵn chỉ mục; các cột `hoTen` và `sdt` trong KhachHang được truy cập thông qua JOIN sử dụng chỉ mục trên khóa ngoại.

#### 2.2.8 Bảo mật, phân quyền và sao lưu dữ liệu

Bảo mật thông tin là yêu cầu không thể thiếu đối với bất kỳ hệ thống nào lưu trữ dữ liệu cá nhân (họ tên, CCCD, email, số điện thoại) và dữ liệu tài chính (hóa đơn, giao dịch thanh toán). Đồ án triển khai chiến lược bảo mật đa tầng, bao phủ từ lớp CSDL đến lớp ứng dụng.

**Bảo mật tại tầng CSDL.** MySQL cung cấp hệ thống tài khoản và phân quyền riêng (GRANT / REVOKE). Ứng dụng kết nối tới MySQL bằng một tài khoản chuyên dụng, chỉ được cấp quyền SELECT, INSERT, UPDATE, DELETE trên database `hoteldb`, không có quyền DROP TABLE hay truy cập database khác. Điều này giới hạn phạm vi thiệt hại nếu xảy ra tấn công SQL Injection (dù đã được giảm thiểu nhờ ORM).

**Bảo mật mật khẩu.** Mật khẩu người dùng không bao giờ lưu dạng rõ ràng (plaintext). Khi đăng ký, hệ thống sử dụng hàm `generate_password_hash()` của thư viện Werkzeug để chuyển mật khẩu thành chuỗi hash bằng thuật toán scrypt (hoặc pbkdf2_sha256, tùy cấu hình). Khi đăng nhập, mật khẩu khách nhập vào được hash lại rồi so sánh với giá trị đã lưu qua hàm `check_password_hash()`. Do đặc tính một chiều của hàm hash, ngay cả khi kẻ tấn công truy cập được CSDL, họ cũng không thể đảo ngược để lấy mật khẩu gốc — chỉ có thể thử brute-force, nhưng scrypt được thiết kế có chi phí tính toán cao để chống lại chính điều này.

**Phân quyền tại tầng ứng dụng.** Hệ thống phân biệt ba vai trò: khách hàng (không có quyền quản trị), nhân viên STAFF (quyền hạn chế) và quản trị viên ADMIN (toàn quyền). Trước mỗi thao tác trên trang quản trị, mã nguồn kiểm tra vai trò của người dùng hiện tại trong session. Nếu nhân viên STAFF cố truy cập route thêm/xóa loại phòng dành cho ADMIN, hệ thống trả về thông báo "Không đủ quyền". Tài khoản admin gốc (được tạo bởi script seed data) được bảo vệ đặc biệt — không ai có thể xóa tài khoản này, kể cả admin khác.

**Kiểm tra quyền sở hữu (Ownership check).** Đây là lớp bảo mật bổ sung ngăn chặn khách hàng A truy cập dữ liệu của khách hàng B. Trước khi hiển thị hóa đơn, cho phép hủy phòng hoặc mở form đánh giá, hệ thống đối chiếu mã khách hàng trong session với mã khách hàng gắn liền với đơn đặt phòng đó. Nếu không khớp, truy cập bị từ chối kèm thông báo lỗi.

**Bảo mật thanh toán trực tuyến.** Mọi giao dịch với cổng MoMo đều được ký bằng HMAC-SHA256 sử dụng khóa bí mật (secretKey). Chữ ký này đảm bảo rằng dữ liệu giao dịch không bị bên thứ ba can thiệp hoặc giả mạo trong quá trình truyền tải giữa server ứng dụng và server MoMo.

**Sao lưu dữ liệu.** MySQL cung cấp công cụ `mysqldump` cho phép xuất toàn bộ CSDL thành file SQL, phục vụ sao lưu logic. Trong quá trình phát triển đồ án, dữ liệu mẫu có thể tái tạo nhanh chóng bằng script `tao_du_lieu.py`. Đối với môi trường vận hành thực tế, nên thiết lập lịch sao lưu tự động (cronjob) ít nhất mỗi ngày một lần và lưu bản sao tại vị trí vật lý khác với server chính để phòng ngừa mất dữ liệu do sự cố phần cứng.

### 2.3 Các mô hình sử dụng trong phân tích và thiết kế

Trước khi bắt tay vào viết mã, nhóm phát triển cần một bộ công cụ mô hình hóa giúp hình dung rõ ràng hệ thống sẽ làm gì, dữ liệu được tổ chức ra sao và các thành phần phần mềm tương tác với nhau theo cách nào. Phần này giới thiệu bốn mô hình chính được sử dụng xuyên suốt quá trình phân tích và thiết kế hệ thống quản lý khách sạn.

#### 2.3.1 Mô hình Use Case

Mô hình Use Case (biểu đồ trường hợp sử dụng) là công cụ thuộc ngôn ngữ mô hình hóa thống nhất UML (Unified Modeling Language), dùng để biểu diễn tập hợp các chức năng mà hệ thống cung cấp cho từng nhóm người dùng. Mỗi Use Case mô tả một tương tác hoàn chỉnh giữa tác nhân (Actor) và hệ thống nhằm đạt được một mục tiêu cụ thể. Tác nhân có thể là con người (khách hàng, nhân viên, quản trị viên) hoặc hệ thống bên ngoài (cổng thanh toán MoMo, máy chủ email).

Trong đồ án, biểu đồ Use Case được chia thành hai nhóm chính. Nhóm thứ nhất gồm 14 Use Case phía khách hàng: đăng ký tài khoản, đăng nhập/đăng xuất, tìm kiếm và lọc phòng, xem chi tiết loại phòng, đặt phòng trực tuyến, áp dụng mã giảm giá, thanh toán cọc MoMo, xem lịch sử đặt phòng, hủy phòng, gọi dịch vụ phát sinh, xem hóa đơn, viết đánh giá, nhận email xác nhận kèm QR Code và chuyển ngôn ngữ. Nhóm thứ hai gồm 12 Use Case phía quản trị: xem Dashboard tổng quan, quản lý loại phòng (CRUD), quản lý phòng cụ thể (CRUD), quản lý đặt phòng, quản lý dịch vụ (CRUD), quản lý khách hàng, quản lý nhân sự, quản lý khuyến mãi, lập hóa đơn và thanh toán tại quầy, xem hóa đơn chi tiết, xuất CSV và tìm kiếm đơn đặt.

Biểu đồ Use Case giúp nhóm xác định rõ phạm vi hệ thống — chức năng nào nằm trong đồ án, chức năng nào nằm ngoài — đồng thời làm cơ sở để phân chia route trong mã nguồn Flask. Mỗi Use Case sau này được hiện thực bằng một hoặc vài route trong file `index.py` (phía khách) hoặc `admin.py` (phía quản trị).

#### 2.3.2 Mô hình thực thể – liên kết ERD

Mô hình thực thể – liên kết (Entity-Relationship Diagram, viết tắt ERD) là sơ đồ biểu diễn trực quan cấu trúc dữ liệu ở mức logic, trước khi chuyển sang hiện thực vật lý trong hệ quản trị CSDL. ERD thể hiện ba thành phần cốt lõi: thực thể (hình chữ nhật), thuộc tính (hình elip hoặc liệt kê trong hình chữ nhật) và mối kết hợp (đường nối kèm ký hiệu lực lượng 1-1, 1-N, N-N).

Sơ đồ ERD của đồ án bao gồm 16 thực thể, trong đó nổi bật các mối kết hợp sau: VaiTro (1-N) → NguoiDung, NguoiDung (1-1) → KhachHang, NguoiDung (1-1) → NhanVien, KhachHang (1-N) → DatPhong, DatPhong (1-N) → ChiTietDatPhong, ChiTietDatPhong (N-1) → Phong, LoaiPhong (1-N) → Phong, LoaiPhong (N-N) ↔ TienNghi thông qua bảng trung gian LoaiPhongTienNghi, DatPhong (1-1) → HoaDon, HoaDon (1-N) → ThanhToan, ChiTietDatPhong (1-N) → SuDung_DichVu, và DatPhong (1-N) → Review.

ERD đóng vai trò bản thiết kế gốc để nhóm xây dựng các class ORM trong file `models.py`. Mỗi hình chữ nhật trong ERD tương ứng một class kế thừa `db.Model`, mỗi đường nối tương ứng một cặp `db.ForeignKey()` – `db.relationship()` trong mã nguồn. Nhờ thiết kế ERD kỹ lưỡng trước khi code, nhóm tránh được tình trạng phải sửa lược đồ CSDL nhiều lần trong quá trình phát triển.

#### 2.3.3 Mô hình dữ liệu quan hệ

Mô hình dữ liệu quan hệ (Relational Data Model) là bước chuyển đổi từ ERD trừu tượng sang lược đồ bảng cụ thể có thể hiện thực trong MySQL. Trong mô hình này, mỗi thực thể trở thành một bảng (table), mỗi thuộc tính trở thành một cột (column) với kiểu dữ liệu và ràng buộc được định nghĩa rõ. Mối kết hợp giữa các thực thể được hiện thực thông qua cơ chế khóa ngoại.

Đồ án thiết kế 16 bảng trong CSDL `hoteldb`. Mỗi bảng được khai báo với đầy đủ: tên cột, kiểu dữ liệu (VARCHAR, INTEGER, FLOAT, BOOLEAN, DATETIME, TEXT), ràng buộc (PK, FK, UNIQUE, NOT NULL, DEFAULT) và quan hệ với bảng khác. Ví dụ, bảng `datphong` có 11 cột: `maDatPhong` (PK, VARCHAR(20)), `ngayDat` (DATETIME, DEFAULT NOW), `ngayNhanDuKien`, `ngayTraDuKien`, `ngayNhanThucTe`, `ngayTraThucTe`, `soLuongKhach` (INTEGER), `trangThai` (VARCHAR(50)), `ghiChu`, `tienGiamGia` (FLOAT, DEFAULT 0), `maKH` (FK → khachhang) và `maNV` (FK → nhanvien, có thể NULL nếu khách tự đặt online).

Mô hình dữ liệu quan hệ tuân thủ dạng chuẩn 3 (3NF) như đã phân tích ở mục 2.2.4, đảm bảo giảm thiểu dư thừa và tránh bất thường dữ liệu. Sơ đồ quan hệ chi tiết giữa 16 bảng được trình bày ở Chương 3.

#### 2.3.4 Mô hình kiến trúc MVC

MVC (Model – View – Controller) là mô hình kiến trúc phần mềm chia ứng dụng thành ba tầng trách nhiệm riêng biệt, giúp mã nguồn dễ bảo trì, dễ mở rộng và dễ phân công công việc trong nhóm.

**Tầng Model** chịu trách nhiệm về dữ liệu và logic nghiệp vụ liên quan đến dữ liệu. Trong đồ án, tầng Model bao gồm file `models.py` (14 class ORM định nghĩa cấu trúc 16 bảng CSDL) và file `dao.py` (7 hàm Data Access Object truy vấn dữ liệu thường dùng như lấy danh sách loại phòng, xác thực người dùng, kiểm tra quyền admin). Tầng Model không biết gì về giao diện hay cách dữ liệu được hiển thị — nó chỉ quan tâm đến việc lưu trữ, truy xuất và đảm bảo tính toàn vẹn dữ liệu.

**Tầng View** đảm nhiệm phần hiển thị giao diện cho người dùng. Trong đồ án, tầng View gồm 28 file template HTML sử dụng Jinja2, chia thành hai nhóm: giao diện khách hàng (kế thừa `base.html`) và giao diện quản trị (kế thừa `base_admin.html`). Tầng View nhận dữ liệu từ Controller, chèn vào template và trả về trang HTML hoàn chỉnh cho trình duyệt. View không trực tiếp truy vấn CSDL.

**Tầng Controller** đóng vai trò trung gian: nhận HTTP request từ trình duyệt, gọi Model để lấy hoặc cập nhật dữ liệu, chọn View phù hợp để render kết quả, rồi trả HTTP response về cho trình duyệt. Trong đồ án, Controller được hiện thực qua hai file: `index.py` (23 route xử lý nghiệp vụ phía khách hàng) và `admin.py` (20 route xử lý nghiệp vụ phía quản trị). Ngoài ra, các file service (`momo_api.py`, `email_service.py`, `translations.py`, `untils.py`) hỗ trợ Controller xử lý các tác vụ đặc thù như thanh toán, gửi email và đa ngôn ngữ.

Mô hình MVC trong Flask là dạng biến thể (không phải MVC cổ điển): Flask không có thư mục `controllers/` riêng mà sử dụng các hàm route đóng vai trò controller, template Jinja2 đóng vai trò view, và SQLAlchemy model đóng vai trò model. Sự linh hoạt này phù hợp với quy mô đồ án vừa và nhỏ, nơi việc tuân thủ cấu trúc MVC cứng nhắc có thể tạo ra overhead không cần thiết.

### 2.4 Công nghệ sử dụng

Phần này trình bày chi tiết từng công nghệ, thư viện và framework đã được sử dụng trong quá trình xây dựng hệ thống. Mỗi công nghệ được giới thiệu khái quát về nguồn gốc, đặc điểm nổi bật và cách thức áp dụng cụ thể trong đồ án.

#### 2.4.1 Ngôn ngữ lập trình Python và Framework Flask

**Python** là ngôn ngữ lập trình bậc cao do Guido van Rossum phát triển từ cuối thập niên 1980, nổi tiếng với triết lý thiết kế nhấn mạnh tính dễ đọc của mã nguồn. Python hỗ trợ đa mô hình lập trình (hướng đối tượng, lập trình hàm, lập trình thủ tục) và sở hữu hệ sinh thái thư viện bên thứ ba cực kỳ phong phú — từ phát triển web, xử lý dữ liệu đến trí tuệ nhân tạo. Đồ án sử dụng Python phiên bản 3.10 trở lên, tận dụng các tính năng hiện đại như f-string, type hint và cú pháp match-case (nếu cần).

Toàn bộ phần back-end của hệ thống bao gồm 9 file Python với tổng cộng khoảng 2.085 dòng mã nguồn. Python đảm nhận mọi tác vụ xử lý phía máy chủ: tiếp nhận HTTP request, xử lý logic nghiệp vụ (kiểm tra phòng trống, tính toán hóa đơn, xác thực người dùng), tương tác với CSDL MySQL thông qua SQLAlchemy, gọi API thanh toán MoMo, sinh mã QR Code và gửi email xác nhận.

**Flask** là micro web framework dành cho Python, được phát triển bởi Armin Ronacher dưới dạng dự án mã nguồn mở. Thuật ngữ "micro" không có nghĩa Flask thiếu tính năng, mà có nghĩa phần lõi (core) của Flask cố tình giữ ở mức tối giản — chỉ cung cấp routing, xử lý request/response và hệ thống template — để nhà phát triển tự lựa chọn các thành phần mở rộng (extension) phù hợp với nhu cầu dự án. Đồ án sử dụng Flask phiên bản 3.0.2.

Flask hoạt động dựa trên hai thành phần nền tảng: Werkzeug (bộ công cụ WSGI xử lý giao tiếp HTTP ở mức thấp) và Jinja2 (template engine render giao diện HTML động). Cơ chế routing của Flask sử dụng decorator `@app.route()` để ánh xạ mỗi URL endpoint tới một hàm Python xử lý logic. Hệ thống trong đồ án triển khai tổng cộng 43 route, chia thành hai module: `index.py` chứa 23 route phục vụ khách hàng và `admin.py` chứa 20 route phục vụ trang quản trị.

#### 2.4.2 Hệ quản trị cơ sở dữ liệu MySQL

MySQL là hệ quản trị CSDL quan hệ mã nguồn mở được sử dụng phổ biến nhất trên thế giới, hiện do Oracle Corporation phát triển và bảo trì. MySQL hỗ trợ đầy đủ ngôn ngữ SQL chuẩn cùng nhiều tính năng nâng cao: stored procedure, trigger, view, transaction, replication và partitioning. Storage engine mặc định InnoDB cung cấp hỗ trợ transaction tuân thủ ACID, khóa ở mức hàng (row-level locking) và ràng buộc khóa ngoại.

Đồ án sử dụng MySQL phiên bản 8.0, chạy trên localhost tại cổng 3307 với database có tên `hoteldb`. Cơ sở dữ liệu gồm 16 bảng lưu trữ toàn bộ dữ liệu nghiệp vụ: thông tin người dùng, khách hàng, nhân viên, loại phòng, phòng cụ thể, tiện nghi, đơn đặt phòng, chi tiết đặt phòng, dịch vụ, sử dụng dịch vụ, khuyến mãi, hóa đơn, thanh toán và đánh giá. Ứng dụng kết nối tới MySQL thông qua chuỗi kết nối `mysql+pymysql://root:Abc123@127.0.0.1:3307/hoteldb`, sử dụng PyMySQL làm database driver.

#### 2.4.3 HTML và CSS

HTML (HyperText Markup Language) là ngôn ngữ đánh dấu chuẩn dùng để xây dựng cấu trúc nội dung của trang web. Phiên bản HTML5 bổ sung nhiều thẻ ngữ nghĩa mới (header, nav, main, section, article, footer) giúp cấu trúc trang rõ ràng hơn, đồng thời hỗ trợ các API hiện đại cho form validation, multimedia và canvas.

CSS (Cascading Style Sheets) là ngôn ngữ định dạng giao diện, chịu trách nhiệm quy định màu sắc, kích thước, khoảng cách, bố cục và hiệu ứng chuyển động trên trang web. CSS3 bổ sung nhiều tính năng mạnh mẽ như flexbox, grid layout, media query (responsive design), transition và animation.

Trong đồ án, HTML5 được sử dụng để xây dựng cấu trúc 28 trang giao diện, từ trang chủ, trang đặt phòng đến các trang quản trị. CSS3 được kết hợp chặt chẽ với Bootstrap 5 để tạo giao diện responsive, đồng thời nhóm viết thêm CSS tùy chỉnh cho các phần đặc thù như hero section trên trang chủ, card hiển thị loại phòng và bảng dữ liệu quản trị. Toàn bộ HTML được render động thông qua template engine Jinja2 tích hợp trong Flask.

#### 2.4.4 Bootstrap

Bootstrap là CSS framework mã nguồn mở phổ biến nhất thế giới, ban đầu được phát triển bởi đội ngũ kỹ sư tại Twitter. Bootstrap cung cấp hệ thống grid responsive 12 cột, bộ component giao diện sẵn có (navbar, card, modal, table, form, badge, alert, pagination…) và hàng trăm utility class tiện ích cho margin, padding, color, display và typography.

Đồ án sử dụng Bootstrap phiên bản 5, bản cập nhật loại bỏ sự phụ thuộc vào thư viện jQuery. Bootstrap 5 giúp giao diện tự động thích ứng với mọi kích thước màn hình — từ desktop (≥1200px), laptop (≥992px), tablet (≥768px) đến điện thoại di động (≤576px) — mà không cần viết media query thủ công. Các component chính được sử dụng trong đồ án bao gồm:

- **Navbar**: thanh điều hướng đầu trang cho cả giao diện khách và quản trị, tự động thu gọn (collapse) thành menu hamburger trên màn hình nhỏ.
- **Card**: thẻ hiển thị thông tin loại phòng trên trang chủ (ảnh, tên, giá, sức chứa, rating).
- **Table**: bảng dữ liệu hiển thị danh sách phòng, đơn đặt, hóa đơn, nhân sự trên trang quản trị.
- **Modal**: hộp thoại popup cho form thêm mới loại phòng, phòng, dịch vụ, nhân viên, khuyến mãi.
- **Badge**: nhãn mã màu phân biệt trạng thái đơn đặt (vàng — chờ nhận, xanh lá — đã cọc, xanh dương — đang thuê, xám — đã trả, đỏ — đã hủy).
- **Form**: các form nhập liệu cho đăng ký, đăng nhập, đặt phòng, lập hóa đơn.

#### 2.4.5 JavaScript

JavaScript là ngôn ngữ lập trình kịch bản chạy trên trình duyệt web, cho phép tạo các tương tác động phía client mà không cần gửi request về server. JavaScript hoạt động theo mô hình hướng sự kiện (event-driven) — mã được thực thi khi người dùng tương tác với giao diện (click, nhập liệu, cuộn trang).

Trong đồ án, JavaScript được sử dụng cho ba mục đích chính. Thứ nhất, gọi API kiểm tra mã khuyến mãi (voucher) bằng kỹ thuật AJAX — khi khách nhập mã giảm giá vào form đặt phòng, JavaScript gửi request POST tới route `/api/check-voucher` và nhận phản hồi JSON; nếu mã hợp lệ, phần trăm giảm giá được hiển thị và tổng tiền được cập nhật tức thì trên giao diện mà không cần tải lại trang. Thứ hai, truyền dữ liệu doanh thu từ Flask vào thư viện Chart.js để vẽ biểu đồ cột doanh thu 12 tháng trên trang Dashboard quản trị. Thứ ba, xử lý các tương tác giao diện nhỏ như xác nhận trước khi xóa (confirm dialog), thu gọn/mở rộng sidebar menu và hiển thị thông báo flash.

#### 2.4.6 Flask-SQLAlchemy

Flask-SQLAlchemy là extension chính thức tích hợp bộ công cụ SQLAlchemy vào Flask, cung cấp interface đơn giản hóa cho việc khai báo model, quản lý session và thực thi truy vấn CSDL. Thay vì cấu hình SQLAlchemy thủ công (tạo engine, tạo session factory, bind metadata), Flask-SQLAlchemy gói gọn mọi thứ vào đối tượng `db = SQLAlchemy(app)` — từ đó mọi model chỉ cần kế thừa `db.Model`, mọi truy vấn được thực hiện qua `db.session`, và việc tạo bảng chỉ cần gọi `db.create_all()`.

Đồ án sử dụng SQLAlchemy phiên bản 2.0.25 kết hợp Flask-SQLAlchemy phiên bản 3.1.1. Bộ đôi này đảm nhận vai trò ORM (Object-Relational Mapping): mỗi bảng trong MySQL được ánh xạ thành một class Python, mỗi cột thành một thuộc tính class, mỗi hàng thành một đối tượng (instance). Các thao tác CRUD (Create, Read, Update, Delete) được thực hiện hoàn toàn bằng cú pháp Python — ví dụ: `Phong.query.filter_by(trangThai='Trống').all()` thay vì viết SQL `SELECT * FROM phong WHERE trangThai = 'Trống'`. Nhờ ORM, mã nguồn vừa dễ đọc, vừa an toàn trước các lỗ hổng SQL Injection vốn thường phát sinh khi ghép chuỗi SQL thủ công.

#### 2.4.7 Công cụ hỗ trợ phát triển

Ngoài các công nghệ cốt lõi kể trên, đồ án còn sử dụng một số công cụ và thư viện hỗ trợ:

**Chart.js** là thư viện JavaScript mã nguồn mở dùng để vẽ biểu đồ trên nền tảng web. Trong đồ án, Chart.js hiển thị biểu đồ cột (bar chart) doanh thu theo 12 tháng trên trang Dashboard quản trị. Dữ liệu được truy vấn từ bảng ThanhToan (GROUP BY tháng), truyền từ Flask vào template dưới dạng mảng JSON.

**Thư viện `qrcode`** của Python được sử dụng để sinh mã QR Code chứa thông tin đặt phòng (mã đơn, tên khách, ngày nhận phòng). Mã QR dạng ảnh PNG được đính kèm trong email xác nhận.

**MoMo Payment Gateway API v2** cho phép khách thanh toán đặt cọc 50% trực tuyến. Hệ thống tạo chữ ký HMAC-SHA256 cho mỗi giao dịch, gửi request tới MoMo và xử lý callback. Đồ án sử dụng môi trường test (`test-payment.momo.vn`).

**Module Email** sử dụng thư viện `smtplib` và `email` có sẵn trong Python, gửi email HTML xác nhận đặt phòng kèm mã QR. Trong môi trường development, email được lưu preview dạng HTML thay vì gửi thật.

**Hệ thống I18N (Internationalization)** do nhóm tự xây dựng, hỗ trợ hai ngôn ngữ Tiếng Việt và Tiếng Anh với hơn 80 key dịch. File `translations.py` chứa từ điển dịch, hàm `get_text()` tra cứu bản dịch theo session, Flask context processor inject hàm dịch vào Jinja2.

**Thư viện `uuid`** sinh mã khóa chính duy nhất với prefix phân loại (DP_, HD_, TT_, CT_, SD_). **Thư viện `csv`** hỗ trợ xuất danh sách hóa đơn sang file CSV tương thích Excel (UTF-8 BOM).

**PyCharm / VS Code** được sử dụng làm IDE phát triển, cung cấp tính năng autocomplete, debug, terminal tích hợp và syntax highlighting cho Python, HTML, CSS, JavaScript. **Git** được sử dụng để quản lý phiên bản mã nguồn.

### 2.5 Vai trò của các công nghệ trong đồ án

Mỗi công nghệ trong hệ thống đảm nhận một vị trí cụ thể trong kiến trúc tổng thể. Để hiểu rõ hơn cách chúng phối hợp với nhau, phần này phân tích vai trò của từng thành phần theo ba tầng kiến trúc: tầng trình bày (Presentation), tầng xử lý (Business Logic) và tầng dữ liệu (Data).

**Tầng trình bày (Presentation Layer)** là lớp giao diện mà người dùng cuối tương tác trực tiếp. Tầng này được xây dựng bởi sự kết hợp của HTML5 (cấu trúc trang), CSS3 và Bootstrap 5 (định dạng và responsive), JavaScript (tương tác động phía trình duyệt), Chart.js (biểu đồ doanh thu) và Jinja2 (render HTML động từ dữ liệu server). Khi người dùng mở trang web, trình duyệt nhận về một trang HTML hoàn chỉnh đã được Jinja2 render, kèm theo CSS từ Bootstrap và JavaScript xử lý tương tác.

**Tầng xử lý (Business Logic Layer)** là nơi diễn ra toàn bộ logic nghiệp vụ. Python và Flask đảm nhận vai trò trung tâm: tiếp nhận request từ trình duyệt, xác thực người dùng (Werkzeug hash password), kiểm tra quyền (session-based authorization), xử lý logic đặt phòng (Overlap Detection), tính toán hóa đơn, gọi API MoMo (HMAC-SHA256), sinh QR Code, gửi email và chuyển đổi ngôn ngữ (I18N). Tầng này giao tiếp với tầng dữ liệu thông qua SQLAlchemy ORM.

**Tầng dữ liệu (Data Layer)** chịu trách nhiệm lưu trữ và truy xuất dữ liệu bền vững. MySQL 8.0 đóng vai trò hệ quản trị CSDL, lưu trữ 16 bảng với đầy đủ ràng buộc toàn vẹn. SQLAlchemy ORM và PyMySQL tạo thành cầu nối giữa tầng xử lý (Python) và tầng dữ liệu (MySQL), cho phép thao tác CSDL bằng cú pháp Python thay vì SQL thuần.

Ngoài ba tầng chính, các dịch vụ bên ngoài (MoMo Payment Gateway, Gmail SMTP Server) đóng vai trò bổ trợ: MoMo xử lý giao dịch thanh toán trực tuyến, Gmail chuyển phát email xác nhận. Hệ thống giao tiếp với các dịch vụ này thông qua HTTP API và giao thức SMTP.

### 2.6 Lý do lựa chọn Flask và MySQL

Việc lựa chọn bộ công nghệ nền tảng (web framework + hệ quản trị CSDL) ảnh hưởng trực tiếp đến tốc độ phát triển, khả năng bảo trì và tiềm năng mở rộng của dự án. Phần này giải thích tại sao nhóm chọn Flask thay vì Django (hoặc các framework khác) và MySQL thay vì PostgreSQL hay MongoDB.

**Lý do chọn Flask thay vì Django.** Django là full-stack framework với nhiều thành phần tích hợp sẵn (admin panel, ORM riêng, authentication, form validation), phù hợp cho dự án lớn cần nhanh chóng có đầy đủ tính năng. Tuy nhiên, Django áp đặt cấu trúc dự án cố định và đường cong học tập dốc hơn. Flask, ngược lại, cho phép nhóm tự do lựa chọn cấu trúc và chỉ tích hợp những extension cần thiết. Với quy mô đồ án (43 route, 16 bảng CSDL, nhóm phát triển nhỏ), Flask mang lại sự cân bằng tốt giữa tính linh hoạt và thời gian phát triển. Hơn nữa, Flask có lượng tài liệu hướng dẫn bằng tiếng Việt phong phú, giúp nhóm tra cứu nhanh khi gặp vướng mắc.

**Lý do chọn MySQL thay vì PostgreSQL.** PostgreSQL có nhiều tính năng nâng cao hơn MySQL (hỗ trợ kiểu dữ liệu JSON nâng cao, full-text search mạnh, CTE đệ quy), nhưng đối với nghiệp vụ khách sạn trong đồ án — chủ yếu là CRUD đơn giản, JOIN giữa các bảng quan hệ và thống kê GROUP BY — MySQL hoàn toàn đáp ứng đủ. MySQL còn có lợi thế về mặt phổ biến: nhiều hosting hỗ trợ MySQL hơn PostgreSQL, tài liệu tiếng Việt nhiều hơn, và công cụ quản trị trực quan (phpMyAdmin, MySQL Workbench) dễ tiếp cận.

**Lý do không chọn MongoDB (NoSQL).** MongoDB lưu trữ dữ liệu dạng document JSON, phù hợp với dữ liệu phi cấu trúc hoặc bán cấu trúc. Tuy nhiên, dữ liệu khách sạn có tính quan hệ rất rõ ràng (khách hàng → đặt phòng → chi tiết đặt → phòng → loại phòng → tiện nghi; hóa đơn → thanh toán), đòi hỏi ràng buộc toàn vẹn chặt chẽ (FK, UNIQUE, NOT NULL). CSDL quan hệ (MySQL) là lựa chọn tự nhiên và hiệu quả hơn cho loại dữ liệu này, đồng thời hỗ trợ transaction ACID — điều cốt yếu khi xử lý nghiệp vụ tài chính (hóa đơn, thanh toán).

**Tóm lại**, bộ công nghệ Python + Flask + SQLAlchemy + MySQL được chọn dựa trên bốn yếu tố: (1) tốc độ phát triển nhanh nhờ cú pháp Python ngắn gọn và cộng đồng hỗ trợ lớn, (2) tính linh hoạt cao nhờ kiến trúc micro-framework của Flask, (3) sự phù hợp của MySQL với dữ liệu quan hệ phức tạp của nghiệp vụ khách sạn, và (4) khả năng mở rộng trong tương lai — hệ sinh thái Python cho phép tích hợp thêm Machine Learning (gợi ý phòng dựa trên lịch sử, phân tích cảm xúc từ đánh giá) mà không cần thay đổi ngôn ngữ hay framework.

---

## CHƯƠNG 3: PHÂN TÍCH, THIẾT KẾ VÀ XÂY DỰNG HỆ THỐNG

Chương này trình bày quá trình phân tích yêu cầu, thiết kế kiến trúc phần mềm, thiết kế cơ sở dữ liệu và phân tích các Use Case của hệ thống quản lý và đặt phòng khách sạn trực tuyến. Nội dung được tổ chức theo trình tự: giới thiệu hệ thống → khảo sát yêu cầu → thiết kế kiến trúc → phân tích Use Case → thiết kế CSDL → thiết kế giao diện.

### 3.1 Giới thiệu hệ thống

#### 3.1.1 Mục đích của hệ thống

Hệ thống quản lý và đặt phòng khách sạn trực tuyến được xây dựng nhằm giải quyết những bất cập trong quy trình vận hành thủ công tại các khách sạn quy mô vừa và nhỏ. Cụ thể, hệ thống hướng tới bốn mục đích chính.

Mục đích thứ nhất là số hóa toàn bộ quy trình đặt phòng. Thay vì khách phải gọi điện hoặc đến trực tiếp quầy lễ tân, hệ thống cho phép khách tìm kiếm phòng trống, so sánh giá và đặt chỗ trực tiếp trên website bất cứ lúc nào, bất kể ngày đêm.

Mục đích thứ hai là tự động hóa nghiệp vụ quản lý nội bộ. Nhân viên và quản trị viên có thể theo dõi tình trạng phòng theo thời gian thực, xử lý đơn đặt phòng, ghi nhận dịch vụ phát sinh, lập hóa đơn và xuất báo cáo doanh thu — tất cả đều thông qua một giao diện web thống nhất.

Mục đích thứ ba là tích hợp thanh toán trực tuyến. Khách hàng có thể đặt cọc 50% giá trị đơn phòng thông qua cổng thanh toán MoMo, giúp khách sạn giảm thiểu rủi ro hủy phòng đột xuất và cải thiện dòng tiền.

Mục đích thứ tư là cung cấp công cụ phân tích kinh doanh. Dashboard quản trị hiển thị biểu đồ doanh thu theo 12 tháng, thống kê số phòng trống/đang thuê/cần dọn, giúp ban quản lý đưa ra quyết định kinh doanh dựa trên dữ liệu thay vì cảm tính.

#### 3.1.2 Đối tượng sử dụng

Hệ thống phục vụ ba nhóm đối tượng người dùng, mỗi nhóm có vai trò, quyền hạn và nhu cầu sử dụng khác nhau.

**Khách hàng (Customer)** là nhóm người dùng cuối, bao gồm khách du lịch trong nước và quốc tế, khách công tác và gia đình có nhu cầu lưu trú. Khách hàng tương tác với hệ thống thông qua giao diện web công khai: đăng ký tài khoản, tìm kiếm phòng, đặt phòng, thanh toán trực tuyến, xem lịch sử đặt phòng, gọi dịch vụ phát sinh, xem hóa đơn và viết đánh giá. Giao diện được thiết kế responsive, tương thích với máy tính để bàn, laptop, tablet và điện thoại thông minh.

**Nhân viên lễ tân (Staff)** là người vận hành hàng ngày, chịu trách nhiệm tiếp nhận đơn đặt phòng, xác nhận nhận/trả phòng, ghi nhận dịch vụ phát sinh, lập hóa đơn thanh toán tại quầy và xuất báo cáo CSV. Nhân viên truy cập hệ thống qua trang quản trị với quyền hạn giới hạn: chỉ được xem và cập nhật, không được thêm mới hoặc xóa danh mục (loại phòng, phòng, dịch vụ).

**Quản trị viên (Admin)** nắm quyền điều hành cao nhất, bao gồm toàn bộ chức năng của nhân viên cộng thêm: quản lý danh mục loại phòng, phòng cụ thể và dịch vụ (CRUD), quản lý tài khoản nhân viên (thêm/xóa, phân quyền ADMIN hoặc STAFF), quản lý khách hàng, quản lý mã khuyến mãi và theo dõi biểu đồ doanh thu.

#### 3.1.3 Các chức năng chính của hệ thống

Hệ thống cung cấp các nhóm chức năng chính sau:

**Nhóm chức năng đặt phòng trực tuyến**: tìm kiếm và lọc phòng đa tiêu chí, xem chi tiết loại phòng (tiện nghi, đánh giá), đặt phòng với kiểm tra trùng lịch tự động (Overlap Detection), áp dụng mã giảm giá, thanh toán đặt cọc qua MoMo, nhận email xác nhận kèm mã QR Code, xem lịch sử đặt phòng và hủy phòng.

**Nhóm chức năng quản lý lưu trú**: cập nhật trạng thái đơn đặt phòng (nhận phòng, trả phòng, hủy), ghi nhận dịch vụ phát sinh trong quá trình lưu trú, lập hóa đơn thanh toán tại quầy với công thức tự động (tiền phòng + dịch vụ − giảm giá − đã cọc).

**Nhóm chức năng quản lý danh mục**: CRUD loại phòng, phòng cụ thể, dịch vụ bổ sung, tiện nghi phòng, mã khuyến mãi.

**Nhóm chức năng quản lý người dùng**: đăng ký/đăng nhập với mật khẩu mã hóa, phân quyền ADMIN/STAFF, quản lý tài khoản khách hàng và nhân viên.

**Nhóm chức năng thống kê và báo cáo**: Dashboard tổng quan (số phòng trống/thuê/cần dọn, doanh thu hôm nay), biểu đồ doanh thu 12 tháng (Chart.js), xuất danh sách hóa đơn CSV.

**Nhóm chức năng bổ trợ**: đánh giá 1-5 sao kèm bình luận, chuyển đổi ngôn ngữ Tiếng Việt / Tiếng Anh (I18N), chuyển đổi đơn vị tiền tệ VND/USD.

### 3.2 Khảo sát và phân tích yêu cầu

#### 3.2.1 Yêu cầu chức năng

Yêu cầu chức năng mô tả những gì hệ thống phải thực hiện được. Dựa trên khảo sát nghiệp vụ thực tế tại các khách sạn quy mô vừa và nhỏ, nhóm xác định các yêu cầu chức năng chia theo hai phía.

**Phía khách hàng (14 chức năng)**:

| STT | Mã | Chức năng | Mô tả |
|-----|----|-----------|-------|
| 1 | F-C01 | Đăng ký tài khoản | Nhập username, email, mật khẩu, họ tên, SĐT, CCCD. Tạo đồng thời NguoiDung + KhachHang |
| 2 | F-C02 | Đăng nhập / Đăng xuất | Xác thực username + password hash, tạo/xóa session |
| 3 | F-C03 | Tìm kiếm và lọc phòng | Lọc theo từ khóa, sức chứa, giá tối đa, khoảng ngày (Overlap Detection) |
| 4 | F-C04 | Xem chi tiết loại phòng | Hiển thị mô tả, diện tích, giá, tiện nghi, rating trung bình, số phòng trống |
| 5 | F-C05 | Đặt phòng trực tuyến | Chọn ngày, số khách → tìm phòng trống → tạo đơn → gửi email + QR |
| 6 | F-C06 | Áp dụng mã giảm giá | Nhập voucher, API kiểm tra hợp lệ, trừ phần trăm giá |
| 7 | F-C07 | Thanh toán cọc MoMo | Cọc 50% qua MoMo, ký HMAC-SHA256, cập nhật trạng thái "Đã cọc" |
| 8 | F-C08 | Xem lịch sử đặt phòng | Liệt kê đơn đặt, sắp xếp mới nhất, badge trạng thái mã màu |
| 9 | F-C09 | Hủy phòng | Hủy nếu trạng thái "Chờ nhận" hoặc "Đã cọc", trước 24 giờ nhận phòng |
| 10 | F-C10 | Gọi dịch vụ phát sinh | Chọn dịch vụ + số lượng cho đơn đặt phòng đang lưu trú |
| 11 | F-C11 | Xem hóa đơn | Xem chi tiết hóa đơn (kiểm tra quyền sở hữu trước khi hiển thị) |
| 12 | F-C12 | Viết đánh giá | Đánh giá 1-5 sao + bình luận, mỗi đơn chỉ được đánh giá 1 lần |
| 13 | F-C13 | Nhận email xác nhận | Email HTML tự động kèm thông tin đặt phòng và mã QR Code |
| 14 | F-C14 | Chuyển ngôn ngữ | Chuyển đổi Tiếng Việt ↔ Tiếng Anh, chuyển đơn vị tiền tệ |

**Phía quản trị (12 chức năng)**:

| STT | Mã | Chức năng | Mô tả | Quyền |
|-----|----|-----------|-------|-------|
| 1 | F-A01 | Dashboard tổng quan | Thống kê phòng, doanh thu, biểu đồ 12 tháng | STAFF/ADMIN |
| 2 | F-A02 | Quản lý loại phòng | CRUD loại phòng (Standard, Deluxe, Suite VIP) | ADMIN |
| 3 | F-A03 | Quản lý phòng cụ thể | CRUD phòng thực tế (số phòng, tầng, trạng thái) | ADMIN |
| 4 | F-A04 | Quản lý đặt phòng | Tìm kiếm, cập nhật trạng thái đơn | STAFF/ADMIN |
| 5 | F-A05 | Quản lý dịch vụ | CRUD dịch vụ bổ sung (minibar, spa, giặt ủi) | ADMIN |
| 6 | F-A06 | Quản lý khách hàng | Xem danh sách, xóa tài khoản khách | ADMIN |
| 7 | F-A07 | Quản lý nhân sự | Thêm/xóa nhân viên, phân quyền ADMIN/STAFF | ADMIN |
| 8 | F-A08 | Quản lý khuyến mãi | Thêm/xóa/bật-tắt mã giảm giá | ADMIN |
| 9 | F-A09 | Lập hóa đơn & thanh toán | Tính tự động: phòng + DV − giảm giá − cọc | STAFF/ADMIN |
| 10 | F-A10 | Xem hóa đơn chi tiết | Bill đầy đủ: khách, phòng, số ngày, tiền phòng, tiền DV | STAFF/ADMIN |
| 11 | F-A11 | Xuất CSV | Tải danh sách hóa đơn dạng CSV (UTF-8 BOM) | STAFF/ADMIN |
| 12 | F-A12 | Tìm kiếm đơn đặt | Tìm theo mã đơn, tên khách, SĐT | STAFF/ADMIN |

#### 3.2.2 Yêu cầu phi chức năng

Yêu cầu phi chức năng quy định các tiêu chí chất lượng mà hệ thống phải đáp ứng, bao gồm hiệu năng, bảo mật, khả năng sử dụng và khả năng bảo trì.

| STT | Yêu cầu | Mô tả chi tiết |
|-----|---------|----------------|
| 1 | Giao diện responsive | Tương thích Desktop, Tablet và Mobile nhờ hệ thống grid của Bootstrap 5 |
| 2 | Hiệu năng | Thời gian phản hồi trung bình dưới 2 giây cho các trang thông thường |
| 3 | Bảo mật mật khẩu | Mã hóa bằng scrypt/pbkdf2_sha256 (Werkzeug), không lưu plaintext |
| 4 | Bảo mật thanh toán | Chữ ký HMAC-SHA256 cho mọi giao dịch MoMo |
| 5 | Phân quyền | Hai vai trò ADMIN và STAFF, kiểm tra trước mỗi thao tác quản trị |
| 6 | Bảo mật session | Secret key bảo vệ session cookie, kiểm tra quyền sở hữu đơn |
| 7 | Toàn vẹn dữ liệu | FK constraints, rollback khi lỗi, kiểm tra overlap đặt phòng |
| 8 | Đa ngôn ngữ | Hỗ trợ Tiếng Việt và Tiếng Anh (I18N), chuyển đổi tiền tệ VND/USD |

#### 3.2.3 Các quy tắc nghiệp vụ

Quy tắc nghiệp vụ là các ràng buộc logic phản ánh chính sách kinh doanh của khách sạn, được hiện thực trong mã nguồn tại tầng ứng dụng.

**QT-01: Quy tắc kiểm tra phòng trống.** Khi khách đặt phòng trong khoảng [ngày_nhận, ngày_trả], hệ thống truy vấn tất cả đơn đặt phòng chưa bị hủy và kiểm tra xung đột thời gian. Hai khoảng bị coi là trùng khi ngày nhận dự kiến của đơn cũ nhỏ hơn ngày trả mới VÀ ngày trả dự kiến của đơn cũ lớn hơn ngày nhận mới. Chỉ phòng không xuất hiện trong bất kỳ đơn nào vi phạm điều kiện trên mới được gán cho đơn mới.

**QT-02: Quy tắc hủy phòng.** Khách chỉ được phép hủy đơn khi trạng thái đơn là "Chờ nhận phòng" hoặc "Đã cọc (Online)" VÀ thời điểm hủy cách ngày nhận phòng dự kiến ít nhất 24 giờ. Nếu vi phạm, hệ thống từ chối hủy và thông báo lý do.

**QT-03: Quy tắc thanh toán cọc.** Số tiền cọc bằng 50% tổng giá trị đơn phòng (đã trừ giảm giá nếu có). Sau khi cọc thành công, trạng thái đơn chuyển từ "Chờ nhận phòng" sang "Đã cọc (Online)".

**QT-04: Quy tắc lập hóa đơn.** Hóa đơn chỉ được tạo khi đơn đặt phòng ở trạng thái "Đã nhận phòng" hoặc "Đang thuê". Tổng tiền = Tiền phòng (đơn giá × số đêm thực tế) + Tổng tiền dịch vụ − Tiền giảm giá − Tiền đã cọc.

**QT-05: Quy tắc đánh giá.** Khách chỉ được viết đánh giá sau khi đơn đặt phòng đã được thanh toán hoàn tất (trạng thái "Đã trả phòng"). Mỗi đơn chỉ được đánh giá một lần duy nhất.

**QT-06: Quy tắc phân quyền.** Nhân viên STAFF không được thực hiện các thao tác: thêm/sửa/xóa loại phòng, phòng, dịch vụ; quản lý nhân sự; quản lý khuyến mãi; xóa khách hàng. Tài khoản admin gốc không thể bị xóa bởi bất kỳ ai.

**QT-07: Quy tắc quyền sở hữu.** Khách hàng chỉ có thể xem hóa đơn, hủy phòng hoặc viết đánh giá cho đơn đặt phòng thuộc về chính mình. Hệ thống đối chiếu mã khách hàng trong session với mã khách hàng trong đơn trước mỗi thao tác.

#### 3.2.4 Danh sách chức năng của hệ thống

Tổng hợp toàn bộ chức năng, hệ thống bao gồm **26 chức năng** (14 phía khách + 12 phía quản trị), được hiện thực bằng **43 route** (23 route client trong `index.py` + 20 route admin trong `admin.py`). Các chức năng bao phủ toàn bộ vòng đời lưu trú: từ khi khách tìm kiếm phòng → đặt phòng → cọc tiền → nhận phòng → sử dụng dịch vụ → trả phòng → thanh toán → đánh giá, cùng với toàn bộ nghiệp vụ quản lý nội bộ.

### 3.3 Kiến trúc hệ thống

#### 3.3.1 Kiến trúc tổng thể của hệ thống

Hệ thống được xây dựng theo mô hình kiến trúc ba tầng (3-Tier Architecture), kết hợp mô hình MVC biến thể phù hợp với Flask framework. Ba tầng bao gồm: tầng trình bày (Presentation), tầng xử lý nghiệp vụ (Business Logic) và tầng dữ liệu (Data).

```
+-------------------------------------------------------------+
|                   TRÌNH DUYỆT (CLIENT)                      |
|       HTML / CSS (Bootstrap 5) / JavaScript (Chart.js)      |
+------------------------------+------------------------------+
                               | HTTP Request / Response
                               v
+-------------------------------------------------------------+
|                 FLASK APPLICATION SERVER                     |
|                                                             |
|  +--------------+  +---------------+  +------------------+  |
|  |  CONTROLLER  |  |     VIEW      |  |      MODEL       |  |
|  |  (Routes)    |  |  (Templates)  |  |      (ORM)       |  |
|  |              |  |               |  |                  |  |
|  | index.py     |  | base.html     |  | models.py        |  |
|  | (23 routes)  |  | base_admin    |  | (14 class ORM)   |  |
|  |              |  | 28 templates  |  | (16 bảng CSDL)   |  |
|  | admin.py     |  |               |  |                  |  |
|  | (20 routes)  |  |               |  | dao.py           |  |
|  |              |  |               |  | (7 hàm DAO)      |  |
|  +------+-------+  +---------------+  +---------+--------+  |
|         |                                       |            |
|  +------+-----------SERVICE LAYER---------------+--------+   |
|  | momo_api.py      | Thanh toán MoMo (HMAC-SHA256)      |   |
|  | email_service.py | Email xác nhận + QR Code            |   |
|  | translations.py  | Đa ngôn ngữ (I18N) VI/EN           |   |
|  | untils.py        | Tiện ích format tiền tệ             |   |
|  +-----------------------------------------------------------+
+------------------------------+------------------------------+
                               | SQLAlchemy ORM + PyMySQL
                               v
+-------------------------------------------------------------+
|                   MySQL 8.0 (hoteldb)                       |
|              16 bảng, FK constraints                        |
|      Host: 127.0.0.1 | Port: 3307 | DB: hoteldb            |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                   DỊCH VỤ BÊN NGOÀI                         |
|  MoMo Payment Gateway (test-payment.momo.vn)                |
|  Gmail SMTP Server (smtp.gmail.com:587)                     |
+-------------------------------------------------------------+
```

#### 3.3.2 Thành phần giao diện người dùng

Tầng giao diện người dùng (Presentation Layer) chịu trách nhiệm hiển thị thông tin và tiếp nhận tương tác từ người dùng cuối. Tầng này được xây dựng bằng sự kết hợp của nhiều công nghệ front-end.

Jinja2 template engine render 28 trang HTML động, sử dụng cơ chế kế thừa template với hai layout chính: `base.html` cho giao diện khách hàng (chứa navbar, hero section, footer) và `base_admin.html` cho giao diện quản trị (chứa sidebar menu, thanh header, vùng nội dung chính). Bootstrap 5 đảm bảo giao diện responsive trên mọi kích thước màn hình. JavaScript xử lý các tương tác phía client như kiểm tra mã voucher bằng AJAX, cập nhật tổng tiền và hiển thị biểu đồ Chart.js.

Giao diện khách hàng gồm các trang: trang chủ (danh sách loại phòng + bộ lọc), chi tiết loại phòng, form đặt phòng, lịch sử đặt phòng, thanh toán online, gọi dịch vụ, xem hóa đơn, form đánh giá, danh sách đánh giá, form đăng ký, form đăng nhập và trang dịch vụ. Giao diện quản trị gồm: Dashboard, quản lý loại phòng, quản lý phòng, quản lý đặt phòng, quản lý dịch vụ, quản lý khách hàng, quản lý hóa đơn, quản lý nhân sự, quản lý khuyến mãi, lập hóa đơn, xem hóa đơn chi tiết và các form sửa.

#### 3.3.3 Thành phần xử lý nghiệp vụ Flask

Tầng xử lý nghiệp vụ (Business Logic Layer) là nơi diễn ra toàn bộ logic của hệ thống. Flask framework đóng vai trò trung tâm, tiếp nhận HTTP request từ trình duyệt, gọi Model để truy vấn hoặc cập nhật dữ liệu, xử lý logic nghiệp vụ và trả về HTTP response kèm template đã render.

Tầng này bao gồm hai module controller chính:

- **`index.py`** (23 route): xử lý mọi nghiệp vụ phía khách hàng — trang chủ, chi tiết phòng, đăng ký/đăng nhập, đặt phòng (kèm Overlap Detection), thanh toán MoMo (kèm HMAC-SHA256), lịch sử đặt phòng, hủy phòng (kiểm tra quy tắc 24h), gọi dịch vụ, xem hóa đơn (kiểm tra ownership), đánh giá, kiểm tra voucher (API JSON) và chuyển ngôn ngữ.

- **`admin.py`** (20 route): xử lý mọi nghiệp vụ phía quản trị — Dashboard (thống kê + biểu đồ), CRUD loại phòng/phòng/dịch vụ/khuyến mãi, quản lý đơn đặt (cập nhật trạng thái), quản lý khách hàng/nhân sự (thêm/xóa + phân quyền), lập hóa đơn (tính tự động), xem bill và xuất CSV.

Ngoài hai controller, tầng này còn có các module service hỗ trợ:

- `momo_api.py`: tạo yêu cầu thanh toán MoMo, ký HMAC-SHA256, gửi POST JSON.
- `email_service.py`: sinh QR Code, tạo template email HTML, gửi qua SMTP.
- `translations.py`: từ điển đa ngôn ngữ 80+ key, hàm `get_text()`, context processor.
- `untils.py`: hàm format tiền tệ VND/USD.

#### 3.3.4 Thành phần cơ sở dữ liệu MySQL

Tầng dữ liệu (Data Layer) chịu trách nhiệm lưu trữ bền vững toàn bộ dữ liệu nghiệp vụ. MySQL 8.0 đóng vai trò hệ quản trị CSDL với database `hoteldb` gồm 16 bảng. Ứng dụng giao tiếp với MySQL thông qua SQLAlchemy ORM (ánh xạ bảng thành class Python) và PyMySQL (database driver).

Tầng Model bao gồm hai file chính:

- **`models.py`** (14 class ORM): mỗi class tương ứng một bảng trong MySQL, khai báo các cột (`db.Column`), khóa chính, khóa ngoại (`db.ForeignKey`) và quan hệ (`db.relationship`). Các class chính: VaiTro, NguoiDung, KhachHang, NhanVien, LoaiPhong, Phong, TienNghi, LoaiPhongTienNghi, KhuyenMai, DatPhong, ChiTietDatPhong, DichVu, SuDung_DichVu, HoaDon, ThanhToan, Review.

- **`dao.py`** (7 hàm DAO): tách biệt logic truy vấn phổ biến khỏi Controller — `lay_danh_sach_loai_phong()`, `lay_danh_sach_phong()`, `lay_danh_sach_dich_vu()`, `lay_danh_sach_khach_hang()`, `xac_thuc_nguoi_dung()`, `kiem_tra_nhan_vien()`, `kiem_tra_quyen_admin()`.

#### 3.3.5 Luồng xử lý tổng quát

Luồng xử lý một request điển hình đi qua các bước sau:

1. **Trình duyệt** gửi HTTP request (GET hoặc POST) tới Flask server.
2. **Flask routing** so khớp URL với route decorator (`@app.route()`), gọi hàm controller tương ứng.
3. **Controller** kiểm tra xác thực (đã đăng nhập?) và phân quyền (ADMIN/STAFF/khách?).
4. **Controller** gọi **Model** (qua SQLAlchemy) để truy vấn hoặc cập nhật CSDL. Nếu cần, gọi thêm **Service** (MoMo API, Email, I18N).
5. **Controller** chọn **template Jinja2** phù hợp, truyền dữ liệu vào context.
6. **Jinja2** render template thành HTML hoàn chỉnh.
7. **Flask** trả về HTTP response (HTML, JSON hoặc redirect) cho trình duyệt.
8. **Trình duyệt** hiển thị trang, JavaScript xử lý tương tác bổ sung (nếu có).

Đối với các thao tác ghi dữ liệu (đặt phòng, lập hóa đơn, thêm dịch vụ…), toàn bộ được thực hiện trong một giao dịch CSDL. Nếu bất kỳ bước nào thất bại, `db.session.rollback()` hoàn tác toàn bộ thay đổi.

### 3.4 Phân tích Use Case hệ thống

#### 3.4.1 Xác định tác nhân

Hệ thống có ba tác nhân chính (Actor) và hai tác nhân phụ (hệ thống bên ngoài):

| Tác nhân | Loại | Mô tả |
|----------|------|-------|
| Khách hàng (Customer) | Chính | Người dùng cuối sử dụng giao diện web công khai để đặt phòng, thanh toán, đánh giá |
| Nhân viên lễ tân (Staff) | Chính | Nhân viên vận hành trang quản trị với quyền hạn chế |
| Quản trị viên (Admin) | Chính | Người quản lý toàn bộ hệ thống với toàn quyền |
| MoMo Gateway | Phụ | Hệ thống thanh toán bên ngoài, giao tiếp qua API HTTP |
| SMTP Server | Phụ | Máy chủ email bên ngoài, gửi email xác nhận đặt phòng |

Tác nhân Nhân viên kế thừa toàn bộ Use Case của Khách hàng (vì nhân viên cũng có thể đặt phòng hộ). Tác nhân Admin kế thừa toàn bộ Use Case của Nhân viên, cộng thêm các Use Case quản trị.

#### 3.4.2 Sơ đồ Use Case tổng quát

```mermaid
graph TB
    subgraph "HỆ THỐNG QUẢN LÝ KHÁCH SẠN"
        subgraph "Phía Khách hàng"
            UC1["Đăng ký tài khoản"]
            UC2["Đăng nhập / Đăng xuất"]
            UC3["Tìm kiếm & Lọc phòng"]
            UC4["Xem chi tiết loại phòng"]
            UC5["Đặt phòng trực tuyến"]
            UC6["Áp dụng mã giảm giá"]
            UC7["Thanh toán cọc MoMo"]
            UC8["Xem lịch sử đặt phòng"]
            UC9["Hủy phòng"]
            UC10["Gọi dịch vụ phát sinh"]
            UC11["Xem hóa đơn"]
            UC12["Viết đánh giá Review"]
            UC13["Nhận email xác nhận + QR"]
            UC14["Chuyển ngôn ngữ VI/EN"]
        end
        subgraph "Phía Quản trị ADMIN/STAFF"
            UC15["Dashboard tổng quan"]
            UC16["Quản lý Loại Phòng CRUD"]
            UC17["Quản lý Phòng CRUD"]
            UC18["Quản lý Đặt phòng"]
            UC19["Quản lý Dịch vụ CRUD"]
            UC20["Quản lý Khách hàng"]
            UC21["Quản lý Nhân sự"]
            UC22["Quản lý Khuyến mãi"]
            UC23["Lập Hóa đơn & Thanh toán"]
            UC24["Xem Hóa đơn chi tiết"]
            UC25["Xuất báo cáo CSV"]
            UC26["Tìm kiếm Đơn đặt"]
        end
    end
    KH["Khách hàng"] --> UC1 & UC2 & UC3 & UC4 & UC5 & UC6 & UC7 & UC8 & UC9 & UC10 & UC11 & UC12 & UC13 & UC14
    NV["Nhân viên / Admin"] --> UC15 & UC16 & UC17 & UC18 & UC19 & UC20 & UC21 & UC22 & UC23 & UC24 & UC25 & UC26
```

#### 3.4.3 Đặc tả Use Case đăng ký và đăng nhập

**Use Case UC-01: Đăng ký tài khoản**

| Mục | Nội dung |
|-----|---------|
| **Tên** | Đăng ký tài khoản khách hàng |
| **Tác nhân** | Khách hàng (chưa có tài khoản) |
| **Mô tả** | Khách tạo tài khoản mới để sử dụng các chức năng đặt phòng |
| **Điều kiện tiên quyết** | Khách chưa đăng nhập |
| **Luồng chính** | 1. Khách truy cập trang đăng ký (`/dang-ky`). 2. Khách nhập thông tin: tên đăng nhập, email, mật khẩu, xác nhận mật khẩu, họ tên, số điện thoại, số CCCD. 3. Hệ thống kiểm tra: tên đăng nhập, email và CCCD chưa tồn tại; mật khẩu và xác nhận khớp nhau. 4. Hệ thống mã hóa mật khẩu bằng `generate_password_hash()`. 5. Hệ thống tạo đồng thời bản ghi NguoiDung (mã ND_ + UUID) và KhachHang (mã KH_ + UUID) trong cùng một giao dịch. 6. Hệ thống hiển thị thông báo đăng ký thành công và chuyển hướng trang đăng nhập. |
| **Luồng ngoại lệ** | 3a. Tên đăng nhập/email/CCCD đã tồn tại → hiển thị thông báo lỗi cụ thể. 3b. Mật khẩu không khớp → yêu cầu nhập lại. 5a. Lỗi CSDL → rollback toàn bộ, hiển thị thông báo lỗi hệ thống. |
| **Kết quả** | Tài khoản mới được tạo, khách có thể đăng nhập |

**Use Case UC-02: Đăng nhập**

| Mục | Nội dung |
|-----|---------|
| **Tên** | Đăng nhập vào hệ thống |
| **Tác nhân** | Khách hàng, Nhân viên, Quản trị viên |
| **Mô tả** | Người dùng xác thực danh tính để truy cập các chức năng yêu cầu đăng nhập |
| **Điều kiện tiên quyết** | Người dùng đã có tài khoản, chưa đăng nhập |
| **Luồng chính** | 1. Người dùng truy cập trang đăng nhập (`/dang-nhap`). 2. Người dùng nhập tên đăng nhập và mật khẩu. 3. Hệ thống gọi `xac_thuc_nguoi_dung()` trong DAO: truy vấn NguoiDung theo tên đăng nhập, so sánh mật khẩu hash bằng `check_password_hash()`. 4. Xác thực thành công: hệ thống lưu thông tin người dùng (mã ND, tên, vai trò) vào session. 5. Hệ thống kiểm tra vai trò: nếu là ADMIN/STAFF → chuyển hướng trang quản trị; nếu là khách hàng → chuyển hướng trang chủ. |
| **Luồng ngoại lệ** | 3a. Tên đăng nhập không tồn tại → thông báo "Sai tên đăng nhập hoặc mật khẩu". 3b. Mật khẩu không khớp → thông báo "Sai tên đăng nhập hoặc mật khẩu" (không tiết lộ cụ thể để bảo mật). |
| **Kết quả** | Session được tạo, người dùng được chuyển đến trang phù hợp với vai trò |

#### 3.4.4 Đặc tả Use Case đặt phòng trực tuyến

**Use Case UC-05: Đặt phòng trực tuyến**

| Mục | Nội dung |
|-----|---------|
| **Tên** | Đặt phòng khách sạn trực tuyến |
| **Tác nhân** | Khách hàng (đã đăng nhập) |
| **Mô tả** | Khách chọn loại phòng, nhập thông tin lưu trú và xác nhận đặt phòng |
| **Điều kiện tiên quyết** | Khách đã đăng nhập, loại phòng còn phòng trống trong khoảng ngày yêu cầu |
| **Luồng chính** | 1. Khách chọn loại phòng trên trang chủ, nhấn "Đặt phòng". 2. Hệ thống kiểm tra đăng nhập (chưa → chuyển trang đăng nhập). 3. Hiển thị form đặt phòng: ngày nhận, ngày trả, số khách, email, mã voucher (tùy chọn). 4. Khách nhập thông tin, nhấn xác nhận. 5. Hệ thống kiểm tra: ngày trả > ngày nhận, số khách ≤ sức chứa. 6. Hệ thống chạy Overlap Detection tìm phòng trống. 7. Tạo DatPhong (mã DP_ + UUID) + ChiTietDatPhong (mã CT_ + UUID) trong cùng giao dịch. 8. Cập nhật trạng thái phòng vật lý → "Đang thuê". 9. Gửi email xác nhận kèm mã QR Code. 10. Chuyển hướng trang lịch sử đặt phòng với thông báo thành công. |
| **Luồng ngoại lệ** | 5a. Ngày không hợp lệ → flash "Ngày trả phải sau ngày nhận". 6a. Hết phòng trống → flash "Loại phòng này hết phòng trong khoảng ngày bạn chọn". 7a. Lỗi CSDL → rollback, thông báo lỗi. |
| **Kết quả** | Đơn đặt phòng được tạo, phòng được giữ, khách nhận email xác nhận |

#### 3.4.5 Đặc tả Use Case thanh toán MoMo

**Use Case UC-07: Thanh toán cọc qua MoMo**

| Mục | Nội dung |
|-----|---------|
| **Tên** | Thanh toán đặt cọc 50% qua ví MoMo |
| **Tác nhân** | Khách hàng (đã đăng nhập, có đơn đặt trạng thái "Chờ nhận phòng") |
| **Mô tả** | Khách cọc 50% giá trị đơn phòng qua cổng thanh toán MoMo |
| **Luồng chính** | 1. Khách chọn "Thanh toán cọc" trong lịch sử đặt phòng. 2. Hệ thống hiển thị tóm tắt đơn: loại phòng, số đêm, tổng tiền, tiền cọc 50%. 3. Khách nhấn "Thanh toán MoMo". 4. Hệ thống tạo rawSignature → ký HMAC-SHA256 → POST JSON tới MoMo. 5. MoMo trả về payUrl → hệ thống redirect khách sang MoMo. 6. Khách xác nhận thanh toán trên MoMo. 7. MoMo callback tới `/momo-return` kèm resultCode và transId. 8. resultCode = 0: cập nhật DatPhong → "Đã cọc (Online)", tạo ThanhToan (mã TT_ + UUID). 9. Chuyển hướng lịch sử đặt phòng với thông báo thành công. |
| **Luồng ngoại lệ** | 4a. Lỗi kết nối MoMo → thông báo "Không thể kết nối cổng thanh toán". 7a. resultCode ≠ 0 → thông báo "Thanh toán thất bại hoặc bị hủy". |
| **Kết quả** | Tiền cọc được ghi nhận, trạng thái đơn chuyển "Đã cọc (Online)" |

#### 3.4.6 Đặc tả Use Case lập hóa đơn tại quầy

**Use Case UC-A09: Lập hóa đơn và thanh toán tại quầy**

| Mục | Nội dung |
|-----|---------|
| **Tên** | Lập hóa đơn và thanh toán khi trả phòng |
| **Tác nhân** | Nhân viên lễ tân / Quản trị viên |
| **Mô tả** | Nhân viên tính toán chi phí và tạo hóa đơn thanh toán cho khách trả phòng |
| **Luồng chính** | 1. Nhân viên chọn đơn đặt phòng cần thanh toán trên trang quản lý hóa đơn. 2. Hệ thống tự động tính: Tiền phòng (đơn giá × số đêm) + Tiền dịch vụ − Giảm giá − Đã cọc. 3. Nhân viên chọn phương thức thanh toán (tiền mặt hoặc chuyển khoản). 4. Nhân viên xác nhận tạo hóa đơn. 5. Hệ thống tạo HoaDon (mã HD_) + ThanhToan (mã TT_), cập nhật DatPhong → "Đã trả phòng", cập nhật Phong → "Cần dọn". |
| **Kết quả** | Hóa đơn và bản ghi thanh toán được tạo, phòng chuyển trạng thái "Cần dọn" |

### 3.5 Thiết kế cơ sở dữ liệu

Cơ sở dữ liệu `hoteldb` gồm 16 bảng được thiết kế đạt dạng chuẩn 3 (3NF). Sơ đồ ERD và chi tiết từng bảng được trình bày dưới đây.

*(Lưu ý: Sơ đồ ERD chi tiết và bảng mô tả các thực thể đã được trình bày đầy đủ tại Chương 2 mục 2.2 và 2.3. Phần này tập trung vào lược đồ quan hệ tổng quát giữa các bảng.)*

**Tổng hợp 16 bảng trong CSDL:**

| STT | Tên bảng | Mô tả | Số cột | Quan hệ chính |
|-----|----------|-------|--------|---------------|
| 1 | `vaitro` | Vai trò (ADMIN, STAFF) | 3 | 1-N → NguoiDung |
| 2 | `nguoidung` | Tài khoản đăng nhập | 7 | 1-1 → KhachHang/NhanVien |
| 3 | `khachhang` | Thông tin khách hàng | 7 | 1-N → DatPhong, Review |
| 4 | `nhanvien` | Thông tin nhân viên | 9 | 0-N → DatPhong, SuDung_DichVu |
| 5 | `loaiphong` | Loại phòng | 6 | 1-N → Phong; N-N → TienNghi |
| 6 | `phong` | Phòng cụ thể | 5 | N-1 → LoaiPhong |
| 7 | `tiennghi` | Tiện nghi | 4 | N-N → LoaiPhong |
| 8 | `loaiphongtiennghi` | Bảng trung gian N-N | 3 | FK → LoaiPhong, TienNghi |
| 9 | `khuyenmai` | Mã giảm giá | 4 | Độc lập |
| 10 | `datphong` | Đơn đặt phòng | 11 | FK → KhachHang, NhanVien |
| 11 | `chitietdatphong` | Chi tiết đặt phòng | 5 | FK → DatPhong, Phong |
| 12 | `dichvu` | Dịch vụ bổ sung | 6 | 1-N → SuDung_DichVu |
| 13 | `sudung_dichvu` | Sử dụng dịch vụ | 7 | FK → ChiTietDatPhong, DichVu |
| 14 | `hoadon` | Hóa đơn | 8 | FK → DatPhong; 1-N → ThanhToan |
| 15 | `thanhtoan` | Thanh toán | 7 | FK → HoaDon |
| 16 | `review` | Đánh giá | 5 | FK → DatPhong, KhachHang |

### 3.6 Thiết kế giao diện

Giao diện hệ thống được thiết kế theo hai phần riêng biệt: giao diện khách hàng (Client) và giao diện quản trị (Admin). Cả hai đều sử dụng Bootstrap 5 đảm bảo responsive.

**Giao diện khách hàng** sử dụng layout `base.html` với navbar phía trên (logo, menu điều hướng, nút đăng nhập/đăng ký, chọn ngôn ngữ) và footer phía dưới. Trang chủ gồm hero section với slogan và nút "Đặt Ngay", bộ lọc tìm kiếm và danh sách loại phòng dạng card. Trang chi tiết loại phòng hiển thị đầy đủ thông tin, tiện nghi, đánh giá trung bình và 5 review mới nhất. Form đặt phòng cho phép chọn ngày, số khách, nhập voucher và xem tổng tiền cập nhật tức thì. Trang lịch sử đặt phòng liệt kê các đơn với badge trạng thái mã màu và các nút hành động tương ứng.

**Giao diện quản trị** sử dụng layout `base_admin.html` với sidebar cố định bên trái (menu: Dashboard, Phòng, Dịch vụ, Đặt phòng, Khách hàng, Hóa đơn, Nhân sự, Khuyến mãi) và vùng nội dung chính bên phải. Dashboard hiển thị 4 card thống kê (số phòng trống, đang thuê, cần dọn, doanh thu hôm nay) kèm biểu đồ cột Chart.js doanh thu 12 tháng. Các trang quản lý danh mục sử dụng table Bootstrap hiển thị dữ liệu, modal popup cho form thêm mới, và nút sửa/xóa cho từng bản ghi.

*(Lưu ý: Khi in báo cáo, sinh viên cần chèn ảnh chụp giao diện thực tế vào từng mục tương ứng.)*

---

## CHƯƠNG 4: HIỆN THỰC VÀ KIỂM THỬ

### 4.1 Môi trường phát triển và triển khai

| Thành phần | Chi tiết |
|-----------|---------|
| **Hệ điều hành** | Windows 10/11 |
| **IDE** | PyCharm / VS Code |
| **Ngôn ngữ** | Python 3.10+ |
| **Web Framework** | Flask 3.0.2 |
| **Database Server** | MySQL 8.0 (Host: `127.0.0.1`, Port: `3307`) |
| **Database Name** | `hoteldb` |
| **ORM** | SQLAlchemy 2.0.25 + Flask-SQLAlchemy 3.1.1 |
| **MySQL Driver** | PyMySQL 1.1.0 |
| **WSGI Toolkit** | Werkzeug 3.0.1 |
| **Template Engine** | Jinja2 (tích hợp Flask) |
| **Front-end** | HTML5, CSS3, Bootstrap 5, JavaScript, Chart.js |
| **Payment Gateway** | MoMo Test Environment (`test-payment.momo.vn`) |
| **Quản lý mã nguồn** | Git |

**File `requirements.txt`**:
```
Flask==3.0.2
Flask-SQLAlchemy==3.1.1
PyMySQL==1.1.0
Werkzeug==3.0.1
SQLAlchemy==2.0.25
```

### 4.2 Cấu trúc mã nguồn dự án

**Bảng 4.1: Cấu trúc thư mục mã nguồn**

```
DAN/                              <-- Thư mục gốc dự án
|-- main.py                       <-- Entry point, khởi chạy Flask app
|-- requirements.txt              <-- Danh sách thư viện phụ thuộc
|-- tao_du_lieu.py                <-- Script tạo dữ liệu mẫu (seed data)
|
|-- eapp/                         <-- Package ứng dụng chính
|   |-- __init__.py               <-- Khởi tạo Flask app + SQLAlchemy
|   |-- models.py                 <-- 14 class ORM (165 dòng)
|   |-- dao.py                    <-- 7 hàm Data Access Object (33 dòng)
|   |-- index.py                  <-- 23 routes Controller Client (714 dòng)
|   |-- admin.py                  <-- 20 routes Controller Admin (775 dòng)
|   |-- momo_api.py               <-- Tích hợp MoMo Payment API (54 dòng)
|   |-- email_service.py          <-- Email xác nhận + QR Code (139 dòng)
|   |-- translations.py           <-- Đa ngôn ngữ VI/EN (187 dòng)
|   |-- untils.py                 <-- Hàm format tiền tệ (4 dòng)
|   |
|   |-- templates/                <-- 28 file template HTML (Jinja2)
|   |   |-- base.html             <-- Layout chính Client
|   |   |-- base_admin.html       <-- Layout chính Admin
|   |   |-- trang_chu.html        <-- Trang chủ
|   |   |-- chi_tiet_phong.html   <-- Chi tiết loại phòng
|   |   |-- dang_nhap.html        <-- Form đăng nhập
|   |   |-- dang_ky.html          <-- Form đăng ký
|   |   |-- form_dat_phong.html   <-- Form đặt phòng
|   |   |-- lich_su_dat_phong.html<-- Lịch sử đặt phòng
|   |   |-- thanh_toan_online.html<-- Trang thanh toán cọc MoMo
|   |   |-- goi_dich_vu_khach.html<-- Gọi dịch vụ phát sinh
|   |   |-- hoa_don_khach.html    <-- Hóa đơn phía khách
|   |   |-- review_form.html      <-- Form viết đánh giá
|   |   |-- review_list.html      <-- Danh sách đánh giá
|   |   |-- dich_vu.html          <-- Trang dịch vụ
|   |   |-- quan_tri.html         <-- Dashboard Quản trị
|   |   |-- quan_ly_phong.html    <-- Quản lý Loại phòng
|   |   |-- danh_sach_phong.html  <-- Quản lý Phòng cụ thể
|   |   |-- quan_ly_dat_phong.html<-- Quản lý Đơn đặt phòng
|   |   |-- quan_ly_dich_vu.html  <-- Quản lý Dịch vụ
|   |   |-- quan_ly_khach_hang.html -- Quản lý Khách hàng
|   |   |-- quan_ly_hoa_don.html  <-- Quản lý Hóa đơn
|   |   |-- quan_ly_nhan_su.html  <-- Quản lý Nhân sự
|   |   |-- quan_ly_khuyen_mai.html -- Quản lý Khuyến mãi
|   |   |-- thanh_toan.html       <-- Lập Hóa đơn (Admin)
|   |   |-- xem_hoa_don.html      <-- Xem bill chi tiết (Admin)
|   |   |-- sua_loai_phong.html   <-- Form sửa loại phòng
|   |   |-- sua_phong.html        <-- Form sửa phòng
|   |   +-- sua_dich_vu.html      <-- Form sửa dịch vụ
|   |
|   +-- static/                   <-- Tài nguyên tĩnh (CSS, JS, Images)
|
+-- scratch/                      <-- Thư mục preview email (development)
```

**Tổng kết mã nguồn**:
- **9 file Python** back-end (khoảng 2,085 dòng code)
- **28 file HTML** template front-end
- **14 class ORM** model (16 bảng CSDL)
- **43 routes** (23 client + 20 admin)

---

### 4.3 Chi tiết hiện thực từng module

#### 4.3.1 Module Khởi tạo (`__init__.py`)

File này khởi tạo ứng dụng Flask và cấu hình kết nối MySQL:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'chuyen_nganh_cntt_2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Abc123@127.0.0.1:3307/hoteldb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app=app)
```

#### 4.3.2 Module Models (`models.py`) — 14 Class ORM

Mỗi class tương ứng 1 bảng trong MySQL, sử dụng SQLAlchemy declarative model:

| Class | Bảng | Quan hệ |
|-------|------|---------|
| `VaiTro` | `vaitro` | 1-N -> NguoiDung |
| `NguoiDung` | `nguoidung` | 1-1 -> KhachHang, NhanVien |
| `KhachHang` | `khachhang` | FK(maKH) -> nguoidung.maND; 1-N -> DatPhong |
| `NhanVien` | `nhanvien` | FK(maNV) -> nguoidung.maND |
| `LoaiPhong` | `loaiphong` | 1-N -> Phong; N-N -> TienNghi (qua LoaiPhongTienNghi) |
| `Phong` | `phong` | FK -> loaiphong |
| `TienNghi` | `tiennghi` | N-N -> LoaiPhong (qua LoaiPhongTienNghi) |
| `LoaiPhongTienNghi` | `loaiphongtiennghi` | Composite PK(maLoaiPhong, maTienNghi) |
| `KhuyenMai` | `khuyenmai` | Độc lập (kiểm tra qua API) |
| `DatPhong` | `datphong` | FK -> KhachHang, NhanVien; 1-N -> ChiTietDatPhong |
| `ChiTietDatPhong` | `chitietdatphong` | FK -> DatPhong, Phong; 1-N -> SuDung_DichVu |
| `DichVu` | `dichvu` | 1-N -> SuDung_DichVu |
| `SuDung_DichVu` | `sudung_dichvu` | FK -> ChiTietDatPhong, DichVu, NhanVien |
| `HoaDon` | `hoadon` | FK -> DatPhong; 1-N -> ThanhToan |
| `ThanhToan` | `thanhtoan` | FK -> HoaDon |
| `Review` | `review` | FK -> DatPhong, KhachHang |

#### 4.3.3 Module DAO (`dao.py`) — Data Access Object

DAO layer tách biệt logic truy vấn CSDL khỏi Controller, gồm 7 hàm:

```python
def lay_danh_sach_loai_phong()      # Lấy tất cả loại phòng
def lay_danh_sach_phong()            # Lấy tất cả phòng
def lay_danh_sach_dich_vu()          # Lấy tất cả dịch vụ
def lay_danh_sach_khach_hang()       # Lấy tất cả khách hàng
def xac_thuc_nguoi_dung(ten, mk)    # Xác thực đăng nhập (check hash)
def kiem_tra_nhan_vien(ma_nd)        # Kiểm tra có phải nhân viên
def kiem_tra_quyen_admin(ma_nd)      # Kiểm tra quyền ADMIN
def lay_danh_sach_nhan_vien()        # Lấy danh sách NV + thông tin tài khoản
```

#### 4.3.4 Module Controller Client (`index.py`) — 23 Routes

**Bảng 4.2: Danh sách routes chính phía Client**

| Route | Method | Chức năng |
|-------|--------|-----------|
| `/` | GET | Trang chủ: hiển thị loại phòng, lọc, rating, tiện nghi, top review |
| `/chi-tiet-phong/<ma_loai>` | GET | Chi tiết loại phòng: tiện nghi, đánh giá, số phòng trống |
| `/dang-nhap` | GET, POST | Đăng nhập (xác thực hash password) |
| `/dang-ky` | GET, POST | Đăng ký (tạo NguoiDung + KhachHang) |
| `/dang-xuat` | GET | Đăng xuất (xóa session) |
| `/dat-phong/<ma_loai_phong>` | GET, POST | Đặt phòng: kiểm tra overlap, tạo đơn, gửi email+QR |
| `/lich-su-dat-phong` | GET | Lịch sử đặt phòng của khách đang đăng nhập |
| `/chi-tiet-hoa-don/<ma_dp>` | GET | Xem hóa đơn (kiểm tra quyền sở hữu đơn) |
| `/goi-dich-vu/<ma_dp>` | GET, POST | Gọi dịch vụ phát sinh cho đơn đặt phòng |
| `/thanh-toan-online/<ma_dp>` | GET, POST | Thanh toán cọc 50% qua MoMo |
| `/momo-return` | GET | Callback từ MoMo sau thanh toán |
| `/review/<ma_dp>` | GET, POST | Viết đánh giá (1-5 sao + bình luận) |
| `/review-xem/<ma_dp>` | GET | Xem đánh giá của một đơn |
| `/loai-phong/<ma_loai>/review` | GET | Tất cả đánh giá của một loại phòng |
| `/api/check-voucher` | POST | API kiểm tra mã giảm giá (JSON response) |
| `/huy-phong/<ma_dp>` | GET | Hủy phòng (kiểm tra 24h rule) |
| `/dich-vu` | GET | Trang danh sách dịch vụ (public) |
| `/set-lang/<lang>` | GET | Chuyển ngôn ngữ VI hoặc EN |

**Thuật toán kiểm tra trùng lịch đặt phòng (Overlap Detection)**:

Đây là logic nghiệp vụ quan trọng nhất của hệ thống, đảm bảo không có hiện tượng overbooking:

```python
# Tìm các phòng ĐÃ BỊ ĐẶT trong khoảng thời gian [check_in, check_out]
overlapping_bookings = db.session.query(ChiTietDatPhong.maPhong)\
    .join(DatPhong, ChiTietDatPhong.maDatPhong == DatPhong.maDatPhong)\
    .filter(
        DatPhong.trangThai != 'Đã hủy',                    # Bỏ qua đơn đã hủy
        DatPhong.ngayNhanDuKien < check_out_date,           # Overlap condition 1
        DatPhong.ngayTraDuKien > check_in_date              # Overlap condition 2
    ).subquery()

# Tìm phòng thuộc loại này KHÔNG NẰM TRONG danh sách đã đặt
phong_trong = Phong.query.filter(
    Phong.maLoaiPhong == ma_loai_phong,
    ~Phong.maPhong.in_(overlapping_bookings)
).first()
```

#### 4.3.5 Module Controller Admin (`admin.py`) — 20 Routes

| Route | Method | Chức năng | Quyền |
|-------|--------|-----------|-------|
| `/quan-tri` | GET | Dashboard: thống kê phòng, doanh thu, biểu đồ tháng | STAFF |
| `/quan-ly-phong` | GET | Danh sách loại phòng | STAFF |
| `/quan-ly-phong/them` | POST | Thêm loại phòng | ADMIN |
| `/quan-ly-phong/sua/<ma>` | GET, POST | Sửa loại phòng | ADMIN |
| `/quan-ly-phong/xoa/<ma>` | GET | Xóa loại phòng | ADMIN |
| `/danh-sach-phong` | GET | Danh sách phòng cụ thể | STAFF |
| `/danh-sach-phong/them` | POST | Thêm phòng | ADMIN |
| `/danh-sach-phong/sua/<ma>` | GET, POST | Sửa phòng | ADMIN |
| `/danh-sach-phong/xoa/<ma>` | GET | Xóa phòng | ADMIN |
| `/quan-ly-dat-phong` | GET | Quản lý đơn đặt (tìm kiếm) | STAFF |
| `/quan-ly-dat-phong/cap-nhat/<ma>` | POST | Cập nhật trạng thái đơn | STAFF |
| `/quan-ly-dich-vu` | GET | Danh sách dịch vụ | STAFF |
| `/quan-ly-dich-vu/them` | POST | Thêm dịch vụ | ADMIN |
| `/quan-ly-dich-vu/sua/<ma>` | GET, POST | Sửa dịch vụ | ADMIN |
| `/quan-ly-dich-vu/xoa/<ma>` | GET | Xóa dịch vụ | ADMIN |
| `/quan-ly-khach-hang` | GET | Danh sách khách hàng | STAFF |
| `/quan-ly-hoa-don` | GET | Quản lý hóa đơn + đơn cần thanh toán | STAFF |
| `/thanh-toan/<ma_dp>` | GET, POST | Lập hóa đơn: tính tiền phòng+DV-giảm giá-cọc | STAFF |
| `/xem-hoa-don/<ma_hd>` | GET | Xem bill chi tiết | STAFF |
| `/xuat-hoa-don-csv` | GET | Xuất toàn bộ hóa đơn sang CSV | STAFF |
| `/quan-ly-nhan-su` | GET | Quản lý nhân viên | ADMIN |
| `/quan-ly-nhan-su/them` | POST | Thêm nhân viên | ADMIN |
| `/quan-ly-nhan-su/xoa/<ma>` | GET | Xóa nhân viên (bảo vệ admin gốc) | ADMIN |
| `/quan-ly-khuyen-mai` | GET | Quản lý mã giảm giá | STAFF |
| `/quan-ly-khuyen-mai/them` | POST | Thêm mã KM | ADMIN |
| `/quan-ly-khuyen-mai/doi-trang-thai/<ma>` | GET | Bật/Tắt mã KM | ADMIN |
| `/quan-ly-khuyen-mai/xoa/<ma>` | GET | Xóa mã KM | ADMIN |

#### 4.3.6 Module MoMo Payment (`momo_api.py`)

```python
def create_momo_payment(order_id, amount, order_info, return_url, notify_url):
    """
    Tạo giao dịch thanh toán MoMo.

    Quy trình:
    1. Chuẩn bị tham số (partnerCode, accessKey, requestType=captureWallet)
    2. Tạo rawSignature: chuỗi nối các tham số theo thứ tự alphabet
    3. Ký bằng HMAC-SHA256 với secretKey
    4. POST JSON tới endpoint MoMo -> Nhận payUrl

    Returns: dict chứa payUrl (URL redirect) hoặc None nếu lỗi
    """
```

**Cấu hình MoMo Test**:
| Key | Value |
|-----|-------|
| Endpoint | `https://test-payment.momo.vn/v2/gateway/api/create` |
| Partner Code | `MOMO` |
| Access Key | `F8BBA842ECF85` |
| Secret Key | `K951B6PE1waDMi640xX08PD3vg6EkVlz` |
| Request Type | `captureWallet` |

#### 4.3.7 Module Email và QR Code (`email_service.py`)

```python
def generate_qr_code(data, filename):
    """Sinh ảnh QR Code chứa thông tin đặt phòng, lưu vào static/qrcodes/"""

def send_booking_email(email_to, ho_ten, ma_dp, checkin, checkout, so_ngay, phong, tong_tien):
    """
    1. Gọi generate_qr_code() sinh mã QR
    2. Tạo template email HTML (header vàng, bảng thông tin, QR code)
    3. Gửi email qua SMTP (hoặc lưu preview HTML trong dev mode)
    """
```

#### 4.3.8 Module I18N (`translations.py`)

Hệ thống đa ngôn ngữ tự xây dựng, hỗ trợ **80+ key dịch** cho cả nhãn giao diện và tên dịch vụ:

```python
translations = {
    'vi': {
        'home': 'Trang chủ',
        'book_now': 'Đặt Ngay',
        'luxury_exp': 'Trải Nghiệm Đẳng Cấp',
        'Bia Heineken': 'Bia Heineken',
        # ... 80+ keys
    },
    'en': {
        'home': 'Home',
        'book_now': 'Book Now',
        'luxury_exp': 'Luxury Experience',
        'Bia Heineken': 'Heineken Beer',
        # ... 80+ keys
    }
}

def get_text(lang, key):
    return translations.get(lang, translations['vi']).get(key, key)
```

#### 4.3.9 Module Seed Data (`tao_du_lieu.py`)

Script tạo dữ liệu mẫu ban đầu cho hệ thống:
- **2 vai trò**: ADMIN (Quản trị viên), STAFF (Nhân viên lễ tân)
- **1 tài khoản admin**: username=`admin`, password=`123456` (đã hash)
- **3 loại phòng mẫu**: Standard (500,000 VND), Deluxe (1,200,000 VND), Suite VIP (2,500,000 VND)

---

### 4.4 Giao diện và chức năng cốt lõi

*(Lưu ý: Khi in báo cáo thật, sinh viên cần chèn ảnh chụp giao diện thực tế vào từng mục dưới đây)*

#### 4.4.1 Giao diện Khách hàng (Client)

**a) Trang chủ (`trang_chu.html`)**
- Hero section với slogan "Trải Nghiệm Đẳng Cấp" và nút "Đặt Ngay".
- Form tìm kiếm nhanh: Ngày nhận, Ngày trả, Số khách.
- Bộ lọc: Từ khóa tên phòng, sức chứa tối thiểu, giá tối đa.
- Danh sách loại phòng dạng card: ảnh, tên, giá/đêm, sức chứa, rating trung bình, tiện nghi.
- Section "Khách Hàng Nói Về Chúng Tôi" hiển thị top 3 review từ 4 sao trở lên.

**b) Trang chi tiết loại phòng (`chi_tiet_phong.html`)**
- Thông tin đầy đủ: tên, mô tả, diện tích, sức chứa, giá cơ bản.
- Danh sách tiện nghi của loại phòng (lấy từ bảng LoaiPhongTienNghi).
- Thống kê: số phòng trống / tổng phòng, đánh giá trung bình, số lượt review.
- 5 review mới nhất.
- Nút "Đặt Phòng Ngay".

**c) Form Đặt phòng (`form_dat_phong.html`)**
- Hiển thị thông tin loại phòng đã chọn.
- Input: Ngày nhận, Ngày trả, Số khách, Email liên hệ.
- Hỗ trợ chuyển loại phòng khác (dropdown).
- Input mã khuyến mãi (gọi API `/api/check-voucher` bằng AJAX).
- Tự động tính tổng tiền và tiền giảm.

**d) Thanh toán trực tuyến (`thanh_toan_online.html`)**
- Hiển thị tóm tắt đơn: loại phòng, số đêm, tổng tiền, tiền cọc 50%.
- Chọn phương thức thanh toán: MoMo.
- Redirect sang cổng MoMo để hoàn tất.

**e) Lịch sử đặt phòng (`lich_su_dat_phong.html`)**
- Danh sách tất cả đơn, sắp xếp mới nhất.
- Trạng thái: Badge màu (Chờ nhận = vàng, Đã cọc = xanh, Đã hủy = đỏ).
- Nút hành động: Thanh toán cọc, Gọi dịch vụ, Viết đánh giá, Hủy phòng, Xem hóa đơn.

**f) Đánh giá (`review_form.html`, `review_list.html`)**
- Form: chọn 1-5 sao + viết bình luận.
- Xem: danh sách review, rating trung bình, thông tin khách hàng.

#### 4.4.2 Giao diện Quản trị (Admin)

**a) Dashboard (`quan_tri.html`)**
- Card thống kê: Số phòng trống, Đang thuê, Cần dọn, Doanh thu hôm nay.
- **Biểu đồ cột Chart.js**: Doanh thu theo 12 tháng trong năm.
- Sidebar menu: Dashboard, Phòng, Dịch vụ, Đặt phòng, Khách hàng, Hóa đơn, Nhân sự, Khuyến mãi.

**b) Quản lý Loại phòng, Phòng, Dịch vụ**
- Bảng dữ liệu (Table) hiển thị danh sách.
- Form Modal thêm mới.
- Nút Sửa chuyển sang trang sửa riêng.
- Nút Xóa (xác nhận trước khi xóa, kiểm tra ràng buộc FK).

**c) Quản lý Đặt phòng (`quan_ly_dat_phong.html`)**
- Tìm kiếm theo: mã đặt phòng, tên khách, SĐT.
- Dropdown cập nhật trạng thái: Chờ nhận, Đã nhận, Đang thuê, Đã trả, Đã hủy.
- Tự động trả phòng trống khi cập nhật "Đã trả phòng" hoặc "Đã hủy".

**d) Lập Hóa đơn (`thanh_toan.html`)**
- Tự động tính: Tiền phòng (đơn giá x số ngày thực tế) + Tiền dịch vụ phát sinh - Giảm giá - Đã cọc.
- Chọn phương thức: Tiền mặt / Chuyển khoản.
- Xác nhận tạo HoaDon + ThanhToan, đổi trạng thái phòng thành "Cần dọn".

**e) Xem Hóa đơn (`xem_hoa_don.html`)**
- Bill chi tiết: Thông tin khách, phòng, số ngày, tiền phòng, tiền DV, phụ thu, giảm giá, tổng cộng.
- Nút in hóa đơn.

---

### 4.5 Kiểm thử (Testing)

**Bảng 4.3: Các ca kiểm thử chức năng (Test Cases)**

| STT | Chức năng | Đầu vào (Input) | Kết quả mong đợi | Kết quả thực tế | Đạt |
|-----|-----------|-----------------|-------------------|------------------|-----|
| 1 | Đăng ký tài khoản | Username, email, mật khẩu, họ tên hợp lệ | Tạo NguoiDung + KhachHang, redirect đăng nhập | Đúng như mong đợi | Đạt |
| 2 | Đăng ký trùng username | Username đã tồn tại | Flash lỗi "Lỗi đăng ký", rollback | Đúng như mong đợi | Đạt |
| 3 | Đăng nhập Admin | Tài khoản `admin` / MK `123456` | Redirect `/quan-tri` (Dashboard) | Đúng như mong đợi | Đạt |
| 4 | Đăng nhập Khách | Tài khoản khách hàng đúng | Redirect `/` (Trang chủ) | Đúng như mong đợi | Đạt |
| 5 | Đăng nhập sai | MK sai | Flash "Tên đăng nhập hoặc mật khẩu không đúng!" | Đúng như mong đợi | Đạt |
| 6 | Tìm phòng theo ngày | Ngày nhận và trả đã bị đặt | Loại phòng có phòng trống bị ẩn | Đúng như mong đợi | Đạt |
| 7 | Tìm phòng theo giá | Giá tối đa = 1,000,000 VND | Chỉ hiện Standard (500,000 VND) | Đúng như mong đợi | Đạt |
| 8 | Đặt phòng hợp lệ | Phòng trống, ngày hợp lệ | Tạo DatPhong + ChiTietDatPhong, gửi email QR | Đúng như mong đợi | Đạt |
| 9 | Đặt phòng ngày sai | Ngày trả nhỏ hơn Ngày nhận | Flash "Ngày trả phải lớn hơn ngày nhận!" | Đúng như mong đợi | Đạt |
| 10 | Đặt phòng khi hết | Tất cả phòng loại đó đã đặt | Flash "Hết phòng trống trong khoảng thời gian" | Đúng như mong đợi | Đạt |
| 11 | Đặt phòng chưa đăng nhập | Chưa login | Redirect đăng nhập + Flash cảnh báo | Đúng như mong đợi | Đạt |
| 12 | Áp dụng mã giảm giá hợp lệ | Mã KM đúng, còn lượt | JSON: success=true, phanTramGiam=10 | Đúng như mong đợi | Đạt |
| 13 | Áp dụng mã giảm giá hết hạn | Mã KM trangThai=False | JSON: success=false, "Mã đã hết hạn" | Đúng như mong đợi | Đạt |
| 14 | Thanh toán MoMo | Thanh toán qua MoMo Test | Redirect sang MoMo, resultCode=0 thì "Đã cọc" | Đúng như mong đợi | Đạt |
| 15 | Thanh toán MoMo thất bại | Hủy trên MoMo | resultCode khác 0 thì Flash "Thất bại" | Đúng như mong đợi | Đạt |
| 16 | Hủy phòng trước 24h | Đơn "Chờ nhận", còn hơn 24h | Trạng thái chuyển "Đã hủy", phòng chuyển "Trống" | Đúng như mong đợi | Đạt |
| 17 | Hủy phòng dưới 24h | Đơn "Chờ nhận", dưới 24h | Flash "Chỉ hủy trước 24 giờ!" | Đúng như mong đợi | Đạt |
| 18 | Gọi dịch vụ | Chọn DV + số lượng | Tạo SuDung_DichVu, Flash thành công | Đúng như mong đợi | Đạt |
| 19 | Viết review | 4 sao + bình luận | Tạo Review, redirect xem review | Đúng như mong đợi | Đạt |
| 20 | Review trùng | Đã review đơn này rồi | Flash "Đã đánh giá đơn này rồi!" | Đúng như mong đợi | Đạt |
| 21 | Admin thêm loại phòng | Mã, tên, sức chứa, giá | Tạo LoaiPhong mới, Flash thành công | Đúng như mong đợi | Đạt |
| 22 | Admin xóa phòng đang dính FK | Phòng có đơn đặt | Flash "Không thể xóa" (FK constraint) | Đúng như mong đợi | Đạt |
| 23 | Admin lập hóa đơn | Đơn "Đang thuê" | Tạo HoaDon + ThanhToan, phòng chuyển "Cần dọn" | Đúng như mong đợi | Đạt |
| 24 | Xuất CSV | Click "Xuất CSV" | Download file .csv, mở được trong Excel (UTF-8) | Đúng như mong đợi | Đạt |
| 25 | Chuyển ngôn ngữ | Click flag EN | Toàn bộ giao diện chuyển sang tiếng Anh | Đúng như mong đợi | Đạt |
| 26 | Bảo mật xem hóa đơn | Khách A xem hóa đơn Khách B | Flash "Không có quyền", redirect | Đúng như mong đợi | Đạt |
| 27 | Admin thêm nhân viên | Thông tin NV hợp lệ | Tạo NguoiDung + NhanVien, Flash thành công | Đúng như mong đợi | Đạt |
| 28 | Admin xóa admin gốc | Xóa tài khoản `admin` | Flash "Không thể xóa admin gốc!" | Đúng như mong đợi | Đạt |

---

## CHƯƠNG 5: KẾT QUẢ, ĐÁNH GIÁ VÀ KẾT LUẬN

### 5.1 Kết quả đạt được

Đồ án đã xây dựng thành công **Hệ thống Quản lý và Đặt phòng Khách sạn Trực tuyến** đáp ứng được toàn bộ các mục tiêu đề ra tại Chương 1. Cụ thể:

| Mục tiêu | Trạng thái | Chi tiết |
|----------|-----------|---------|
| Giao diện web cho khách hàng | **Hoàn thành** | Trang chủ, chi tiết phòng, lịch sử, đặt phòng, review — đầy đủ bộ lọc và tìm kiếm |
| Tích hợp thanh toán MoMo | **Hoàn thành** | Thanh toán cọc 50% qua MoMo Test, chữ ký HMAC-SHA256, callback xử lý |
| Trang quản trị Admin | **Hoàn thành** | Dashboard + 8 module quản lý CRUD + biểu đồ doanh thu Chart.js |
| Quản lý toàn diện dữ liệu | **Hoàn thành** | 14 class ORM, 16 bảng CSDL, FK constraints đầy đủ |
| Email xác nhận + QR Code | **Hoàn thành** | Gửi email HTML + QR Code tự động sau đặt phòng |
| Đa ngôn ngữ (I18N) | **Hoàn thành** | 80+ key dịch Tiếng Việt / Tiếng Anh, format tiền tệ VND/USD |
| Mã giảm giá (Voucher) | **Hoàn thành** | CRUD mã KM + API kiểm tra + áp dụng khi đặt phòng |
| Phân quyền ADMIN/STAFF | **Hoàn thành** | Kiểm tra quyền trước mỗi thao tác CRUD |
| Xuất báo cáo CSV | **Hoàn thành** | Download danh sách hóa đơn dạng CSV (UTF-8 BOM, Excel compatible) |

### 5.2 Bàn luận và Đánh giá

#### Ưu điểm

1. **Kiến trúc rõ ràng**: Dự án tuân theo mô hình MVC với sự phân tách rõ ràng giữa Model (`models.py`), View (`templates/`), Controller (`index.py`, `admin.py`), và Service layer (`momo_api.py`, `email_service.py`).

2. **CSDL toàn diện**: 14 bảng với quan hệ phức tạp (1-1, 1-N, N-N) bao quát được đa số nghiệp vụ của một khách sạn thực tế: từ quản lý quyền, loại phòng, tiện nghi, đặt phòng, dịch vụ phát sinh, hóa đơn, thanh toán, đến đánh giá.

3. **Bảo mật nhiều lớp**:
   - Mật khẩu: hash scrypt/pbkdf2 (Werkzeug).
   - Thanh toán: HMAC-SHA256 (MoMo).
   - Session: secret_key + kiểm tra quyền sở hữu.
   - Phân quyền: ADMIN/STAFF/KhachHang.

4. **Logic nghiệp vụ thông minh**:
   - Overlap Detection: Đảm bảo không overbooking.
   - 24-hour Cancellation Rule: Bảo vệ khách sạn khỏi hủy phòng sát giờ.
   - Tự động trả phòng trống khi check-out hoặc hủy.
   - Tính tiền chính xác: tiền phòng + dịch vụ - giảm giá - đã cọc.

5. **Trải nghiệm người dùng tốt**:
   - Responsive (Bootstrap 5).
   - Đa ngôn ngữ VI/EN.
   - Flash messages thân thiện.
   - Email xác nhận + QR Code.

#### Nhược điểm

1. **Front-end còn đơn giản**: Sử dụng Server-Side Rendering (Jinja2) thay vì SPA (React/Vue), giới hạn trải nghiệm tương tác real-time.

2. **Thiếu xác thực MoMo callback**: Chưa verify signature khi nhận callback từ MoMo (chỉ kiểm tra `resultCode`).

3. **DAO layer mỏng**: Module `dao.py` chỉ có 7 hàm cơ bản, phần lớn logic truy vấn vẫn nằm trực tiếp trong Controller.

### 5.3 Hạn chế và hướng phát triển

#### Hạn chế

| STT | Hạn chế | Mức độ ảnh hưởng |
|-----|---------|-----------------|
| 1 | Giao diện Front-end chưa tối ưu hiệu ứng UX/UI (animation, transition) | Trung bình |
| 2 | Thiếu thông báo thời gian thực (Real-time Notification) khi có đặt phòng mới | Thấp |
| 3 | Email service đang ở chế độ Mock (chưa kết nối SMTP thật) | Trung bình |
| 4 | Chưa có upload ảnh cho phòng (hiện dùng ảnh mặc định) | Trung bình |
| 5 | Chưa có pagination cho danh sách dài (phòng, hóa đơn, khách hàng) | Thấp |

#### Hướng phát triển tương lai

| STT | Hướng phát triển | Công nghệ đề xuất |
|-----|-----------------|------------------|
| 1 | Tích hợp SMTP thật (Gmail) để gửi email xác nhận production | smtplib, Gmail App Password |
| 2 | Xác thực callback MoMo (verify HMAC signature on return) | HMAC-SHA256 verify |
| 3 | Real-time notification (WebSocket) khi có đặt phòng mới | Flask-SocketIO |
| 4 | Upload ảnh phòng (multiple images per room type) | Flask-Uploads, Cloudinary |
| 5 | AI gợi ý phòng dựa trên lịch sử đặt phòng | scikit-learn, Collaborative Filtering |
| 6 | Phân tích cảm xúc từ Review (Sentiment Analysis) | NLP, transformers |
| 7 | Responsive admin với Dashboard nâng cao | React/Vue.js SPA, Recharts |
| 8 | Containerization và CI/CD | Docker, GitHub Actions |
| 9 | Pagination + Full-text search | Flask-Paginate, Elasticsearch |
| 10 | Tích hợp thêm cổng thanh toán: VNPay, ZaloPay | VNPay API, ZaloPay API |

---

## TÀI LIỆU THAM KHẢO

[1] Miguel Grinberg, *Flask Web Development: Developing Web Applications with Python*, 2nd Edition, O'Reilly Media, 2018.

[2] Flask Documentation, *Flask Official Documentation*, URL: https://flask.palletsprojects.com/

[3] SQLAlchemy, *SQLAlchemy 2.0 Documentation*, URL: https://docs.sqlalchemy.org/

[4] MoMo Developers, *Tài liệu hướng dẫn tích hợp thanh toán MoMo v2*, URL: https://developers.momo.vn/

[5] Bootstrap Team, *Bootstrap 5 Documentation*, URL: https://getbootstrap.com/docs/5.0/

[6] Chart.js, *Chart.js Documentation*, URL: https://www.chartjs.org/docs/

[7] Python Software Foundation, *Python 3.10 Documentation*, URL: https://docs.python.org/3.10/

[8] Werkzeug, *Security Helpers — Werkzeug Documentation*, URL: https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security

[9] Jinja2, *Jinja2 Template Engine Documentation*, URL: https://jinja.palletsprojects.com/

[10] MySQL, *MySQL 8.0 Reference Manual*, URL: https://dev.mysql.com/doc/refman/8.0/en/

[11] PyMySQL, *PyMySQL Documentation*, URL: https://pymysql.readthedocs.io/

[12] qrcode library, *Python QR Code Image Generator*, URL: https://pypi.org/project/qrcode/

---

## PHỤ LỤC

### Phụ lục A: Hướng dẫn cài đặt và chạy dự án

```bash
# 1. Clone hoặc giải nén mã nguồn
cd DAN/

# 2. Tạo Virtual Environment
python -m venv .venv
.venv\Scripts\activate       # Windows

# 3. Cài đặt thư viện
pip install -r requirements.txt

# 4. Khởi tạo MySQL Database
# Tạo database 'hoteldb' trong MySQL (port 3307)
# mysql -u root -pAbc123 -P 3307 -e "CREATE DATABASE hoteldb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# 5. Tạo dữ liệu mẫu
python tao_du_lieu.py

# 6. Chạy ứng dụng
python main.py

# 7. Truy cập
# Client:  http://127.0.0.1:5000/
# Admin:   http://127.0.0.1:5000/quan-tri
# Tài khoản Admin: admin / 123456
```

### Phụ lục B: Tài khoản thử nghiệm

| Vai trò | Username | Password | Ghi chú |
|---------|----------|----------|---------|
| Admin / Quản lý | `admin` | `123456` | Toàn quyền quản trị |
| Khách hàng | (Tự đăng ký) | (Tự chọn) | Đăng ký tại `/dang-ky` |

---

*Báo cáo được hoàn thành vào tháng 09/2026*
*Trường Đại học Mở Thành Phố Hồ Chí Minh — Khoa Công nghệ Thông tin*
