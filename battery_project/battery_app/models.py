from django.db import models

class BatteryData(models.Model):
    csv_file = models.FileField(upload_to='uploads/')

# models.py
# models.py


class GeneratedID(models.Model):
    image_id = models.CharField(max_length=10)


class CellInformation(models.Model):
    condition = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cell_type = models.CharField(max_length=100)
    form_factor = models.CharField(max_length=100)
    mass = models.FloatField()
    height = models.FloatField()
    diameter = models.FloatField()
    volume = models.FloatField()
