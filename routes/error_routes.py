# -*- coding: utf-8 -*-
from bottle import error

error_log = error

for status_code in range(200, 600):
    @error(status_code)
    def errorCustom(error_log):
        error_log.content_type = 'application/json'
        return error_log.body
