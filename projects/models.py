from django.db import models
from django_dropbox_storage.storage import DropboxStorage

# Create your models here.
DROPBOX_STORAGE = DropboxStorage()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects/img',storage=DROPBOX_STORAGE)
def __str__(self):
    return self.title
class Meta:
    verbose_name = 'Project Lists'
