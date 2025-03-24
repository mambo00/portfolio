from django.db import models


class Skill(models.Model):
    name1 = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    name3 = models.CharField(max_length=255)
