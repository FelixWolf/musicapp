from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Track(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    
    title = models.CharField(max_length=255)
    
    trackNumber = models.SmallIntegerField(null=True)
    
    artist = models.ForeignKey("artist.Artist", null=True, on_delete=models.SET_NULL)
    album = models.ForeignKey("album.Album", null=True, on_delete=models.SET_NULL)
    
    artwork = models.UUIDField(null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL, related_name="track_creator")
    
    modified = models.DateTimeField(auto_now=True)
    modifier = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL, related_name="modifier_modifier")
    
    rendition = models.ForeignKey("rendition.Rendition", null=True, on_delete=models.SET_NULL, related_name="track_rendition")
    
    class Maturity(models.IntegerChoices):
        GENERAL = 13, _("General")
        MODERATE = 21, _("Moderate")
        ADULT = 42, _("Adult")
        __empty__ = _("(Unrated)")

    maturity = models.IntegerField(choices=Maturity.choices, null=True)
    
    score = models.IntegerField(default=0)


class TrackVote(models.Model):
    id = models.PositiveBigIntegerField(primary_key = True)
    
    class Meta:
        unique_together = ('track', 'user',)
    
    track = models.ForeignKey("track.Track", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    
    vote = models.SmallIntegerField()