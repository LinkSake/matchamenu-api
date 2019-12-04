# -*- coding: utf-8 -*-
from bottle import route, response
# from bottle_jwt import jwt_auth_required
from controllers.base_controller import BaseController

base_controller = BaseController()


@route('/', method='GET')
def landing():
    response.content_type = 'application/json'
    return base_controller.landing()
