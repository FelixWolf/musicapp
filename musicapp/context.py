from django.conf import settings
import datetime
import uuid
from user.models import User

def Context(request):
    context = {
        "LOGGED_IN": False,
        "APP_NAME": settings.APP_NAME
    }
    
    if "userid" in request.session:
        try:
            user = User.objects.get(id=uuid.UUID(request.session["userid"]))
            context["USERNAME"] = user.username
            context["DISPLAYNAME"] = user.displayname
            context["USER_ID"] = request.session["userid"]
            context["LOGGED_IN"] = True
        
        except User.DoesNotExist:
            pass
    
    return context
