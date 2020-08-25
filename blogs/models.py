from django.db import models

class Blogs(models.Model):
	title = models.CharField(max_length=100)
	pub_date= models.DateField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')
