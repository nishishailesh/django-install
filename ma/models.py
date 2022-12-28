from django.db import models

# Create your models here.

class Examination(models.Model):
    id = models.AutoField(primary_key=True,db_column='examination_id')
    name = models.CharField(max_length=50)
    sample_requirement = models.CharField(max_length=100)
    edit_specification = models.CharField(max_length=2000)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examination'


class Result(models.Model):
    id = models.BigAutoField(primary_key=True)
    sample_id = models.BigIntegerField()
    examination_id = models.ForeignKey(Examination, models.DO_NOTHING,db_column='examination_id')
    result = models.CharField(max_length=5000, blank=True, null=True)
    recording_time = models.DateTimeField(blank=True, null=True)
    recorded_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result'
        unique_together = (('sample_id', 'examination_id'),)
