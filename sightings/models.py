from django.db import models
class Data(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    unique_squirrel_id = models.CharField(unique=True, max_length=200)
    shift = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    primary_fur_color = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    running = models.BooleanField(blank=True, null=True)
    chasing = models.BooleanField(blank=True, null=True)
    climbing = models.BooleanField(blank=True, null=True)
    eating = models.BooleanField(blank=True, null=True)
    foraging = models.BooleanField(blank=True, null=True)
# Create your models here.
