from django.db import models

# Create your models here.

class  Song(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	artist = models.CharField(max_length=100)
	album = models.CharField(max_length=100, null=True)
	image = models.ImageField(upload_to='songs/', default='songs/image.png')
	year = models.DateTimeField()


	def __str__(self):
	 return self.name

	class Meta():
		ordering = ['name']
