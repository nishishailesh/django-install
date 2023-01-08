from django.db import models

# Create your models here.

class Intake(models.Model):
    date = models.DateField(blank=True, null=True)
    food_id = models.CharField(max_length=40, blank=True, null=True)
    gm = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    recorded_by = models.CharField(max_length=200, blank=True, null=True)
    recording_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intake'


class Myfood(models.Model):
    food_item = models.CharField(max_length=100, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    calcium = models.IntegerField(blank=True, null=True)
    phosphorus = models.IntegerField(blank=True, null=True)
    potassium = models.IntegerField(blank=True, null=True)
    sodium = models.IntegerField(blank=True, null=True)
    protein = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fiber = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    recorded_by = models.CharField(max_length=100, blank=True, null=True)
    recording_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'myfood'
