import uuid
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
from django.utils import timezone
import os

  
# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=30, null=True,unique=True)
    slug=models.SlugField(unique=True,null=True)
    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"slug": self.slug})
    def __str__(self):
        return self.category 
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)    
    return os.path.join('uploads', filename)
#
class Post(models.Model):
    titte=models.CharField(max_length=200,unique=True,null=True)
    image=ResizedImageField(size=[1000, 800],crop=['middle', 'center'], upload_to='thumbnail_post',)
    content=RichTextField()
    category=models.ManyToManyField(Category,related_name='posts')
    slug=models.SlugField(unique=True,null=True)
    day_create=models.DateTimeField(auto_now_add=True)
    view=models.IntegerField(default=1)
    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"slug": self.slug})
    def __str__(self):
        return self.titte

