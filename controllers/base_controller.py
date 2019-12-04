# -*- coding: utf-8 -*-
import json
# from db_connection import db
from bottle import abort, request
# from bson.json_util import loads, dumps

class BaseController():

    def __init__(self):
        '''
        Funcion constructora
        '''
        self.request = request

    def landing(self):
        '''
        Funcion encargada de regresar
        la landing
        '''
        return {'msg':'It works!'}

    def abort_error(self, status_code, msg):
        '''
        Funcion encargada de abortar cuando un
        error salga
        '''
        abort(status_code, str(json.dumps({'error': msg})))