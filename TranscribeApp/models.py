from django.db import models
from django.contrib.auth.models import User
from django import forms
  

class Video(models.Model):
  url = models.URLField()

  
class Note(models.Model):
  videos = models.OneToOneField(Video)
  date_created = models.DateTimeField()
  text = models.TextField()
  user = models.ManyToManyField(User)
  
class UserProfile(models.Model):
  user = models.ForeignKey(User, unique=True)
  
class NoteForm(forms.Form):
  videos = models.OneToOneField(Video)
  date_created = models.DateTimeField()
  text = models.TextField()
  user = models.ManyToManyField(User)
  
