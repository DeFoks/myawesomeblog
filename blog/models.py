from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=150)
    post_date = models.DateTimeField(null=True)
    post_text = models.TextField(blank=True)
    post_image = models.ImageField(upload_to = 'blog_mages/')
