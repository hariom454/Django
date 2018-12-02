from django.db import models
# Create your models here.

class Actor(models.Model):
	name = models.CharField(max_length = 200)
	SEX = [("M","Male"), ("F", "Female")]
	sex = models.CharField(max_length = 1, choices=SEX)
	dob = models.DateField()
	bio = models.TextField()

class Producer(models.Model):
	name = models.CharField(max_length = 200)
	SEX = [("M","Male"), ("F", "Female")]
	sex = models.CharField(max_length = 1, choices=SEX)
	dob = models.DateField()
	bio = models.TextField()


class Movie(models.Model):
	Name = models.CharField(max_length = 200)
	Year_of_Release = models.DateField()
	actor = models.ManyToManyField(Actor)
	producer = models.ForeignKey(Producer, on_delete = models.CASCADE, null = True, blank = True)
	Plot = models.TextField()
	#Poster = models.ImageField()
	#producer = models.ForeignKey(Producers, on_delete = models.CASCADE, null = True, blank = True)
