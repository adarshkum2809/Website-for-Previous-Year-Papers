from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class News(models.Model):
    news_title= models.CharField(max_length=100)
    news_desc=HTMLField()
    news_slug= AutoSlugField( populate_from='news_title',unique=True,null=True,default=None)
    news_img= models.FileField(upload_to="news/",max_length=250,null=True,default=True)
    
# Create your models here.