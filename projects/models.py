from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    languages = models.CharField(max_length=500)


