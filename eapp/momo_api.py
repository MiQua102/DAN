import json
import uuid
import hmac
import hashlib
import urllib.request
from eapp import app

def create_momo_payment(order_id, amount, order_info, return_url, notify_url):
    # Public MoMo Test Keys
    endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
    partnerCode = "MOMO"
    accessKey = "F8BBA842ECF85"
    secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
    
    orderInfo = order_info
    amount = str(int(amount))
    orderId = str(order_id)
    requestId = str(uuid.uuid4())
    requestType = "captureWallet"
    extraData = ""
    
    # signature
    rawSignature = f"accessKey={accessKey}&amount={amount}&extraData={extraData}&ipnUrl={notify_url}&orderId={orderId}&orderInfo={orderInfo}&partnerCode={partnerCode}&redirectUrl={return_url}&requestId={requestId}&requestType={requestType}"
    
    h = hmac.new(bytes(secretKey, 'ascii'), bytes(rawSignature, 'ascii'), hashlib.sha256)
    signature = h.hexdigest()
    
    data = {
        'partnerCode' : partnerCode,
        'partnerName' : "Luxury Hotel",
        'storeId' : "LuxuryHotelStore",
        'requestId' : requestId,
        'amount' : amount,
        'orderId' : orderId,
        'orderInfo' : orderInfo,
        'redirectUrl' : return_url,
        'ipnUrl' : notify_url,
        'lang': 'vi',
        'extraData' : extraData,
        'requestType' : requestType,
        'signature' : signature
    }
    
    data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(endpoint, data, {'Content-Type': 'application/json'})
    
    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode('utf-8'))
        return result
    except Exception as e:
        print(f"Lỗi MoMo API: {str(e)}")
        return None
