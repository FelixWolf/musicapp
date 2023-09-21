from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class User(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    
    username = models.CharField(max_length=255)
    displayname = models.CharField(max_length=255)
    
    registered = models.DateTimeField(auto_now_add=True)
    lastOnline = models.DateTimeField(auto_now=True)
    
    class Access(models.IntegerChoices):
        BANNED = 0, _("Banned")
        MEMBER = 10, _("Member")
        TRUSTED = 20, _("Trusted")
        MODERATOR = 30, _("Moderator")
        ADMINISTRATOR = 40, _("Administrator")

    access = models.IntegerField(
        choices=Access.choices,
        default=Access.MEMBER,
    )