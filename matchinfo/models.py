from django.db import models


# Create your models here.
class Hometeam(models.Model):
    Nameteam = models.CharField(max_length=190, null=False)
    score = models.CharField(max_length=190)
    pos = models.CharField(max_length=190)
    red_card = models.CharField(max_length=190)
    ya_card = models.CharField(max_length=190)


class Awayteam(models.Model):
    Nameteam = models.CharField(max_length=190, null=False)
    score = models.CharField(max_length=190)
    pos = models.CharField(max_length=190)
    red_card = models.CharField(max_length=190)
    ya_card = models.CharField(max_length=190)
