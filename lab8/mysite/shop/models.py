from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=20)


class Description(models.Model):
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    description = models.CharField(max_length=1500)
