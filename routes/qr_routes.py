# -*- coding: utf-8 -*-
from bottle import route, response
from controllers.qr_controller import QRController

qr_controller = QRController()

@route('/qr/<uid>', method='POST')
def make_qr(uid):
    response.content_type = 'application/json'
    return qr_controller.makeQR(uid)
