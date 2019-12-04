import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

try:
    from env import os
    cred = credentials.Certificate(os.environ.get('firebase_json'))
    firebase_admin.initialize_app(cred)
except:
    firestore_cred = os.environ.get('firebase_json')
    firestore_cred = json.loads(firestore_cred)
    cred = credentials.Certificate(firestore_cred)
    firebase_admin.initialize_app(cred)

db = firestore.client()