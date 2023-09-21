from django.http import HttpResponse, Http404
from django.views.decorators.cache import never_cache
from django.shortcuts import render
from django.conf import settings
from utils.login import createLogin, verifyLogin
from utils.lslrpc import LSLError, llRequestUserKey, llRequestUsername, llRequestDisplayName, llInstantMessage
import uuid
from .models import User

@never_cache
def login(request):
    if request.method == "POST":
        reqAddr = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR", "(UNKNOWN)"))
        try:
            uid = llRequestUserKey(request.POST["username"])
            loginUrl = createLogin(uid)
            llInstantMessage(uid, "A request to log into {site} was made by {addr}. " \
            "If this was you, click here to complete the login:\n{login}\n"\
            "Didn't make this request? Report it to secondlife:///app/agent/796b1537-70d8-497d-934e-0abcc2a60050/im".format(
                site = settings.APP_NAME,
                addr = reqAddr,
                login = request.build_absolute_uri() + loginUrl
            ))
            
        except LSLError as e:
            return render(request, "login.htm", {"state": "error", "reason": str(e)})
        return render(request, "login.htm", {"state": "requested"})
        
    else:
        if all(_ in request.GET for _ in ("uuid", "token")):
            success = verifyLogin(
                request.GET["uuid"],
                request.GET["token"]
            )
            
            if success:
                try:
                    username = llRequestUsername(request.GET["uuid"])
                    displayname = llRequestDisplayName(request.GET["uuid"])
                except LSLError as e:
                    return render(request, "login.htm", {"state": "error", "reason": str(e)})
                
                try:
                    user = User.objects.get(id=uuid.UUID(request.GET["uuid"]))
                except User.DoesNotExist:
                    user = User(id=uuid.UUID(request.GET["uuid"]))
                
                user.username = username
                user.displayname = displayname
                user.save()
                
                request.session["userid"] = request.GET["uuid"]
                return render(request, "login.htm", {"state": "success"})
            
            else:
                return render(request, "login.htm", {"state": "error", "reason": "Invalid or expired token."})
        
        else:
            return render(request, "login.htm", {"state": "login"})

@never_cache
def logout(request):
    if request.method == 'POST':
        request.session.flush()
        return render(request, "logout.htm", {"success": True})
    
    else:
        return render(request, "logout.htm", {"success": False})

@never_cache
def userSettings(request):
    if request.method == 'POST':
        return render(request, "settings.htm", {"success": True})
    
    else:
        return render(request, "settings.htm", {"success": None})

@never_cache
def profile(request, userid = None):
    return render(request, "profile.htm", {})

