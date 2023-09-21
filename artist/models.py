from django.db import models
import uuid

class Artist(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    
    name = models.CharField(max_length=255)
    
    artwork = models.UUIDField(null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL, related_name="artist_creator")
    
    modified = models.DateTimeField(auto_now=True)
    modifier = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL, related_name="artist_modifier")
    
    score = models.IntegerField(default=0)


class ArtistVote(models.Model):
    id = models.PositiveBigIntegerField(primary_key = True)
    
    class Meta:
        unique_together = ('artist', 'user',)
    
    artist = models.ForeignKey("artist.Artist", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    
    vote = models.SmallIntegerField()