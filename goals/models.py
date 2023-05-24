from django.db import models
from django.utils import timezone
# Create your models here.


class Goal(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    current = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    measure = models.CharField(max_length=100)
    end_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100)

    def __str__(self):
        pass

    class Meta:
        managed = True
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'

class Diary(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    data=models.CharField(max_length=250)
    
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Diary'
        verbose_name_plural = 'Diaries'