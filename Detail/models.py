from django.db import models
# Create your models here.

class Actor(models.Model):
	name = models.CharField(max_length = 200)
	SEX = [("M","Male"), ("F", "Female")]
	sex = models.CharField(max_length = 1, choices=SEX)
	dob = models.DateField()
	bio = models.TextField()
	def __str__(self):
		return self.name

class Producer(models.Model):
	name = models.CharField(max_length = 200)
	SEX = [("M","Male"), ("F", "Female")]
	sex = models.CharField(max_length = 1, choices=SEX)
	dob = models.DateField()
	bio = models.TextField()
	def __str__(self):
		return self.name


class Movie(models.Model):
	Name = models.CharField(max_length = 200)
	Year_of_Release = models.DateField()
	actor = models.ForeignKey(Actor, on_delete = models.CASCADE, null = True, blank = True)
	producer = models.ForeignKey(Producer, on_delete = models.CASCADE, null = True, blank = True)
	Plot = models.TextField()
	poster = models.ImageField(upload_to = 'poster', blank = True)
	