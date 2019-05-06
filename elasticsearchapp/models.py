from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from .search import BlogPostIndex


# Blogpost to be indexed into ElasticSearch
class BlogPost(models.Model):
   username = models.ForeignKey(User, on_delete=models.CASCADE)
   posted_date = models.DateField(default=timezone.now)
   title = models.CharField(max_length=200)
   text = models.TextField(max_length=1000)
