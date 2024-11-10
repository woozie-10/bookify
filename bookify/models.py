from django.db import models
from django.conf import settings

class Book(models.Model):
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='books')
    file = models.FileField(upload_to='books/')
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=60)
    cover = models.FileField(upload_to='covers/')
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
