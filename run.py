# -*- coding: utf-8 -*-
import re
import sys
from gunicorn.app.wsgiapp import run

open('error.log', 'w').close()

sys.argv = [
    'gunicorn', '-w 1', '-b 0.0.0.0',
    'app:app', '--reload', '--error-logfile',
    './error.log', '--capture-output', '--enable-stdio-inheritance']

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(run())
