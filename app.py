# -*- coding: utf-8 -*-
from sys import stdout
from import_env import os
from bottle import run, default_app, response

from error import handler
from cors import EnableCors, route

from routes.base_routes import route
from routes.qr_routes import route
from routes.error_routes import error

# from auth.jwt_custom_providers import CustomJWTProviderPlugin

#Confugure the server
app = default_app()
app.install(EnableCors())
# app.install(CustomJWTProviderPlugin(
#     keyword='jwt',
#     auth_endpoint='/auth',
#     fields=('email', 'password'),
#     secret=os.environ.get('secret'),
#     ttl=os.environ.get('ttl'),
#     response=response)
# )
app.error_handle = handler
stdout.flush()

run(host = 'localhost', port = 8080, debug=True)
