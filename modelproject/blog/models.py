from django.db import models
from account.models import CustomUser
from django.conf import settings

# Create your models here.

class Blog(models.Model):
  genre_choices = [
    ('Indie', 'Indie'),
    ('Rock', 'Rock'),
    ('K-pop', 'K-pop'),
    ('Pop', 'Pop'),
    ('Else', 'Else')
  ]
  user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
  pub_date = models.DateTimeField()
  title = models.CharField(max_length=100)
  singer = models.CharField(max_length=100)
  code = models.CharField(max_length=300, null=True, blank=True)
  genre = models.CharField(max_length=10, choices = genre_choices)
  memo = models.TextField(null=True, blank=True)
  lyrics = models.TextField(null=True, blank=True)
  image = models.ImageField(upload_to='blog/', blank=True, null=True)

  def __str__(self):
    return self.title

  def summary(self):
    return self.memo[:70]

class Comment(models.Model):
  post = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank = True, on_delete=models.CASCADE)
  content = models.CharField(max_length=500)
  created_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.content
