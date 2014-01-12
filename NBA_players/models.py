from django.db import models

# Create your models here.
class Player(models.Model):	#our single model with 3 fields
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    age = models.IntegerField()

    def __unicode__(self):
    	return self.name

