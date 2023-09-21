from django.db import models
import uuid

class Album(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    
    title = models.CharField(max_length=255)
    
    artist = models.ForeignKey("artist.Artist", null=True, on_delete=models.SET_NULL)
    
    artwork = models.UUIDField(null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL, related_name="album_creator")
    
    modified = models.DateTimeField(auto_now=True)
    modifier = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL, related_name="album_modifier")
    
    score = models.IntegerField(default=0)


class AlbumVote(models.Model):
    id = models.PositiveBigIntegerField(primary_key = True)
    
    class Meta:
        unique_together = ('album', 'user',)
    
    album = models.ForeignKey("album.Album", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    
    vote = models.SmallIntegerField()