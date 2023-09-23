from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Rendition(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    
    track = models.ForeignKey("track.Track", null=True, on_delete=models.SET_NULL, related_name="rendition_track")
    
    title = models.CharField(max_length=255)
    
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL, related_name="rendition_creator")
    
    modified = models.DateTimeField(auto_now=True)
    modifier = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL, related_name="rendition_modifier")
    
    duration = models.FloatField()
    
    segmentLength = models.FloatField()
    
    _segments = models.BinaryField(max_length=65535)
    
    @property
    def segments(self):
        return [uuid.UUID(bytes=self._segments[i:i+16]) for i in range(0, len(self._segments), 16)]

    @segments.setter
    def segments(self, value):
        if len(value) > 4095:
            raise ValueError("Too many segments!")
        
        self._segments = b"".join([i.bytes for i in value])
    
    score = models.IntegerField(default=0)


class RenditionVote(models.Model):
    id = models.PositiveBigIntegerField(primary_key = True)
    
    class Meta:
        unique_together = ('rendition', 'user',)
    
    rendition = models.ForeignKey("Rendition", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    
    vote = models.SmallIntegerField()


