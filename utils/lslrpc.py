import datetime
import random
import json
import urllib.request
import urllib.parse
import urllib.error
import ssl
from django.conf import settings

INSECURE_CONTEXT = ssl.create_default_context()
INSECURE_CONTEXT.check_hostname = False
INSECURE_CONTEXT.verify_mode = ssl.CERT_NONE

class LSLError(Exception):
    pass

def executeLSLFunc(func, pathargs, data = None, timeout = 1.0):
    if not hasattr(settings, "LSLRPC"):
        raise LSLError("LSLRPC setting isn't set!")
    
    
    req = urllib.request.Request(
        settings.LSLRPC["host"] + "/" + func + "/" + "/".join([urllib.parse.quote(str(i)) for i in pathargs]),
        data = (data if data == bytes else str(data).encode()) if data else None,
        method = "POST" if data else "GET",
        headers = {
            "Content-type": "Application/Json",
            "Authorization": "Bearer {}".format(settings.LSLRPC["token"])
        }
    )
    
    try:
        with urllib.request.urlopen(req, timeout = timeout, context = INSECURE_CONTEXT) as res:
            return res.read().decode()
    
    except urllib.error.HTTPError as res:
        raise LSLError(res.read().decode())
    
    except TimeoutError as res:
        raise LSLError("LSLRPC timeout")
    

#Communication
def llInstantMessage(user, message):
    return executeLSLFunc("llInstantMessage", (user,), message, timeout = 7)

#Dataserver
def llGetNotecardLine(name, line):
    return executeLSLFunc("llGetNotecardLine", (name, line,))

def llGetNumberOfNotecardLines(name):
    return executeLSLFunc("llGetNumberOfNotecardLines", (name,))

DATA_ONLINE = 1
DATA_NAME = 2
DATA_BORN = 3
DATA_RATING = 4
DATA_PAYINFO = 8
def llRequestAgentData(agent, data):
    return executeLSLFunc("llRequestAgentData", (agent, data))

def llRequestDisplayName(agent):
    return executeLSLFunc("llRequestDisplayName", (agent,))

def llRequestUsername(agent):
    return executeLSLFunc("llRequestUsername", (agent,))

def llRequestUserKey(username):
    return executeLSLFunc("llRequestUserKey", (username,))

DATA_SIM_POS = 5
DATA_SIM_STATUS = 6
DATA_SIM_RATING = 7
def llRequestSimulatorData(region, data):
    return executeLSLFunc("llRequestSimulatorData", (region, data,))

def llCreateKeyValue(k, v):
    return executeLSLFunc("llCreateKeyValue", (k,), v)

def llDataSizeKeyValue():
    return executeLSLFunc("llDataSizeKeyValue")

def llDeleteKeyValue(k):
    return executeLSLFunc("llDeleteKeyValue", (k,))

def llKeyCountKeyValue():
    return executeLSLFunc("llKeyCountKeyValue")

def llKeysKeyValue(first, count):
    return executeLSLFunc("llKeysKeyValue", (first, count,))

def llReadKeyValue(k):
    return executeLSLFunc("llReadKeyValue", (k,))

def llUpdateKeyValue(k, v, checked = None):
    return executeLSLFunc("llUpdateKeyValue", (k,), v)