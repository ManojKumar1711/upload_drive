from django.db import models

# Create your models here.
class File(models.Model):
    title = models.CharField(max_length=100)
    owner_name = models.CharField(max_length = 50)
    file = models.FileField(upload_to = 'upload/files/')

    def __str__(self):
        return self.title

