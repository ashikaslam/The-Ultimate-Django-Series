from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # What tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type (Procuct,video,article)
    # ID
    content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()





class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

