from django.db import models

# Create your models here.

class Result(models.Model):
    id= models.AutoField(primary_key=True)
    sample_id = models.BigIntegerField()
    examination_id = models.IntegerField()
    result = models.CharField(max_length=5000, blank=True, null=True)
    recording_time = models.DateTimeField(blank=True, null=True)
    recorded_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'result'
        unique_together = (('sample_id', 'examination_id'),)
