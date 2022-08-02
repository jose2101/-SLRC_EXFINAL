from django.db import models

class Course(models.Model):
    idcourse = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=80)
    hour = models.CharField(max_length=80)
    credits = models.CharField(max_length=1)
    state = models.CharField(max_length=20)

class Career(models.Model):
    idcareer = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    shortname = models.CharField(max_length=20)
    image = models.ImageField (upload_to='Logos')
    state = models.CharField(max_length=6)
