import qrcode
import qrcode.image.svg

class QRController():

    def __init__(self):
        '''
        Función constructora
        '''
        super().__init__()
        # self.db = db

    def makeQR(data):
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(data, image_factory=factory)
        print(img)
        return {'msg':'YAHOO!'}