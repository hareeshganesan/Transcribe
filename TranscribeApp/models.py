from django.db import models
from django.contrib.auth.models import User



# class Notes(models.Model):

# 	students = models.ManyToManyField(Student)
# 	videos = models.OneToOneField(Video)
# 	date_created = models.DateTimeField()

# class Student(models.Model):
# 	user = models.OneToOneField(User)
# 	notes = models.ManyToManyField(Notes)
	
# 	organization = models.CharField(
# 		max_length=255,
# 	)
	
class Video(models.Model):

	url = models.URLField()
