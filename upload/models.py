from django.db import models
import uuid

class Upload(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    
    data = models.JSONField(max_length=65535)
    
    created = models.DateTimeField(auto_now_add=True)
    