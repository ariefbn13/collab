from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects/img')
def __str__(self):
    return self.title
class Meta:
    verbose_name = 'Project Lists'
