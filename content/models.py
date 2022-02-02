from django.db import models

# Create your models here.
class Feed(models.Model):
    content     = models.TextField()
    image       = models.TextField()
    profile_img = models.TextField()
    user_id     = models.TextField()
    like_count  = models.IntegerField()