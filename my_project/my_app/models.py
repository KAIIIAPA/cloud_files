from django.conf import settings
from django.db import models

# Create your models here.

class Allfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

