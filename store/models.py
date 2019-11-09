from django.db import models

# Create your models here.

class  Song(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField()
	genre = models.CharField()
	

