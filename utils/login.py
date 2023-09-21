import hashlib
import base64
import struct
import urllib.parse
import urllib.request
import time
from django.core.signing import Signer

#Derive secret
SECRET = Signer().sign("LoginUrl").encode()

HASHALGO = hashlib.sha256
sTime = struct.Struct(">Q")

def verifyLogin(uuid, token):
    token = base64.urlsafe_b64decode(token + ('=' * (-len(token) % 4)))
    tokentime, = sTime.unpack_from(token)
    
    if tokentime + (60 * 1) < time.time():
        return False
    
    test = HASHALGO()
    test.update(uuid.encode())
    test.update(b":")
    test.update(token[:sTime.size])
    test.update(b":")
    test.update(SECRET)
    
    return token[sTime.size:] == test.digest()
    

def createLogin(uuid):
    tokentime = round(time.time())
    token = HASHALGO()
    token.update(uuid.encode())
    token.update(b":")
    token.update(sTime.pack(tokentime))
    token.update(b":")
    token.update(SECRET)
    token = base64.urlsafe_b64encode(sTime.pack(tokentime) + token.digest()).decode().rstrip("=")
    loginUrl = "?uuid={}&token={}".format(
        uuid,
        token
    )
    return loginUrl

def usernameToKey(username):
    pass