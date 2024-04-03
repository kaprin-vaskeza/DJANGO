from django.db import models


class Hive(models.Model):

    name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    active = models.BooleanField(True)
