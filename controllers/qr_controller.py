import base64
import os.path
import qrcode
import qrcode.image.svg
from bottle import request
from db_connection import db

class QRController():

    def __init__(self):
        '''
        Función constructora
        '''
        super().__init__()

    def makeQR(self, uid):
        data = request.json
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(data, image_factory=factory).save('qr.svg')
        with open("qr.svg", "rb") as image_file:
            encoded_img = base64.b64encode(image_file.read())
            doc = db.collection('restaurant').document(uid)
            doc.update({'qr': encoded_img})
        return {'msg':'YAHOO!'}