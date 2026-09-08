import os
import qrcode
from datetime import datetime

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to static/qrcodes
    save_dir = os.path.join(os.path.dirname(__file__), 'static', 'qrcodes')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    filepath = os.path.join(save_dir, filename)
    img.save(filepath)
    return f"/static/qrcodes/{filename}"

def send_booking_email(email_to, ho_ten, ma_dp, checkin, checkout, so_ngay, phong, tong_tien):
    # Generate QR Code for booking
    qr_filename = f"{ma_dp}.png"
    qr_data = f"Booking ID: {ma_dp} | Name: {ho_ten} | Check-in: {checkin.strftime('%d/%m/%Y')}"
    qr_url = generate_qr_code(qr_data, qr_filename)
    
    # Generate HTML Email Content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }}
            .header {{ background-color: #4A3B32; color: #D4AF37; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; }}
            .footer {{ background-color: #f4f6f9; text-align: center; padding: 15px; font-size: 12px; color: #777; }}
            .bill-table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            .bill-table th, .bill-table td {{ padding: 10px; border-bottom: 1px solid #ddd; text-align: left; }}
            .text-gold {{ color: #D4AF37; font-weight: bold; }}
            .qr-box {{ text-align: center; margin-top: 30px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>LUXURY HOTEL</h2>
                <p>Xác Nhận Đặt Phòng Thành Công</p>
            </div>
            <div class="content">
                <p>Kính chào quý khách <strong>{ho_ten}</strong>,</p>
                <p>Cảm ơn quý khách đã tin tưởng và lựa chọn Luxury Hotel. Chúng tôi xin xác nhận đơn đặt phòng của quý khách như sau:</p>
                
                <table class="bill-table">
                    <tr>
                        <th>Mã Đặt Phòng:</th>
                        <td class="text-gold">{ma_dp}</td>
                    </tr>
                    <tr>
                        <th>Ngày Nhận Phòng:</th>
                        <td>{checkin.strftime('%d/%m/%Y')}</td>
                    </tr>
                    <tr>
                        <th>Ngày Trả Phòng:</th>
                        <td>{checkout.strftime('%d/%m/%Y')}</td>
                    </tr>
                    <tr>
                        <th>Số Đêm:</th>
                        <td>{so_ngay} đêm</td>
                    </tr>
                    <tr>
                        <th>Hóa Đơn Tạm Tính:</th>
                        <td class="text-gold">{tong_tien:,.0f} VND</td>
                    </tr>
                </table>
                
                <div class="qr-box">
                    <p>Vui lòng xuất trình mã QR này tại quầy lễ tân khi nhận phòng:</p>
                    <img src="cid:qrcode_image" alt="QR Code" width="200" style="border: 2px solid #ddd; padding: 10px; border-radius: 10px;">
                </div>
            </div>
            <div class="footer">
                <p>Luxury Hotel | 123 Đường Hoa Hồng, Quận 1, TP.HCM</p>
                <p>Hotline: 1900 1234 | Email: support@luxuryhotel.com</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # -------------------------------------------------------------
    # MOCK SMTP SENDING - WE SAVE TO SCRATCH FILE FOR DEMONSTRATION
    # -------------------------------------------------------------
    
    preview_path = os.path.join(os.path.dirname(__file__), '..', 'scratch', f'email_preview_{ma_dp}.html')
    # Replace cid with local path for preview
    preview_html = html_content.replace('cid:qrcode_image', f'/static/qrcodes/{qr_filename}')
    
    with open(preview_path, 'w', encoding='utf-8') as f:
        f.write(preview_html)
        
    print(f"Mock Email sent to {email_to}. Preview saved to {preview_path}")
    
    # In a real app, you would use smtplib or Flask-Mail here:
    '''
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    import smtplib
    
    msg = MIMEMultipart('related')
    msg['Subject'] = f"Xác nhận đặt phòng tại Luxury Hotel - {ma_dp}"
    msg['From'] = "no-reply@luxuryhotel.com"
    msg['To'] = email_to

    msg.attach(MIMEText(html_content, 'html'))

    # Attach QR Code Image
    qr_filepath = os.path.join(os.path.dirname(__file__), 'static', 'qrcodes', qr_filename)
    with open(qr_filepath, 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data, name=qr_filename)
    image.add_header('Content-ID', '<qrcode_image>')
    msg.attach(image)

    # Send Email (Need real credentials)
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.starttls()
    # server.login('YOUR_GMAIL', 'APP_PASSWORD')
    # server.send_message(msg)
    # server.quit()
    '''
    return True
