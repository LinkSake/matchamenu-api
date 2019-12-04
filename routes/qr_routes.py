# -*- coding: utf-8 -*-
from bottle import route, response
from controllers.qr_controller import QRController

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

qr_controller = QRController()

@route('/qr', method='POST')
def make_qr():
    response.content_type = 'application/json'
    return qr_controller.makeQR()
